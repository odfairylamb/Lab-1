% inputs for voltage and resistors
V1_volts = 5;
R1_ohms = 4;
R2_ohms = 2;
R3_ohms = 9;
R4_ohms = 10;
% solved for req
Req = round(((((R4_ohms+R2_ohms)*R3_ohms)/((R4_ohms+R2_ohms)+R3_ohms)) + R1_ohms), 2);
% solving for currents V/R, KVL, or KCL
I_R1 = round((V1_volts/Req), 2);
I_R3 = round(((V1_volts - R1_ohms*I_R1)/R3_ohms),2);
I_R2 = round((I_R1 - I_R3),2);
I_R4 = I_R2; %series have same current
disp("The current in R1 is: " + I_R1)
disp("The current in R2 is: " + I_R2)
disp("The current in R3 is: " + I_R3)
disp("The current in R4 is: " + I_R4)
% solving for power 
P_R1 = round(((I_R1^2)*R1_ohms),4);
P_R2 = (I_R2^2)*R2_ohms;
P_R3 = (I_R3^2)*R3_ohms;
P_R4 = (I_R4^2)*R4_ohms;
disp("The power in R1 is: " + P_R1)
disp("The power in R2 is: " + P_R2)
disp("The power in R3 is: " + P_R3)
disp("The power in R4 is: " + P_R4)
p = [P_R1 P_R2 P_R3 P_R4];
bar(p)