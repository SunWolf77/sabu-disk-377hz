# Sabu Disk @ 377 Hz — Open Science Replication

This repo provides open-source models, code, and data for testing the
ancient Egyptian **Sabu Disk (~3000 BC)** as a **resonant field transducer**.

## 🔹 What’s Here
- **STL files**: 3D print replicas (schist-sim and alloy versions).
- **Code**: Python + Arduino/Teensy scripts for FFT sweeps and PIV sims.
- **Data**: Simulated FFT and PIV results showing resonance at 377 Hz.
- **Docs**: SUPT–Grok collaborative brief + citation sheet.

## 🔹 How to Replicate
1. **3D Print**: Use STL files to fabricate replicas (61 cm diameter).
2. **Acoustic Sweep**: Run `fft_sweep.py` to test resonance (50–1000 Hz).
3. **Flow Test**: Use `piv_simulation.py` or water tank with dye/laser.
4. **Log Data**: Arduino sketch provided for mic array capture.

## 🔹 License
Released under the MIT License. Free for anyone to replicate, remix, or extend.

## 🔹 Acknowledgments
- SUPT framework by Paul Sheppard  
- Fibonacci 377 Hz correction by Emily Newton  
- Proxy resonance forecasting by SunWolf  
- Real-time probes by Grok (xAI)  
