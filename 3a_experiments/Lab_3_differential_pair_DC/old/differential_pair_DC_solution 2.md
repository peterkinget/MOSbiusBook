# Lab3: Solution 

```{warning}
This solution needs to be updated to match the latest lab assignment
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

1. Measure the common-mode gain. Plot $V_{CS}-V_{COM}$ and $V_{OUT}-V_{COM}$
   ![Fig. Circuit implementation for NMOS diff-pair common mode response measurement.](img/NMOS_diff_pair_CM_Circuit.png)
   ![Fig. NMOS diff-pair common mode response.](img/NMOS_diff_pair_cm_measure_result_4k7.png)
2. Measure the differential gain with a 1.25V common-mode voltage. 
    ![Fig. Circuit implementation for NMOS diff-pair differential mode response measurement.](img/NMOS_diff_pair_DM_Circuit.png)
    ![Fig. NMOS diff-pair differential mode response with VCOM=1.25V.](img/NMOS_diff_pair_dm_measure_result_4k7.png)
1. Explore how the differential gain varies with changing common mode input voltage.
    The circuit connections are the same as the previous measurement. 
    ![Fig. NMOS diff-pair differential mode response with different common-mode voltage.](img/NMOS_diff_pair_dm_measure_result_CMvaries.png)
>Within its operating range, the differential output gain of a diff-pair is independent of the common-mode input voltage.
1. Investigate more on differential gain and input/output range. ![Fig. Circuit implementation for the last measurement. ](img/NMOS_diff_pair_DM_Circuit_RIVary.png)
![Fig. NMOS diff-pair differential mode response with different load and current.](img/NMOS_diff_pair_dm_measure_diffR_Current.png)

