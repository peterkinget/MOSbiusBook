## Optional
1. Common-source amplifier
   * Step 1: Power the chip with a 2.5V power supply on ADALM2000. You will see the red power indicator LED light up.
    ![Fig. Power of the chip. ](<img/Power of the chip.png>)
   * Step 2: Find one NOMS on the chip from the schematic. Connect the drain of the transistor (Pin 46) to a 4.7k Ohm to build a common-source amplifier. Connect the body (Pin 47) of the transistor and the source (Pin 44) of the transistor to the ground, and gate to the waveform generator. 
    ![Fig. The transistor used for common-source amplifer.](<img/Common-Source Amplifier.png>)
   * Step 3: Generate a ramp to sweep the DC response of the common-source amplifer. Use X-Y plot to see Vout-Vin curve. Determain the DC operating range and the gain of the common-source amplifier.  
   * Step 4: Generate a 100Hz sin wave with an appropriate DC offset to verify the gain of this amplifer.