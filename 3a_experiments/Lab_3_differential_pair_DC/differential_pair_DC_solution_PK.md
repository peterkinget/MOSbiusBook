# Lab3: Solution 

```{note}
Your results might differ slightly from the results presented here depending on the specific components used in your setup. 
```
<!-- >
 Review your course notes on differential signals and the theory of the operation of the differential pair. 
## Principles & Simulations
1. Common Mode Response
   **Common Source Node:** After the current source and input transistors enter saturation, the current flowing through the input transistors remains equal and constant under common-mode conditions. If we ignore the effects of channel length modulation, this constant current implies that the VGS of the input transistors remains essentially unchanged. Therefore, at the common source (*SF* in the figure) of the input transistors, we observe a "Source Follower" as the blue curve shows.
   ![NMOS diff-pair common mode response with Rload=10k Ohm and bias current of 200uA.](img/NMOS_diff_pair_CM_BodyEffect.png)
   **Body Effect:** If you connect the body (P well in the deep N well) of NMOS (Pin 47) to the common source node, the M1 and M2 do not exhibit Body Effect (Blue Curve). However, when the body is connected to GND, Body Effect occurs due to the presence of VBS (Green Curve). It can be observed that the Body Effect becomes more pronounced as the VSB increases. For NMOS transistors, as VSB increases, the threshold voltage (VTH) rises. Therefore, to achieve the same Vov, the Common Source node voltage needs to be lower for a given gate voltage to maintain a higher VGS.
   ![NMOS diff-pair common mode response with Rload=10k ](img/NMOS_diff_pair_CM_1_X.png)
   **Bias Current:** When all transistor enter saturation, the current should not change (ignore channel modulation), so V(out+) should be stable as $V_{out+}=V_{DD}-I_{DS}R_{load}$. Thus, it can be observed from the graph that as the current increases, the minimum common mode voltage required for all transistors to enter saturation increases. DC operating range shrinks. Moreover, if the current is too large (X8), the voltage at V(out+) will be pulled down, which in turn may cause the input transistor to be pushed into the linear region ($V_{DS}<V_{dsat}$).
2. Differential Mode Response
   **Differential Gain and Common Mode Input:** Here, let's compare the differential pair with a Common Source Amplifier to evaluate the advantages of the differential pair. One of the most notable advantages of the differential pair is that, within its operating range, its differential output gain is independent of the common-mode input voltage.
   ![NMOS diff-pair common mode response with Rload=1.2k Ohm and different bias current. ](img/NMOS_diff_pair_DM_1_X.png)
   **Bias Current:** From the graph, we can see that not only is the gain proportional to the square root of the current ($gm\propto \sqrt{I_{DS}}$), but the output range (diff-input/output range, output common mode voltage) is also dependent on the current. 
   **Input/Output Range:** To observe it clearly, we could fix the output range by changing the load resistrance at the same time. Since $gm\propto \sqrt{I_{DS}}$ and $G_{diff}=gmR_{load}$ so the gain would reduce from 1:1 to 1:8. And from the figure, the output range is almost fix but the input range (x-axis) increases from -/+100mV to -/+250mV.
    ![NMOS diff-pair common mode response with Rload=1.2k Ohm and different bias current.](img/NMOS_diff_pair_DM_1_X_fixed_outrange.png)
--> 
## Experiments

**Bias Point**

The DC node voltages of the circuit when $V_{INp}=V_{INn}=1.25V$ are as follows:

```{figure} img/NMOS_diff_pair_cm_OP.png
:height: 400px
DC Operating Point
```

**DC Common-Mode Response** 

<!-- Plot $V_{CS}-V_{COM}$ and $V_{OUT}-V_{COM}$
 ![Fig. Circuit implementation for NMOS diff-pair common mode response measurement.](img/NMOS_diff_pair_CM_Circuit.png) -->

```{figure} img/NMOS_diff_pair_cm_measure_result_4k7.png

NMOS differential-pair common-mode responses vs $V_{COM} = V_{in}$
```
- For a common-mode input $V_{COM} > ~\sim 1V$ the differential pair starts to function. 
    - At that point the $V_{CMSRC} > ~\sim 200mV$ so that the current source transistor *MCM2* starts to operate in saturation. 
    - The output voltages *OUTp* and *OUTn* become $\sim 2.02V$ corresponding to a DC current of $102\mu A$ through the load resistors and the transistors *M1* and *M2*. 
