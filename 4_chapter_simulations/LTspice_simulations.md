# Spice Simulations

A library of symbols is available from [Github](https://github.com/peterkinget/MOSbiusCADFlow/) to simulate the circuits built with
the MOSbius chip in [LTspice](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html), which is freely available simulator for Windows and MacOS. If there is sufficient interest, libraries for other simulators can be created.

## Custom Library
```{figure} img/LTspiceSymbolLibrary.png
Screenshot of the custom symbol library for LTspice containing all transistors and transistor groups available on the MOSbius chip
```

Download `MOSbius_chip_library.zip` from the `LTspice` folder in [Github](https://github.com/peterkinget/MOSbiusCADFlow/) and unzip it in your working directory. 

The library `MOSbius_chip_library` contains symbols for each of the transistor arrangements on the MOSbius chip. The terminals are labeled with the corresponding pcb pin numbers[^chipnumbers]. 

The simplest way to start a circuit schematic for an experiment is to copy[^ltspice_lib] the `MOSbius_chip.asc` file in the same folder and name it for your experiment. Then rearrange the transistors you will be using in your circuit as shown in the examples below. 

Many nMOS transistors are directly connected to *VSS* (node 0) and many pMOS transistors are directly connected to *VDD* (declared as a global node); make sure to keep the `.global`, the `.param` and the `.inc` statements in your schematic, along with the voltage source for *VDD*.

There are 10 buses available `BUS01` through `BUS10`; use those to name your internal nodes and the [MOSbius chip programming tools](../5_sw_support/MOSbiusTools.md) can then generate the connection pattern and bitstream file for the on-chip switch matrix (see also below). You can choose to connect the *VDD* and *VSS* to a BUS, but you have to use the provided circuit blocks `chip_vdd` and `chip_vss`. In our examples, we typically choose to connect `BUS09` to *VSS* and `BUS10` to *VDD* where needed. 

## MOS Model File

The necessary `.inc` include statement is in the example schematic file. The model include files are in the folder. We use a [MOS model file](https://www.ee.iitm.ac.in/~nagendra/cadinfo/tsmc025.lib) for 0.25$\mu$m CMOS transistors available from [N. Krishnapura's Model Page](https://www.ee.iitm.ac.in/~nagendra/cadinfo.html). 

**Note on the models:** Whereas the devices on the MOSbius chip are thick-oxide devices in a 65nm foundry process, we have found that the experimental results are quite close to the simulation results obtained with these model files. The model files are definitely adequate to perform functionality verification of the circuits in simulation. 

## Example

Here are two examples:
- [Blinky](../2_chapter_blinky/sim/blinky_relaxation_osc.zip)
- [3-Stage Ring Oscillator](../2_chapter_ring_oscillator/sim/3stage_RO_16_16_8.zip)

<!--
There are examples provided all throughout this book/website but here we show a larger circuit. 

>```{figure} img/Example555SimulationSchematic.png
Illustration of how a MOS version of a 555 timer can be implemented with the MOSbius chip and simulated with the symbol library
```
```{figure} img/Example555OscillatorSchematic.svg
External components are added to the 555 timer realization with the MOSbius chip to create an oscillator
```
-->

## Creating a Bitstream File from an LTspice Schematic

The process of creating a bitstream file to program the MOSbius chip from the simulation schematic is described in the [tools chapter](../5_sw_support/MOSbiusTools.md). 



[^chipnumbers]: In the `OLD` folder in the repository you can find symbols using the chip numbers; however, the MOSbiusTools to generate bitstreams are currently written assuming the schematic is using PCB pin numbers. 

[^ltspice_lib]: You can add the library as a custom library in LTspice and then start a schematic from scratch. However, by starting from the full schematic and using the available components, you will not by accident use more copies of transistor arrangements than are available on the chip. 