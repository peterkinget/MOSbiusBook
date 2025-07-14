# Introduction of ADALM2000 and MOSbius
## Objective
Learn how to use MOSBius and ADALM2000 through some simple circuits. 
## Materials
* ADALM2000 Active Learning Module
* Breadboard & Wires
* Resistor: 1k Ohm, 4.7k Ohm
* Capacitor: 4.7 nF
* MOSbius Chip & PCB

## Experiments
![Fig. Schematics of RC networks.](<img/RC networks.png>)
1. **X-Y Plot and Signal Generator:** Resistive Divider
   * Step 1: Build a resistive divider on the breadboard as shown below, i.e. $R_1=R2=10k \Omega$. 
   * Step 2: Generate a ramp signal from 0V-2.5V (100Hz) and put your probes as shown to measure voltage respectively. 
   * Step 3: Use X-Y plot in the oscilloscope. Set X-channel 1 and Y-channel2.  
![Fig. Connections for resistor divider and X-Y plot. ](img/Ramp_X_Y_Resistor_Devider.png)
2. **Oscilloscope:** Step Response of RC Circuit. 
   * Calculate the transfer function of these RC Circuit. 
   * Generate an 0-2.5V 50kHz square wave at the 1+ point. 
   * Analyse those transient response and compare it with your results.
Here is an example:
![Fig. Calculations and analysis of the RC curcuit.](<img/Calculation and Analysis of RC networks.png>)
![Fig. Step response of RC networks. ](img/Step_Response_of_RC.png)
1. **Network Analyzer:** First Order RC Response
   * Step 1: Watch [this video](https://www.youtube.com/watch?v=VZqPyR455UE&list=PLE6soOeVPOJ0Pj5sMui4KPDiTa7HY50y3&index=10) and follow the steps introduced in the video to get a Bode plot of an RC (1k Ohm and 4.7 nF) circuit. 
   * Step 2: Identify the bandwidth and corresponding phase shift of these RC networks shown in the figure. Show your calculation and explain. 
![Fig. Analysis of frequency response of RC networks](<img/Analysis frequency response of RC networks.png>)
![Fig. Frequency response of RC networks. ](img/Frequency_Response_of_RC.png)
