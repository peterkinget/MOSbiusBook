# Operational Transconductance Amplifiers

With the MOSbius chip you can build an OTA from scratch and then measure its DC, AC, transient, noise ... performance, including probing the waveforms at internal nodes. You have to choose a topology, select transistor sizes, and bias currents. You further have to add a frequency compensation network and feedback network. 

Many topologies can be built including:
* single-stage OTAs, 
* two-stage Miller-compensated OTAs, 
* folded-cascode OTAs, 
* and even a fully differential two-stage Miller-compensated OTA. 

The chip has enough transistors to build four single-ended OTAs making possible experiments of small analog systems. 

The student can do hand calculations to size the OTA, using a (gm/I) approach, run simulations to verify biasing, small-signal parameters and performance, and then compare measured results to calculations and simulations. 

Last but not least, the measurements require careful thinking about how to conduct the circuit-parameter characterization and how to deal with non-idealities like loading, parasitics or offsets (which are often overlooked in simulations). 


% **Two-Stage Miller-Compensated OTA with pMOS Input Pair**
% - [Two-Stage Miller-Compensated OTA with pMOS Input Pair](./mota-se-p-16/mota-se-p-16.md)
% 
% 
% **Two-Stage Miller-Compensated OTA with nMOS Input Pair**
% - [Two-Stage Miller-Compensated OTA with nMOS Input Pair](./mota-single-ended/mota-single-ended.md) (under construction)

<h2 id="two-stage-miller"> Two-Stage Miller-Compensated OTA with pMOS Input Stage</h2>


```{figure} img/Miller_OTA_pin_IMG_2989.jpeg
Solderless breadboard setup for the two-stage Miller-compensated OTA configured in unity-gain feedback
```

```{note}
This section is a work *in progress*. Many of the measurements presented here are relatively straightforward configurations. There are various methods to measure offset, DC gain, frequency response, noise, linearity, ... and it will be instructive to the student to explore some of these techniques. At this stage, we are often starting with simpler measurements not to overwhelm the student and to build some appreciation of the challenges involved in experimental characterization. 
```

<!-- <h2 id="keywords"> Keywords</h2> -->

## Keywords

<div style="display: flex; flex-wrap: wrap; gap: 0.5em;">

<a href="#schematic-design-and-operating-point" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">Schematic & OP</a>

<a href="#measuring-offset-and-dc-gain" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">DC Gain</a>

<a href="#measuring-offset-and-dc-gain" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">Offset</a>

<a href="#studying-the-frequency-response" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">OL Freq. Resp.</a>

<a href="#unity-gain-configuration" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">Unity Gain</a>

<a href="#non-inverting-configuration-with-11x-gain" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">11x Gain</a>

<a href="#measuring-the-input-stage-transconductance" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">Input Gm</a>

<a href="#open-loop-measurement-with-low-frequency-ota-feedback" style="padding: 0.4em 0.8em; background-color: #007acc; color: white; text-decoration: none; border-radius: 5px;">Noise</a>

</div>

<!--
## Table of Contents
<details>
<summary style="font-size: 1.1em; font-weight: bold; cursor: pointer;">[click to expand]</summary>