- As $V_{COM}$ increases,
    - the output voltages do not significantly change.
    - The common-source voltage $V_{CMSRC}$ increases and tracks the $V_{COM}$; *M1* and *M2* operate as source followers. Due to the body effect, the threshold voltage $V_{TH}$ of *M1* and *M2* increases so that the $V_{CMSRC}$ deviates from $V_{COM} - V_{TH,0}$, where $V_{TH,0}$ is the threshold voltage for $V_{BS} = 0$.  

**DC Differential-Mode Response**
<!-- ![Fig. Circuit implementation for NMOS diff-pair differential mode response measurement.](img/NMOS_diff_pair_DM_Circuit.png) -->

```{figure} img/NMOS_diff_pair_dm_measure_result_4k7.png
Differential-mode response $(V_{OUTp}-V_{OUTn})$ vs $(V_{INp}-V_{INn})$ for $V_{CM}$=1.25V.
```
- When $|V_{INp}-V_{INn}| \leq \sim150-200mV$, the differential pair acts as a linear amplifier with a small-signal differential gain of $4.3\times$; outside that range, the differential output becomes constant and the small-signal differential gain is close to $0$. 
- In the linear region the gain is $g_m \cdot R_L = 4.3\times$, so $g_m = 914\mu S$ and $(g_m/I_{DS}) = 9.14 V^{-1}$ for the differential-pair input transistors.

```{figure} img/NMOS_diff_pair_Vcmsrc_Vindiff.png
NMOS diff-pair $V_{CMSRC}$ vs ($V_{INp} - V_{INn}$) with $R_L=4.7K\Omega$ and $2 I_{REF}=200\mu A$
```
- When the differential pair is it in its linear region, or $|V_{INp}-V_{INn}| \leq \sim200mV$, $V_{CMSRC}$ is nearly constant. 

- When $|V_{INp}-V_{INn}| > \sim200mV$, all the bias current goes to one of the differential-pair transistors, while the other transistor turns off. The $V_{CMSRC}$ then tracks the gate voltage of the transistor that is on, as in a source-follower circuit. 

**DC Differential-Mode Response for Different Bias Conditions**
<!-- 
 ![Fig. Circuit implementation for the last measurement. ](img/NMOS_diff_pair_DM_Circuit_RIVary.png)
-->
```{figure} img/NMOS_diff_pair_dm_measure_diffR_Current.png
NMOS diff-pair differential mode response $V_{OUTp}-V_{OUTn}$ vs $V_{INp}-V_{INn}$ for different loads $R_L$ and bias currents.
```
- Since the bias current and the load resistance $R_L$ are changed in tandem so that the DC voltage drop across $R_L$, $V_{DC,R_L}$ stays constant, the maximum differential output voltage remains the same for the different bias settings. 
- The differential gain for the transistors operating in strong inversion can be written as:

$$
A_{DD} = \frac{V_{OUTp}-V_{OUTn}}{V_{INp}-V_{INn}} = g_m R_L = (g_m/I_{DS}) V_{DC,R_L} = \frac{2V_{DC,R_L}}{V_{ov}} \propto \frac{1}{\sqrt{I_{DS}}}
$$

| $I_{DS}$ | $R_L$ | $A_{DD}$ | $gm$ | $V_{ov}$ |   $\sqrt2V_{ov}$  |
|  :----------:  |  :----------: |  :----------:  |  :----------:  |  :----------:  |:----------:  |
| | | (meas.) | (est.) | (est.) | (est.) |
| 100uA | $4.7k\Omega$ | 4.5 | $957uS$ | $209mV$ | $295mV$ |
| 200uA | $2.35k\Omega$ | 3.6 | $1.53mS$ | $261mV$ | $369mV$ |
| 400uA | $1.2k\Omega$ | 2.65 | $2.21mS$ | $362mV$ | $512mV$ |
| 800uA | $600\Omega$ | 1.85 | $3.08mS$ | $519mV$ | $734mV$ |

