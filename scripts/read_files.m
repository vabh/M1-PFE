% d = dir('*.txt_epoch');
% nfiles = length(d);
% data = [];
% 
% for k = 1:nfiles
%    data = [data importdata(d(k).name)];
%    disp(d(k).name);
% end

hold on
for k = 1:nfiles
    
    plot(data(:,k), zeros(1,300) + k, '.');
end


xt = get(gca, 'XTick');
xt = datestr(xt./86400 + datenum(1970,1,1))
set(gca,'XTickLabel',xt(:, 13:20));
title('Tweet timeline', 'FontSize', 20)
xlabel({'Time','(in seconds from Unix epoch)'}, 'FontSize',20)
ylabel('Accounts', 'FontSize', 20);
grid on
grid minor
hold off