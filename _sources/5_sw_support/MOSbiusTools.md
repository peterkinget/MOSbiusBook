# Programming the Chip Using the MOSBiusTools

We currently provide two tools to generate bitstream files that you can use to program the switch matrix on the MOSbius chip. The tools are available from Github and as a python package.

* The [Github repository](https://github.com/peterkinget/MOSbiusCADFlow/) contains python modules and command-line scripts to interface with the Mobius chip. 

* A python package is available from TestPyPI as [MOSbiusTools](https://test.pypi.org/project/MOSbiusTools)
  - we advise to create a virtual environment to install the tools
  - install using `pip3 install -i https://test.pypi.org/simple MOSbiusTools`
  - installs the `MOSbiusTools` module and two executable scripts described below.

## Executable Scripts

After installing the package the scripts should be executable from your command line. 

### connections_to_bitstream

*  `connections_to_bitstream` converts a connections.json file into a bitstream to program the MOSbius chip.
* run `connections_to_bitstream -h` and you get a brief description of
  script usage. 
* There is a blank `connections.json` file provided and some [examples](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_connections/). 

### cir_to_connections

*  `cir_to_connections` converts an LTSpice netlist (`.cir`)
  into a `connections.json` file that the `connections_to_bitstream`
  script can convert into a bitstream file. 
* Run `cir_to_connections -h` and you get a brief description of
  script usage. 
* There are some example `.cir` files provided in
  [examples](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_cir). 

## Basic Steps to Create Bitstream Files

### From LTspice Schematic
* create an LTspice schematic using the [LTspice Library](../4_chapter_simulations/LTspice_simulations.md)
* save your design as a `.cir` file, e.g. `my_circuit.cir`. You obtain a `.cir`
  netlist for your LTSpice circuit by right clicking on the schematic,
  then 'View SPICE Netlist', then 'Save As'. 
* create a `connections.json` file:
  - `cir_to_connections -i my_circuit.cir -o connections_my_circuit.json -d`
  - the `-d` is not required but will provide some output to review the conversion process.
  - you can choose your own filename for the json file, but a .json is recommended.
* convert the `connections_my_circuit.json` to a bitstream file with `connections_to_bitstream` -- see next topic.

### From Connections Json File
* prepare connections file:
  - You can create a connections file in your text editor by starting from [connections.json](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_connections/connections.json); for each *BUS* list the pcb pin numbers that need to be connected to it [(OTA example)](https://github.com/peterkinget/MOSbiusCADFlow/tree/main/MOSbiusTools/MOSbiusTools/scripts/examples_connections/connections_Miller_OTA_pin.json); let's assume you save it as `connections_my_circuit.json`. 
  - Or, you can use the `cir_to_connections` script described above.
* convert connections file to bitstream files:
   - `connections_to_bitstream -i connections_my_circuit.json -o my_circuit_bitstream.txt -d`
  - `-d` is not required but will provide output so you can review the conversion.
  - you can choose your own filename for the output file, but a `.txt` extension is recommended; besides `my_circuit_bitstream.txt`, `my_circuit_bitstream_clk.txt` will also be generated.
  - the bitstream files can be used with the ADALM2000 to generate the digital programming waveforms (CLK and DATA).

## Example of Programming a Three-Stage Ring Oscillator

### Starting from LTspice Schematic
We build the 3-stage 16-16-8 ring-oscillator circuit schematic in LTspice using the MOSbius library. It uses the two 16x inverter stages and creates an 8x inverter stage by combining the pairs of 4x nMOS and pMOS transistors; we use `BUS9` for VSS and `BUS10` for VDD.
![3stage_RO_8x_schematic](../2_chapter_ring_oscillator/img/3stage_RO_8x_schematic.png)

We save the netlist of the circuit as a `.cir` file by right clicking on the schematic, then View Spice Netlist, and File Save as. 

Next, we translate the schematic `cir` file to [connections json file](../2_chapter_ring_oscillator/img/connections_3stage_RO_8x_vdd_10_vss_9.json) (see instructions above):

```
> cir_to_connections -i 3stage_RO_8x_vdd_10_vss_9.cir -o connections_3stage_RO_8x_vdd_10_vss_9.json`
```

Continue on with the next step. 

### Starting from a Connections File

We can generate the [connections json file](../2_chapter_ring_oscillator/img/connections_3stage_RO_8x_vdd_10_vss_9.json) from a schematic or create it manually in a text editor. 

Then we translate it into a [bitstream](../2_chapter_ring_oscillator/img/3stage_RO_8x_vdd_10_vss_9.txt) and [clock file](../2_chapter_ring_oscillator/img/3stage_RO_8x_vdd_10_vss_9_clk.txt):

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

[^dio_choice]: You can choose any DIO channels of your preference. 
[^en_jumper]: We chose to use a short jumper cable to short the `EMU_PU` jumper but you can use a standard jumper as well. 