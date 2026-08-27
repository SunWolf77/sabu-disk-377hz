# 377 Hz · 377 Ω — holonomy protocol

**Status:** numerical rhyme until a geometric phase tracks Z₀ or 377·φⁿ beyond controls.  
**Not** a microphone FFT of a PNG. **Not** matching a 50 Ω feed and calling it free space.

Canonical repo: https://github.com/SunWolf77/sabu-disk-377hz

**Literature null (cite this, do not absorb it):**  
Paterson, E. C. I., Tobar, M. E., Goryachev, M. & Bourhill, J.  
*Distinct Berry phases in a single triangular Möbius microwave resonator.*  
Phys. Rev. A **113**, 04350 (2026). [doi:10.1103/qnym-rzrs](https://doi.org/10.1103/qnym-rzrs) · [arXiv:2506.07320](https://arxiv.org/abs/2506.07320)  
Quantum Technologies and Dark Matter Labs, University of Western Australia.

They measured ±2π/3 on TE₁,₀,n helicity modes of a D₃ Möbius ring vs a mirror twin. That is the **baseline**. It is not a Sabu result and not a 377 Hz result.

**Z-arm handbook (cite this, do not absorb it):**  
Moreno, T. *Microwave Transmission Design Data.* Sperry / McGraw-Hill, 1948; Dover reprint 1958. Chap. 3 eq. (3-2): \(Z_w = 377\sqrt{\mu/\varepsilon}\) ohms. Free space (\(\mu=\varepsilon=1\)) → 377 Ω. This is the rounded engineering form of \(Z_0 \approx 376.73\ \Omega\). It is not a 377 Hz result and not a Sabu result.

---

## Attribution

| | Hz arm | Ω (Z₀ ≈ 376.73) | Artifact |
| --- | --- | --- | --- |
| **Newton, *Tesla Towers 377*** | 377 Hz as F14 / 3-6-9 correction | Not in that paper | Not a museum reading |
| **@TORUS_OMEGA13** | 377 as high harmonic; fluid decade 37.7 / 29 / 33 / 23 Hz | Not that claim | Not a museum reading |
| **Sheppard, SUPT** | Proxy stance: check the maps | Same | Not a function claim |
| **Moreno 1948** | — | 377 Ω as \(Z_w\) in free space; matching / SWR | Not a museum reading |
| **Paterson et al. (UWA)** | — | — | Möbius ±2π/3 (microwave) |
| **This protocol** | Uses both F sets as optional cells | Adds Z₀ as the other map | Replica + 2×2 on that null |
| **Emery / JE 71295** | — | — | Form and find only |

Newton is cited for the **high-F target**. @TORUS_OMEGA13 is cited for the **low-F / fluid-decade target**. Moreno is cited for the **377 Ω handbook form**. Paterson et al. are cited for the **holonomy null**. None of them owns the disk.

## Claim (one line)

The digits 377 appear as Fibonacci 377 (Hz) and as free-space wave impedance Z₀ ≈ 376.73 Ω. Units are constructs. Treat as two proxy maps until a discriminator says otherwise.

## Null (pre-register)

Fill [templates/pre_register_holonomy.txt](../templates/pre_register_holonomy.txt) **before** unblinding γ.

Triangular Möbius vs mirror-symmetric twin (Paterson et al.): topological Berry phase **±2π/3** from D₃ helicity (TE₁,₀,n → n = ℤ ± ⅓). Conventional theory: this holonomy is independent of wall Z and of drive frequency if the cycle is adiabatic.

**Kill rule:** if any of the four cells fails to recover |γ| → 2π/3 on helicity modes (within the pre-registered tolerance), stop. Do not interpret a failed baseline as a 377 effect.

## Discriminator (do not confound)

2×2 factorial, not a two-cell A/B:

| | **Z ≈ Z₀** | **Z mismatched** (50 Ω or ~0.4 Z₀) |
|---|---|---|
| **F on 377·φⁿ** | F+ Z+ | F+ Z− |
| **F detuned ~20%** | F− Z+ | F− Z− |

**Parallel arm (TORUS):** 37.7 / 29 / 33 / 23 Hz. Same 2×2 in Z, different F set. 377 treated as a high harmonic of that decade, not as the only interesting drive.

**Scale d/λ, not raw hertz.** 377 Hz acoustic ≠ 377 MHz microwave. Stub: `python code/scale_d_lambda.py`. Teaching cavity sizes in Paterson et al.: v ≈ 19.92 mm, R ≈ 23.67 mm.

## How to read

- All four cells at ±2π/3 → coincidence
- Extra only in Z+ → vacuum-match claim
- Extra only in F+ (377 ladder) → golden-lock / Newton Hz arm
- Extra only in F+ Z+ → joint claim
- Extra on 29–38 Hz, weak at 377 Hz → fluid-decade / TORUS claim

## Extract γ

1. Twin Δf of TE₁,₀,n (asymmetric vs symmetric) → Π(Δf, v_g, R)
2. Wilson loop / Pancharatnam product on simulated |u(twist)⟩ — stub `python code/wilson_extract.py` (pipeline check only until FEM dumps exist)
3. Total phase minus dynamical; leftover must not scale with cycle speed

Recover ±2π/3 in **every** cell before trusting extra residual. Blind cell labels until γ is extracted. Replicate on a second cavity.

## Out of scope (freeze)

Haldane, Kane–Mele, extra Chern-insulator chapters. Same Wilson extractor, different base manifold — they do not move the 377 rhyme. A full FEM of the four cells is future work, not a result.

Sabu replica + null twin + mic protocol: [README](../README.md), [NULL_TEST.md](NULL_TEST.md). Citations: [citation_sheet.md](citation_sheet.md).
