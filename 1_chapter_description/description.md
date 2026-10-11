# MOSbius Platform for MOS Circuit Labs

The MOSbius platform offers the MOSbius chips, adapter PCBs to place a chip on a solderless breadboard, and software tools to program the chip and process the measurement results. An LTspice library is also provided to run circuit simulations. The platform allows the (student) designer to experiment with and learn about MOS circuits in a uniquely hands-on environment. 

## MOSbius Twist Classic Chip
### Description
```{figure} img/MOSbius_schematic_updated.png
:height: 700px
Schematic of the MOSbius chip; pin numbers correspond to the numbering in the shift-register bitstream and the PCB labels
```
- The MOSbius chip is fabricated in a foundry 65nm CMOS technology and uses nMOS and pMOS thick-oxide transistors, i.e. the 2.5V I/O devices. It's packaged in a 68-pin PLCC package. 
- The **max. supply voltage $V_{DD}$ is 2.5V**. When the chip is in use, the supply should **always** be provided for ESD protection.
- Device sizing: The *'unit'* nMOS and pMOS have been sized to operate with an overdrive voltage $(V_{GS}-V_{TH})$ of 200mV for a drain-source current $I_{DS}$
  of 100$\mu$A. 
  - The unit nMOS has a (W/L) of 16 and dimensions 8$\mu$m/0.5$\mu$m, laid out with 2 fingers
  - The unit pMOS has a (W/L) of 48 and dimensions 24$\mu$m/0.5$\mu$m, laid out with 6 fingers
  - These devices are marked as size 1 on the schematic; the sizes of other transistors are shown as multiples of the unit devices; they are laid out with the same finger size but the appropriate number of fingers.
- Device configurations
    - nMOS
      - nMOS pair of size 1, with body connected to VSS
      - deep-nWell nMOS pair of size 4, with their common body terminal brought out to a pin
    - nMOS current mirrors
      - 1 : 1, 2, 4, 8, 16, 32 nMOS current mirror with grounded sources and bodies
      - 1 : 1 nMOS current mirror with grounded sources and bodies
    - nMOS common-source pair
      - common-source nMOS transistor pair of size 4 with grounded bodies
    - pMOS
      - pMOS pair of size 1, with body connected to VDD
      - nWell pMOS pair of size 4, with their common body terminal brought out to a pin
    - pMOS current mirrors
      - 1 : 1, 2, 4, 8, 16 pMOS current mirror with sources and bodies connected to VDD
      - 1 : 1 pMOS current mirror with sources and bodies connected to VDD
    - pMOS common-source pair
      - common-source pMOS transistor pair of size 4 with bodies connected to VDD
    - Operational Transconductance Amplifiers (OTAs)
      - one-stage, nMOS-input, load-compensated OTA
      - one-stage, pMOS-input, load-compensated OTA
      - The OTAs are biased through the current mirror with a 2x device
    - nMOS/pMOS stacks
      - two nMOS/pMOS stacked devices of size 16  
- The `EN` pin
    - The pin is pulled down to $V_{SS}$ with an internal pull-down
	resistor.
        - When `EN` is LOW, the on-chip switch matrix disabled; the chip can
        be used without digitally programming the switch matrix.
    - The pin can be externally pulled up to $V_{DD}$ to enable the
    switch matrix (see below).
        - When `EN` is HIGH, the on-chip switch matrix connects devices
        according to the bit pattern streamed into the on-chip memory
        through the digital serial interface.
- ESD series resistors
    - To meet ESD requirements series resistors have been inserted
      between the device terminals and the chip pads; the resistor size
      depends on the transistor size: 50$\Omega$ for the 1x device,
      25$\Omega$ for the 1x device,  and 12.5$\Omega$ for the 4x and larger
      devices.  
### On-Chip Switch Matrix
- The chip can be used without using the switch matrix; if the `EN` signal is left disconnected[^pulldown] or kept LOW, all switches remain open. All devices are hardwired to the chip pins and circuits can be constructed using external connections. 
- Switch matrix and buses
    - There is a 65x10 switch matrix than can connect each of the 63 transistor-terminal pins and the VDD and VSS to 10 buses on the chip to build circuits without
      requiring external wiring. 
    - Through the serial interface pins `DATA` and `CLK` a digital bit
      stream can be read into the on-chip memory while `EN` is LOW;
      after asserting `EN` to HIGH, the respective 15$\Omega$ transmission-gate
      switches are activated. 

