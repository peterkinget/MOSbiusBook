# First Experiment: Blinky
As a first experiment we show a **Schmitt-Trigger Relaxation Oscillator with LEDs**. It's always good to start off a project with blinking LEDs ... 

## Schmitt-Trigger Relaxation Oscillator
```{figure} img/IMG_2993.mov
```
**Circuit Schematic:** 
We build a Schmitt Trigger out of cascade of a 16x, 16x and 4x inverter with a 4x inverter providing positive feedback around the second stage, resulting in hysteresis in the input-output tranfer characteristic. Overall feedback around the Schmitt Trigger is created with an R-C network. LEDs are connected at the output of the second stage; the red LED ligths up when the output is high, and the green LED lights up when it is low. 
```{figure} img/relaxation_osc_v1.png
LTSpice schematic for the relaxation oscillator experiment
```

**Building the Circuit:** You can use manual connections or use the on-chip switch matrix (Files: [bitstream](img/relaxation_osc_v1_bitstream.txt), [bitsteam_clk](img/relaxation_osc_v1_bitstream_clk.txt), [connections](img/connections_relaxation_osc_v1.json)). When using the on-chip connections, the solderless breadboard only requires and external resistor and capacitor, along with the LEDS.
```{figure} img/relaxation_osc_v1_IMG_2992.jpeg
Photo of the *blinky* setup using the on-chip connections; the external components are a 100K$\Omega$ resistor, a 10uF capacitor, and two LEDs with 47$\Omega$ resistors; the orange and blue wires connect to the ADALM2000 oscillscope channels `1+` and `2+` respectively; `1-` and `2-` are grounded; the ADALM `V+` provides the 2.5V power supply; digital channels `DIO8` and `DIO9` are used to feed the bitstream to the `CLK` and `DATA` pin of the MOSbius chip to program the switch matrix. 
```

**Measurements:**
Besides the blinking LEDs the following waveforms can be observed:
```{figure} img/relaxation_bus01_bus02.png
Measured waveforms on *BUS01* and *BUS02*.
```
```{figure} img/relaxation_bus01_bus04.png
Measured waveforms on *BUS01* and *BUS04*.
```
**Quick Analytical Estimations**:
The oscillation across the capacitor has an amplitude of approx. 500mVpp. The average charging current is roughly $I_{ch} = (V_{DD} - V(\mathrm{BUS01})_{avg})/R = C \frac{\Delta V}{\Delta T}$, so $\Delta T = R C \frac{\Delta V}{(V_{DD} - V(\mathrm{BUS01})_{avg})}$; using $V_{DD}$ = 2.5V, $V(\mathrm{BUS01})_{avg}$ = 1.25, and $\Delta V$ = 500mV, we obtain $\Delta T$ = 400ms which corresponds to half the period. This is close to the measured result of 445ms[^exactanalysis].

**Comparison to Simulations:** The measured results correspond qualitatively very well to the results obtained from an LTspice simulation using models[^commentsim] for the chip components:
```{figure} img/relaxation_osc_v1_sim.png
Simulation results for the relaxation oscillator obtained with LTSpice
```

## Schmitt-Trigger Transfer Characteristic
After removing the resistor, *BUS01* can be driven with a slow 2.5Vpp sawtooth waveform with a 1.25V DC offset to measure the DC transfer characteristic of the Schmitt Trigger:
```{figure} img/Schmitt_Trigger_bus01_to_bus04.png
Measured Schmitt Trigger characteristic between *BUS01* and *BUS04*
```
The Schmitt trigger has a inverting characteristic with a hysteresis of approx. 500mV centered at about 1.25V.

[^exactanalysis]: A more detailed analysis can be performed using the expressions for the exponential charging and discharging waveforms.
[^commentsim]: The current LTSpice library for the chip components is using public domain 0.25um CMOS models and does not include accurate models of the on-chip layout and ESD parasitics; however, for low-frequency circuits qualitively accurate simulations can be obtained.  