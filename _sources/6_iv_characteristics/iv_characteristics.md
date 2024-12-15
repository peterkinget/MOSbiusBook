# Transistor I-V Characteristics

## Oscilloscope Measurements
```{figure} img/ids_vds_4x.png

IDS-VDS measurement of a 4x nMOS transistor with a $100\Omega$ series resistor in the drain; CH1 is measuring the VDS voltage and CH2 is measuring the voltage across the drain series resistor
```

```{figure} img/vgs_vds_4x.png
VGS (orange) and VDS (purple) waveforms used for the IDS-VDS measurements
```

We performed nMOS IDS-VDS measurements for varying VGS by connecting the ADALM2000 waveform generator `W1` to the gate of the transistor under test and the drain to the waveform generator `W2` through a $100 \Omega$ series resistor $R_D$. The scope channel `1` measures the drain to source voltage (VSS) and the `2` channel measures the voltage across the drain series resistor. 

The VGS voltage is stepped from 0.25 to 1.25V with 0.1V steps, and for each VGS the VDS voltage is swept from 0 to 2.5V. 

This is a simple but relatively crude way to measure IDS-VDS characteristics. As the IDS increases, the voltage drop across the resistor $R_D$ increases and thus the effective range for the VDS measurements reduces, so a small value of $R_D$ is preferred; however, small $R_D$ results in small current-to-voltage conversion and hence low current-measurement accuracy given the accuracy limit of the scope channels. 

## Automated Measurements

We wrote a `python` script using the `libm2k` package to collect the measurement data from the ADALM2000 and made sure that the scope channels operate in their most sensitive $\pm 2.5V$ range to improve measurement accuracy. `<consider adding script>`

For the pMOS we used a similar setup with a $100 \Omega$ series resistor but with the appropriate adjustments to the voltage source sweeps. 


```{tableofcontents}
```
