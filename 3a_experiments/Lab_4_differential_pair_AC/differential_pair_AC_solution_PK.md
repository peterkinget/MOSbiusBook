# Lab 4: Solution

```{note}
Your results might differ slightly from the results presented here depending on the specific components used in your setup. 
```

## Experiments

### Bias Point

| Node | Voltage |
| --- | ---: | 
|     | mV |
| *INp* | 1,250 |
| *INn* | 1,250 |
| *OUTp* | 2,047 |
| *OUTn* | 2,030 |
| *CMSRC* | 306 | 
| *pin 19* | 878 |

- The $V_{GS}$ of *MCM1* and *MCM2* is $878mV$, which seems reasonable. The $V_{DS}$ of *MCM2* is $306mV$, which is sufficient for it to operate in saturation. 
- The $V_{GS}$ of *M1* and *M2* is $944mV$, which seems reasonable given the presence of the body effect for those transistors. 
- From the voltage drop across $R_L = \frac{1}{4}\cdot 4.7K\Omega$ we determine that $I_{DS1} \approx I_{DS2} \approx 382\mu A$, which again seems reasonable; the 1:8 current mirror is expected to have a mirroring error given that the $V_{DS}$ of $MCM1* and *MCM2* are different. 

### Standard Operation $C_{CS}=0$

#### Oscilloscope Measurements
```{figure} img/meas/Vout_in_200mVpp_SE.png
Measurement of *OUTp* (purple) and *OUTn* (orange) when the differential pair is driven with a single-ended $200mV_{pp}$ input at *INp*; the mathematical channels show the common-mode (green) and the differential mode (cyan).
```
- After connecting $V_{REF} = 1.25V$ to *INn* and *W1* set to $1.25V$ to *INp* and output offset was observed; $V_{REF}$ was adjusted to $1.224V$ to null the output offset. This would indicate a $26mV$ input offset for the differential pair which is rather larger but not unfeasible either, in particular since we are also limited by the measurement accuracy of the oscilloscope channels.

- For a $200mV_{pp}$ single-ended input, which has a $200mV_{pp}$ component, the differential output was $594mV$, yielding an $A_{dd}$ of $2.97\times$ or $9.5dB$. 

- At low frequencies, $A_{dd} = g_m R_L$ so $g_{m,1} = g_{m,2} = 2.53mS$ and $(g_m/I_{DS}) = 6.6 V^{-1}$ which seems reasonable. 

- For a $200mV_{pp}$ single-ended input, which has a $100mV_{pp}$ component, the common-mode output was $24mV$, yielding an $A_{cc}$ of $0.24\times$ or $-12.4dB$. 

- At low frequencies, $A_{cc} \approx \frac{1}{2} R_L/R_{CS}$, so $R_{CS}$ the output impedance of the current source is $2.46K\Omega$ which again seems reasonable for a transistor running $\approx 800\mu A$. 

#### Network Analyzer Measurements

**Differential Gain $A_{dd}$**

```{figure} img/meas/NA_Voutd_Vind_CL_1n2_0_Ccs_0.png
Measured differential gain with $C_L = 1.2nF$ (red) and $C_L = 0$ (orange/purple)
```
- The low-frequency $A_{dd}$ is $9.46dB \angle 0^o$ at low frequencies, which is very close to the oscilloscope measurement. 
- For $C_{L} = 1.2nF$, the measured bandwidth is $110kHz$, which is very close to the calculated bandwidth $1/(2\pi R_L C_L) = 113KHz$, indicating that $C_L$ dominates over the chip and breadboard parasitics.  
- For $C_{L} = 0 $, the measured bandwidth is $2.3MHz$, yielding a $C_{L,par}$ of $59pF$; the scope channel has a loading of $30pF$ leaving $30pF$ of additional parasitics due to the breadboard, packaging, etc., which is somewhat large. In any case, with $C_L = 1.2nF$ the operation is dominated by the external capacitor.

**Common-Mode Gain $A_{cc}$**

