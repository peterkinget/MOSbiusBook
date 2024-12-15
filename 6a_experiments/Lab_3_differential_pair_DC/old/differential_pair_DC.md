# Lab 3: Differential Pair DC Response

```{warning}
 This is a preliminary **preview** version, updates pending
 ```
 
## Objective
In this experiment, you will learn about differential signals and circuits through building and characterizing a differential pair. The most important takeaway is that within its operating range, its differential output gain is independent of the common-mode input voltage. 

## Preparation
* Review your course notes on differential signals and the theory of the operation of the differential pair.
* Consider doing some circuit simulations to get familiar with the DC operation of a differential pair.  

## Materials
* ADALM2000 Active Learning Module
* Breadboard & Wires
* Resistor: 1.2k Ohm, 4.7k Ohm,
* Potentiometer: 20k Ohm
* MOSbius Chip & PCB

![Fig. NMOS diff-pair devices used.](img/NMOS_diff_pair_pin.png)

## Experiments

```{attention}
The **IREF** of the current mirror is set to be 200uA in this experiment. You can use the potentiometer on the PCB to set the IREF current. 

The **body** of the DNW pair (Pin47) is connected to ground for the experiments.
```
1. Measure the common-mode gain. Investigate the common-mode response of the differential pair. Sweep the common-mode voltage from 0V to 2.5V. Find where the transistors work in the saturation region. Plot $V_{CS}-V_{COM}$ and $V_{OUT}-V_{COM}$ as shown. Explain and make some conclusions. 
    * measure the voltages at the drains and common source with large common-mode signal sweeps
    * determine the feasible common-mode operating range
    * determine the common-mode gain
![Fig. Measurement of NMOS diff-pair common mode response.](img/NMOS_diff_pair_cm_measure_probe_4k7.png)
2. Measure the differential gain. Investigate the differential-mode response. Sweep the differential-mode response from 0V to 2.5V with a 1.25V common-mode voltage. 
    * measure the voltages at the drains and common source with large differential signal sweeps
    * determine the linear operating range for the differential mode
    * in the linear operating mode, determine the differential gain
![Fig. Measurement of NMOS diff-pair differential mode response.](img/NMOS_diff_pair_dm_measure_probe_4k7.png)
1. Explore how the differential gain varies with changing common mode input voltage. Try the same diff-pair with 1:1 current mirror and 4.7k Ohm as shown. 
![Fig. How to change the common mode voltage for differential gain measurement. ](img/NMOS_diff_pair_dm_CMVsetting_4k7.png)
   
1. Sweep the differential input from 0-2.5V and common mode 1.25V of the same diff-pair with different current sources (1:2, 1:4, 1:8) and different loads (1.2k, 2.35k, 4.7k) as shown. Find the differnetial gain. See the impact on the differential input and output range. Explain the result.   
![Fig. Circuit diagram to investigate differential input and output range and gain. ](img/NMOS_diff_pair_dm_measure_range.png)
   

## Suggestions

* Run simulations of the experiments to observe the difference between simulated circuits where the transistors are perfectly identical and real-world circuits where there are small manufacturing variations between ideally designed transistors.
    * Determine the offset voltage of the differential pair 
* Determine the impact of the body effect
  