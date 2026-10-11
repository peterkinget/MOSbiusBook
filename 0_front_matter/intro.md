<!-- 
```{raw} html
<center>
<video controls width="320" autoplay muted>
  <source src="../_static/videos/MOSbius.mp4" type="video/mp4">
  Your browser does not support the video tag
</video>
</center>
```
-->

# Welcome to the MOSbius Project

```{admonition} What's new
- New MOSbius chips: 
  - [Twist (V3)](chip-family) is coming soon, stay tuned; 
  - [Toggle (V2)](chip-family) samples are available for collaborators. 
  - Twist Classic (V1) is sold out.
- [News & Publications](../7_news/news.md): read about MOSbius in *IEEE Spectrum* and the *IEEE Solid-State Circuits Magazine*, and watch the video interview with Matt Venn.
```

The MOSbius chip contains nMOS and pMOS devices as individual transistors, as
well as in typical configurations like current mirrors, differential pairs, common source configuration, simple operational transconductance amplifiers or inverters. 

```{figure} img/mosbius_flow.png
Overview of the MOSbius platform. Transistors and circuits on the MOSbius chip allow the student to create an electronic circuit that they can evaluate experimentally.
```

**Project Goals:** 
- give students and designers the opportunity to try out MOS circuit topologies that are typically used on chips, on a breadboard;
- give access to MOS transistors in various configurations and sizes;
- learn about circuit debugging, measurements, and the 'chip bring-up' process;
- learn to compare calculations, simulations and measurements through simulation models provided for LTspice. 

```{figure} img/cycle.png
The MOSbius chip enables the student designer to learn about measuring practical CMOS circuits and comparing their operation to analytical design & analysis and circuit simulations. 
```

The chip also contains a switch matrix so every pin can be connected to any of 10 on chip buses, allowing for building circuit wiring on chip and simplifying the test setup. 

We will describe the operation of the MOSbius chip and show examples of experiments that can be conducted to learn transistor-level MOS circuit design. 


**Project Status:**
- the project is still in full development and new materials are still under development. The materials on this website use the MOSbius Twist Classic (V1) chip, which is now sold out; the pin-compatible MOSbius Twist (V3) is coming soon, stay tuned. See [The MOSbius Chip Family](chip-family) for the availability of the MOSbius chips.
- If you find an error or have suggestions, please [open an issue on Github](https://github.com/peterkinget/MOSbiusBook/issues/new) or email [Peter Kinget](mailto:pk171+mosbius@columbia.edu).

**Table of Contents**
```{tableofcontents}
```
