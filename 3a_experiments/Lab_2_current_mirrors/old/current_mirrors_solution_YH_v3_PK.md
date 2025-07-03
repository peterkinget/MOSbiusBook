# Lab 2: Solution
```{note}
The results presented here may differ from yours. If you chose different load resistor values, the current measured can be slightly, or a lot, different depending on your choices and the resulting channel-length modulation. Also there will be variations across chips used in the experiments. 
```
## Some Theory and Simulations
```{note}
This section is not required in your report
```

Some brief theory and spice simulation results to understand the operation of MOS current mirrors. 

### Single MOS Transistor Operation

* __IDS vs VGS/VDS:__ 
Review the relationship between IDS current and VGS/VDS voltages, including the square law model and channel length modulation shown below. 
<!-- * __Diode Connected__ 
Diode connected (VDS=VGS) transistor IDS-VDS curves for 1X PMOS (Pin 68) and 1X NMOS (Pin 19) are on [this page (nMOS IDS-VGS Measurement vs Simulation)](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/6_iv_characteristics/plotting_i_v_data_sims_nmos.html) and [this page (pMOS IDS-VGS Measurement vs Simulation)](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/6_iv_characteristics/plotting_i_v_data_sims_pmos.html).  -->
* __IDS vs W/L:__
Review how IDS current depends on the MOSFET's aspect ratio (W/L).
* __Operating Regions:__
Review the MOSFET operating regions: cutoff, linear (triode), and saturation.

![<em>Fig.</em> Single transistor characteristics. IDS-VGS/VDS plot of NMOS transistors, square law, channel-length modulation and operating regions. ](img/Sigle_Trans_Charact.png)

### Current Mirror Operation Simulation
![<em>Fig.</em> Current mirror (1:1, 1:2, 1:4, 1:8) I-V characteristics with fixed IBIAS 200uA. ](img/NMOS_sweep_VDS_LTSpice.png)

The LTSpice simulation results shown above illustrate the following properties of CMOS current mirrors:
1. The current mirror typically cannot replicate the current with 100% accuracy. Because of channel-length modulation, it only does so when the VDS of the input and output MOSFETs is identical.
2. In an ideal current source, the output current remains constant independent of the voltage across it. However, due to the channel-length modulation, the current-mirror output current changes slightly when operating in the saturation region as VDS varies due to the finite output resistance. <!-- >. This change rate can be described by the output resistance (e.g. $R_{out\times 1}=\frac{\delta V}{\delta I}=\frac{2.5V-0.9V}{233uA-199uA}=47k\Omega$ and $R_{out\times 4}=\frac{\delta V}{\delta I}=\frac{2.5V-0.9V}{932uA-798uA}=11.94k\Omega\approx R_{outx1}/4$).-->
3. If the output VDS is too low, the output transistor operates in the linear region and the output current will deviate significantly from the input current. When operating in the linear region, the transistor behaves like a resistor with a current proportional to VDS; its conductance increases as the gate-source voltage increases. 


## Experiments & Results


### Measurement 1: IOUT vs IIN for 1:1 Current Mirror 

1. Test setup:
    ![<em>Fig.</em> Circuit implementation and measurement of IBIAS sweep.](img/NMOS_sweep_IBIAS.png)

1. Results: The current is $I_{measure}=\frac{V_{measure}}{470\Omega}$[^acc] and is plotted below. 
    ![<em>Fig.</em> Plot of 1：1 current mirror IOUT vs IIN with a 470 Ohms resistor for measurement.](img/NMOS_Sweep_IBIAS_result_470.png)

2. **Answer to Q1 "Is IOUT the same as IIN? If not, what are possible physical sources for the errors?":** 
- **Source 1:** When the output current is small, the output MOSFET's VDS is larger, resulting in the output current exceeding the input current. 

- **Source 2:** When the output current and input current are large (>1mA), the output current becomes lower than the input current, while the VDS of the output transistor is still larger than the of the input transistor. Hence channel-length modulation cannot explain this error. 

    A series resistor (~10 Ohms) between the source of M2 and ground reduces the effective transconductance of M2 (a.k.a. source degeneration) and can explain that current reduction (see simulation below). It seems there could be a parasitic routing resistance in the source path of M2. 

    ![<em>Fig.</em> Error verification for IBIAS Sweeping. A series resistor with several Ohms between the ground and the source of M2 can cause VGS dropping and thus ~30uA error when the current is larger than 1mA. ](img/NMOS_Sweep_IBIAS_result_error_rec.png) 

3. **Answer to Q2 "Increase the resistance used for the current measurement to 4.7KOhms. Are there any changes in the error between IIN and IOUT?":** 
    ![<em>Fig.</em> Plot of 1：1 current mirror IOUT vs IIN with a 4.7k Ohms resistor for measurement.](img/NMOS_Sweep_IBIAS_result_4P7k.png)
 
   The 1:1 current mirror now accurately replicates current only when the current is below $200\mu A$. As the current increases to $400\mu A$ and beyond, a noticeable error appears between the output current and the ideal output. 
   
   The primary cause is that output MOSFET M2 goes out of saturation when IOUT>$400\mu A$ since the MOSFET's VDS drops below 0.62V ($V_{DS}=V_{DD}-I_{OUT}\times R_{measure}=2.5V-400uA\cdot 4.7k\Omega=0.62V$); VGS is typically around 1.1 to 1.2V, the NMOS $V_{TH}$ is between 0.5V and 0.6V, so $V_{DS,sat} \approx V_{GS}-V_{TH} \approx 0.6V$. Thus, when the current exceeds $400\mu A$, M2 goes into the linear region. Now, as the input current further increases, the $V_{GS}$ increases, the $R_{DS} \to 0$ and the current goes to $2.5V/4700\Omega = 530\mu A$. 
   
