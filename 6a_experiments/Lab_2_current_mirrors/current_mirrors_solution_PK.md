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

* __$I_{DS}$ vs $V_{GS}$/$V_{DS}$:__ 
Review the relationship between $I_{DS}$ current and $V_{GS}$/$V_{DS}$ voltages, including the square law model and channel length modulation shown below. 
<!-- * __Diode Connected__ 
Diode connected ($V_{DS}$=$V_{GS}$) transistor $I_{DS}$-$V_{DS}$ curves for 1X PMOS (Pin 68) and 1X NMOS (Pin 19) are on [this page (nMOS $I_{DS}$-$V_{GS}$ Measurement vs Simulation)](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/6_iv_characteristics/plotting_i_v_data_sims_nmos.html) and [this page (pMOS $I_{DS}$-$V_{GS}$ Measurement vs Simulation)](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/6_iv_characteristics/plotting_i_v_data_sims_pmos.html).  -->
* __$I_{DS}$ vs W/L:__
Review how $I_{DS}$ current depends on the MOSFET's aspect ratio (W/L).
* __Operating Regions:__
Review the MOSFET operating regions: cutoff, linear (triode), and saturation.

```{figure} img/Sigle_Trans_Charact.png

Single transistor characteristics: $I_{DS}$-$V_{GS}$/$V_{DS}$ plots for NMOS transistors; square law; channel-length modulation; and, operating regions.
```

### Current Mirror Operation Simulation

```{figure} img/NMOS_sweep_VDS_LTSpice.png

Current mirror (1:1, 1:2, 1:4, 1:8) I-V characteristics with fixed IBIAS 200uA.
```


The LTSpice simulation results shown above illustrate the following properties of CMOS current mirrors:
1. The current mirror typically cannot replicate the current with 100% accuracy. Because of channel-length modulation, it only does so when the $V_{DS}$ of the input and output MOSFETs is identical.
2. In an ideal current source, the output current remains constant independent of the voltage across it. However, due to the channel-length modulation, the current-mirror output current changes slightly when operating in the saturation region as $V_{DS}$ varies due to the finite output resistance. <!-- >. This change rate can be described by the output resistance (e.g. $R_{out\times 1}=\frac{\delta V}{\delta I}=\frac{2.5V-0.9V}{233uA-199uA}=47k\Omega$ and $R_{out\times 4}=\frac{\delta V}{\delta I}=\frac{2.5V-0.9V}{932uA-798uA}=11.94k\Omega\approx R_{outx1}/4$).-->
3. If the output $V_{DS}$ is too low, the output transistor operates in the linear region and the output current will deviate significantly from the input current. When operating in the linear region, the transistor behaves like a resistor with a current proportional to $V_{DS}$; its conductance increases as the gate-source voltage increases. 


## Experiments & Results


### Measurement 1: $I_{OUT}$ vs $I_{IN}$ for 1:1 Current Mirror 

1. Test setup:
```{figure} img/NMOS_sweep_IBIAS.png
:height: 450px

Circuit implementation and measurement of IBIAS sweep.
```

1. Results: The current is $I_{measure}=\frac{V_{measure}}{470\Omega}$[^acc] and is plotted below. 

```{figure} img/NMOS_Sweep_IBIAS_result_470.png

Plot of 1:1 current mirror $I_{OUT}$ vs $I_{IN}$ with a $470\Omega$ resistor for current measurement.
```

2. **Q1 "Is $I_{OUT}$ the same as $I_{IN}$? If not, what are possible physical sources for the errors?":** 
- **Source 1:** When the output current is small, the output MOSFET's $V_{DS}$ is larger, resulting in the output current exceeding the input current. 

- **(Advanced - can be skipped) Source 2:** When the output current and input current are large (>1mA), the output current becomes lower than the input current, while the $V_{DS}$ of the output transistor is still larger than the of the input transistor. Hence channel-length modulation cannot explain this error. 

    A series resistor (~10 Ohms) between the source of M2 and ground reduces the effective transconductance of M2 (a.k.a. source degeneration) and could explain that current reduction (see simulation below). It seems there could be a parasitic routing resistance in the source path of M2. There might be other valid explanations as well and more experimental characterization is necessary to fully identify the underlying issue(s). 

```{figure} img/NMOS_Sweep_IBIAS_result_error_rec.png

Error verification for IBIAS Sweeping. A series resistor of several Ohms between the ground and the source of M2 can cause a $V_{GS}$ reduction and thus $\sim 30\mu A$ error when the current is larger than $1mA$.
```

3. **Q2 "Increase the resistance used for the current measurement to 4.7KOhms. Are there any changes in the error between $I_{IN}$ and $I_{OUT}$?":** 

```{figure} img/NMOS_Sweep_IBIAS_result_4P7k.png

Plot of 1:1 current mirror $I_{OUT}$ vs $I_{IN}$ with a $4.7K\Omega$ resistor for current measurement.
```

 
   The 1:1 current mirror now accurately replicates current only when the current is below $200\mu A$. As the current increases to $400\mu A$ and beyond, a noticeable error appears between the output current and the ideal output. 
   
   The primary cause is that output MOSFET M2 goes **out of saturation** when $I_{OUT}$>$400\mu A$ since the $V_{DS}$ of M2 drops below 0.62V ($V_{DS}=V_{DD}-I_{OUT}\times R_{measure}=2.5V-400uA\cdot 4.7k\Omega=0.62V$); $V_{GS}$ is typically around 1.1 to 1.2V, the NMOS $V_{TH}$ is between 0.5V and 0.6V, so $V_{DS,sat} \approx V_{GS}-V_{TH} \approx 0.6V$. Thus, when the current exceeds $400\mu A$, M2 goes into the linear region. Now, as the input current further increases, the $V_{GS}$ increases, the $R_{DS} \to 0$ and the current goes to $2.5V/4700\Omega = 530\mu A$. 
   
