% 
% 1: reference audiolab
% 2: reference audimax
%    Audiolab:
% 3:  N=3 Subsampling
% 4:  N=3 alternative approach (magLS)
% 5:  N=3 SARITA
% 6:  N=5 Subsampling
% 7:  N=5 alternative approach (magLS)
% 8:  N=5 SARITA
% 9:  N=7 Subsampling
% 10: N=7 alternative approach (magLS)
% 11: N=7 SARITA
%
%     Audimax:
% 12: N=3 Subsampling
% 13: N=3 alternative approach (magLS)
% 14: N=3 SARITA
% 15: N=5 Subsampling
% 16: N=5 alternative approach (magLS)
% 17: N=5 SARITA
% 18: N=7 Subsampling
% 19: N=7 alternative approach (magLS)
% 20: N=7 SARITA
%
clear all; close all; clc;

global attributes gap marg_h marg_w yticks_ ylims_

%results = check_results(1);
results = check_results(2);

dimensions = [50 100 2000 400];
gap = [0.04, 0.01];
marg_h = [0.2, 0.06]; 
marg_w = [0.02, 0.01];

color_1 = [139/255, 0, 0];
color_2 = [0, 139/255, 139/255];
color_3 = [0.3, 0.3, 0.3];

ylims_ = [-35, 35];
yticks_ = -30 : 10 : 30;

attributes = {'difference', ...
              'Klangverfaerbung', ...
              'Schallquellenposition', ...
              'Externalisierungsgrad', ...
              'Quellausdehnung', ...
              'Nachhallumhuellung'};

figure()
set(gcf, 'Position', dimensions);
suptitle('Audiolab', 0.97, 13)

plot_saqi(1, results{3}.drums, 'N=3, Subsamplig Drums', 0, 1)
plot_saqi(2, results{6}.drums, 'N=5, Subsamplig Drums')
plot_saqi(3, results{9}.drums, 'N=7, Subsamplig Drums')
 
plot_saqi(4, results{3}.speech, 'N=3, Subsamplig Speech')
plot_saqi(5, results{6}.speech, 'N=5, Subsamplig Speech')
plot_saqi(6, results{9}.speech, 'N=7, Subsamplig Speech')

plot_saqi(7, results{4}.drums, 'N=3, MagLS Drums', 0, 1)
plot_saqi(8, results{7}.drums, 'N=5, MagLS Drums')
plot_saqi(9, results{10}.drums, 'N=7, MagLS Drums')

plot_saqi(10, results{4}.speech, 'N=3, MagLS Speech')
plot_saqi(11, results{7}.speech, 'N=5, MagLS Speech')
plot_saqi(12, results{10}.speech, 'N=7, MagLS Speech')

plot_saqi(13, results{5}.drums, 'N=3, SARITA Drums', 1, 1)
plot_saqi(14, results{8}.drums, 'N=5, SARITA Drums', 1)
plot_saqi(15, results{11}.drums, 'N=7, SARITA Drums', 1)

plot_saqi(16, results{5}.speech, 'N=3, SARITA Speech', 1)
plot_saqi(17, results{8}.speech, 'N=5, SARITA Speech', 1)
plot_saqi(18, results{11}.speech, 'N=7, SARITA Speech', 1)




figure()
set(gcf, 'Position', [dimensions(1), ...
                      dimensions(2)+dimensions(4)+15, ...
                      dimensions(3:4)]);
                  
suptitle('Audimax', 0.97, 13)
plot_saqi(1, results{12}.drums, 'N=3, Subsamplig Drums', 0, 1)
plot_saqi(2, results{15}.drums, 'N=5, Subsamplig Drums')
plot_saqi(3, results{18}.drums, 'N=7, Subsamplig Drums')
 
plot_saqi(4, results{12}.speech, 'N=3, Subsamplig Speech')
plot_saqi(5, results{15}.speech, 'N=5, Subsamplig Speech')
plot_saqi(6, results{18}.speech, 'N=7, Subsamplig Speech')

plot_saqi(7, results{13}.drums, 'N=3, MagLS Drums', 0, 1)
plot_saqi(8, results{16}.drums, 'N=5, MagLS Drums')
plot_saqi(9, results{19}.drums, 'N=7, MagLS Drums')

plot_saqi(10, results{13}.speech, 'N=3, MagLS Speech')
plot_saqi(11, results{16}.speech, 'N=5, MagLS Speech')
plot_saqi(12, results{19}.speech, 'N=7, MagLS Speech')

plot_saqi(13, results{14}.drums, 'N=3, SARITA Drums', 1, 1)
plot_saqi(14, results{17}.drums, 'N=5, SARITA Drums', 1)
plot_saqi(15, results{20}.drums, 'N=7, SARITA Drums', 1)

plot_saqi(16, results{14}.speech, 'N=3, SARITA Speech', 1)
plot_saqi(17, results{17}.speech, 'N=5, SARITA Speech', 1)
plot_saqi(18, results{20}.speech, 'N=7, SARITA Speech', 1)



function plot_saqi(plt_ID, result_struct, title_str, plot_x_labels, plot_y_labels)
    global attributes gap marg_h marg_w yticks_ ylims_
    
    if nargin < 4
        plot_x_labels = 0;
    end
    if nargin < 5
        plot_y_labels = 0;
    end
    
    subtightplot(3, 6, plt_ID, gap, marg_h, marg_w) 
    if length(fieldnames(result_struct)) > 1
        plot([1:length(fieldnames(result_struct))], [result_struct.difference, ...
                                                     result_struct.Klangverfaerbung, ...
                                                     result_struct.Schallquellenposition, ...
                                                     result_struct.Externalisierungsgrad, ...
                                                     result_struct.Quellausdehnung, ...
                                                     result_struct.Nachhallumhuellung], ...
            'o', 'Color', 'black', 'MarkerSize', 8, 'LineWidth', 1.5);%, 'MarkerFaceColor', 'black')
    end
    grid on;
    hold on;
    yline(0, 'LineWidth', 1, 'Color', [0.5, 0.5, 0.5])
    yline(-30, 'LineWidth', 1, 'Color', [0.5, 0.5, 0.5])
    yline(30, 'LineWidth', 1, 'Color', [0.5, 0.5, 0.5])
    
    ylim(ylims_)
    yticks(yticks_)
    
    title(title_str)
    if plot_x_labels
        xticklabels(attributes)
        xtickangle(45)
    else
        xticklabels({})
    end
    
    if ~plot_y_labels
        yticklabels({})
    end
end