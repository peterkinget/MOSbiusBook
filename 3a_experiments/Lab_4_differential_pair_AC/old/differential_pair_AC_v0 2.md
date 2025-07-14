# Lab 4: Differential Pair AC Response

```{warning}
 This is a preliminary **preview** version, updates pending
 ```
 
## Objective
In this experiment, you will learn about frequency response through building and characterizing a differential pair. 
## Preparation
* Review your course notes on frequency response and the theory of the operation of the differential pair.
* Make sure you can use the network analyzer on ADALM2000 and understand what it can do. 

## Materials
* ADALM2000 Active Learning Module
* Breadboard & Wires
* Resistor: 4.7k Ohm
* Capacitors: 2nF
* MOSbius Chip & PCB

## Experiments
>Notes: 4.7k Ohm load.
1. Explore common-mode gains at increasing frequencies. 
    * add load capacitors (differential and single-ended) 
    >200pF is tested, 200pF is too small so I may need to use around 2nF to see the pole caused by load capacitance instead of a pole-zero doublet of source capacitance and load capacitance. 
    * add source capacitors
    >200pF is tested, a zero is very obvious. 
    * evaluate the small-signal common-mode gains w.r.t. frequency
2. Explore differential gains at increasing frequencies. 
    * add load capacitors (differential and single-ended)
    * add source capacitors
    * evaluate the small-signal differential-mode gains w.r.t. frequency