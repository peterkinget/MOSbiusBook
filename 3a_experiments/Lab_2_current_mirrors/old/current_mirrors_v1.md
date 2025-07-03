# Current Mirrors
 The MOSbius chip provides you with nMOS and pMOS current mirrors. This lab will help you get a sense of transistor characteristics and the principles of current mirrors. 


## Objective

* Explore the operation of MOS transistors in current mirror applications
* Understand the effect of transistor sizing
* Understand the effect of drain-source voltage on mirror accuracy

## Preparation

* Review your course notes on current mirrors and sigle transistor characteristics 
* Review the pin map for the chip and find where the current mirrors are
![<em>Fig.</em> The current mirrors used in this experiment; blue pin numbers correspond to the numbers on the PCB.](img/Current_Mirror.png)

## Materials
* ADALM2000 Active Learning Module
* Breadboard & Wires
* Resistor: 1k Ohm, 470 Ohm, 
* Potentiometer: 20k Ohm
* MOSbius Chip & PCB

## Measurement
(Questions marked with a * are optional)
1. **IOUT vs IIN:**
- Set up the circuit shown below on your breadboard with the following parameters:
    - M1 and M2 are the transistors on the MOSbius chip of the current mirror under test  
    - use a VDD of 2.5V
    - R1 = R2 = 470 Ohm for the 1:1 current mirror 
    - Attach the differential scope channels 1+/1- and 2+/2- as shown

![<em>Fig.</em> Schematic of the measurment of the current for nMOS and pMOS current mirror. The connections can be used for IBIAS sweeping directly.](img/How_to_measure_current.png)

- Measure the IOUT of the 1:1 current mirror while sweeping IIN. Turn the potentiometer to change IIN. Monitor the current IIN and IOUT by observing the voltages across R1 and R2.  Plot IOUT vs IIN. 

- Data Analysis Questions: 
    - Q1: Is IOUT the same as IIN? If not, what are possible physical sources for the errors? 
    - Q2*: Increase the resistance at the output used for the current measurement to 4.7K Ohms. Are there any changes in the error between IIN and IOUT? Can you explain? 

1. **IOUT vs VDS:** 
- Change the setup as shown below: 
    - Generate a ramp to slowly sweep the VDS from 0V to 2.5V using the signal generator in the ADALM2000. 
    - Connect 2- to the ground and 2+ to the drain node of load transistor Q2 to measure VDS. 
    - Connect 1+  and 1- across the load resistor R2 to measure the current. 


![<em>Fig.</em> Measurement of VDS sweep.](img/How_to_measure_VDS_sweep.png)

- Measure the 1:1 nMOS current mirror IOUT while sweeping VDS with a fixed IBIAS of around 100uA. Plot the IOUT-VDS curve.

- Data Analysis Questions:
    - Q1: Identify the operating regions of the transistor (i.e. linear or saturation region).
    - Q2: When is IOUT equal to IBIAS? Explain.
    - Q3: Estimate the DC output impedance of M2.
    - Q4: Determine the output voltage range of this 1:1 current mirror when used as a current source.

- (Optional) Change IBIAS to 400uA (X4) and repeat the measurement and analysis

- Repeat for the pMOS 1:1 current mirror but make the appropriate adjustments to the setup. 

3. **1:2, 1:4, 1:8 Current Mirrors**

> **PK Question: what measurements do you want to be repeated? I suggest to measure IOUT-IIN with appropriately scaled current mirror loads so they can focus on the current ratios while keeping the VDS the same, at least between the 2, 4, and 8 transistor. If the VDS needs to be VGS, a potentiometer will be need be added at the output to set the VDS=VGS in those branches as well**
> Yuechen 's Answer: Based on your suggestions, I think we can ask the student to find the resistor values to make the VDS=VGS. The most convient way is to fix the resistance value for the IREF (e.g. 4.7k Ohms) And then ask them to find a proper load for accurate current replication. 


-  Each of student in the group can be responsible for a different ratio. 
-  Fix the load resistance for the IREF as 4.7k Ohms and measure the IREF. Find a proper load that gives you the current as you expect (1:2, 1:4, 1:8). The most straight forward way is to use a variable resistor as shown to scan and obtain the appropriate load value. Or you can calculate the resistance value and directly use a resistor with this fixed value as your load. Then measure the current flowing through this resistor to verify your calculation. ![<em>Fig.</em> Measurement of 1:X current mirror.](img/NMOS_sweep_load_1_X.png)

- Analysis:
    - Q1: Based on your observations in previous measurements, find the proper value for R3, R4, and R5 to make the output current to be exactly expected. Explain. 
    - (Optional) Estimate the DC output impedance of each ratio through IOUT-VDS.
    - Q2: Based on the experiments above, under what conditions the current mirror can accurately replicate the current? 


