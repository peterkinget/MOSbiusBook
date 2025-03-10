# First-Order, Continuous-Time, Low-Pass, Delta-Sigma Modulator

We build a first-order, continuous-time (CT), low-pass delta-sigma modulator (DSM) with the MOSbius chip. A DSM is a type of analog-to-digital (ADC) converter, more specifically, an oversampling, noise-shaping converter. The analog input voltage is converted in a high-rate, clocked {1,0} bit stream that encodes the signal. With a decimation filter, the 1-bit, high-rate digital signal can be converted to a multi-bit, lower-rate digital signal while rejecting the quantization noise. 

## Block Diagram

The modulator consists of a CT integrator followed by a clocked comparator. The digital signal is fed back with a 1-bit DAC and subtracted from the input signal; the result of the subtraction is fed into the integrator. 

### Signal Transfer Function

### Noise Transfer Function

### Sizing

Choice of $f_{CLK}$, $\omega_{o,int}$ 

Expected performance

System-level simulation

## MOSbius Implementation

```{figure} img/DSM1_v2.svg
LTspice schematic of the DSM1 circuit
```

- Continuous-Time R-C Integrator
    - We use a two-stage Miller-compensated OTA to build an active-R-C integrator. The integrator feedback capacitance is $20nF$.
    - The OTA is constructed with a pMOS 1x input stage biased with $100\mu A$/transistor and an 4x nMOS second stage biased with $400\mu A$; the Miller compensation cap is $150pF$.
    - The input signal is connected with a $10K\Omega$ input resistor to the *virtual ground* node of the integrator. 
    - The OTA operates from $2.5V$ and the common-mode voltage is set to $1.25V$.

- Continuous-Time Comparator
    - The CT comparator is build using a two-stage OTA without compensation in open loop. While this is not the best possible comparator circuit, it will work well for the purposes of this demonstration. 
    - The OTA is constructed with an nMOS 1x input stage biased with a $100\mu A$/transistor and a 4x pMOS second stage biased with $400\mu A$. 

- D-Flip-Flop
    - The DFF is constructed using inverter stages and transmission gates; the feedback inverters are sized smaller (1x) so that the stored state in each latch can be overwritten by the input inverters (4x and 16x). 
    - The DFF captures the input data signal at the falling edge of *CLK* and provides and output signal that changes at the *CLKB* rising edge; the output data can be best read at the rising edge of the *CLK*.

- Feedback DAC
    - In this configuration the feedback DAC consists of a simple $10K\Omega$ resistor connected to the *virtual ground* node of the active-RC integrator.

- Clock Signal
    - The $2.5Vpp$ clock signal *CLK* is provided by an external generator and an on-chip 'inverter' is used to generate *CLKB*; we use the 1x nMOS and 1x pMOS current mirror to build an 'inverter' albeit with a low-input impedance that has to be driven by the external clock generator. 

- Connections
    - All 10 buses are being used for the realization of this circuit. In fact, there are not enough buses to make all connections, so the $VSS$ and $VDD$ connections in the DFF have been made on the breadboard. 
    - The stages are not connected to each other, but need to be connected by the user; this allows for characterization of the individual blocks.



## LTspice Simulations

### Verification of the Stages

First, we simulated the circuit in open loop. We disconnected the integrator from the comparator and placed feedback resistors across the integrator and comparator to verify the operating point of the stages. 

Next we verify the frequency response of the active-RC integrator reconfigured as a low-pass filter.

The operation of the comparator

The operation of the DFF 

### Open-Loop Configuration

We operate the circuit as a low-pass filter followed by a clocked comparator. 

### Closed-Loop Configuration

Now we remove the feedback resistors and operate the DSM in closed loop. 


## Measurements

### DSM1 Clocked at 10Ksps

```{figure} img/waveforms_10kHz.png
Time-domain waveform of the input and output signals of the DSM1; overall the DSM1 is inverting, so when the input is high, more zeros are generated, when the input is low, more ones are generated and when the input is close to the common mode, one-zero signal is generated. 
```

```{figure} img/spectra_10kHz.png
Spectrum of the analog input signal and of the digital output signal. The digital signal has not been sampled, so we are looking at the output signal passed through a zero-order hold filter with notches at multiples of the clock frequency. We observe the 20dB/decade shaping of the noise. 
```