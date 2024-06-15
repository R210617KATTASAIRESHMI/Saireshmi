f=[440,880,1320]
amp=[0.5,0.3,0.2]
s=cell(length(f),2)
s(:, 1)=num2cell(f)
s(:, 2)=num2cell(amp)
t=0:0.001:1
figure;
hold on;
for i=1:length(s)
  f=s{i, 1}
  amp=s{i, 2}
  wave=amp*sin(2*pi*f*t)
  plot(t,wave,'displayName',['frequecy',num2str(f),'Hz'])
endfor
hold off;
xlabel('time(s)')
ylabel('amplitude')
title('sine wave')
legend