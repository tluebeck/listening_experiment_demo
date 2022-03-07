function results = check_results(ID)
    path_to_results = sprintf('res_part_%d/', ID);
    base_name = sprintf('%d_result_file', ID);
    obj = load([path_to_results, base_name]);
    result_files = dir(sprintf('%s%s_*.mat', path_to_results, base_name));
    
    fprintf('Check results of participant: %d\n', ID);
    fprintf('     age: %s\n', obj.participant_infos.age);
    fprintf('     gender: %s\n', obj.participant_infos.gender);
    fprintf('     finished pages: %d\n', length(result_files));
    fprintf('---------------------------------\n');
    test_signal_1 = 'Test_signals/MARA_LE_SPEECH_calibrated_HPC.wav';
    test_signal_2 = 'Test_signals/MARA_LE_DRUMS_calibrated_HPC.wav';
    
    results = [];
    for page = 1:length(result_files)
        % load data 
        obj = load([path_to_results, result_files(page).name]);
        % difference rating 
        if length(obj.page.stimuli_ids) == 1
            if strcmp(obj.page.test_signals, test_signal_1)
               results{obj.page.stimuli_ids(1)}.speech.difference = obj.page.result_values;
            elseif strcmp(obj.page.test_signals, test_signal_2)
               results{obj.page.stimuli_ids(1)}.drums.difference = obj.page.result_values;
            end
        else
            for i = 1:length(obj.page.stimuli_ids)
                fname = string(obj.page.attributes(i, :));
                %fname = fname(find(~isspace(fname)));
                fname = strrep(fname,' ','');
                fname = strrep(fname,'(','');
                fname = strrep(fname,')','');
                fname = strrep(fname,'ä','ae');
                fname = strrep(fname,'ü','ue');
                fname = strrep(fname,'ö','oe');
                test_signal = obj.page.test_signals(1, :);
                if strcmp(obj.page.test_signals(1, :), test_signal_1)
                    results{obj.page.stimuli_ids(1)}.speech.(fname) = obj.page.result_values(i);
                elseif strcmp(obj.page.test_signals(1, :), test_signal_2)
                    results{obj.page.stimuli_ids(1)}.drums.(fname) = obj.page.result_values(i);
                end
            end
        end
    end
    results{1}.id = ID;
    results{1}.age = obj.participant_infos.age;
    results{1}.gender = obj.participant_infos.gender;
end