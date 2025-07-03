> PK Comments
> *W1 in some of the figures, not in the first one...*
> YH: Solved
> Can we do the DC transfer for a diode or 4007 Inverter?
> YH: Diode
> What is the fourier stuff about?
> YH: Deleted
> You cannot connect a diode between supply and ground -- you need a current limiting resistor
> YH: Cut from all pictures. 
> This seems to be a mix of solution and experiment
> Where is the solution?
> YH: Split it. 

# Lab 1: Basic Measurements
## Objective
Learn various measurement techniques using the ADALM2000

## Preparation
* Review the [ADALM2000 Introduction Video Series](https://www.youtube.com/watch?v=LCf-_iREESQ&list=PLE6soOeVPOJ0Pj5sMui4KPDiTa7HY50y3&pp=iAQB). 
* In the experiments here we will be using the calibration (Video 3), signal generator (Video 4), oscilloscope (Video 4), and network analyzer (Video 7). 
* Install the Scopy software on your laptop (Video 2). 

## Materials
* ADALM2000 Active Learning Module
* Laptop with Scopy software installed
* Breadboard & Wires
* Resistor: 1k Ohm, 4.7k Ohm
* Capacitor: 4.7 nF

## Experiments
### Circuits Used
![Fig. Schematics of RC networks.](<img/Diode_RC_Networks.png>)

### DC Transfer Characteristic of a Resistive Divider Using a Signal Generator and the X-Y Plot of the Oscilloscope
   * Build a resistive divider on the breadboard with $R_1=R2=10k \Omega$. 
   * Generate a ramp signal from 0V-2.5V (100Hz) and apply it across the resistive divider; connect channel 1 of the oscilloscope across $R_1 + R_2$ and channel 2 across $R_2$ (as shown in the figure). 
   * Turn on the X-Y plotting in the oscilloscope. Set X to channel 1 and Y to channel2.  
   * What is the transfer characteristic of the resistive divider? What is the gain?


### Step Response of RC Circuits using a Signal Generator and Oscilloscope
   * Calculate the step response of the various RC circuits. 
   * Build the RC circuits on your breadboard 
   * Generate an 0-2.5V 50kHz square wave with signal generator 1 (W1) and apply at the input of the RC networks; attach channel 1 of the scope to the input and channel 2 to the output.  
   * Analyze the measured step responses and compare your calculations.


### Frequency Response of RC Circuits using the Network Analyzer

Watch [this video](https://www.youtube.com/watch?v=VZqPyR455UE&list=PLE6soOeVPOJ0Pj5sMui4KPDiTa7HY50y3&index=10) and follow the steps introduced in the video to get a Bode plot of an RC (1k Ohm and 4.7 nF) circuit. 

   * Calculate the frequency response of the various RC circuits; find gain, poles, zeros, ...
   * Use the network analyzer to measure the frequency response; carefully consider how to set the signal amplitude for the measurement.
   * Compare measurements and calculations

