# Acoustic resonance testing — Sabu replica

**Purpose:** How to run real acoustic measurements on a printed Sabu-form object and its null twin.

This is **not** a certificate that the Cairo bowl (JE 71295) was a 377 Hz device.  
377 Hz is a **test target** (F14 / Z₀ rhyme lives on the L3 shelf). The measurement is L1.

Related docs:

- `docs/NULL_TEST.md` — blind / kill-rule protocol  
- `docs/REPLICA.md` — print geometry, supports, scales  
- `code/acoustic_logger.ino` — basic multi-mic stream  
- `code/fft_sweep.py` — **simulation only** (not mic data)

---

## 1. Two modes (do not mix the claims)

| Mode | Question | A peak means |
| --- | --- | --- |
| **A — Forced acoustic response** | Under the same sound field, does the Sabu-form couple differently than the null twin in a chosen band? | Shape-dependent coupling under *this* drive |
| **B — Structural eigenmodes** | What natural frequencies does *this print* ring at when struck or shaken? | Material + geometry + scale + mount |

- Mode **A** is the default for this repo’s null protocol.  
- Mode **B** is optional fingerprinting of the PLA (or other) object.  
- A Mode B peak near 377 Hz on a desk-scale print does **not** transfer to the museum siltstone bowl without a scale/material model.

---

## 2. Mode A — Forced response vs null

### Claim under test (edit if you change it)

> Under the same acoustic drive and mic geometry, the three-lobed Sabu-form shows a higher response in band \(f_0 \pm \Delta f\) (default example: 377 ± 2 Hz) than a null object of similar mass and outline.

### Bench (minimum)

| Piece | Requirement |
| --- | --- |
| **Source** | Powered monitor or midrange driver on a fixed stand |
| **Drive** | Sine dwells, stepped sine, or log sweep (e.g. 100–1000 Hz) |
| **Sensors** | 1–4 mics at **fixed** positions (hub, rim, optional far-field reference) |
| **Mount** | Soft foam / compliant pads — **identical** for Sabu-form and null |
| **Objects** | Printed Sabu-form + `null_twin` (see OpenSCAD); coded labels only |
| **Room** | Quiet as practical; note that small rooms have strong modes below a few hundred Hz |

Wavelength reminder (air, ~20 °C):  
\( \lambda \approx 343 / f \). At 377 Hz, \( \lambda \approx 0.91\,\mathrm{m} \).  
Room modes and speaker response can dominate absolute SPL — that is why the **null in the same place** matters more than a single number.

### Drive options

| Drive | Use when |
| --- | --- |
| **Sine dwell** at target Hz | Simple SNR in one band |
| **Stepped sine** | Survey several bands with clear dwells |
| **Log sweep** + FFT | Broadband relative response |
| **Pink noise** | Quick relative spectrum (harder to interpret single lines) |

Keep **gain, distance, and orientation schedule** fixed across objects.

### Positive check (required)

No object on the mount. Play pure tone at the target frequency.  
The logger / recorder **must** show the line. If it does not, fix the chain before any object run.

### Metric examples (pre-register one)

- Amplitude in FFT bin(s) covering \(f_0 \pm \Delta f\)  
- SNR: in-band level minus mean of a side band (e.g. 350–360 and 390–400 Hz)  
- Optional: ratio of object mic to far-field reference (reduces speaker drift)

### Kill rule example

> Sabu metric − null metric ≤ 0 (or below a stated threshold) under this protocol → claim fails **this** test.

### Blind sequence

Follow `docs/NULL_TEST.md` in full:

1. Codes on objects and filenames (`OBJ-17`, not `sabu_final`).  
2. Interleave runs.  
3. Score from coded files only.  
4. Open key last.  
5. Publish **both** Sabu and null numbers.

### Orientations

Repeat at 0°, 120°, 240° rotation about the hub axis (symmetry check).  
Pre-register whether you average orientations or report each.

### Filename hygiene

| Prefix | Meaning |
| --- | --- |
| `mic_` | Real recording |
| `sim_` | Synthetic / teaching only |
| `null_` | Null-twin run (after unblinding, or in private key notes) |

Never mix `sim_` plots into a results table labeled as measured.

---

## 3. Mode B — Structural eigenmodes

### Question

What does **this printed object** ring at under light impact or contact drive?

### Bench (minimum)

