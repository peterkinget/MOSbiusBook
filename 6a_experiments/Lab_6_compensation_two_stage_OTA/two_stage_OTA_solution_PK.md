# Lab 6: Solution

```{note}
Your results might differ slightly from the results presented here depending on the specific components used in your setup. 
```

## Experiments

### Two-Stage pMOS-input OTA without Compensation

#### Build the Test Circuit and Check the Bias Point

**Operation:** *at low frequencies* all capacitors are open circuits and given there is no current flowing into the gate of M1, *out* and *inp* are at the same potential. The gain from *inp* to *OTAout* is non-inverting and the gain from *OTAout* to *out* is inverting so the overall loop has negative feedback. 

When applying a reference of $1.25V$ to *in*, the feedback loop will generate the correct voltage at *inp* to keep *out* at $1.25V$ and 'store' it on $C_{B1}$ to compensate the offset of the two-stage OTA. 

At *higher frequencies* the impedance of the capacitor $C_{B1}$ starts to decrease and the feedback is determined by $R_1$ and $R_2$. The feedback network transfer function $\beta(s) = V_{inp}/V_{out}$ has a pole at $f_{p,\beta} = 1/(2\pi(R_1+R_2)C_{B1})$ and a zero at $f_{z,\beta} = 1/(2\pi R_1 C_{B1})$. For frequencies below $f_{p,\beta} = 1.6Hz$ the feedback factor is $1$ and for frequencies above $f_{z,\beta} = 1.6kHz$ the feedback factor is $R_1/(R_1 + R2) = 1/1,001$.

If $R_1$ is connected to a $1.25V$ reference instead, then the DC gain would be $(1 + R_1/R_2)$ and the offset would be amplified and likely saturate the output.

**Bias Point**
```{list-table}
:header-rows: 2
:align: "center"

* - Node
  - Voltage
* - 
  - [V]
* - in 
  - 1.275
* - inp
  - 1.280
* - OTAout
  - 1.280
```
The circuit is operating as expected. The difference between *in* and *inp* is the offset which is around $5mV$ in this measurement. However, we need to remember that the oscilloscope input has a DC impedance of $1M\Omega$ which can affect the measurements. In any case, the circuit is biased properly and we can proceed with the next steps. 

#### Build and Characterize an Input-Signal Attenuator

```{figure} img/meas/NA_40dB_input_attenuator.png

Measured Transfer function of the 40dB input attenuator
```
- The input attenuator has a similar transfer function as the feedback network discussed above. It passes DC and low frequency signals and attenuates high frequency signals. 
- The input attenuator offers a measured attenuation of -40.1dB, which is very close to the expected value of -40.08dB (1/101).
- At low frequencies there is a zero at $208Hz$ compared to a predicted value of $160Hz$; there is a pole at $1.6Hz$ which is outside the measurement range. 
- At high frequencies there is an additional zero at $8.2MHz$; this is likely due to a parasitic shunt capacitor across the resistor $R_{atten2}$ of $1.9pF$ which is not unreasonable[^respar]. 

#### Oscilloscope Measurements

#### Network Analyzer Measurements

```{figure} img/meas/NA_simple_pMOS_OTA_4x_CS_nMOS.png

Transfer function of the two-stage OTA without compensation.
```

For frequencies above $f_{z,\beta}$ the OTA operates in open loop. The LF gain is measured at $3kHz$ as $19.10dB$ yielding an effective gain of $59.10dB$. The unity-gain frequency $f_u$ for the open-loop transfer function corresponds to the $-40dB$ gain point in this measurement, i.e. $162kHz$. The slope between $10kHz$ and $100kHz$ is very close to -40dB/decade. There are two poles closely spaced at $59/40$ decades below $f_u$ or $5.4kHz$. 

In a unity-gain feedback application, the phase margin for this amplifier will be very small since the phase shift is close to $-180^o$. The phase measurements are unreliable since the output signal amplitudes are so small at that frequency that the network analyzer cannot measure the phase reliably. 

#### Measurement vs. Behavioral-Model Predictions

The behavioral models for the first and second stage were measured in [Lab 5](../Lab_5_simple_OTA_and_CS/simple_OTA_CS_PK.md):

| Stage | 1: Simple OTA | 2: CS | 
| --- | ---: | ---: |
| $C_{L}$ | $470pF$ | $4.2nF$ |
| $f_u$ | $228kHz$ | $102kHz$ |
| $g_m$ | $673\mu S$ | $3.0 mS$|
| $A_{DC}$ | $44\times$ | $43.7\times$ |
|  | $(32.9dB)$ |$(32.8dB)$|
| $R_{out}$ | $65.3K\Omega$  | $14.5K\Omega$ | 
| $f_1$ | $7.6kHz$ | $2.8kHz$ |

