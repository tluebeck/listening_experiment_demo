import scipy.io as scyio
import numpy as np
import os.path
import os
import sys
from random import randrange
from distutils.dir_util import copy_tree

from . import SAQI_vocabulary

class SAQI_test():

    def __init__(self,
                 stimuli_ids,
                 attributes,
                 categories,
                 test_signals,
                 randomize_stimuli=True,
                 randomize_btn_assignment=False,
                 randomize_categories=False,
                 randomize_attributes=False,
                 randomize_test_signals=False,
                 randomize_all_conditions=False,
                 restore=None,
                 attributes_per_page=1,
                 language='english',
                 back_up_path=None,
                 debug=True):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory


        (C) 2021 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing
        SAQI_test:
        this class defines the main experiment paradigm

        Parameters
        ----------
        stimuli_ids: array of stimuli ids in the form: [[condition_0, reference_0],
                                                        [condition_1, reference_1],
                                                        ...
                                                        [condition_N, reference_N]]
        attributes:
        categories:
        test_signals:
        randomize_stimuli:
        randomize_btn_assignment:
        randomize_categories:
        randomize_attributes:
        randomize_test_signals:
        attributes_per_page:
        language:
        debug:
        """

        self._language = language
        self.debug = debug
        self._stimuli_ids = stimuli_ids

        # overall difference attribute is mandatory for each SAQI test:
        overall_difference_attribute = SAQI_vocabulary.OveralDifference()

        self._attributes = attributes
        self._attributes.insert(0, overall_difference_attribute)

        self._categories = categories  # not necesarry so far
        self._attributes = attributes

        for attribute in self._attributes:
            attribute.set_language(self._language)

        self._test_signals = test_signals
        self.attributes_per_page = attributes_per_page

        self._randomize_stimuli = randomize_stimuli
        self._randomize_btn_assignment = randomize_btn_assignment
        self._randomize_categories = randomize_categories  # not implemented so far
        self._randomize_qualities = randomize_attributes
        self._randomize_test_signals = randomize_test_signals
        self._rand_all = randomize_all_conditions
        self._path_to_back_ups = back_up_path

        # -------------------------------------------------------------------------------------------------------------#
        self._current_category = 0
        self.current_attribute_list = list()
        self.finished_trials = 0
        self._trial_page_cnt = 0
        self._is_complete = False
        self._restore = restore
        self._total_num_ratings = None
        self._paused = 0

        if not restore:
            self.setup_experiment_plan()

            # set the first attribute
            self.current_attribute_list = [self._attributes[self._experiment_plan[0][2]]]

            if not self.debug:
                if not os.path.isfile('results/overall_id_cnt.mat'):
                    self._overall_id_cnt = 0
                    scyio.savemat('results/overall_id_cnt.mat', {'overall_id_cnt': self._overall_id_cnt})
                else:
                    self._overall_id_cnt = int(scyio.loadmat('results/overall_id_cnt.mat')['overall_id_cnt'][0] + 1)
                    scyio.savemat('results/overall_id_cnt.mat', {'overall_id_cnt': self._overall_id_cnt})

                self._path_to_results = f'results/res_part_{self._overall_id_cnt}'
                try:
                    os.mkdir(self._path_to_results)
                except:
                    print(f'WARNING: Could not create dir {self._path_to_results}!',
                            file=sys.stderr)
                self._result_file_name = f'{self._path_to_results}/{self._overall_id_cnt}_result_file'

        elif restore > 0:
            self._overall_id_cnt = restore
            self._path_to_results = f'results/res_part_{restore}'
            self._result_file_name = f'{self._path_to_results}/{restore}_result_file'
            obj = scyio.loadmat(f"{self._result_file_name}.mat")
            infos = obj['participant_infos']
            self.participant_infos = {'participant_id': infos['participant_id'][0, 0][0, 0],
                                      'age': infos['age'][0, 0][0],
                                      'gender': infos['gender'][0, 0][0],
                                      'ListeningExperimentExperience': infos['ListeningExperimentExperience'][0, 0][0],
                                      'BinauralExperience': infos['BinauralExperience'][0, 0][0]}

            self._experiment_plan = obj['experiment_plan']
            self.trial_page_cnt = obj['trial_page_cnt'][0, 0]
            self.finished_trials = obj['finished_trials'][0, 0]
            self._total_num_ratings = self._experiment_plan.shape[0]
            if self.finished_trials < self._total_num_ratings/2:
                self._paused = 0

            print(f'Load experiment data and continue at trial {self.finished_trials}')

    def setup_experiment_plan(self):
        # [attribute_index, stimuli_idx, test_signal_index]
        stimuli_id_list = np.arange(0, len(self._stimuli_ids))
        test_signal_id_list = np.arange(0, len(self._test_signals))
        attribute_id_list = np.arange(1, len(self._attributes) + 1)  # start at one, because the first is not randomized
        # maybe use real attributes ids instead?

        if self._randomize_stimuli:
            stimuli_id_list = np.random.permutation(stimuli_id_list)

        self._experiment_plan = np.zeros([len(attribute_id_list) * len(test_signal_id_list) * len(stimuli_id_list), 4],
                                         dtype=int)

        trial = 0
        for s_idx in range(0, len(stimuli_id_list)):
            if self._randomize_test_signals:
                test_signal_id_list = np.random.permutation(test_signal_id_list)
            for t_idx in range(0, len(test_signal_id_list)):
                if self._randomize_qualities:
                    attribute_id_list = np.random.permutation(attribute_id_list)
                complete_attribute_list = np.append(np.array([0]),
                                                    attribute_id_list)  # at overal difference id at the top
                if self._randomize_btn_assignment:
                    toggle_ref = randrange(0, 2)
                else:
                    toggle_ref = 0  # per default reference is under button 'A'
                                                         # if flag is set, reference is under 'B'

                for a_idx in range(0, len(attribute_id_list)):
                    self._experiment_plan[trial, 0] = stimuli_id_list[s_idx]
                    self._experiment_plan[trial, 1] = test_signal_id_list[t_idx]
                    self._experiment_plan[trial, 2] = complete_attribute_list[a_idx]
                    self._experiment_plan[trial, 3] = toggle_ref
                    trial += 1

        if self._rand_all:
            condition_ids = np.random.permutation(np.arange(0, len(test_signal_id_list) * len(stimuli_id_list)))
            rand_plan = np.zeros([len(attribute_id_list) * len(test_signal_id_list) * len(stimuli_id_list), 4],
                                         dtype=int)
            cnt = 0
            for c_id in condition_ids:
                rand_plan[cnt:cnt+len(attribute_id_list), :] = self._experiment_plan[c_id*len(attribute_id_list):(c_id+1)*len(attribute_id_list), :]
                cnt = cnt + len(attribute_id_list)
            self._experiment_plan = rand_plan

        self._total_num_ratings = self._experiment_plan.shape[0]

    def trial_finished(self, values, skip=False):
        if skip:  # if no difference was detected, skip attributes
            self.finished_trials += self.attributes_per_page

        # update experiment status
        if self.finished_trials >= len(self._experiment_plan) - 1:
            self._is_complete = True
            print('Experiment complete')

        # write results
        self.write_results(values)
        self._trial_page_cnt += 1

        if not self._is_complete:
            print(f'--------------- NEXT TRIAL -----------------------------\n')
            print(f'    page: {self._trial_page_cnt}')
            print(f'    finished trials: {self.finished_trials}')
            if self._attributes[self._experiment_plan[self.finished_trials + 1][2]].id == 0:
                # next attribute is a overall difference rating
                self.current_attribute_list.clear()
                self.current_attribute_list.append(self._attributes[self._experiment_plan[self.finished_trials + 1][2]])
                self.finished_trials += 1
            else:
                # next attributes are 'attributes_per_page' attribues
                self.current_attribute_list.clear()
                for idx in range(self.finished_trials + 1, self.finished_trials + 1 + self.attributes_per_page):
                    self.current_attribute_list.append(self._attributes[self._experiment_plan[idx][2]])
                    self.finished_trials += 1
            
           
            print(f'    - attribute(s):')
            for idx in range(0, len(self.current_attribute_list)):
                print(f'                 {self.current_attribute_list[idx].get_quality_name()}')
            print(f'    - test_signal:')
            print(f'                 {self.get_current_test_signal()}')
            print(f'    - stimuli ids:')
            print(f'                 {self.get_current_stimuli_ids()}')

    def restore_experiment(self):
        if not self._is_complete:
            if self._attributes[self._experiment_plan[self.finished_trials + 1][2]].id == 0:
                # next attribute is a overall difference rating
                self.current_attribute_list.clear()
                self.current_attribute_list.append(self._attributes[self._experiment_plan[self.finished_trials + 1][2]])
                self.finished_trials += 1
            else:
                # next attributes are 'attributes_per_page' attribues
                self.current_attribute_list.clear()
                for idx in range(self.finished_trials + 1, self.finished_trials + 1 + self.attributes_per_page):
                    self.current_attribute_list.append(self._attributes[self._experiment_plan[idx][2]])
                    self.finished_trials += 1

            if self.debug:
                print(f'Next trial (page of attributes): {self._trial_page_cnt}')
                print(f'  - attribute(s):')
                for idx in range(0, len(self.current_attribute_list)):
                    print(f'                 {self.current_attribute_list[idx].get_quality_name()}')
                print(f'  - test_signal:')
                print(f'                 {self.get_current_test_signal()}')
                print(f'  - stimuli ids:')
                print(f'                 {self.get_current_stimuli_ids()}')

    def get_current_attributes(self):
        return self.current_attribute_list

    def get_current_test_signal(self):
        idx = self._experiment_plan[self.finished_trials][1]
        return self._test_signals[idx]

    def get_current_stimuli_ids(self):
        idx = self._experiment_plan[self.finished_trials][0]
        # per default, the reference is on position 1, the test condition on position 2
        # if random btn assignment is enabled, the positions are toggled
        if self._experiment_plan[self.finished_trials][3]: # if set, toggle reference and test signal
            return [self._stimuli_ids[idx][1], self._stimuli_ids[idx][0]]
        else:
            return [self._stimuli_ids[idx][0], self._stimuli_ids[idx][1]]

    def get_current_categroy(self):
        attribute = self._attributes[self._experiment_plan[self.finished_trials][2]]
        return attribute.get_category_name()

    def set_participant_infos(self, infos):
        if not self.debug:
            self.participant_infos = {'participant_id': self._overall_id_cnt,
                                      'age': infos[0],
                                      'gender': infos[1],
                                      'ListeningExperimentExperience': infos[2],
                                      'BinauralExperience': infos[3]}

            scyio.savemat(f'{self._result_file_name}.mat', {'participant_infos': self.participant_infos,
                                                            'experiment_plan': self._experiment_plan,
                                                            'trial_page_cnt': self._trial_page_cnt,
                                                            'finished_trials': self.finished_trials},
                                                            appendmat=True)

    def write_results(self, values):
        if not self.debug:
            # collect all infos per page and store in page dict
            attribute_list = list()
            stimuli_list = list()
            reference_id_list = list()
            test_signal_list = list()
            btn_assignment = list()
            values_raw = values
            for idx in range(0, len(self.current_attribute_list)):
                attribute_list.append(self.current_attribute_list[idx].get_quality_name())

                if self._experiment_plan[self.finished_trials][3]:  # if set, reference and test signal were toggled
                    stimuli_list.append(self.get_current_stimuli_ids()[1])
                    reference_id_list.append(self.get_current_stimuli_ids()[0])
                    btn_assignment.append(['A:Test', 'B:Ref'])
                    if self.current_attribute_list[idx].rating_scale_mode == 'bipolar':
                        # if ref and test signal were toggled, and rating was bipolar we need to toggle the results
                        values[idx] = -values[idx]
                else:
                    stimuli_list.append(self.get_current_stimuli_ids()[0])
                    reference_id_list.append(self.get_current_stimuli_ids()[1])
                    btn_assignment.append(['A:Ref', 'B:Test'])

                test_signal_list.append(self.get_current_test_signal())

            if self.current_attribute_list[0].id == 0:
                diff_rating = values[0]
                if len(values) > 1:
                    values = values[1]
            else:
                diff_rating = ''

            print(f'Results: {values}')

            page = {'trial_ids': self._trial_page_cnt,
                    'stimuli_ids': stimuli_list,
                    'reference_ids': reference_id_list,
                    'test_signals': test_signal_list,
                    'result_values': values,
                    'attributes': attribute_list,
                    'diff_rating': diff_rating,
                    'btn_assignment': btn_assignment,
                    'values_from_gui': values_raw}

            # export results as matfile
            experiment = {'participant_infos': self.participant_infos, 'page_id': self._trial_page_cnt, 'page': page}
            scyio.savemat(f'{self._result_file_name}_{self._trial_page_cnt}.mat', experiment, appendmat=True)

            # just in case the experiment crashes, save all infos to properly restart the experiment without
            # repeating all trials
            scyio.savemat(f'{self._result_file_name}.mat', {'participant_infos': self.participant_infos,
                                                            'experiment_plan': self._experiment_plan,
                                                            'trial_page_cnt': self._trial_page_cnt,
                                                            'finished_trials': self.finished_trials},
                                                            appendmat=True)

    def back_up_results(self):
        back_up_path = f'{self._path_to_back_ups}/res_part_{self._overall_id_cnt}'
        try:
            os.mkdir(back_up_path)
            copy_tree(self._path_to_results, back_up_path)
            print(
                f"Successfully copied results of particpant no '{self._overall_id_cnt}' to '{self._path_to_back_ups}', be shure internet connection is running!")
        except:
            print(f'WARNING: Results could not be copied to {self._path_to_back_ups}, back up results manually!',
                  file=sys.stderr)
