function init_experiment()
    fprintf('Initialize listening experiment: Set overall ID to 0.\n');
    overall_id_cnt = 0;
    save('overall_id_cnt.mat', 'overall_id_cnt')
    files = dir('res_part_*');
    fprintf(' ... also found %d old result files, do you want to delete? (y/n)\n', length(files))
    k = waitforbuttonpress;
    value = double(get(gcf,'CurrentCharacter'));
    close all
    if value == 121
        fprintf('delete ...\n')
        for f = 1:length(files)
            fprintf('   %s\n', files(f).name)
            rmdir(files(f).name, 's');
        end
    end
end