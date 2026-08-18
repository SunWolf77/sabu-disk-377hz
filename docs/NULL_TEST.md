# Null test — Sabu replica @ target frequency

A null test asks whether **this shape**, under a fixed drive, differs from a **matched twin that should be quiet** if the shape-story is right.

---

## Claim under test (one line)

> Under the same acoustic drive and mic geometry, the three-lobed Sabu-form replica shows a higher response in a stated band (e.g. 377±2 Hz) than a null object of similar mass and outline.

If you change the claim, rewrite this file before running.

---

## Objects

| Object | Code example | Requirement |
| --- | --- | --- |
| Sabu-form print | `OBJ-A` | Approx museum geometry at chosen scale |
| Null twin | `OBJ-B` | Same scale, same material, **no three-lobe order** (flat disc or scrambled lobes), similar mass |
| Optional positive | tone only | Pure tone into the mic path with no object — proves logger hears the line |

Mark physical objects with **codes only**. Keep the key sealed until scores are written.

---

## Pre-register (before first run)

Write these down:

1. Scale factor and measured Ø / height after print.  
2. Speaker distance, level, sweep or dwell schedule.  
3. Metric: e.g. amplitude in 377±2 Hz, or SNR vs 350–400 Hz baseline.  
4. Kill rule: e.g. “Sabu − null ≤ 0 on metric → claim fails this protocol.”  
5. Number of repeats and orientations.  
6. Who holds the key; who scores.

---

## Blind sequence

1. Prep assigns codes; seals key.  
2. Runner places coded objects, records `run_<code>_<n>.wav` (or CSV). Interleave order.  
3. Scorer receives **coded files only**, fills metric column.  
4. Key opens; merge; apply kill rule.  
5. Publish **both** Sabu and null numbers.

Do not name files `sabu_peak_final.png` before scoring.

---

## Solo operator

Prep day 1 → rename files with a random map → score day 2 from renamed set only → open key last.

---

## What a pass means

Only: under this protocol, this shape differed from this null.  

It does **not** mean ancient purpose, SUPT validation, or “modulator.” Those are L3. Keep them off the results table.
