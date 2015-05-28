% d = dir('../spam_users_timeline/*.txt_epoch');
% nfiles = length(d);
% data = [];
% for k = 1:nfiles
%    data = [data importdata(d(k).name)];
%    disp(d(k).name);
% end

hold on
for k = 1:nfiles
    plot(data(:,k), zeros(1,300) + k, '.');
end
hold off