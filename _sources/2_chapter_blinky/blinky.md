# First Experiment: Blinky
As a first experiment we show a **Schmitt-Trigger Relaxation Oscillator with LEDs**. It's always good to start off a project with blinking LEDs ... 

```{raw} html
<center>
<video controls width="640" autoplay loop muted>
  <source src="../_static/videos/IMG_2993.mov" type="video/mp4">
  Your browser does not support the video tag
</video>
</center>
```
## Schmitt-Trigger Relaxation Oscillator

The 'Blinky' circuit is built using a Schmitt-Trigger relaxation oscillator as shown below. 

```{figure} img/blinky_block.png
:height: 200px

Block diagram of the blinky circuit
```

**Circuit Schematic:** 
We build the Schmitt Trigger out of cascade of a 16x, 16x and 4x inverter with a 4x inverter providing positive feedback around the second stage, resulting in hysteresis in the input-output transfer characteristic. Overall feedback around the Schmitt Trigger is created with an R-C network. LEDs are connected at the output of the second stage; the red LED ligths up when the output is high, and the green LED lights up when it is low.

```{figure} img/blinky_block_inv.png
:height: 250px

Implementation of the Schmitt Trigger for the blinky circuit using inverters
```



```{figure} img/blinky_relaxation_osc_v1.png
[LTSpice schematic](sim/blinky_relaxation_osc.zip) for the MOSbius realization of the blinky circuit  
```

**Building the Circuit with MOSbius:** You can use manual connections or use the on-chip switch matrix (Files: [bitstream](img/relaxation_osc_v1_bitstream.txt), [bitsteam_clk](img/relaxation_osc_v1_bitstream_clk.txt), [connections](img/connections_relaxation_osc_v1.json)). When using the on-chip connections, the solderless breadboard only requires and external resistor and capacitor, along with the LEDS.
```{figure} img/relaxation_osc_v1_IMG_2992.jpeg
Photo of the *blinky* setup using the on-chip connections; the external components are a 100K$\Omega$ resistor, a 10uF capacitor, and two LEDs with 47$\Omega$ resistors; the orange and blue wires connect to the ADALM2000 oscillscope channels `1+` and `2+` respectively; `1-` and `2-` are grounded; the ADALM `V+` provides the 2.5V power supply; digital channels `DIO8` and `DIO9` are used to feed the bitstream to the `CLK` and `DATA` pin of the MOSbius chip to program the switch matrix. 
```

```{tip}
A step-by-step guide to learn how to program the MOSbius chip is provided in [Programming the Chip Using the MOSbiusTools](../4_sw_support/MOSbiusTools.md)
```

**Measurements:**
Besides the blinking LEDs the following waveforms can be observed:
```{figure} img/osciloscope_waveoforms_2.png
Measured waveforms on *BUS01* and *BUS02*.
```
```{figure} img/osciloscope_waveoforms_3.png
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
```{figure} img/xy_timedomain.png 

Time domain waveforms to create the Schmitt Trigger characteristic between *BUS01* and *BUS04*
```
```{figure} img/xy_xy.png
Schmitt Trigger characteristic between *BUS01* and *BUS04* using X-Y plotting
```

The Schmitt trigger has a inverting characteristic with a hysteresis of approx. 500mV centered at about 1.25V.

[^exactanalysis]: A more detailed analysis can be performed using the expressions for the exponential charging and discharging waveforms.
[^commentsim]: The current LTSpice library for the chip components is using public domain 0.25um CMOS models and does not include accurate models of the on-chip layout and ESD parasitics; however, for low-frequency circuits qualitively accurate simulations can be obtained.  