So when we combine the two stages we expect a LF gain of $65.7dB$, two closely spaced poles around $4.6kHz$ and a unity-gain frequency of $\sqrt{f_{1,1} f_{1,2} A_{DC,1} A_{DC,2}}$ or $202kHz$. 

The measured unity-gain frequency of $162kHz$ is close and the measured LF gain of $59.1dB$ is off by $6.5dB$ or $2.1\times$. The latter is not unexpected given that the feedback network has a zero only at $f_{z,\beta}$ of $1.6kHz$. 

#### Step Response Measurements

```{figure} img/meas/Step_simple_pMOS_OTA_4x_CS_nMOS.png 

Step response of the uncompensated two-stage OTA in a unity-gain configuration
```
As expected, the step response when the two-stage OTA is put in unity-gain feedback has significant ringing since the phase margin is close to zero. 

### Two-Stage pMOS-input OTA with Dominant-Pole Compensation

#### Calculations
- Replacing $C_{L1}$ with a larger capacitor will move the pole of the first stage to a lower frequency and make it the dominant pole. The pole of the second stage will not change and will be the non-dominant pole. 
- To get a decent phase margin, we aim for an $f_u$ of about $f_{nd}/2$ to $f_{nd}/3$. Given $f_2 = 2.8kHz$ we aim to make $f_u = 1kHz$. Then 

$$ 
C_{L1n} = \frac{A_{DC,2}\ g_{m,1}}{2\pi f_u} = 4.7\mu F
$$

- The dominant pole now moves to $f_u/(A_{DC,1}A_{DC,2}) = 0.5Hz$ and will not be observable in the measurement.

#### Network Analyzer Measurements

```{figure} img/meas/NA_two_stage_CD_4uF.png

Frequency response of the two-stage OTA with dominant-pole compensation; the input attenuator was not used. 
```
- The transfer function was measured without input attenuator. The measured $f_u$ is close to $1kHz$ with a phase shift close to $-90^o$.

#### Step Response Measurements

```{figure} img/meas/Step_no_miller_dominant.png

Step response (magenta) of the two-stage OTA with dominant-pole compensation in a unity-gain configuration
```
- Focusing on the magenta curve we observe a strongly damped step response. The output reaches about $67\%$ of its value (i.e. 3 vertical divisions) at about $175\mu s$ (i.e. 3.5 horizontal divisions). A $1kHz$ first-order system has a time constant of $160\mu s$ which is close. 

### Two-Stage pMOS-input OTA with Miller Compensation

#### Calculations

- First we assume that $C_c$ is sufficiently large that the pole of the second stage moves to 

$$
f_{2,n,est} = g_{m,2} / (2\pi (C_{L1}+C_{L2})) = 92.7kHz.
$$

- Now we set $f_u = f_{2,n,est}/1.5$ and find $C_c = 1.73nF$. We round this value up to $C_c = 2nF$ for some extra safety and to obtain an easily available capacitor value. So the unity gain frequency becomes: 

$$
f_u =53.6kHz.
$$

- Next, we can calculate the actual

$$
f_{2,n} = g_{m,2} C_c/(2\pi (C_c C_{L1} + C_c C_{L2} + C_{L1} C_{L2})) = 76.4kHz
$$

- The RHP zero is at 

$$
f_{z,RHP} = g_{m,2}/(2\pi C_c) = 239.7kHz
$$

- The phase margin is 

$$
PM = 90 - \arctan(f_u/f_{2,n}) - \arctan(f_u/f_{z,RHP})= 42.4^o
$$

- The damping[^damping] 

$$
\zeta = 0.5 \sqrt{f_{2,n}/f_u} (1-f_u/f_{z,RHP}) = 0.46
$$ 

- or a quality factor $Q=0.5/\zeta = 1.1$. We expect an overshoot in the order of $20$ to $25\%$.

```{note}
Fix the XXXX --> lab5 talk about the measurement setup for open loop measurement
```
#### Network Analyzer Measurements

```{figure} img/meas/NA_two_stage_OTA_Cc_2n_Cc_0.png

Transfer function of the OTA without compensation and with Miller compensation using a $2nF$ $C_c$
```
- The OTA was measured with a feedback factor $\beta = 1/1,001$ so that for frequencies beyond XXXX the we measure the open-loop response. 
- The generator input signal was attenuated by $A_{atten} = -40.1dB$.
- The unity-gain frequency for the OTA open-loop response is where we measure $A = -40dB$ so $f_u=58.5kHz$ and the phase shift at that frequency is $-134^o$.
- In a unity-gain feedback application, the loop gain will have a phase margin of $46^o$. 
- The measured values are very close to the expected values. 

