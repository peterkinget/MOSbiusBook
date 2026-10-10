# MOSbius Book To-Do List

Not published (only files in `_toc.yml` are built). Keep short `TBD` notes in
the pages where the gap is, and list them here so none get forgotten.
Reader-reported problems go to GitHub Issues.

## New chapters and experiments

- Delta-sigma modulator (DSM1): finish `experiment_DSM1/DSM1.md`
  (signal and noise transfer functions, sizing, choice of f_CLK, expected
  performance, system-level simulation), then add it to `_toc.yml`
- Chip Design Details chapter (`10_chapter_chip_design_details`): device
  layouts, current mirrors, simple OTAs are all `<TBD>`
- Experiments for courses: 1201, 3331, 4314 (RF)
- First experiment: blinky? (the suggestion to start with blinky or the ring
  oscillator is commented out in `3a_experiments/experiments.md`)

## Solutions for instructors

The solution pages (`3a_experiments/Lab_*/*solution*.md`, incl. `old/`
drafts, and the measurement results they use) are in this **public** repo,
so anyone can read them on GitHub. Plan:

- Create a private repo for the solutions in the `mosbiuschip`
  organization, so instructors can get the **Read** role (a personal
  account's private repo can only give collaborators write access).
  Do not enable GitHub Pages on it: Pages sites are public.
- Move the solution files and their images/results there; remove them from
  this repo; decide whether to purge them from this repo's git history
  (`git filter-repo` + force-push: rewrites every commit hash)
- Make the solutions readable for instructors: GitHub does not render MyST
  (`{figure}` etc.), so add a built PDF/HTML or instructions to build it
- Replace the empty table of contents on `3a_experiments/solutions.md` with
  how instructors can request access (fixes the build warning)

## Improvements to existing pages

- Blinky: describe/show building it with manual connections (the page says
  it is possible, but only the on-chip switch-matrix setup is shown)
- Simulations chapter:
  - 555 example screenshots are commented out; clean up and restore
  - describe the example `.asc` files (the `examples` folder in
    MOSbiusCADFlow/LTspice)
  - clean up the MOSbiusCADFlow GitHub repo
  - tool for the operating point printout
- Software tools: GUI for scripts, GUI to program the chip, include Cade's
  routines
- ADALM2000 appendix: resolve the 3 "TBC" notes on input/output range mapping;
  add automation script examples?
- OTA chapter (`2_chapter_ota/mota-se-p-16`): add the signal-range
  measurements of the internal nodes
- `1_chapter_description/description.md`: 4 bit-to-pin entries are `TBD`
- Lab 6 solution (`two_stage_OTA_solution_PK.md:160`): "Fix the XXXX" note

## Build warnings

- `3a_experiments/solutions.md`: table of contents with no pages (the
  solution pages are commented out in `_toc.yml`)

## Done (from the old 10_to_do_list, checked 2026-10-10)

- 3-stage ring oscillator schematic (1-16-16 and 16-16-8, with LTspice zip)
- OTA: unity-gain configuration, transconductance measurement, calculations
  (design table), simulations (operating point) and measurements
- Simulation library with pcb pin numbers; example schematics (blinky, ring
  oscillator) linked
- Programming chapter (MOSbiusTools: connections file, cir_to_connections,
  PICO and pattern generator)
- ADALM2000 appendix, first version
- Reference to Tsividis' first lab (cited in the lab manual)
- MOS OTA experiment (pMOS): OTA chapter and Lab 5
- I/V characteristics chapter