```{figure} img/differential_pair_add_gm_ids.png
:height: 400px 
Differential gain $A_{DD}$ and transconductance $g_m$ of the differential-pair transistors versus the bias current, and models based on a square-law $I_{DS}$-$V_{GS}$ dependency
```

- Summary
    - We estimated the gain $A_{DD}$ from the slope of the $(V_{OUTp}-V_{OUTn})$ vs. $(V_{INp}-V_{INn})$ curve close to the origin; the $g_m$ is then estimated from $A_{DD}$ and $R_L$; next, the $V_{ov}$ is estimated from $(g_m/I_{DS})=2/V_{ov}$ (assuming in strong inversion). The current in a differential pair switches over completely to one side for  $(V_{INp}-V_{INn})\approx \sqrt{2} V_{ov}$.
    - Reviewing the data in the table we observe a good correspondence between the saturation of the output voltages and the boundaries estimated by $\sqrt(2) V_{ov}$.
    - Reviewing the plot of the $A_{DD}$ and $g_m$ versus bias current $2 I_{DS}$, we observe a square root dependence; indeed, a plot of $g_m \propto \sqrt{I_{DS}}$ and $A_{DD} \propto 1/\sqrt{I_{DS}}$ referenced to the $400\mu A$ current data point gives an excellent fit. 

```{figure} img/NMOS_diff_pair_dm_measure_diffIV.png
Plot the $I_{DS,1}-I_{DS,2}$ vs $V_{INp}-V_{INn}$ for the different bias currents.
```
- We clearly observe the expected differential-pair behavior. Outside of the linear region, the current saturates to the bias current, which is being varied. 

**DC Responses for a Single-Ended Input Signal**

- The differential pair is biased with $2I_{REF}=800uA$ and $R_{Load}=1.2k\Omega$. 
- Differential Input Signal 
    - Input Signal: a triangle-wave, $100Hz$, differential input signal with a DC offset of $1.25V$ and a peak-to-peak amplitude of $500mVpp$

```{figure} img/NMOS_diff_pair_Single_End_DiffOutIn.png
($V_{OUTp} - V_{OUTn}$) (purple) vs ($V_{INp} - V_{INn})$ (orange) for differential input signal; $A_{DD} \approx 2.6$
```
```{figure} img/NMOS_diff_pair_Single_End_DiffVcmsrcIn.png
$V_{CMSRC}$ (purple) vs $(V_{INp} - V_{INn})$ (orange) for differential input signal
```
- Single-Ended Input Signal
    - Input Signal: *INn* is connected to a fixed bias of $1.25V$ and *INp* is connected to a triangle-wave, $100Hz$ signal with a DC offset of $1.25V$ and a peak-to-peak amplitude of $500mVpp$

```{figure} img/NMOS_diff_pair_Single_End_Vari_Vco_DiffOutIn.png
($V_{OUTp} - V_{OUTn}$) (purple) vs $(V_{INp} - V_{INn})$ (orange) for single-ended input signal; $A_{DD} \approx 2.6$
```
```{figure} img/NMOS_diff_pair_Single_End_Vari_Vco_VcmsrcIn.png
$V_{CMSRC}$ (purple) vs $(V_{INp} - V_{INn})$ (orange) for a single-ended input signal 
```

- Comparison
    - The differential output is the same in both cases, since the differential input signal $(V_{INp} - V_{INn})$ is the same in both cases. The differential gain $A_{DD}$ is close to $3\times$ in both cases. 
    - The $V_{CMSRC}$ is different. 
        - When driven differentially, there is no input common-mode signal, and since the differential pair is operated in its linear range, the $V_{CMSRC}$ is nearly constant.
        - When driven single-endedly, there is an input common-mode signal of $\sim(V_{INp} - V_{INn})/2$  which ideally appears on the common-source node $V_{CMSRC}$ of the differential pair; we measured  $\sim(V_{INp} - V_{INn})/2.8$ at the source which is due to the body effect (see next lab.)

**DC Differential-Mode Response for Varying Input Common-Mode Levels.**

```{figure} img/NMOS_diff_pair_dm_measure_result_CMvaries.png

Differential-mode response ($V_{OUTp} - V_{OUTn}$) vs $(V_{INp} - V_{INn})$ for different common-mode voltages.
```

- When operating within its common-mode input range, the differential gain of a differential pair is independent of the common-mode input voltage. 
