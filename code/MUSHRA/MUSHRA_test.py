import numpy as np
import scipy.io as sio
import datetime
from shutil import copyfile
import sys


# handler for conducting mushra tests
class MUSHRA_test(object):

    def __init__(self, debug_mode=False, do_training=True):
        self._VA_exp = None
        self._LE_exp = None
        self._user_age = None
        self._user_id = None
        self._do_training = do_training

        self._debug_mode=debug_mode

        self._results_file_name = None

        self._num_conditions = None
        self._num_repititions = None
        self._random_vector = None  # random vector of scene indices for order of stimuli to play

    def set_participant_infos(self, age, VA_expertise, Listen_Exp_expertise):
        self._user_age = age
        self._VA_exp = VA_expertise
        self._LE_exp = Listen_Exp_expertise

    def set_test_design(self, random_vector):
        self._reference_ids = random_vector[0, :]  # store reference IDs of each trial
        self._random_vector = random_vector
        self._num_trials = self._random_vector.shape[1]
        self._num_stimuli_per_page = self._random_vector.shape[0]

    def initialize(self):
        self.randomize_stimuli()

        if self._debug_mode:
            self._user_id = 9999
            print('Experiment in DEBUG mode!')
        else:
            self._user_id = int(sio.loadmat('MUSHRA/results/id_counter.mat')['current_id'][0])
            print(f'Participant No. {self._user_id }!')
            sio.savemat('MUSHRA/results/id_counter.mat', {'current_id' : self._user_id+1 } )

        self._results_file_name = f'MUSHRA/results/subject_no_{self._user_id:d}_' + datetime.datetime.now().strftime("%m-%d-%Y") + '.mat'

        sio.savemat(self._results_file_name,   {'user_id': self._user_id,
                                                'age': self._user_age,
                                                'VA_exp': self._VA_exp,
                                                'LE_exp': self._LE_exp,
                                                'random_vector': self._random_vector,
                                                'results': [],
                                                'num_trials': self._num_trials
                                                })

    def randomize_stimuli(self):

        # randomize trials
        rand_order = np.random.permutation(np.arange(0, self._num_trials))
        idx = np.argsort(rand_order)
        self._random_vector = self._random_vector[:, idx]
        self._reference_ids = self._reference_ids[idx]

        # randomize conditions per mushra trial including hidden anchor and hidden reference
        for rv in range(0, self._num_trials):
            self._random_vector[:, rv] = np.random.permutation(self._random_vector[:, rv])

        print('random vector:')
        print(self._random_vector)
        print('coresponding references:')
        print(self._reference_ids)

    def store_result(self, trial, result):
        file = sio.loadmat(self._results_file_name)
        result_array = file['results']
        result_array = np.append(result_array, [result])

        sio.savemat(self._results_file_name, {'user_id': file['user_id'],
                                              'age': file['age'],
                                              'VA_exp': file['VA_exp'],
                                              'LE_exp': file['LE_exp'],
                                              'random_vector': file['random_vector'],
                                              'results': result_array,
                                              'num_trials': self._num_trials
                                              })

    def back_up_results(self, path_to_cloud):
        try:
            file_name = self._results_file_name.rsplit('MUSHRA/results/', 1)[1]
            copyfile(self._results_file_name, path_to_cloud + file_name)
            print(f"Successfully copied results '{file_name}' to '{path_to_cloud}', be shure internet connection is running!")
        except:
            print(f'WARNING: Results could not be copied to {path_to_cloud}, back up results manually.', file=sys.stderr)

    def is_training_desired(self):
        return self._do_training

    def get_num_trails(self):
        return self._num_trials

    def get_num_stimuli_per_page(self):
        return self._num_stimuli_per_page