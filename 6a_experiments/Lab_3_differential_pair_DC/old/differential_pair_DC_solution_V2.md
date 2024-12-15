# Lab3: Solution 

```{warning}
This solution needs to be updated to match the latest lab assignment
Updated on Oct 27, 2024 -Yuechen
```

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
## Experiments

1. **Measure the DC Common-Mode Response.** Plot $V_{CS}-V_{COM}$ and $V_{OUT}-V_{COM}$
   ![Fig. Circuit implementation for NMOS diff-pair common mode response measurement.](img/NMOS_diff_pair_CM_Circuit.png)
   ![Fig. NMOS diff-pair common mode response.](img/NMOS_diff_pair_cm_measure_result_4k7.png)
2. **Measure the DC Differential-Mode Response.**
    ![Fig. Circuit implementation for NMOS diff-pair differential mode response measurement.](img/NMOS_diff_pair_DM_Circuit.png)
    ![Fig. NMOS diff-pair differential mode response with VCOM=1.25V.](img/NMOS_diff_pair_dm_measure_result_4k7.png)
    ![Fig. NMOS diff-pair $V_{CMSRC}$ vs ($V_{INp} - V_{INn}$) with Rload=4.7k and 2IREF=200uA](img/NMOS_diff_pair_Vcmsrc_Vindiff.png)


>This result is the most tricky to understand for the students. When the bias current is totally steered to one side of the diff-pair, the $V_{CMSRC}$ should be like a source follower. That is why there is still a triangle wave at the $V_{CMSRC}$ instead of a "constant voltage". And the gain of $V_{CMSRC}$ vs ($V_{INp} - V_{INn}$) should be around +0.5/-0.5. 

1. **DC Differential-Mode Response for Different Input Common-Mode Levels.**
 ![Fig. Circuit implementation for the last measurement. ](img/NMOS_diff_pair_DM_Circuit_RIVary.png)
![Fig. NMOS diff-pair differential mode response with different load and current.](img/NMOS_diff_pair_dm_measure_diffR_Current.png)
>($I_{DS,1}-I_{DS,2}$) should be equal to $\frac{V_{OUTp}-V_{OUTn}}{R_{L}}$, which means I just need to scale the data with $R_{L}$.

![Fig. plot the $I_{DS,1}-I_{DS,2}$ vs $V_{OUTp}-V_{OUTn}$ for the different bias currents and compare.](img/NMOS_diff_pair_dm_measure_diffIV.png)
3. **DC Responses for a Single-Ended Input Signal**
a. Differential Gain
- Use a triangle-wave, $100Hz$, differential input signal with a DC offset of $1.25V$ and a peak-to-peak amplitude of $500mVpp$, and measure the ($V_{OUTp} - V_{OUTn}$) vs ($V_{INp} - V_{INn}$).
![Fig. Single End Test 1: Diff Vout-Vin with Fixed Vco=1.25V](img/NMOS_diff_pair_Single_End_DiffOutIn.png)
- Connect *INn* to a fixed bias of $1.25V$ and use a triangle-wave, $100Hz$ signal with a DC offset of $1.25V$ and a peak-to-peak amplitude of $500mVpp$; measure the ($V_{OUTp} - V_{OUTn}$) vs ($V_{INp} - V_{INn}$)
![Fig. Single End Test 2: Diff Vout-Vin with Various Vco](img/NMOS_diff_pair_Single_End_Vari_Vco_DiffOutIn.png)
b. $V_{CMSRC}$ vs ($V_{INp} - V_{INn}$)
- Fixed Vco=1.25V
![Fig. Single End Test 3: Vcmsrc vs Diff Vin with Fixed Vco=1.25V](img/NMOS_diff_pair_Single_End_DiffVcmsrcIn.png)
- Various common-mode input voltage
![Fig. Single End Test 4: Vcmsrc vs Diff Vin with Various Vco](img/NMOS_diff_pair_Single_End_Vari_Vco_VcmsrcIn.png)
> As for differential input signal $V_{DIFF}=V_{INp}-V_{INn}$, they are exactly the same from -250mV to 250mV. However, the common mode $V_{CO}=\frac{V_{INp}+V_{INn}}{2}$ input are different. When the *INn* is fixed to 1.25V, $V_{CO}=(\frac{V_{INp}}{2}+0.625)V$, which means $V_{CO}$ varies with $V_{INp}$. Therefore, $V_{CMSRC}$ changes with $V_{INp}$.
1. **DC Differential-Mode Response for Different Bias Conditions.**
    The circuit connections are the same as the previous measurement. 
    ![Fig. NMOS diff-pair differential mode response with different common-mode voltage.](img/NMOS_diff_pair_dm_measure_result_CMvaries.png)
>Within its operating range, the differential output gain of a diff-pair is independent of the common-mode input voltage. 