| Piece | Notes |
| --- | --- |
| Soft support | Foam so the table does not pin modes |
| Excitation | Finger tap, soft hammer, or light pluck at rim vs hub |
| Sensor | Mic near surface, **or** very light accelerometer (mass loading shifts small PLA parts) |
| Analysis | Record ring-down → FFT → list peaks |

Average several taps. Discard hits that clip.

### Scale and material (hard limits)

- For similar shapes, natural frequencies scale roughly as \(1/L\) and with \( \sqrt{E/\rho} \).  
- A 1:4 PLA print will **not** share eigenfrequencies with a 61 cm siltstone bowl.  
- Log for every Mode B run: filament, infill %, wall count, measured mass, scale_factor, mount type.

Finding a PLA peak near 377 Hz is a fact about **that print**. It is not JE 71295.

---

## 4. Instrumentation notes

### `code/acoustic_logger.ino`

- Streams analog readings from up to four MEMS mics over serial.  
- Suitable as a **relative** multi-point amplitude logger for Mode A if:
  - sample rate is adequate for your band of interest, and  
  - the drive is known and time-aligned in your analysis script.  
- It is **not** a calibrated SPL meter and does not output phase-accurate audio WAVs by itself.

### Preferred path for publishable Mode A

1. Sound card or audio interface.  
2. Measurement mic (or consistent consumer mic in a **fixed** jig).  
3. Record WAV at ≥ 44.1 kHz.  
4. Offline FFT / SNR in Python (same windowing for all files).  
5. Optional: transfer function = object channel / reference channel.

### Phone mics

Allowed only for **relative** comparisons with a locked geometry (same phone, same stand, same distance).  
Do not treat phone dB readouts as absolute truth across apps or OS versions.

---

## 5. Pre-register template (copy before first run)

```text
Date:
Operator:
Scale factor / measured Ø / H / mass (Sabu):
Scale factor / measured Ø / H / mass (null):
Filament / infill / walls:
Drive type (dwell / sweep / noise):
Target band f0 ± Δf:
Metric definition:
Kill rule:
n repeats / orientations:
Mic positions (sketch or photo):
Mount description:
Room notes:
Key holder / scorer:
Positive check (pass/fail):
```

Store the filled sheet with the data folder.

---

## 6. Analysis checklist

1. Confirm positive check passed.  
2. Same window, FFT length, and scaling for every file.  
3. Compute metric for each coded run.  
4. After key open: table of Sabu vs null (mean ± scatter).  
5. Apply kill rule.  
6. Archive raw WAV/CSV + pre-register sheet + photos of open kidneys / mount.

Suggested results table:

| Code | Object (after key) | Orientation | Metric | Notes |
| --- | --- | --- | --- | --- |
| OBJ-… | Sabu / null | 0° / 120° / 240° | … | … |

---

## 7. What a result may claim

| Allowed | Not allowed |
| --- | --- |
| “Under protocol P, Sabu-form metric exceeded null by Δ in band B.” | “Sabu disk is a 377 Hz modulator.” |
| “This PLA print’s Mode B peaks were … at scale X.” | “Museum siltstone resonates at 377 Hz.” |
| “Null and Sabu were indistinguishable under P.” | “Resonance theory falsified forever” (one protocol is one protocol) |

L3 notes (F14, Z₀ ≈ 376.73 Ω, downloads) stay **off** the results table unless a separate, labeled framework section is clearly marked as non-measurement.

---

## 8. Link to the rest of the stack

| Piece | Role |
| --- | --- |
| Print + null twin | Objects under test (`REPLICA.md`, OpenSCAD) |
| Mode A + blind | Shape coupling claim (`NULL_TEST.md` + this file) |
| Mode B | Optional fingerprint of the print |
| SUPT probe | Separate ruler for ordered **series** — not a WAV peak oracle |
| Glyph / mechanism desks | Geometry and critique; they do not hear the disk |

---

## 9. Honest backlog

- [ ] WAV-oriented Python analysis script (`mic_` in → metric out) with fixed windowing  
- [ ] Calibrated single-mic path notes (interface + mic model)  
- [ ] Contact-piezo Mode B option for small scales  
- [ ] Segmented 1:1 acoustic plan (large object, near-field mapping)  
- [ ] Publish one fully blinded example dataset (even if Δ ≈ 0)
