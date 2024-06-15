
image=imread('/home/rguktrkvalley/computational lab/week8/1701322810442.png');
red=image(:,:,1);
green=image(:,:,2);
blue=image(:,:,3);
csvwrite("red_channel.csv",red);
csvwrite("green_channel.csv",green);
csvwrite("blue_channel.csv",blue);
disp('red,green,and blue channels saved to seperate csv files succesfully');
