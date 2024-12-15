# Lab 1: Basic Measurements Solution

## DC Transfer Characteristic of a Resistive Divider
![Fig. Connections for resistor divider and X-Y plot. ](img/Ramp_X_Y_Resistor_Divider_Circuit.png)
![Fig. Resistor divider and X-Y plot. ](img/Ramp_X_Y_Resistor_Divider_Result.png)
As shown in the figure, $V_{2+}=\frac{V_{1+}}{2}$ so the gain of this circuit is 0.5. 

## I-V Transfer Characteristic of an LED Diode
![Fig. Connections for LED diode and X-Y plot.](img/Ramp_X_Y_Diode_Circuit.png)
![Fig. LED diode I-V curve.](img/Ramp_X_Y_Diode_Result.png)
In forward bias, the diode conducts after a certain forward voltage (for this orange LED, it is around 1.8V) is reached. Then, the current rises exponentially with the forward voltage. For other colors, you could take a look at [this website](https://lednique.com/current-voltage-relationships/iv-curves/).
![Fig. Typical IV curves for various colours of LEDs](img/IV_Diode_Color.png)
## Frequency Response of RC Circuits
Here are some examples of calculations:
![Fig. Analysis of frequency response of RC networks](<img/Analysis_frequency_response_of_RC_networks.png>)

Here are some examples of measurements:
![Fig. Frequency response of RC networks. ](img/Frequency_Response_of_RC.png)

Here are some calculations for the other 2 RC circuits. For C, the transfer function can be written as $H(s)=\frac{\frac{1}{sC_1}+R_2}{R_1+R_2+\frac{1}{sC_1}}=\frac{s+\frac{1}{R_2C_1}}{s+\frac{1}{C_1(R_1+R_2)}}$. There should be one zero at around 1MHz and one pole at around 100kHz. For D, the transfer function can be written as $H(s)=\frac{s+\frac{1}{R_2C_1}}{s+\frac{R_1+R_2}{C_1 R_1 R_2}}$. There should be one zero at around 10kHz and one pole at around 100kHz. 
![Fig. RC network (C,D) results.](img/RC_Network_CD_Result.png)
## Step Response of RC Circuits
Here are some example calculations:
![Fig. Analysis of the RC circuit.](<img/Calculation_and_Analysis_of_RC_networks.png>)
Here are some example measurements:
![Fig. Step response of RC networks.](img/Step_Response_of_RC.png)