- [Schematic Design and Operating Point](#schematic-design-and-operating-point)
- [Unity Gain Configuration](#unity-gain-configuration)
    - [DC Ranges](#dc-ranges)
        - [Gain and Offset from DC Sweep](#gain-and-offset-from-dc-sweep)
    - [Frequency Response](#frequency-response)
    - [Step Responses](#step-responses)
- [Non-Inverting Configuration with 11x Gain](#non-inverting-configuration-with-11x-gain)
    - [DC Transfer Characteristic](#dc-transfer-characteristic)
    - [Frequency Response](#frequency-response-1)
    - [Step Response](#step-response)
- [Measuring Offset and DC Gain](#measuring-offset-and-dc-gain)
    - [Offset Measurement](#offset-measurement)
    - [DC Gain Measurement](#dc-gain-measurement)
- [Studying the Frequency Response](#studying-the-frequency-response)
    - [Measuring the Open-Loop Transfer Function](#measuring-the-open-loop-transfer-function)
        - [DC Gain](#dc-gain)
        - [Unity-Gain Frequency](#unity-gain-frequency)
    - [The Effect of a Zero-Compensation Resistor](#the-effect-of-a-zero-compensation-resistor)
- [Measuring the Input-Stage Transconductance](#measuring-the-input-stage-transconductance)
    - [Additional Experiment Ideas](#additional-experiment-ideas)
- [Open-Loop Measurement with Low-Frequency OTA Feedback](#open-loop-measurement-with-low-frequency-ota-feedback)

</details>
-->

## Schematic Design and Operating Point


```{figure} img/Miller_OTA_pin.png
Simulation schematic of the two-stage Miller-compensated OTA including an external DC feedback for open-loop AC simulations
```

A two-stage Miller-Compensated OTA with a 4x pMOS input differential pair and a 16x nMOS second stage is biased with a nominal 1x current of 100uA. The files used for [programming](../4_sw_support/MOSbiusTools.md) are: [bitstream](img/Miller_OTA_pin_bitstream.txt) and [clk_bitstream](img/Miller_OTA_pin_bitstream_clk.txt) generated from [the spice netlist](img/Miller_OTA_pin.cir). 

The operating point of the transistors is obtained from an LTSpice simulation[^oppoint]:
```{figure} img/operating_point_printout.png
Simulated DC operating point
```
The pMOS input pair M1/M2 are biased towards weak inversion with a $(g_m/I)$ of ~12 and a $g_{m,1}$ of 1.1mS; the second stage M5 is biased in strong inversion with a $(g_m/I)$ of ~7 and a $g_{m,5}$ of 12mS.

Here is an overview of the OTA design:

| parameter  | expression | value |
| ----       | ---        | ---   | 
| $C_L$      |            | 1nF   |
| $C_{comp}$ |            | 150pF  |
| $R_{comp}$ |            | 200$\Omega$   |
| $f_u$      | $g_{m,1}/(2\pi C_{comp})$ | 1.16MHz|
| $f_2$      | $g_{m,5}/(2\pi C_{L})$ | 1.91MHz |
| $f_z$      | $g_{m,5}/(2\pi C_{comp})$ | 12.73 MHz|

We connect the $C_L$ between the output (BUS04) VSS (multiple pins can be chosen in the attached picture we used pin 29) and connect the series combination of $R_{comp}$ and $C_{comp}$ between the output (BUS04, pin29) and the input of the second stage (BUS03, pin28). 

## Studying the Frequency Response


### Measuring the Open-Loop Transfer Function

Measuring the open-loop transfer function of the OTA requires a careful setup in to address the issues of DC offset and the very large gain to be measured, possibly requiring very small reference signal sources. 

The OTA is configured with an $C_L$  of 1nF, a $C_{comp}$ of 150pF, and an $R_{comp}$ of 200$\Omega$. We embed the OTA in the following test schematic that addresses the measurement challenges:

```{figure} img/ac_open_loop/ac_open_loop.png
Test setup to measure the AC loop gain of the OTA; RA = 100K, RB = 1K, CA = 1uF; R2 = 1M and R1 is varied from 10K, 1K, to 100 to change the in-band gain; CB = 22uF//1uF; buffer amplifier is the AD8542 and CR = 1uF
```

The resistive divider R1, R2 from the output 'OUT' to the negative input 'inn' sets the AC closed-loop gain to $(1+R2/R1)$. However, we do not connect R1 to the common-mode, mid-supply voltage 'cm', but rather to a large capacitor CB of (1uF // 22uF). As a result, for DC and at very, very low frequencies the OTA is in a unity-gain feedback configuration, which is needed to avoid large amplification of the DC offset. 

The resistive divider RA, RB attenuates the input signal. This allows for a larger AC coupled signal from the signal source which will improve measurement accuracy[^source]. As long as we can rely on the input attenuation to be constant across the frequency range of interest, we can add it back to the measured gain from the signal source to the amplifier output to obtain the amplifier gain. RB connects to a buffered and decoupled common-mode, mid-supply reference. 

We configured the amplifier for closed loop AC gains of 101x, 1001x, 10,001x and performed network analysis measurements using the ADALM2000 between 'IN' and 'OUT', making sure to adjust the input signal amplitude to avoid out-of-range signals at the output. 

```{figure} img/ac_open_loop/AC_open_loop_80dB.png
Bode plot of the gain with the amplifier configured for a 10,001x gain (orange/purple); note that there is a 40dB attenuation of the input signal
```

```{figure} img/ac_open_loop/AC_open_loop_60dB_80dB.png
Bode plot of the gain with the amplifier configured for a 1001x gain (orange/purple) compared to the 10,001x gain case; note that there is a 40dB attenuation of the input signal
```

```{figure} img/ac_open_loop/AC_open_loop_40dB_80dB.png
Bode plot of the gain with the amplifier configured for a 101x gain (orange/purple) compared to the 10,001x gain case; note that there is a 40dB attenuation of the input signal
```
#### DC Gain
We note that for the 10,001x gain case, the low-frequency gain is limited by the DC gain of the OTA; at 100Hz we measure a DC gain of **69dB**. 

#### Unity-Gain Frequency
All plots overlap at high frequencies and indicate a unity gain frequency of about **1.10MHz** for the open-loop OTA; the notes under the plots analyze the various ways to measure the unity-gain frequency as the LF gain times the bandwidth vs the frequency at which the gain reaches -40dB; all cases give very similar results likely within the measurement accuracy of the setup. 

<!-- % ### Different Gain Settings (1x, 11x, 101x) -->
<!-- ```{figure} img/Miller_OTA_pin_different_gain.png
The frequency response of the OTA configured as a non-inverting amplifier with different gain settings
```
In this setup, a fixed feedback resistor of 100K$\Omega$ was used between the output and the inverting input; the gain was adjusted using 1K$\Omega$ and 10K$\Omega$, for a 101x and 11x gain respectively, from the inverting input to a 1uF capacitor to ground; they were not connected to a 1.25V reference since that would amplify the OTA offset; for the unity-gain configuration the output was shorted to the inverting input; the signal source is connected directly to the non-inverting input of the OTA and the input signals are kept sufficiently small to avoid out-of-range output signals.

We expect the **unity-gain frequency**, $f_u$, for the three cases to be identical and the measurements for the 101x and 11x are indeed close; for the unity-gain configuration, the $f_u$ is lower, which requires further investigation. 

The phase response for the three cases overlaps when beyond the 3dB frequency of the respective configuration; that is to be expected since it corresponds to the open-loop phase response. The phase measurements at high frequencies become erratic, due to measurement errors, in particular for the high gain configurations[^phasemeas].

The 101x phase curve can be used to estimate the **phase margin** for the 11x by measuring the phase shift at the 3dB frequency of the 11x configuration. Similarly for the 11x and 1x cases.  -->

### The Effect of a Zero-Compensation Resistor
`<Preliminary, needs more description and work>`

```{figure} img/Miller_OTA_pin_R_noR.png
The frequency response of the OTA configured as a 11x non-inverting amplifier with a Miller compensation with a 200$\Omega$ or no zero-compensation resistor
```
Here we measure the effect of the zero-compensation resistor; we note an improvement in the phase response when the resistor is present. When the frequency is sufficiently above the 3dB frequency of the closed loop gain, we observe the open-loop phase response. The resistor improves the phase shift measurably. 


## Unity-Gain Configuration


We now put the OTA in a unity gain configuration by connecting the output (BUS04, pin 29) to the negative input (pin 7).

### DC Signal Ranges

```{figure} img/unity_gain/dc_sweep_output_with_XY.png
:name: DC-ranges

The measured DC transfer characteristic of the OTA in unity-gain feedback (XY-plot, right) measured using a sawtooth input (left)
```

Applying a rail-to-rail, low-frequency, sawtooth waveform to the positive input allows the measurement of the signal ranges. The output follows the input for inputs between about 0.57V and 2V

```{figure} img/unity_gain/dc_sweep_all.png
Measurement of all internal OTA nodes for a rail-to-rail input signal; CH1 was kept on the input, while CH2 was moved to different nodes and 'snapshots' were taken and saved.
```

```{figure} img/unity_gain/sim_dc_sweep_all.png
Simulated internal nodes of the OTA with a rail-to-rail input signal
```

Measured and simulated internal voltage nodes are qualitatively similar to some extent but there are important differences. The output (BUS04), BUS02, and BUS03 behavior are quite different for low input voltages; the BUS03 behavior for high input voltages are also quite different. For an input of 1.25V, the correspondence between measurement and simulation is very good. The differences warrant further investigations; they could be due to limited modeling accuracy of the simulated circuits given that in the experimental device all nodes are connected off-chip. This introduces additional parasitics (pads, pins, ESD) and the measurement equipment also introduces additional loading.

### Gain and Offset from DC Sweep

Taking the Vout-Vin data measured with the sawtooth input into a jupyter notebook and performing linear regression using the `scipy.stats.linregress` function, we get the following fits:

```{figure} plot_dc_sweep_meas/output_11_0.png
Input-Output characteristic of the unity-gain buffer with a linear fit for Vin $\in$ [0.65, 1.85]
```

```{figure} plot_dc_sweep_meas/output_12_0.png
Zoom in for the input-output characteristic and linear fit
```
We then run the fitting for different input voltage ranges:

    1.15 < Vin < 1.35
    Linear Regression: Vout = -0.0083 + 1.0046 Vin
    Linear Regression: Vout = 1.0046 (Vin + -0.0083)
    
    1.05 < Vin < 1.45
    Linear Regression: Vout = -0.0025 + 1.0000 Vin
    Linear Regression: Vout = 1.0000 (Vin + -0.0025)
    
    0.95 < Vin < 1.55
    Linear Regression: Vout = -0.0023 + 0.9999 Vin
    Linear Regression: Vout = 0.9999 (Vin + -0.0023)
    
    0.85 < Vin < 1.65
    Linear Regression: Vout = -0.0034 + 1.0006 Vin
    Linear Regression: Vout = 1.0006 (Vin + -0.0034)
    
    0.75 < Vin < 1.75
    Linear Regression: Vout = -0.0062 + 1.0025 Vin
    Linear Regression: Vout = 1.0025 (Vin + -0.0062)
    
    0.65 < Vin < 1.85
    Linear Regression: Vout = -0.0105 + 1.0054 Vin
    Linear Regression: Vout = 1.0054 (Vin + -0.0104)

Ideally, small changes of the Vin range should not affect the fitting results, especially in the middle of the range; in practice, due to measurement accuracy limitations we see variations in the offset estimation at the mV level and in the gain estimation below the 1% level. We can conclude that the transfer curve has a gain which is close to 1.00 and an negative offset of a few mV. We investigate the offset measurement further in [Measuring Offset and DC Gain](#measuring-offset-and-dc-gain).

### Frequency Response

```{figure} img/AC_closed_loop/na_0dB_atten_various_gains.png
```
We measured the frequency response of the OTA in unity-gain feedback and various other feedback configurations. The feedback resistor from the OTA output to the negative input is varied to 200K, 100K, 10K, and short (OK), while the resistor from OTA negative input to AC ground (1uF cap) is kept at 10K and removed for the unity-gain configuration (0K); we expect gains of 21x, 11x, 2x, 1x or 26.4, 20.8, 6 and 0dB. With the negative input connected through a resistor and capacitor to ground, the OTA is always in unity gain for DC which avoids amplification of the offset. 

The ADALM2000 network analyzer function is used with the generator `W1` connected to the positive input of the OTA. The amplitude is adjusted to avoid out-of-range signals on the outputs; lower amplitudes are used for the higher gain cases; as a result, the high frequency measurement accuracy degrades in those cases. 

The measurements were saved in `.csv` files an plotted with a `python` Jupyter notebook. Beyond their respective bandwidth we expect the transfer functions to overlap, and this can indeed be observed in the magnitude and phase response. As expected the various transfer functions have a similar unity-gain frequency $f_u$ of about 770KHz. Beyond the bandwidth we measure close to the open-loop transfer function. At 770KHz the phase shift on the 26dB transfer function is -138deg, which can be used to estimate a phase margin for the 0dB case of approx. 42deg. The magnitude of the 0dB transfer function indeed shows some peaking. 

### Step Response
```{figure} img/unity_gain/unity_gain_p600m.png

At t=0s, positive step responses of the OTA configured as a unity-gain buffer. Notes provide a legend for the traces
```
Positive step responses are collected for the unity-gain case with the OTA output connected to the negative input; the signal generator `W1` is connected to the positive OTA input and and generates 200KHz square waves between 1.25V and 100mV, 200mV, 400mV and 600mV higher. 

As expected for the given phase margin, we do see some overshoot. The 100mV to 200mV step response scales linearly, however the higher amplitude step responses show the presence of slewing. 

```{figure} img/unity_gain/unity_gain_m600m.png

At t=0s, negative step responses of the OTA configured as a unity-gain buffer. Notes provide a legend for the traces
```

For the negative step responses, the signal generator `W1` generates 200KHz square waves between 1.25V and 100mV, 200mV, 400mV and 500mV lower. 

As expected for the given phase margin, we again see some overshoot. The 100mV to 200mV step response scales linearly, however the higher amplitude step responses show the presence of slewing, although less than for positive steps. 

## Non-Inverting Configuration with 11x Gain

We configure the OTA as a non-inverting 11x amplifier by connecting a 100K resistor between the output (BUS04) and the gate of M1 and a 10K resistor between the gate of M1 and a 1.25V DC bias; the bias is generated with a 20K potentiometer between VDD and VSS and a 47uF decoupling cap to VSS. 

### DC Transfer Characteristic
```{figure} img/dc_transfer.png
DC transfer characteristic measured with a low-frequency rail-to-rail sawtooth input
```
<!-- `<TBD Need to add the signal range measurements of the internal nodes>` -->

### Frequency Response
```{figure} img/network_comp_and_no_comp.png
Measured AC transfer characteristic of the compensated amplifier (purple) and uncompensated amplifier (red) in a 10x non-inverting configuration
```
The DC gain is 20.7dB (10.8x), the unity-gain frequency, $f_u$, is 756kHz, and the phase shift at $f_u$ is -(180-44)deg. Note that we are doing a closed-loop measurement but above the 3dB bandwidth of the amplifier (i.e. the unity-gain frequency of the loop gain), the closed-loop response is close to the open-loop response. 

```{figure} img/network_comp_no_r_and_comp.png
Measured AC transfer characteristic of the compensated amplifier without $R_{comp}$ (purple) and compensated amplifier (red) with $R_{comp}$ in a 10x non-inverting configuration
```

### Step Response
```{figure} img/step_response_100mVpp.png 
Measured step response of the compensated amplifier (purple) in a 10x non-inverting configuration for a 100mVpp input signal
```
```{figure} img/step_response_20_50_100mVpp_comp.png
Measured step responses of the compensated amplifier in a 10x non-inverting configuration for a 20, 50 and 100mVpp input signal around 1.25V common mode[^csvplot]
```
```{figure} img/step_response_100mVpp_no_comp2.png 
Measured step response of the uncompensated amplifier (purple) in a 10x non-inverting configuration for a 100mVpp input signal
```
```{figure} img/step_response_20_50_100mVpp_comp_no_comp.png
Measured step responses of the compensated and uncompensated amplifier in a 10x non-inverting configuration for a 20, 50 and 100mVpp input signal around a 1.25V common mode
```

## Measuring Offset and DC Gain

```{figure} img/offset_dc_gain/Offset_DC_Gain_measurement.png
:scale: 75%
A circuit setup to measure the offset (keep red, remove green) and DC gain (keep green, remove red) of an operational amplifier; we used R1=1K, R2=100K, R3 = R4 = 10K
```
### Offset Measurement
Assuming R4 $\ll$ R2, the offset voltage $V_{os}$ will appear between 'B' and 'inp' as $(1+R2/R1)V_{os}$ or $101 V_{os}$ and between 'out' and 'inp' as $2(1+R2/R1)V_{os}$ or $202 V_{os}$ with R1 = 1K, R2 = 100K, and R3 = R4 = 10K. An AD8542 was configured in unity-gain feedback to buffer the common-mode voltage of 1.25V and apply it to 'inp'.

```{figure} img/offset_dc_gain/dc_offset_measurement.png

Oscilloscope traces obtained for the DC offset measurement
```
The measured voltages at 'B' (CH1) and 'out' (CH2) compared to 'inp' result in an offset measurement of -5.0mV and -5.2mV respectively. We note that the resistors used were 5% resistors. 

This offset is a combination of the systematic and random offset. Mulitple chip samples need to be measured to separate the systematic and random offsets. 

### DC Gain Measurement

We apply a VDC of approximately 0.5V and an 100Hz sinusoid of 200mVpp and then measure the voltage at 'B' and 'out'; VDC is adjusted to make sure the 'out' is within the output range of the amplifier.

Assuming R4 $\ll$ R2, $( V_{out} - V_{inp} ) = -R3/R4 (V_{AC} - V_{inp})$ so the AC gain is about $-2$. The voltage between 'inp' and 'inn' is $V_{out}/A$, so the voltage between 'B' and 'inp' is $-(1+R2/R1)V_{out}/A$ or $-101 V_{out}/A$. 

The ratio $V_{out, AC} / V_{B, AC} = -A/101$

```{figure} img/offset_dc_gain/dc_gain_measurement_scope.png
Measurement of 'out' (CH1) and 'B' (CH2) on the oscilloscope with a 100Hz input signal; the channels are AC coupled
```
Estimating the amplitude of the waveform at 'B' is difficult in the time domain using the oscilloscope. 

```{figure} img/offset_dc_gain/dc_gain_measurement_spectrum.png
Measurement of 'out' (CH1) and 'B' (CH2) on the spectrum analyzer with a 100Hz input signal
```
Using the spectrum analyzer, a better estimate of the ratio of $V_{out, AC} / V_{B, AC} $ can be obtained, and the OTA gain $A$ at 100Hz is estimated to be **68.6dB**. 



## Measuring the Input-Stage Transconductance


The DC transfer characteristic of the input differential pair (M1, M2) requires the measurement of its differential output current w.r.t. a differential input voltage. We repurpose the second stage, M5, as a transresistance stage[^tia], by placing a 1K$\Omega$ resistor R1 from drain to gate. 
```{figure} img/Miller_OTA_gm_stage1.png
The second stage, M5, is configured as a transresistance amplifier to measure the differential output current of the differential input pair (M1, M2) when driven with external input signals. 
```

We now apply a differential sawtooth waveform, with a common-mode of 1.25V, to the gates of M1 and M2 (using the waveform generators on the ADALM2000), and measure the gate and drain voltage of M5.
```{figure} img/Miller_OTA_pin_Gm1_1K_200u_G_D_M5.png
```
The gate voltage of M5 is not changing much, as expected since M5 acts as a transresistance stage. Any current pushed into the gate of M5 by M2 or M4 is going into the feedback resistor R1. 

```{figure} img/Miller_OTA_pin_Gm1_1K_200u_dif.png
```

Measuring the voltage across the feedback resistor R1, we can determine the output current of the differential pair (M1, M2); the current mirror (M3, M4) takes the output of M1 and subtracts it from M2, the difference flowing into R1. With an X-Y plot on the oscilloscope we recognize the typical S-curve response of a differential pair. 
```{figure} img/dc_transfer_Gm1_meas_sim.png
```

We varied the bias current for the current-mirror diode M8 from 63uA to 100uA to 200uA. We saved the measurement results in `.csv` files which we imported into a python notebook and plotted the measured curves along with simulated curves. The correspondence is quite good, taking into account the limitations of the measurements, as well as the transistor models used for the simulation. We note that since this is a current-biased circuit, it is more robust. 

```{figure} img/dc_transfer_Gm1_meas_sim_zoom.png
```
Zooming in around the origin we observe an offset of the differential pair of -10 to -15mV. There are better techniques to measure the offset, but this gives a rough estimate. 

### Additional Experiment Ideas 

This experiment can now be expanded to measure responses to common-mode input signals, or to measure responses across frequency. 

A more sophisticated transresistance amplifier can be constructed to try to improve measurement accuracy. Averaging the waveforms will improve measurement accuracy as well. 

## Open-Loop Measurement with Low-Frequency OTA Feedback


```{figure} img/Miller_OTA_pin_feedback.png
The OTA is placed in DC feedback by using an active unity-gain buffer with a very low bandwidth 
```
When using a very low bandwidth active unity-gain feedback path, the OTA is in open loop for frequencies higher than $A_{DC}/(2\pi R_{DC}C_{DC})$, where $A_{DC}$ is the DC gain the OTA under test. 

When applying no input signal, the OTA will amplify its own noise by its open-loop gain. 
```{figure} img/open_loop_output_w_histogram2.png
The output of the OTA when placed in DC feedback but AC open loop; we observe the output noise of the OTA
```
```{figure} img/open_loop_output1.png
The output of the OTA when placed in DC feedback but AC open loop; we observe the output noise of the OTA at a different time scale
```
```{figure} img/open_loop_output_spectrum.png
The output of the OTA when placed in DC feedback but AC open loop; we observe the spectrum of the output noise of the OTA
```
This requires further analysis, but a rough analysis indicates that the noise is dominated by 1/f noise. 

<!-- ## To Do
<div style="text-align: right; margin-top: -1.5em;">
    <a href="#quick-navigation" title="Back to top" style="font-size: 0.9em; text-decoration: none;">↑ Back to top</a>
</div>

* Show the effect of zero compensation resistor
    * take unity-gain case since phase margin is largest there
* Look at scaling of the step responses with amplitude via csv files
* Investigate the difference between the two frequency domain results
    * combine the frequency domain csv files
    * does this have anything to do with the input signal attenuator
    * or the feedback resistor value
* Why are the DC sweeps off?
* Do an inverting configuration
* Lower frequency for fu of 100KHz
* More comparison to simulation
* Non-linearity measurements -- distortion -->


[^source]: The ADALM2000 waveform generator is based on a 12-bit DAC; it is always best to generate as large a voltage as possible to avoid any effects of quantization noise; as we are trying to measure very large gains, we need very small input signals that would be limited by the quantization noise of the DAC; the analog input attenuator allows for larger waveform test signals to be used. 

[^oppoint]: The operating point information is extracted from the `.log` file of a `.op` simulation using the `<To be renamed>.py` script. 

[^csvplot]: The trace data was saved as `.csv` files and plotted using a Jupyter notebook for `python` with `matplotlib`.

[^phasemeas]: The network analysis module on the ADALM uses the oscilloscope and does not have very high sensitivity; for more accurate measurements a network analyzer should be used; alternatively, higher amplitudes can be used at higher frequencies where the gain becomes less, of course, while taking care not to overdrive the amplifier, and multiple measurements can be stitched together. 

[^tia]: This is not a very high performance transresistance amplifier given the limited gain offered by a single transistor stage, but it is sufficient for a first evaluation. Students can be encouraged to analyze the accuracy of the measurements or the difference between measuring differentially across the feedback resistor or simply measuring the output voltage. 