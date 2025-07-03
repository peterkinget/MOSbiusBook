# Programming the Chip 

At this point, there are two documented flows on how to program the on-chip switch matrix on the MOSbius chip using the *CLK, DATA,* and *EN* pins:

- using the MOSbiusTools to generate bitstreams for a **digital pattern generator**,
- or using a **Rasperry Pi Pico microcontroller** with the MOSbius micropython flow.

In both cases, you need a `connections.json` file [^filename] that describes which pins are connected to which BUSes. The example below is for the 3-stage ring oscillator circuit that is explained in more detail below. The format is straightforward; for each bus, the connected pins are listed in a list; buses with no connections can be listed with an empty list or can be skipped altogether. 

```json
{
"1": [], 
"2": [], 
"3": [53, 52, 11, 6, 41, 46], 
"4": [51, 48, 50], 
"5": [45, 7, 42, 10, 49], 
"6": [], 
"7": [], 
"8": [], 
"9": [18, 43, 44, 47], 
"10": [1, 5, 8, 9] 
}
```

You can create the connections file manually or from an LTspice schematic using the `cir_to_connections` script (see below).

Once you have the connections file you can proceed with generating bitstream files for your digital pattern generator or upload the connections file to the Raspberry Pi PICO.

<span style="font-size: 150%;">**Installing the MOSbiusTools**</span>[^noneed]