### Measurement 2: 1:1 Current Mirror VDS Sweep 
1. **Measurement Setup**
    ![<em>Fig.</em>Connections for 1:1 NMOS current mirror VDS sweeping measurement. 1+ and 2+ channels are connected to the load resistor to measure the output current and VDS (Pin 20). W2 is one signal generator channel, which generates a ramp signal to sweep the VDS.](img/NMOS_sweep_VDS.png)
        
    - Tune the potentiometer to set the reference current as 200uA ($V_{measure}=200uA\cdot R_{measure}=94mV$); note that the current-measuring resistors are now both 470 Ohms. 

```{error}
first you say vov=0.5 and then 0.4 in the optional experiment ...

what is asymptote of Rout

why is this for 200uA, the manual asks 100uA?; we can keep it 200u and keep 400u for the optional but then need to adjust the numbers to sqrt{2}
```

2. **Results**
    ![<em>Fig.</em> Plot of 1：1 current mirror IOUT vs VDS with IREF=169uA and a 470 Ohms resistor for measurement.](img/NMOS_Sweep_VDS_result_470.png)

3. **Analysis:** 
    - IREF equals IOUT when the VDS of M2 is equal to the VDS of M1, both at 0.95V. 
    - For M2 to operate as a current source, the output voltage needs to be $\geq V_{ov}=(V_{GS}-V_{TH}) \approx 0.5V$ so that M2 is in saturation. 
    - You can estimate the output impedance of the current source as $R_{OUT} = \frac{\Delta V_{DS}}{\Delta I_{out}}=\frac{2.45-1}{220.08-201}\cdot10^6$ or $76k\Omega$ 

```{error}
Why did you change the current to 135 and 542 and not 400

bunch of changes might be needed below
```
3. **Optional "Change IBIAS to $400\mu A$":** 
    - Results:
    ![<em>Fig.</em> Plot of 1：1 current mirror IOUT vs VDS with IREF=135uA and 542uA (~4X) and a 470 Ohms resistor for measurement.](img/NMOS_Sweep_VDS_result_470_X4Current.png)

        - As IBIAS increases 4x, IOUT is now roughly 4x larger  
        - As IBIAS increases 4x, the point where VDS equals VGS shifts to the right.
        - The $V_{ov}$ doubles since roughly $V_{ov} = (V_{GS}-V_{TH}) \propto \sqrt{I_{DS}}$ so for M2 to operate as a current source, $V_{DS} \geq \approx 0.8V$ and the output voltage operating range of the current mirror has reduced.  
        - $R_{OUT}$ decreases since $R_{OUT} = V_{A}/I_{DS}$ <!-- for a given transistor which is due to the increased channel length modulation as Vov increases, which can also be verified $$R_{OUT}=\frac{\partial V_{DS}}{\partial I_{DS}}=\frac{1}{\beta Vov^2 \lambda}=\frac{V_{A}}{I_{D}}, $$ where $\beta=\frac{1}{2}\mu_n C_{ox}\frac{W}{L}$ and $\lambda V_{DS}=\frac{\Delta L}{L}$. We use the same transistors so $\beta$ are the same. Therefore, we expect Rout to decrease as Vov increases. --> $R_{OUT542u}=\frac{2-1}{(557.2-525)\cdot 10^{-6}}=31k\Omega$ and $R_{OUT135u}=\frac{2.3-1.1}{(148.2-137.1)\cdot 10^{-6}}=106k\Omega$.

        | IREF | W/L | Vov(V) | VGS(V) | Rout($k\Omega$) | 
        |  :----------:  |  :----------: |  :----------:  |  :----------:  |  :----------:  |
        | 135uA | 8um/0.5um | 0.4 | 0.9 | 31 |
        | 540uA | 8um/0.5um | 0.8 | 1.3 | 106 |


### Measurement 3: 1:X Current Mirror VDS Sweep
- Test Setup:

    ![<em>Fig.</em> Connections for 1:2 NMOS current mirror load resistance sweeping measurement.](img/NMOS_sweep_load_1_2.png)

```{error}
why show $\delta v$?
```
- Results:
    ![<em>Fig.</em> DC operating points expected from 1:X current mirrors.](img/NMOS_sweep_load_1_X_result.png)

    For accurate current mirroring, a key requirement is to keep VDS the same, so the load resistors need to be scaled inversely proportional with the output current. 

- Optional VDS Sweep:
    - Test Setup:
    ![<em>Fig.</em> Connections for 1:X NMOS current mirror VDS sweeping measurement.](img/NMOS_sweep_VDS_1_X.png)

    - Results:
    ![<em>Fig.</em> IOUT-VDS measured from 1:X current mirrors.](img/NMOS_sweep_VDS_measure_300uA.png)

    | Transistor | W/L | Vov(V) | Rout($k\Omega$) | VGS(V) |
    |  :----------:  |  :----------: |  :----------:  |  :----------:  |  :----------:  |
    | M1 | 8um/0.5um | 0.5 | 39.7 | 1.05 |
    | M2 | 16um/0.5um | 0.5 | 24.9 | 1.05 |
    | M3 | 32um/0.5um | 0.5 | 13.7 | 1.05 |
    | M4 | 64um/0.5um | 0.5 | 6.8 | 1.05 |

    - The output impedance is inversely proportional to the current and thus the W/L ratio since the $V_A$ for all transistors is the same given they have the same length.

[^acc]: Besides the accuracy of the voltage measurement by the scope, the tolerance of the resistor value also determines the accuracy of the current measurement. Typical resistor tolerances can vary from 10% to 5% to 1% or less, depending on the type of resistor you are using. Here we are using the 'nominal' resistor values, but consider using a high-precision multimeter to measure your resistor values. 