### Measurement 2: 1:1 Current Mirror $V_{DS}$ Sweep 
1. **Measurement Setup**
```{figure} img/NMOS_sweep_VDS.png
:height: 450px

Connections for the 1:1 NMOS current mirror $V_{DS}$ sweep measurement. 
```

- The 1+ and 2+ channels are connected to the load resistor to measure the output current and $V_{DS}$ (Pin 20).

- W2 is the signal generator channel that generates a ramp signal to sweep the $V_{DS}$.
        
- Tune the potentiometer to set the reference current to $200\mu A$, so $V_{measure}=200\mu A\cdot R_{measure}=94mV$; note that the current-measuring resistors are now both $470\Omega$. 

2. **Results**
```{figure} img/NMOS_Sweep_VDS_result_470_v2.png

Plot of the 1:1 current mirror $I_{OUT}$ vs $V_{DS}$ with $I_{REF}$=169uA and a $470\Omega$ resistor for measurement.
```

3. **Analysis:** 
    - $I_{REF}$ equals $I_{OUT}$ when the $V_{DS}$ of M2 is equal to the $V_{DS}$ of M1, both at 0.8V. 
    - For M2 to operate as a current source, the output voltage needs to be $\geq V_{ov}=(V_{GS}-V_{TH}) \approx 0.35V$ so that M2 is in saturation. 
    - You can estimate the output impedance of the current source as $R_{OUT} = \frac{\Delta V_{DS}}{\Delta I_{out}}=\frac{2.1-1.1}{223.78-205.74}\cdot10^6$ or $55.4K\Omega$ 

3. **Optional: "Change IBIAS to $800\mu A$":** 
```{figure} img/NMOS_Sweep_VDS_result_470_X4Current_V2.png

Plot of the 1:1 current mirror $I_{OUT}$ vs $V_{DS}$ with $I_{REF}=135\mu A$ and $542 \mu A$ (~4X) and a $470\Omega$ resistor for measurement.
```
 - Results:
    
    - As $I_{REF}$ increases 4x, $I_{OUT}$ is now roughly 4x larger  
    - The $V_{ov}$ doubles since roughly $V_{ov} = (V_{GS}-V_{TH}) \propto \sqrt{I_{DS}}$ so for M2 to operate as a current source, $V_{DS} \geq \approx 0.7V$ and the output voltage operating range of the current mirror has reduced.   
    - As $I_{REF}$ increases, $V_{GS}=V_{TH}+V_{ov}$ increases, and the point where $V_{DS}$ equals $V_{GS}$ shifts to the right.    
    - $R_{OUT800u}=\frac{1.9-0.8}{(831.17-777.15)\cdot 10^{-6}}=20.3k\Omega$ while $R_{OUT200u}=55.4k\Omega$. Theoretically, we expect a 4x reduction since $R_{OUT} = V_{A}/I_{DS}$ but this is not fully observed in the measurement. 
    - Summary

        | $I_{REF}$ | W/L | Vov(V) | $V_{GS}$(V) | Rout($k\Omega$) | 
        |  :----------:  |  :----------: |  :----------:  |  :----------:  |  :----------:  |
        | 200uA | 8um/0.5um | 0.35 | 0.8 | 55.4 |
        | 800uA | 8um/0.5um | 0.7 | 1.15 | 20.3 |


### Measurement 3: 1:X Current Mirror $V_{DS}$ Sweep
- Test Setup:

```{figure} img/NMOS_sweep_load_1_2.png
:height: 450px

Connections for the 1:2 NMOS current mirror load-resistor sweep measurement.
```

- Results:

```{figure} img/NMOS_sweep_load_1_X_result_v2.png

DC operating points expected for the 1:X current mirrors.
```
For accurate current mirroring, a key requirement is to keep $V_{DS}$ the same, so the load resistors need to be scaled inversely proportional with the output current. 

**Optional $V_{DS}$ Sweep:**
- Test Setup:

```{figure} img/NMOS_sweep_VDS_1_X.png
:height: 450px

Connections for the 1:X NMOS current mirror $V_{DS}$ sweep measurement.
```

- Results:
```{figure} img/NMOS_sweep_VDS_measure_300uA.png

$I_{OUT}$-$V_{DS}$ measured from 1:X current mirrors.
```

| Transistor |Current(uA)| W/L | Vov(V) | Rout($k\Omega$) | $V_{GS}$(V) |
|  :--------:  | :--------: | :--------: |  :--------:  |  :--------:  |  :--------:  |
| M1 | 300| 8um/0.5um | 0.5 | 39.7 | 1 |
| M2 | 600|16um/0.5um | 0.5 | 24.9 | 1 |
| M3 | 1200|32um/0.5um | 0.5 | 13.7 | 1 |
| M4 | 2400|64um/0.5um | 0.5 | 6.8 | 1 |

- The output impedance is inversely proportional to the current and thus the W/L ratio since the $V_A$ for all transistors is the same given they have the same length.

[^acc]: Besides the accuracy of the voltage measurement by the scope, the tolerance of the resistor value also determines the accuracy of the current measurement. Typical resistor tolerances can vary from 10% to 5% to 1% or less, depending on the type of resistor you are using. Here we are using the 'nominal' resistor values, but consider using a high-precision multimeter to measure your resistor values. 