```{figure} img/meas/NA_Voutcm_Vincm_CL_0.png
Measured common-mode gain with $C_L = 1.2nF$ (red) and $C_L = 0$ (orange/purple)
```
- The low-frequency $A_{cc}$ is $-14.5dB \angle 180^o$ which is within $2dB$ of the oscilloscope measurement.
- For $C_{L} = 1.2nF$, the measured bandwidth is $96.7kHz$, which is close to the calculated bandwidth $1/(2\pi R_L C_L) = 113KHz$,
- For $C_{L} = 0 $, the measured bandwidth is $3.6MHz$, yielding a $C_{L,par}$ of $38pF$. **(Extra)** Assuming that the bandwidth in the common mode is limited by the load, this should be the same as for the differential mode. However, as we will see below, there could be a zero due to the capacitance from *CMSRC* to GND that extends the bandwidth of $A_{cc}$ to some extent. 

**Response at the Common Source**

```{figure} img/meas/NA_Vcmsrc_Vind_CL_1n2_Ccs_0.png
Measurement of the gain from *INp* to *CMSRC* (orange/purple) compared to $A_{dd}$ (red)
```

- A single-ended input signal $V_{in}$ applied to *INp* with *INn* AC grounded, has a common-mode component of $V_{in}/2$, which appears at the *CMSRC* node. The measured gain from *INp* to *CMSRC* is $-8dB$ which is $2dB$ lower that the theoretically expected gain of $\frac{1}{2}$. **(Extra)** This is most likely due to the body effect which makes the source-follower gain $=g_m/(g_m+g_{mb})$; if $g_{mb} = 0.25 g_m$, which is a reasonable assumption, an additional $2dB$ loss occurs. 
- The bandwidth is $> 10MHz$, which is not unexpected since it corresponds to the bandwidth of the source follower formed by *M1* and *M2* in parallel for common-mode signals and only loaded with a small $C_{CS}$.

**Common-Mode Rejection Ratio**
```{figure} img/meas/NA_Add_Acc_CL_1n2_Ccs_0.png
Measured $A_{dd}$ (red) and $A_{cc}$ (orange/purple) for $C_L=1.2nF$
```
- The $CMRR = A_{dd}/A_{cc}$ is almost constant across frequency and is $ 9.48 - (-14.7) = 24.2dB$

```{warning}
Next we are going to add a large capacitor from the *CMSRC* node to *GND*. In actual design this is NOT recommended. We do this here for educational purposes so you can learn about the effect of capacitance at the *CMSRC* node. 
```

### Studying the Effect of $C_{CS}$

#### Network Analyzer Measurements

**Differential Gain $A_{dd}$**

```{figure} img/meas/NA_Add_Acc_CL_1n2_Ccs_8n2.png
Measured differential gain (red) and common-mode gain (orange/purple) (see below) with $C_L = 1.2nF$ and $C_{CS}=8.2nF$
```
- There is no change in the $A_{dd}$ by adding $C_{CS}$.

**Common-Mode Gain $A_{cc}$**

```{figure} img/meas/NA_Voutcm_Vincm_CL_1n2_Ccs_0_8n2.png
Measured common-mode gain with $C_{L} = 1.2nF$ and $C_{CS} = 0$ (orange/purple) and $C_{CS} = 8.2nF$ (red)
```
- The low-frequency $A_{cc}$ remains $-14.2dB \angle 180^o$.
- For $C_{CS} = 8.2nF$, there is a zero at $9.65KHz$, followed by a pole at $\sim 100kHz$, and a pole at $\sim 200kHz$
    - The zero is due to $C_{CS}$ becoming a lower impedance than $R_{CS} \approx 2.46K\Omega$, which should occur at $7.9KHz$, which is close to the measurement.
    - One pole is due to the pole at the load $R_L //  C_L$ which is calculated to be at $113KHz$. 
    - One pole is due to the pole in the source follower which happens when $2 (g_m + g_{mb}) \approx 2\cdot 1.25 \cdot g_m$ becomes a higher impedance than $C_{CS}$; this is calculated to happen at $123KHz$.
    - The shape of the $A_{cc}$ corresponds to the predicted behavior. The presence of a large $C_{CS}$ increases $A_{cc}$ at higher frequencies, which will be detrimental for the $CMRR$. 

