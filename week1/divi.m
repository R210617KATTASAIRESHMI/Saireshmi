clc
clear all
close all
a=input("enter a value")
b=input("enter b value")
try
    div=a/b
    #disp(['result of division';num 2 str(div)])
catch
    disp("error :enter either float or integer value")
end_try_catch
