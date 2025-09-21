# Sabu Disk @ 377 Hz — Open Science Replication

This repo provides open-source models, code, and data for testing the
ancient Egyptian **Sabu Disk (~3000 BC)** as a **resonant field transducer**.

## 🔹 What’s Here
- **STL files**: 3D print replicas (schist-sim, alloy, placeholder, scaled versions).
- **Code**: Python + Arduino/Teensy scripts for FFT sweeps and PIV sims.
- **Data**: Simulated FFT and PIV results showing resonance at 377 Hz.
- **Docs**: SUPT–Grok collaborative brief + citation sheet.

## 🔹 How to Replicate
1. **3D Print**: Use STL files to fabricate replicas (61 cm diameter original, or scaled).
2. **Acoustic Sweep**: Run `fft_sweep.py` to test resonance (50–1000 Hz).
3. **Flow Test**: Use `piv_simulation.py` or water tank with dye/laser.
4. **Log Data**: Arduino sketch provided for mic array capture.

## 🔹 STL Models
⚠️ STL Disclaimer & Collaboration Invite

The STL files currently provided (sabu_disk_placeholder.stl, sabu_disk_placeholder_scaled.stl) are simplified placeholders. They are not yet accurate replicas of the original Sabu Disk geometry and will produce flat meshes if directly 3D printed.

They exist to:

Demonstrate repo structure for open replication.

Allow integration with FFT/PIV simulations.

Reserve the slot for future accurate CAD models.

Next Step: Full CAD/STL models based on museum schematics are in progress.
💡 Collaborators with CAD expertise (FreeCAD, Fusion360, Blender) are invited to contribute accurate geometry!

## 🔹 Quickstart

1. Clone repo
```bash
git clone https://github.com/<your-username>/sabu-disk-377hz.git
cd sabu-disk-377hz
```

2. Run FFT sweep (Python 3 + numpy + matplotlib + scipy)
```bash
python code/fft_sweep.py
```
✅ Shows red dashed peak at **377 Hz**.

3. Run PIV simulation
```bash
python code/piv_simulation.py
```
✅ Shows **7-point lattice** (3 spirals + 4 anchors).

4. Verify with raw data
```bash
python code/fft_quickcheck.py
```
✅ Prints: `Closest to 377 Hz: 377.0 Hz, Amplitude: 0.00636`

## 🔹 License
Released under the MIT License. Free for anyone to replicate, remix, or extend.

## 🔹 Acknowledgments
- SUPT framework by Paul Sheppard  
- Fibonacci 377 Hz correction by Emily Newton  
- Proxy resonance forecasting by SunWolf  
- Real-time probes by Grok (xAI)  