We currently provide two scripts [^source] to assist with generating *connections* and *bitstream files* to program the switch matrix on the MOSbius chip. The tools can be installed with a python package from TestPyPI called [MOSbiusTools](https://test.pypi.org/project/MOSbiusTools):
- we advise to create a virtual environment to install the tools;
- install using `pip3 install -i https://test.pypi.org/simple MOSbiusTools`;
- this installs the MOSbiusTools module and two executable scripts, more details below:     
  - `cir_to_connections` converts an LTSpice netlist (.cir) into a connections.json file;
  - `connections_to_bitstream` converts a connections.json file into a bitstream file for a digital pattern generator to program the MOSbius chip; 
 - after installing the package the scripts should be executable from your command line.

## Step 1: Creating a Connections File

### Manually

  - You can create a connections file in your text editor by starting from [connections.json](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_connections/connections.json); for each *BUS* list the pcb pin numbers that need to be connected to it [(OTA example)](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_connections/connections_Miller_OTA_pin.json).

There are `.json` file examples above and in
  [examples](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_connections). 

### From an LTspice Schematic Using `cir_to_connections`

* create an LTspice schematic using the [MOSbius LTspice Symbol Library](../5_chapter_simulations/LTspice_simulations.md)
* save your design as a `.cir` file, e.g. `my_circuit.cir`. You obtain a `.cir`
  netlist for your LTSpice circuit by right clicking on the schematic,
  then 'View SPICE Netlist', then 'Save As'. 
* create a connections file:
```
> cir_to_connections -i my_circuit.cir -o connections_my_circuit.json -d
```
  - Note: 
    - the `-d` is not required but will provide some output to review the conversion process.
    - you can choose your own filename for the json file, but a .json extension is recommended.

There are some example `.cir` files provided in
  [examples](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_cir). 

## Step 2: Programming MOSbius 

### Option 1: Using a Raspberry Pi PICO

To use the Raspberry Pi PICO, you only need a *connections.json* file and the MOSbius micropython scripts on the PICO will generate the necessary *CLK, DATA,* and *EN* signals. 

Please review the documentation at the [MOSbius_MicroPython_Flow](https://github.com/Jianxun/MOSbius_MicroPython_Flow) by Jianxun Zhu for detailed instructions and examples. 

### Option 2: Using a Digital Pattern Generator

To use a digital pattern generator (like e.g., the one in the ADALM2000 used in the example below) you need to create bitstream files from the connections file *connections_my_circuit.json*. 

``` 
> connections_to_bitstream -i connections_my_circuit.json -o my_circuit_bitstream.txt -d
```
- `-d` is not required but will provide output so you can review the conversion.
- you can choose your own filename for the output file, but a `.txt` extension is recommended; besides `my_circuit_bitstream.txt`, `my_circuit_bitstream_clk.txt` will also be generated.

The bitstream files can be used with the ADALM2000 to generate the digital programming waveforms (CLK and DATA), see the worked-out example below.

## Worked-out Example of Programming the MOSbius Chip using the ADALM 2000 Digital Pattern Generator

Here we go through all the steps to program the chip using a digital pattern generator. We use a 3-stage ring oscillator as an example. 

### Making the Connections File 

#### Making the Connections File from an LTspice Schematic
First, we build the 3-stage 16-16-8 ring-oscillator circuit [schematic in LTspice](../2_chapter_ring_oscillator/sim/3stage_RO_16_16_8.zip) using the MOSbius symbol library. It uses the two 16x inverter stages and creates an 8x inverter stage by combining the pairs of 4x nMOS and pMOS transistors; we use `BUS9` for VSS and `BUS10` for VDD.
![3stage_RO_8x_schematic](../2_chapter_ring_oscillator/img/3stage_RO_8x.png)

Then, we save the netlist of the circuit as a `.cir` file by right clicking on the schematic, then View Spice Netlist, and File Save as. 

Next, we translate the schematic `cir` file to [connections json file](../2_chapter_ring_oscillator/img/connections_3stage_RO_8x_vdd_10_vss_9.json) (see instructions above):

```
> cir_to_connections -i 3stage_RO_8x_vdd_10_vss_9.cir -o connections_3stage_RO_8x_vdd_10_vss_9.json`
```

#### Making the Connections File Manually

You can also create the [connections json file](../2_chapter_ring_oscillator/img/connections_3stage_RO_8x_vdd_10_vss_9.json) manually in a text editor. 

### Generating the Bitstream File

Then we translate the connections file into a [bitstream](../2_chapter_ring_oscillator/img/3stage_RO_8x_vdd_10_vss_9.txt) and [clock file](../2_chapter_ring_oscillator/img/3stage_RO_8x_vdd_10_vss_9_clk.txt):

```
> connections_to_bitstream -i connections_3stage_RO_8x_vdd_10_vss_9.json -o 3stage_RO_8x_vdd_10_vss_9.txt 
```

### Uploading the Bitstream File into the MOSbius Chip

The chip is connected to the ADALM2000 as shown here:
![3stage_RO_ready_for_programming](../2_chapter_ring_oscillator/img/3stage_RO_8x_ready_for_programming.jpeg)

DIO channels 8 and 9[^dio_choice] are wired to the `CK` and `DT` headers respectively at the top of the PCB that are the inputs of the digital level converters. Jumpers are placed on the `DATA` and `CLK` headers on the top left to connect the level-converted digital signals to the MOSbius chip. In this example, we are using a *manual* `EN1`. A jumper is placed on the bottom header on the top left of the PCB. The `EMU_PU`is left open for now (short jumper cable is dangling in the air in the photo). Please review [the PCB description](../1_chapter_description/description.md). 

```{figure} img/jumpers.gif
Location of the digital signal connections and jumpers.
```

We configure the **Pattern Generator** function of the ADALM2000 to have two digital output channels: DIO 8 and 9 and upload the *clock* and the *bitstream* file to channel 8 and 9 respectively as shown below. The frequency for the clock waveform has to be twice the frequency for the bitstream waveform; we typically use *200kHz* for the frequency for *CLK* and *100kHz* for the frequency for *DATA*. 

```{figure} img/pattern_generator_screenshot.png
Screenshot of the *Pattern Generator* screen of Scopy controlling the ADALM2000 after the bitstream and clock file have been read in for channels 9 and 8 respectively. 
```

```{figure} img/pattern_generator_screenshot_zoom.png
Zoom in on the digital waveforms showing the alignment between the data and clock waveforms.
```

During programming the `EN` needs to be LOW; we leave it floating so the internal pull-down will hold it LOW; and we also disconnect the `1+` and `2+` scope inputs, or any other connections from the ADALM2000. 

We *turn on* the 2.5V power supply for the MOSbius chip (the red LED on the PCB turns on) and then upload the bitstream into the MOSbius chip using the **Single (Run)** function. If you look closely you see the data/clock LEDs on the PCB flicker briefly.   

### Enabling the MOSbius Chip
![3stage_RO_ready_for_programming](../2_chapter_ring_oscillator/img/3stage_RO_8x_in_operation.jpeg)

We now enable the connection matrix by asserting the `EN` signal by shorting the `EMU_PU` jumper connection[^en_jumper]. Notice that the red LED shows that the chip is powered and the orange LED shows the switch matrix is enabled.

The measurements are further described [here](../2_chapter_ring_oscillator/ring_oscillator.md). 

[^filename]: You can choose any filename of your liking. 
[^noneed]: If you create your connections files manually and use the Raspberry Pi PICO for programming you will not need the MOSbiusTools. 
[^source]: The source code of the scripts is available from this [Github repository](https://github.com/peterkinget/MOSbiusCADFlow/).
[^dio_choice]: You can choose any DIO channels of your preference. 
[^en_jumper]: We chose to use a short jumper cable to short the `EMU_PU` jumper but you can use a standard jumper as well. 
