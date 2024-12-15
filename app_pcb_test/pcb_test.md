# Testing Your MOSbius PCB

## Review the PCB Description
Read the [PCB Description](../1_chapter_description/description.md). Note all the `GND` are connected on the PCB and are connected to the `-` power rail terminal. 

## Visually Inspect the PCB
Preferably under a microscope or using a magnifier glass (e.g., use the magnifier glass app on your phone), inspect the PCB and verify that all components are properly soldered to the pads and that there are no 'cold' solder joints.  

## Remove the MOSbius Chip
Start your tests **without a MOSbius** chip in the socket. When removing the chip, make sure that your use ESD safe practices. Use an ESD grounding strap. Store the chip in a ESD safe container after removing it from the PCB. 

## Plug Your PCB in a Solderless Breadboard
```{figure} img/testing/Slide1.png
```
Make sure to orient your PCB correctly so that the top power rail is GND (or VSS) (typically colored blue) and the power rail below is VDD (typically colored red).

Push the PCB down and make sure that all pins are inserted properly, including the VDD/VSS pins on top. 

## Testing the Power Supply and Supply Protection

```{figure} img/testing/Slide2.png
```

* Apply 2.5V to `V+` and verify that the red `PWR` LED lights up; verify that the 2.5V voltage appears on the solderless breadboard power rail. Once this works you can choose to connect your external 2.5V power supply to the breadboard or the `V+` terminal. 
* Increase the supply voltage beyond 2.5V and verify that the `PWR` LED goes off; the protection circuit should cut the power to the chip. 

## Testing the Digital Level Shifters

```{figure} img/testing/Slide3.png
```
* Apply a 3.3V logic signal, e.g. a clock, to the data `DT` terminal on the top of the PCB. The blue `DATA` LED should light up or flicker, depending on the frequency you use. Make sure to properly connect the ground between the PCB and your signal source. 
* Using a scope, verify that the signal on the header is reduced in voltage to a 2.5V logic signal.
* (not shown) Repeat this for the clock `CK` (yellow `CLK` LED) and the enable `EN` (green `EN` LED).

## Testing the Manual Enable
```{figure} img/testing/Slide4.png
```
* Put a jumper on the `EM_PU` header and verify that the `EM` signal is 2.5V and that the orange `EN_MAN` LED ligths up. 

## Connecting the Logic Signals
```{figure} img/testing/Slide5.png
```
* You can now place jumpers to connect the logic signals to the chip. Figure shows the case for using the manual enable. See [Programming the Chip](../5_sw_support/MOSbiusTools.md).

## Testing the LDO

```{figure} img/testing/Slide6.png
```

If you plan to use an external power supply that is higher than 2.5V, you can the LDO to regulate the supply to 2.5V. 
* Apply 3.3V between `LDOI` and `GND`. No capacitive load is connected to the `LDOO` and it will not properly stabilize.
* If no chip is in the socket, you can place a jumper between `LDOO` and `V+` and use the PCB supply decoupling caps to load and stabilize the `LDOO`. Measure the `V+` waveform with a scope to verify that it is 2.5V and noise and ripple free. 
* If you have a chip in the socket, do not connect `LDOO` to `V+`, but connect an external $1\mu F$ capacitor between `LDOO` and `GND` (e.g. on a spare node the breadboard). Measure the `LDOO` waveform with a scope to verify that it is 2.5V and noise and ripple free. If so, you can remove the external capacitor and place a jumper between `LDOO` and `V+`.

*Typically not required:* If you connect a jumper on the LDO power good signal `LDO_PG`, it will go to the `LDOI` level if the LDO is operating properly. For most uses of the PCD you will not need this. 

## Insert MOSbius Chip

```{figure} img/testing/Slide7.png
```
* Verify that the socket is correctly soldered on the PCB. Pin 1 is in the upper left corner. 
* Insert a chip in the socket. Normally the chip only fits one way in the socket. Verify that the chip is seated properly. 

## Testing the Current Bias Potentiometers

```{figure} img/testing/Slide8.png
```
* **nMOS**: Connect a current meter at the `I_REFN` terminal. You should measure a current of tens of microamperes. Turn the potentiometer and verify that you can change the current bias. A typical current bias is $100\mu A$ so you can set it to this value for now. 

```{figure} img/testing/Slide9.png
```
* **pMOS**: Similarly, connect a current meter at the `I_REFP` terminal. You should measure a current of tens of microamperes. Turn the potentiometer and verify that you can change the current bias. A typical current bias is $100\mu A$ so you can set it to this value for now. 

## Ready, Start, Experiment!

Your PCB is now ready to use for your MOS circuits exploration. Have fun!