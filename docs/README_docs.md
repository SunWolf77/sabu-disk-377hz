# Tech notes in plain language

## FFT (Fast Fourier Transform)

Splits a recorded (or simulated) waveform into frequency components.  
**In this repo:** `fft_sweep.py` builds a **synthetic** sweep for teaching. A real test needs a microphone recording of a driven object.

## PIV (Particle Image Velocimetry)

Lab method to image how seeded fluid moves.  
**In this repo:** `piv_simulation.py` draws a **synthetic** quiver field. It is not a laser lab run on a printed disk.

## STL / OpenSCAD

Printable mesh.  
`code/openscad/sabu_disk_approx.scad` approximates published dimensions (61 cm Ø class). Replace when a museum-grade scan is available.

## Why the labels matter

Calling a simulation a “result” collapses measurement into story.  
Keep filenames honest: `sim_`, `mic_`, `null_`.