**(Extra) Common-Mode Gain $A_{cc}$ with $C_L = 0$**
```{figure} img/meas/NA_Voutcm_Vincm_CL_0_1n2_Ccs_8n2.png
Measured common-mode gain with $C_{CS} = 8.2nF$ and $C_L = 1.2nF$ (orange/purple) and $C_L = 0$ (red)
```
- When $C_L=0$ we can separate the effect of the pole due to the output load and the pole in the source follower. 
    - The zero remains at $9.65KHz$.
    - There is a pole at $119.3KHz$ which is due to the source-follower pole related to $2 (g_m + g_{mb})$ and $C_{CS}$ since $C_L = 0$; this is very close to the predicted value of $123KHz$. 
    - There is a pole at $2.7MHz$ which is due to the $R_L$ and the $C_{L,par}$ (see above).

**Response at the Common Source**

```{figure} img/meas/NA_Vcmsrc_Vind_CL_1n2_Ccs_8n2.png
Measurement of the gain from *INp* to *CMSRC* with $C_{CS}=8.2nF$ (orange/purple) and $C_{CS}=0$ (red) ($C_L =1.2nF$ for both)
```
- The measured gain from *INp* to *CMSRC* remains $-8dB$. 
- The pole in the source follower is predicted at $123KHz$ whereas the measurement shows $134KHz$ which is close. 

**Common-Mode Rejection Ratio**
```{figure} img/meas/NA_Add_Acc_CL_1n2_Ccs_8n2.png
Measured $A_{dd}$ (red) and $A_{cc}$ (orange/purple) for $C_L=1.2nF$ and $C_{CS}=8.2nF$
```
- The $CMRR = A_{dd}/A_{cc}$ remains $ 9.48 - (-14.7) = 24.2dB$ at low frequencies. 
- The $CMRR$ starts to degrade at $9.65KHz$ when the $A_{cc}$ starts to increase. 
- The $CMRR$ is close to $0dB$ above $100KHz$

### Differential Load Capacitors vs Single-Ended Load Capacitors

**$A_{dd}$ and $A_{cc}$ for $C_{CS} = 0 $** 

```{figure} img/meas/NA_Add_Acc_CL_0n6dif_Ccs_0.png
Measured $A_{dd}$ (red) and $A_{cc}$ (orange/purple) for a differential load and $C_{CS}=0$
```
- When using a differential load, the $A_{dd}$ frequency response does not change, but the $A_{cc}$ frequency response becomes very wideband since there is no more pole at the load for common-mode signals. 
- As a result, the $CMRR$ becomes $< 1$ at high frequencies. 

**$A_{dd}$ and $A_{cc}$ for $C_{CS} = 8.2nF $** 

```{figure} img/meas/NA_Add_CL_1n2se_CL_0n6dif.png
(Extra) Measured $A_{dd}$ for $C_L=1.2nF$ single-ended (red) and $A_{dd}$ for $C_L = 0.6nF$ differential (orange/purple) with $C_{CS}=8.2nF$ for both
```

- (Extra) This measurement overlays the $A_{dd}$ measurement with a single-ended and differential load and they are identical. 

```{figure} img/meas/NA_Add_Acc_CL_0n6dif_Ccs_8n2.png
Measured $A_{dd}$ (red) and $A_{cc}$ (orange/purple) for a differential load and $C_{CS}=8.2nF$
```
- By now adding $C_{CS}$, the $A_{dd}$ frequency response again does not change, but $A_{cc}$ becomes high at higher frequencies due to the lack of a pole and due to the zero introduced by $C_{CS}$; at high frequencies, $A_{cc} = g_m R_L$ or $9.4dB$.
- As a result, the $CMRR$ becomes $\ll 1$ at high frequencies. 

```{figure} img/meas/Vout_in_200mVpp_SE_CL_0n6d_Ccs_8n2.png
Oscilloscope measurement at $1MHz$
```
- Applying a $V_{in,SE}$ of $200mV_{pp}$ at $1MHz$ now results in suppression of the differential-mode signal component and in gain for the common-mode signal component; the $100mV_{pp}$ common-mode signal appears as a $272mV_{pp}$ common-mode signal at the output, corresponding to an $A_{cc} = 2.7\times$ which is $8.6dB$ and close to the predicted $9.4dB$.