#### Step Response Measurements

```{figure} img/meas/Step_Cc_2n_Rc_1K_0.png

Comparing the step responses for Miller compensation (yellow, purple) vs Miller compensation with RHP zero removal (green, cyan, and magenta)
```

- As expected the step response exhibits some ringing. Note that the screen capture include step responses with and without RHP removal (next section). Focusing on the ones without RHP removal (*REF4*, *CH2*), specifically looking at the *CH2* response for a $200mV$ step, the ringing has about one cycle and an overshoot $\approx 25\%$.  The $Q$[^Q] is roughly $1.0$ to $1.5$. 
- The performance is very close to the predictions. 
- For the linear vs non-linear response, see the next section. 

#### RHP Zero Compensation

```{figure} img/meas/Step_Cc_2n_Rc_1K_0_zoom.png 

Zoom in on the step responses for Miller compensation (yellow, purple) vs Miller compensation with RHP zero removal (green, cyan, and magenta)
```

- Looking closely at the beginning of the step response, we notice that the simple Miller compensation response starts by going in the wrong direction (i.e. dipping below zero) due to the presence of a RHP zero. 

**Calculations**
- Placing a resistor $R_c > 1/g_{m,2}$ in series with $C_c$ moves the zero from the RHP to the LHP. We chose $R_c = 3/g_{m,2} = 1K\Omega$ to have a safety margin; this results in a LHP zero at 

$$
f_{z,LHP} = \frac{1}{2\pi R_c (1-\frac{1}{g_{m,2}R_c})} = 119kHz.
$$

- A new third pole will appear at 

$$
f_3 = \frac{1}{2\pi R_c C_{L1}} = 339kHz.
$$

- The estimated phase margin now is 

$$
PM = 90 - \arctan(f_u/f_{2,n}) + \arctan(f_u/f_{z,LHP}) - \arctan(f_u/f_{3})= 70.2^o.
$$

- The damping[^damping] 

$$
\zeta = 0.5 \sqrt{f_{2,n}/f_u} (1+f_u/f_{z,LHP}) = 0.87
$$ 

- or a quality factor $Q=0.5/\zeta = 0.58$. We expect a significantly reduced overshoot. 

**Measurements**

```{figure} img/meas/NA_two_stage_OTA_Cc_2n_Rc_0_1K.png

Comparison of the frequency response of the two-stage OTA with Miller compensation with and without a RHP removal resistor
```
- Frequency Response:
    - Comparing the transfer functions for $R_c = 0$ and $R_c = 1K\Omega$ we see a significant improvement of the phase margin to $59^o$, although this is still lower than estimated. 
    - We also notice a change in the magnitude response. The LHP zero is at a lower frequency than the RHP zero and as a result the slope changes back to $-20dB/dec$ sooner. 
    - At higher frequencies the slope indeed increases again to $-40dB/dec$ due to the presence of the new third pole. The phase response measurement is unreliable so the additional phase shift of $-90^o$ due to the third pole cannot be observed. 

- Step Response:
    - See measurement plot higher up. 
    - Indeed the overshoot is greatly reduced when the series resistor $R_c$ is introduced. See the *REF1*, *REF2*, and *REF3* traces. 
    - Going from the *REF1* trace ($100mV$ step) to the *REF2* trace ($200mV$ step), we see a linear scaling. However then going to the *REF3* trace ($300mV$ step), the initial slope of the step response does not increase anymore; at this point, the output voltage is slew-rate limited. 

### Dominant-Pole vs Miller Compensation

```{figure} img/meas/Step_no_miller_dominant.png

Response to a $1.25$ to $1.35V$ step input using dominant pole compensation (purple), Miller compensation with RHP zero removal (green) and no compensation (cyan)
```
**Brief Comparison**
- Clearly the Miller compensation offers an amplifier with a much larger bandwidth while using the same 'resources' (i.e. $g_m$, $I_{DD}$). 
- Dominant pole compensation results in a unity-gain amplifier with a bandwidth of $1kHz$ whereas Miller compensation offers a bandwidth of $54kHz$. 
- The size of the compensation capacitor is significantly smaller. 




[^respar]: see [Resistors aren't resistors](https://www.edn.com/resistors-arent-resistors/)

[^damping]: See P. Kinget,*"EE4312 Notes: Feedback: Stability and Phase Margin"*, 2023. Strictly speaking the $GBW$ of the first stage needs to be used in this formula instead of the $f_u$, but we have no easy way to accurately measure the $GBW$ here so the $f_u$ is a close proxy. 

[^Q]: The quality factor can be estimated from the number of cycles one can visually observe in the step response. See P. Kinget, *"EE4312 Notes: Second Order Systems"*, 2023. 