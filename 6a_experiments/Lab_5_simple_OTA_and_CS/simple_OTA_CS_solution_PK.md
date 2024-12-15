# Lab 5: Solution

```{note}
Your results might differ slightly from the results presented here depending on the specific components used in your setup. 
```

## Experiments

### Single-Stage pMOS OTA

#### Operation and Bias Point

```{figure} img/meas/OTA_DC_feedback.png 
:name: fig-ota-feedback
:height: 400px

Bode diagram for the various transfer functions of the OTA with DC feedback
```
**Operation:** 
- *At low frequencies* all capacitors are open circuits and given there is no current flowing into the gate of M2, *out* and *inn* are at the same potential. 

- When applying a reference of $1.25V$ to *in*, the feedback loop generates the correct voltage at *inn* to keep *out* at $1.25V$ and 'stores' it on $C_{B1}$ to compensate the offset of the two-stage OTA. 

- At *higher frequencies* the impedance of the capacitor $C_{B1}$ decreases and the feedback is determined by $R_1$ and $R_2$: 

$$\beta(s) = \frac{V_{inn}}{V_{out}} = \frac{1+s/(2\pi f_{z,\beta})}{1+s/(2\pi f_{p,\beta})}$$

- The feedback network transfer function $\beta(s)$ has a pole at $f_{p,\beta} = 1/(2\pi(R_1+R_2)C_{B1})$ and a zero at $f_{z,\beta} = 1/(2\pi R_1 C_{B1})$. For frequencies below $f_{p,\beta} = 0.03Hz$ the feedback factor is $1$ and for frequencies above $f_{z,\beta} = 33Hz$ the feedback factor is $R_1/(R_1 + R2) = 1/1,001 = -60dB$.

- If $R_1$ is connected to a $1.25V$ reference instead, then the DC gain would be $(1 + R_1/R_2)$ and the offset would be amplified and likely saturate the output.

- The closed-loop gain for the OTA in feedback $G(s) = out/in$ is shown in the Bode plot in {numref}`fig-ota-feedback`. When the magnitude of the open-loop gain of the OTA $|A(j\omega)|$ is larger than $|1/\beta(j\omega)|$ the loop gain $G(s)$ is $1/\beta(s)$. However when $|A(j\omega)| < |1/\beta(j\omega)|$, G(s) = A(s). So this setup allows us to measure the open-loop transfer function[^DCgain] of the OTA. In the Bode plot, the OTA has an assumed DC gain $|A(0)|$ of $50dB$ and for frequencies above $10Hz$ the $|G(j\omega)|$ will follow $|A(j\omega)|$; for the phase, this occurs at $\approx 100Hz$. So, when we do our measurements next, we have to look out if the DC gain of our device under test is below $60dB$ to be sure the setup gives us reliable results. 

**Bias point:** The circuit was biased with a *in* of $1.25V$ and both *inn* (pin 55) and *out (pin 54) settled to a voltage very close to $1.25V$ as expected. 

#### Oscilloscope Measurements

- For a 1kHz sinusoidal signal with a $1.25V$ DC offset, the following amplitudes where observed:

| Vin | Vout | Est. Gain |
| :---: | :---:| :---:| 
| $mV_{pp}$ | $mV_{pp}$ | V/V |
| 12 | 241 | 20 |
| 26 | 697 | 27 |
| 54 | 1350 | 25 |

- For the smallest input signal the waveforms showed the quantization steps of the waveform generator DAC. Up to an input amplitude of $54 mV_{pp}$ the OTA output was not showing signs of clipping, so that amplitude can be used in the network-analyzer measurements to get as large an output signal as possible. 

#### Network Analyzer Measurements

```{figure} img/meas/NA_simple_pMOS_OTA.png
Measured transfer function of the OTA with $C_{L1} = 470pF$
```
**Measurement with $C_L=470pF$**
- The network analyzer measurement between $100$ and $1MHz$ shows a clean first-order response for the OTA. 
- The LF gain $A_{DC}$ is $29.dB$ or $30.2\times$.
- Reviewing the Bode plot in {numref}`fig-ota-feedback`, for a $30dB$ DC gain, the measurement yields the open-loop transfer function of the OTA for frequencies beyond $\approx 1Hz$, so over the measurement range here, we are only observing the effect of the OTA. 
- The unity-gain frequency is $228kHz$, yielding a $g_m = 673\mu S$. 
- The first pole is at $7.63kHz$
- The output impedance can be estimated from $f_1$ or $A_{DC}$ and yield $44.4$ and $44.9K\Omega$ respectively. 
- Even at $1MHz$ the phase shift is still $-90^o$ so higher order poles will be at frequencies beyond $10MHz$. 

**Measurement with $C_L=0$**
- The results of the measurement without $C_{L1}$ have not been saved but yielded a significantly larger unity-gain bandwidth, indicating that the parasitics were sufficiently smaller than $C_{L1}$. 

#### Behavioral Model
```{figure} img/meas/OTA_model.png
:name: fig-ota-model-sol
:height: 200px
Schematic for the OTA behavioral model
```
Based on the measurements and our understanding of the simple OTA circuit we propose the OTA small-signal equivalent model in {numref}`fig-ota-model-sol` with the following parameters:

| Stage | 1: Simple OTA |
| --- | ---: | 
| $g_m$ | $673\mu S$ | 
| $R_{out}$ | $65.3K\Omega$  | $14.5K\Omega$ | 
| $C_{L}$ | $470pF$ | 


### 4x nMOS Common-Source Amplifier

#### Operation and Bias Point

**Operation:** 
- *M6* and *M8* form a current mirror and *M6* acts as a current source trying to force a $4\times I_{ref}$ current into the common-source transistor *M5*. This requires an adequate $V_{GS,5}$ that is provided by the OTA; it monitors the $V_{DS,5}$ and regulates $V_{GS,5}$ to set $V_{DS,5}$ at $V_{REF}$. Thanks to the inverting gain of *M5* the overall two-stage feedback loop with the OTA and *M5* is in negative feedback. 
- For *higher frequencies*, once the loop gain becomes less than $1$ and the bias feedback loop 'opens', *out* will become the gain of the CS stage M5 times *in*. Due to the presence of the large $C_{B2}$, the frequency response of the OTA is now limited to $\approx 0.47n \cdot 228k/47n = 2.28Hz$. Assuming the CS stage (i.e. the second stage in the biasing feedback loop) has a gain[^gainM5] of $40\times$, the unity-gain of the biasing feedback loop will be $\approx 90Hz$[^powerhum]. So beyond this frequency, we can measure the frequency response of the CS stage *M5*. 

**Bias Point:**

| Node | Voltage |
| --- | ---: |
| *OTAout* | $903mV$ |
| *out* | $1.28V$ |
| *$V_{REF}$ (pin 55)* | $1.275V$ |

- The $V_{REF}$ was slightly off from the desired $1.25V$, however, the *out*, or the drain voltage for *M5* is close to $V_{REF}$ indicating that the bias loop is working. It generates a $V_{GS}$ of $903mV$ for *M5*, which is a reasonable value. 


#### Oscilloscope Measurements

- For a 1kHz sinusoidal signal with a $0V$ DC offset, the following amplitudes where observed:

| Vin | Vout | Est. Gain |
| :---: | :---:| :---:| 
| $mV_{pp}$ | $mV_{pp}$ | V/V |
| 12.8 | 519 | 40 |
| 23.8 | 1,184 | 49.8 |
| 31.7 | 1,612 | 50.8 |

- For the smallest input signal the waveforms showed the quantization steps of the waveform generator DAC. Up to an input amplitude of $30 mV_{pp}$ the OTA output was not showing signs of clipping, so that amplitude can be used in the network-analyzer measurements to get as large an output signal as possible. 

#### Network Analyzer Measurements

```{figure} img/meas/NA_nMOS_CS_4x_CL_4n7_CL_0.png
Comparing the transfer function of the CS amplifier for $C_{L2} = 4.7nF$ and $0$.
```
**Measurement with $C_L=4.7nF$**
- The network analyzer measurements between $1KHz$ and $1MHz$ show a clean first-order response for the CS amplifier. 
- The LF gain $A_{DC}$ is $32.8dB$ or $43.7\times$.
- The unity-gain frequency is $102kHz$, yielding a $g_m = 3.01m S$. 
- The first pole is at $2.8kHz$
- The output impedance can be estimated from $f_1$ or $A_{DC}$ and yield $12.2$ and $14.5K\Omega$ respectively. 
- Even at $1MHz$ the phase shift is still $-90^o$ so higher order poles will be at frequencies beyond $10MHz$. 

**Measurement with $C_L=0$**
- The unity-gain frequency is $5MHz$; assuming a $g_m = 3.01mS$, the parasitic load capacitance, $C_{L,par}$, is $96pF$. The scope probe accounts for $30pF$ so that there are an additional $66pF$ of parasitics due to the chip packaging and breadboard. In any case, this measurement confirms that using a $C_L$ of $4.7nF$ guarantees that the external load capacitance dominates the other parasitics in the previous measurement. 

#### CS Amplifier Behavioral Model

Based on the measurements and our understanding of the common-source stage we propose the small-signal equivalent model in {numref}`fig-ota-model-sol` with the input applied to $V_{inn}$ and $V_{inp}$ grounded and with the following parameters:

| Stage | 2: Common-Source Stage |
| --- | ---: | 
| $g_m$ | $3.01m S$ | 
| $R_{out}$ | $14.5K\Omega$ | 
| $C_{L}$ | $4.7nF$ | 

[^DCgain]: If the DC gain of the OTA is larger than $(1+ R2/R1)$, we cannot accurately measure DC gain or first pole, but can still determine the unity-gain frequency etc. for the open-loop response. 
[^powerhum]: Whereas one might want to argue to further reduce the bandwidth of the bias feedback loop, one challenge is the coupling of AC power signals (i.e. $60Hz$ in the U.S.A.) into the loop and being amplified if they loop bandwidth is too low. 
[^gainM5]: At this point we do not know yet what that gain is since we are about to measure it, but we are using a guess. Once the measurement is complete, one should come back to this calculation to verify the assumptions. 

