<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="img/NMOS_sweep_VDS_results.png" >
    <br>
    <div style="color:gray; 
    display: 
    color: #999;
    padding: 2px;"> 
    <em>Fig.</em> Settings in ADALM2000 to sweep the VDS from 0V to 2.5V. You need to make sure the "Time Base" is large enough for you to see your 1Hz trianlge signal. You can press "Single" button on the top right corner to get one cycle and change the horizontal/vertical scale to see them clearly.</div>
</center>

### Light up your chip and get start with ADALM2000

1. Make sure you can connect the ADALM2000 to your computer. You need to use “Power Supply,” “Signal Generator,” and “Oscilloscope” in this and the next section. So make sure you have watched the [tutorial video series](https://www.youtube.com/watch?v=LCf-_iREESQ&list=PLE6soOeVPOJ0Pj5sMui4KPDiTa7HY50y3), from video 2 to video 5. 
2. Go through this webpage [1. MOSbius Platform for MOS Circuit Labs](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/1_chapter_description/description.html), so that you can match the labels on the PCB with the ports of devices on the chip. 
3. 2. Plug the MOSbius PCB into a standard solderless breadboard as [Fig. 1.2](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/_images/MobiusPCB_v3_2024_3d_fullboard_ray_ortho.png) illustrates. Connect +/- or V+/GND ports on the PCB to V+/V- ports of the ADALM2000 and set the supply voltage to be 2.5V. Then, you will see the red LED on the PCB light up.
3. Tune the 25K potentiometers on the top and the left of the PCB to bias the pMOS and nMOS current mirrors respectively. From [1.2.2. Using the PCB: nMOS and pMOS Current Mirror Bias](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/1_chapter_description/description.html), you may need another ammeter to monitor the current. 
    - Or you can use your potentiometer (eg. 20K Ohm) with the middle port connected to the Pin 19 or Pin 68.
    - To measure the IBIAS current, you need to put a series resistor (eg.1k Ohm) to one side of the potentiometer and connected it to the VDD or GND. Measure the voltage drop across this resistor and calculate the bias current IBIAS, as shown in the following figure.
    - To measure the output current of the current mirror, you can put another resistor and measure the current in the same way. 
  


<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="img/NMOS_sweep_IBIAS.png" >
    <br>
    <div style="color:gray; 
    display: 
    color: #999;
    padding: 2px;"> 
    <em>Fig.</em> Connections for 1:1 NMOS current mirror IBIAS sweeping measurement. 1+ channel is connected to the series resistor with potentiometer to measure the bias current (Pin 19). 2+ channel is connected to the load resistor to measure the output current (Pin 20). </div>
</center>
<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="img/NMOS_sweep_VDS.png" >
    <br>
    <div style="color:gray; 
    display: 
    color: #999;
    padding: 2px;"> 
    <em>Fig.</em> Connections for 1:1 NMOS current mirror VDS sweeping measurement. 1+ and 2+ channels are connected to the load resistor to measure the output current (Pin 20). W2 is one signal generator channel, which generates a ramp signal to sweep the VDS. </div>
</center>
<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="img/NMOS_sweep_VDS_1_X.png" >
    <br>
    <div style="color:gray; 
    display: 
    color: #999;
    padding: 2px;"> 
    <em>Fig.</em> Connections for 1:X NMOS current mirror VDS sweeping measurement. 1+ and 2+ channels are connected to the load resistor to measure the output current (Pin 20, 21, 22, 23). W2 is one signal generator channel, which generates a ramp signal to sweep the VDS from 0V to 2.5V. </div>
</center>

Set up for ramp and X-Y plot
2. Set up the signal generator as shown. The reference current is set to be 200uA so the voltage across the resistor for measurement is around 100mV. You can sweep the VDD from 0-2.6V to make VDS sweep from 0-2.5V. However, the on-chip ESD module prevents the voltage from exceeding 2.5V. When using a voltage higher than 2.5V, be cautious of potential additional current flowing through the ESD protection circuit. Therefore we sweep the VDD from 0-2.5V and plot VDS from 0 to 2.4V. ![<em>Fig.</em> The settings in Signal Generator for 0-2.5V ramp signal](img/NMOS_sweep_VDS_ramp_setting.png)
3. Click on the "General Setting" button on the top right corner, you can use X-Y to directly plot the voltage measured across the 470 Ohms resistor versus VDS. Export the data or pick several points on the X-Y plot to draw a IDS-VDS curve. ![<em>Fig.</em> XY Plot of VDS sweep](img/NMOS_sweep_VDS_results.png)

## Suggestions
*  Compare your results with diode connected (VDS=VGS) transistor IDS-VDS curve for 1X PMOS (Pin 68) and 1X NMOS (Pin 19). The experiment and results are on [this page (nMOS IDS-VGS Measurement vs Simulation)](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/6_iv_characteristics/plotting_i_v_data_sims_nmos.html) and [this page (pMOS IDS-VGS Measurement vs Simulation)](https://www.ee.columbia.edu/~kinget/BOOKS/MOSbiusBook/6_iv_characteristics/plotting_i_v_data_sims_pmos.html).  
* Add a cascode transistor
    * estimate the DC output impedance
    * check the output range of the cascode current mirror by sweeping VDS with fixed IBIAS
    * Compare the result with the simple current mirror

### Measurement 4: Cascode Transistor
* Add a cascode transistor
    * estimate the DC output impedance
    * check the output range of the cascode current mirror by sweeping VDS with fixed IBIAS
    * Compare the result with the simple current mirror