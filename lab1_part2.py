import matplotlib.pyplot as plt
# inputs for voltage and resistors
V1_volts = 5
R1_ohms = 4
R2_ohms = 2
R3_ohms = 9
R4_ohms = 10
# solved for req
Req = round(((((R4_ohms+R2_ohms)*R3_ohms)/((R4_ohms+R2_ohms)+R3_ohms)) + R1_ohms), 2)
# solving for currents V/R, KVL, or KCL
I_R1 = round((V1_volts/Req), 2)
I_R3 = round(((V1_volts - R1_ohms*I_R1)/R3_ohms),2)
I_R2 = round((I_R1 - I_R3),2)
I_R4 = I_R2 #series have same current
print("The current in R1 is: ", I_R1, "\nThe current in R2 is: ", I_R2, "\nThe current in R3 is: ", I_R3, "\nThe current in R4 is: ", I_R4)
# solving for power 
P_R1 = round(((I_R1**2)*R1_ohms),4)
P_R2 = (I_R2**2)*R2_ohms
P_R3 = (I_R3**2)*R3_ohms
P_R4 = (I_R4**2)*R4_ohms
print("The power in R1 is: ", P_R1, "\nThe power in R2 is: ", P_R2, "\nThe power in R3 is: ", P_R3, "\nThe power in R4 is: ", P_R4)

#graphing data
fig, ax = plt.subplots()
resistors = ['R1', 'R2', 'R3', 'R4']
counts = [P_R1, P_R2, P_R3, P_R4]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
ax.bar(resistors, counts, label=bar_labels, color=bar_colors)

plt.show()
