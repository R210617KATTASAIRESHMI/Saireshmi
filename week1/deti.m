clc
clear all
close all
a=[1,2;3,4]
det=a(1,1).*a(2,2)-a(1,2).*a(2,1)
disp(['det of the 2x2 matrix:',num2str(det)])