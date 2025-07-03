# Operational Transconductance Amplifier Experiments

With the MOSbius chip you can build an OTA from scratch and then measure its DC, AC, transient, noise ... performance including probing the waveforms at internal nodes. You have to choose a topology, select transistor sizes, and bias currents. You further have to insert a frequency compensation network and feedback network. 

Many topologies can be built including:
* single-stage OTAs, 
* two-stage Miller-compensated OTAs, 
* folded-cascode OTAs, 
* and even a fully differential two-stage Miller-compensated OTA. 

The chip has enough transistors to build four single-ended OTAs making possible experiments of small analog systems. 

The student can do hand calculations to size the OTA, run simulations to verify biasing, small-signal parameters and performance, and then compare measured results to calculations and simulations. 

Last but not least, the experiments require careful thinking about how to conduct the circuit-parameter characterization and how to deal with non-idealities like loading, parasitics or offsets (which are often overlooked in simulations). 

```{tableofcontents}
```

% **Two-Stage Miller-Compensated OTA with pMOS Input Pair**
% - [Two-Stage Miller-Compensated OTA with pMOS Input Pair](./mota-se-p-16/mota-se-p-16.md)
% 
% 
% **Two-Stage Miller-Compensated OTA with nMOS Input Pair**
% - [Two-Stage Miller-Compensated OTA with nMOS Input Pair](./mota-single-ended/mota-single-ended.md) (under construction)