- The chip can be programmed using the [MOSbiusTools](../4_sw_support/MOSbiusTools.md). 
<!-- #### Programming the On-Chip Memory for the Switch Matrix
- The on-chip memory is configured as a shift register with 650 stages
- On every 'falling' edge of the `CLK` a data bit from `DATA` is read in
- To program the connections:
  - Put `EN` to LOW
  - Stream in 650 bits via `DATA` and `CLK`
    - bit 1 sets the connection between `BUS1` and pin `TBD`
    - bit 2 sets the connection between `BUS1` and pin `TBD`
    - and so on
    - bit 66 sets the connection between `BUS2` and pin `TBD`
    - bit 67 sets the connection between `BUS2` and pin `TBD`
    - and so on for the remaining pins and remaining `BUS3` through `BUS10`
  - Put `EN` to HIGH to activate the switches
#### Generating the Bitstream
--> 


### Test PCB

#### Description
The MOSbius PCB is a 'breakout' board that allows to connect the chip to a standard solderless breadboard. All the pins of the chip are routed to pins on the breadboard so that external connections and external components can be connected to the circuit. 

[Schematic](img/Schematic_MobiusPCB_v3_2024.pdf) and [PCB Silk/Labels](img/pcb_f_silk_etc.pdf), [PCB Top Wires](img/pcb_f_cu.pdf), [PCB Bottom Wires](img/pcb_b_cu.pdf)

```{figure} img/MOSbiusPCB_v3_2024_with_power.png
3D Render of the MOSbius chip on the MOSbius break-out PCB inserted in a solderless breadboard.
```


#### Testing the PCB Before Use
[Testing the PCB](../10_app_pcb_test/pcb_test.md) has images showing the various functions on the PCB. 

#### Using the PCB

- Power Supply:
  - The MOSbius chip **always needs to be powered by 2.5V** to reverse bias the pad ESD protection diodes. All `GND` on the PCB are connected, but make sure to connect it correctly to your external power supply. 
  - You can apply a 2.5V supply to the `V+` pin on the top of the PCB; the PCB contains a protection circuit against supply voltages larger than 2.5V. The power supply is connected to the breadboard power rails as well. The 2.5V supply can be supplied from there also. 
  - Or you can use the [LDO](./img/NCV8164-D.PDF) regulator[^ldo] on the PCB to convert an input voltage `LDOI` between 2.7V and 5.5V to 2.5V. In that case place a jumper between `LDOO` and `V+`. You can obtain the 'Power Good' logic signal with a jumper on `LDO_PG` and measuring the voltage, but this is not required.
  - The red power LED indicates that 2.5V is applied to the chip. The PCB also contains supply decoupling. 
- nMOS and pMOS Current Mirror Bias:
  - The 25K potentiometer on the top, close to `I_REFP` can be used to bias the pMOS current mirror. Connect a current meter across `I_REFP` with the positive lead on the left and the negative lead on the right side of the header; adjust the potentiometer for the desired current and then replace the current meter with a jumper. The left terminal of the `I_REFP` header is connected to `pin 68` of the Mobius chip. 
  - Similarly, the 25K potentiometer on the left, close to `I_REFN` can be used to bias the nMOS current mirror. Connect a current meter across `I_REFN` with the positive lead on the left and the negative lead on the right side of the header; adjust the potentiometer for the desired current and then replace the current meter with a jumper. The left terminal of the `I_REFN` header is connected to `pin 19` of the Mobius chip. 
- Digital Interface Level Conversion:
  - The PCB contains resistive dividers to convert 3.3V logic signals to 2.5V logic signals compatible with the MOSbius chip.
  - Connect the `DATA`, `CLK`, and `EN` from your 3.3V digital signal source to the respective headers `DT`, `CK` and `EN` on the **top** of the PCB. 
  - The 2.5V logic signals will appear on the right side on of the header in the upper left corner of the PCB. Place a jumper to connect the `DT`, `CK` and `EN` to the chip. The left side of the header is connected to the MOSbius chip `pins 3, 2, 1` respectively. 
  - The blue, yellow and green LED's will light up when you send the digital `DT`, `CLK` and `EN` signals to the chip: . 
