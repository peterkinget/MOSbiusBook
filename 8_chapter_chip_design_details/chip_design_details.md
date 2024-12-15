# MOSbius Chip Design Details
`<This chapter is under construction>`
## Device Layouts
### Devices
`<TBD>`
### Current Mirrors
`<TBD>`
### Simple OTAs
`<TBD>`
## Switch Matrix and Shift Register
```{figure} img/ShiftRegisterSchematic.png
Partial schematic of the 650-stage shift register
```
`<Labeling of the signals is not consistent; what is RST compared to EN? D needs to be DATA; RST is active-low so it must be inverse of EN>`

The off-chip clock `CLK` is converted into two non-overlapping clock phases $\phi$ and $\overline{\phi}$ on chip to make sure that no hold-time violations occur in the register. A Schmitt Trigger is added to the `DATA` and `EN` line (not shown) to further improve the noise robustness of the signaling. 

```{figure} img/ShiftRegisterStageLayout.png
Organization of the layout of a stage in the shift register
```
`<Add a timing diagram for the shift register>`

## Top-Level Layout
```{figure} img/layout.png
Layout view of the 1mm x 1mm MOSbius chip
```
The chip includes 424pF of nMOS decoupling capacitance between VDD and VSS