- Manual Enable:
  - If you want to control `EN` manually, then connect a jumper to connect `EM` to the chip; if you then connect a jumper at `EM_PU`, `EN` at the chip will go high enabling the switch matrix and the orange LED will light up; if you leave the `EM_PU` jumper open, `EN` at the chip will stay low and the on-chip switches in the switch matrix will remain open. 


  
## Testbench
The MOSbius chip can be measured using standard test equipment on a typical student lab bench. 

We recommend the use of USB-based instrumentation since it allows the student to do the experiments in their dorm room or at home. For many of the experiment demonstrations shown here we use the [ADALM 2000 Active Learning Module](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adalm2000.html), but other modules can be used as well. 


(chip-family)=
## The MOSbius Chip Family

This website documents the **MOSbius Twist Classic (V1)** chip, which is now sold out (Summer 2026). Two new MOSbius chips are on their way:

- **MOSbius Twist (V3)** is the new baseline chip. It is designed to be pin-compatible with Twist Classic (V1), so the experiments on this website will carry over. **Coming soon, stay tuned!**
- **MOSbius Toggle (V2)** is an advanced chip for more complex experiments. Samples are available for collaborators who want to help develop experiments and materials; email [Peter Kinget](mailto:pk171+mosbius@columbia.edu) if you are interested.

Follow the [News](../7_news/news.md) for updates.

|                | Twist Classic (V1)                 | Twist (V3)                              | Toggle (V2)                                  |
| ---            | ---                                | ---                                     | ---                                          |
| Level          | baseline                           | baseline                                | advanced                                     |
| Technology     | 65nm CMOS, 2.5V devices            | GF180MCU, 3.3V                          | 180nm CMOS, 3.3V                             |
| Package        | 68-pin PLCC on an adapter PCB      | chip-on-board and adapter PCB.          | 100-pin QGN on adapter PCB.                  |
| Compatibility  |                                    | compatible with Twist Classic (V1)      | new pinout                                   |
| Availability   | sold out                           | coming soon, stay tuned                 | samples for collaborators                    |

### MOSbius Twist (V3)

Twist (V3) is the new baseline MOSbius chip. It was fabricated in the GF180MCU technology on the first [wafer.space](https://wafer.space) run, operates from 3.3V, and is designed to be pin-compatible with Twist Classic (V1). The die is mounted directly on a small chip-on-board (CoB) PCB that plugs into a breadboard adapter. 

```{figure} img/chip_family/twist_v3_die_and_cob.jpg

The MOSbius Twist (V3) chip: die photo (left), and the die mounted with chip-on-board packaging (right)
```

```{figure} img/chip_family/twist_v3_adapter_pcb.jpg
:height: 300px

The CoB-to-breadboard adapter PCB for Twist (V3)
```

### MOSbius Toggle (V2)

Toggle (V2) is an advanced MOSbius chip in a 180nm CMOS technology, packaged in a 100-pin QFN package. It adds programmable transistor sizes and switched buses driven by an on-chip non-overlapping clock generator, so that circuits such as switched-capacitor amplifiers can be built and programmed on the chip. Samples are available for collaborators who want to help develop experiments and materials; email [Peter Kinget](mailto:pk171+mosbius@columbia.edu) if you are interested.

```{figure} img/chip_family/toggle_v2_chip_and_breadboard.jpg

The MOSbius Toggle (V2) chip: layout and die photo (left), and a Toggle (V2) chip on its PCB, programmed as a single-stage switched-capacitor amplifier (right)
```

```{figure} img/chip_family/toggle_v2_sc_amp_schematic.jpg

Schematic of a two-stage switched-capacitor amplifier built with the switched buses of Toggle (V2)
```

```{figure} img/chip_family/toggle_v2_sc_amp_waveforms.jpg

Measured input, output, and clock waveforms of a switched-capacitor amplifier on Toggle (V2)
```

[^pulldown]: The MOSbius chip has a pulldown resistor on the `EN` pin. 
[^ldo]: The LDO chip does not see a decoupling capacitor until you connect `LDOO` to `V+`. If you want to test out the LDO before connecting it, make sure to place some external decoupling capacitance on `LDOO`. 