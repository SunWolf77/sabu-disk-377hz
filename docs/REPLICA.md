# 3D-print replica instructions — Sabu disk

**Goal:** A printable form that tracks **published museum geometry**, not a fantasy gear.

---

## 1. Sourced measurements (use these)

Consensus figures used for this replica brief:

| Dimension | Value | Notes / source |
| --- | --- | --- |
| Outer diameter | **610 mm** | Emery 1949; Egypt Museum / Wikipedia |
| Max height | **106 mm** | Emery 1949 |
| Central hole diameter | **~80 mm** | Museum descriptions (~8 cm) |
| Wall thickness (thin regions) | **~8–12 mm** | Not a single official number; treat as **approx.** for print strength |
| Lobe count | **3** | 120° rotational symmetry |
| Material (original) | Metasiltstone / siltstone | Fragile; not plastic |

**Primary references**

1. Emery, W. B. (1949). *Great Tombs of the First Dynasty*, Vol. 1. Cairo: Government Press. Fig. 58 (plan + section).  
2. Egyptian Museum, Cairo — inventory **JE 71295**.  
3. El-Khouli, A. (1978). *Egyptian Stone Vessels: Predynastic Period to Dynasty III*. Mainz: Zabern. Cat. 5586; pls. 135, 158.  
4. Summary pages: [Wikipedia — Sabu disk](https://en.wikipedia.org/wiki/Sabu_disk); [Egypt Museum — Sabu Disk](https://egypt-museum.com/sabu-disk/).

**Caveat:** No public laser scan was used here. Until a museum mesh exists, any STL is an **approximation** of Emery’s drawing + the measurements above. Do not call it “museum exact.”

---

## 2. What the form must look like

From the published description (Emery / museum summaries):

- Shallow **bowl**, not a flat plate.  
- Slightly raised **outer rim**.  
- Three **wide curved lobes** folded **inward** toward a central tubular socket.  
- Outer rim continues as **narrow arches** between the non-folded segments.  
- Central **socket / hub** whose height is roughly the bowl depth; open hole ~80 mm.  
- **No gear teeth.** No serrated circumference. Those belong to wrong modern analogies.

If your print looks like a bicycle sprocket, it is the wrong object.

### OpenSCAD lobe model (current)

File: `code/openscad/sabu_disk_approx.scad`

| Feature | How it is built |
| --- | --- |
| Plan openings | Three **kidney** voids (`OPEN_HALF`, `OPEN_R0`/`OPEN_R1`) — smooth, not sphere bites |
| Spokes / lobes | Remaining solid between kidneys + raised **lobe_surface** hull (rim → mid-fold → hub) |
| Rim arches | Outer ring kept; kidneys stop short of the lip |
| Null twin | `null_twin()` module — same envelope, no kidneys / no lobe surfaces |

Tune curvature without rewriting the file:

- `OPEN_HALF` ↑ → wider openings, narrower spokes  
- `OPEN_HALF` ↓ → wider spokes (more “steering wheel”)  
- `SPOKE_RISE` ↑ → stronger inward fold in elevation  
- `OPEN_R0` / `OPEN_R1` → move openings toward hub or rim  

---

## 3. Recommended print scales

Full scale (610 mm) needs a large-format printer or segmented print.

| Scale | Diameter | Height | Use |
| --- | --- | --- | --- |
| **1:1** | 610 mm | 106 mm | Museum-scale; specialist beds or multi-part |
| **1:2** | 305 mm | 53 mm | Serious acoustic / photo study |
| **1:4** | 152.5 mm | 26.5 mm | Desk acoustic null tests |
| **1:10** | 61 mm | 10.6 mm | Geometry check only |

OpenSCAD parameter `scale_factor` sets this (1.0 = full scale). Default in file is `0.25`.

---

## 4. Print settings (practical)

- **Material:** PLA or PETG for geometry tests. Stone-fill filaments are cosmetic only — density and stiffness ≠ siltstone.  
- **Orientation:** Flat on the bed, **bowl opening up** (default). See §5 for alternatives.  
- **Walls / infill:** High perimeter count (3–5); 15–25% infill is enough for geometry checks. Thicken for strength if needed and **record the deviation**.  
- **Tolerance:** Central hole should stay circular; measure with calipers after print and log Ø.

---

## 5. Support structure recommendations

The hard rule: **supports must not permanently plug the three kidney openings.** Those openings are the plan-view signature. If they fill solid, the print is the wrong object for geometry or acoustic work.

### Preferred orientation

| Orientation | When to use | Support load |
| --- | --- | --- |
| **Bowl up (floor on bed)** | Default for desk scales (1:4, 1:2) | Lobes may need light support under overhangs; rim sits on bed |
| **Bowl down (rim on bed)** | Only if your slicer bridges lobe tops cleanly | More interface under the floor; harder to keep kidneys clear |
| **On edge** | Avoid for this model | Destroys symmetry; heavy supports; not worth it |

### Where supports are actually needed

| Region | Risk | Recommendation |
| --- | --- | --- |
| **Lobe undersides** (inward fold, mid-span) | Overhang / bridge sag | Tree or organic supports *under the solid lobe only* |
| **Kidney openings** | Slicer may want to fill the void | **Blocker / support enforcer off** inside openings; paint-on supports excluding voids |
| **Rim arches** | Usually printable from the floor | Often **no** support if bowl-up |
| **Hub outer wall** | Near-vertical | Usually **no** support |
| **Hub inner bore** | Can get stray interface | Disable supports inside the bore; clean with drill/ream if needed |
| **Null twin** | Almost none | Often **support-free** bowl-up |

### Slicer settings (FDM starting point)

Use as a checklist; tune to your machine.

| Setting | Suggested start |
| --- | --- |
| Support type | **Tree / organic** preferred (less scarring on lobe undersides) |
| Support placement | Everywhere **or** touching buildplate — then **paint-exclude** the three kidneys and the hub bore |
| Overhang threshold | ~50–55° (lets mild bridges go unsupported) |
| Support density | 10–15% (low — easier removal on thin lobes) |
| Top Z distance / air gap | 0.25–0.35 mm (one layer-ish) so interface breaks clean |
| Interface layers | 2–3; pattern lines or grid |
| Support brim | Optional on large scales only |
| Avoid supports on | Kidney voids, central bore, outer vertical rim |

**Paint-on workflow (recommended):** auto-generate supports → manually erase any pillar that sits inside a kidney or the hub hole → keep pillars only under solid lobe mass.

### Removal without breaking lobes

1. Let the part cool fully on the bed.  
2. Remove tree trunks from the outside in; do not twist thin spoke mid-spans.  
3. Needle-nose / flush cutters for stubs under lobes.  
4. Check each kidney is fully open — light should pass. If a film remains, trim; do not melt-close the opening.  
5. Photograph the open kidneys before any acoustic run (geometry record).

### Scale-dependent notes

| Scale | Support note |
| --- | --- |
| **1:10** | Often little or no support; walls are short |
| **1:4** | Light tree under lobes if `SPOKE_RISE` is high |
| **1:2** | Tree supports likely; watch bed adhesion on large footprint |
| **1:1** | Segment the print or use a large-format machine; plan support access per segment |

### Null twin

`null_twin()` has no kidneys and no raised lobe folds. Print **bowl-up**, supports usually **off**. Same material and wall settings as the Sabu-form so mass stays comparable for the null test (`docs/NULL_TEST.md`).

### What not to do

- Solid “everywhere” supports that fill the three openings.  
- Soluble support *inside* kidneys unless you can guarantee full wash-out (record if used).  
- Sanding the openings shut “to look cleaner.”  
- Claiming museum-exact after support scars change lobe thickness — log the scar / sand depth if you measure acoustics.

---

## 6. Workflow

1. Open `code/openscad/sabu_disk_approx.scad`.  
2. Set `scale_factor` (e.g. `0.25` for 1:4).  
3. Optional: nudge `OPEN_HALF` / `SPOKE_RISE` until plan view matches Emery’s wide-spoke look.  
4. Render → export STL (`sabu_approx`).  
5. Comment out `sabu_approx();`, uncomment `null_twin();`, export second STL under a **code name**.  
6. Slice with §5 support rules → print both.  
7. Clear kidneys; photograph next to a ruler; log actual diameter and height.  
8. Acoustic work: follow `docs/NULL_TEST.md`.

---

## 7. What a successful print allows

| Allowed claim | Not allowed claim |
| --- | --- |
| “This PLA object approximates published Sabu disk dimensions at scale X.” | “This is the Sabu disk.” |
| “Under drive D, amplitude at 377 Hz differed from null by …” (if measured) | “Ancient 377 Hz modulator proven.” |
| “Form matches Emery plan-view features (3 inward lobes, central socket).” | “Museum-certified exact mesh.” |

---

## 8. Next upgrades (honest backlog)

- [ ] Replace approx SCAD with measurements from a licensed museum scan or measured replica.  
- [ ] Segmented 1:1 print plan (bolt circle, alignment pins).  
- [ ] Density-matched composite if acoustic mass loading matters.  
- [ ] Publish caliper sheet + photos with every acoustic CSV.  
- [ ] Optional: tighter lobe profile from Emery Fig. 58 digitised centreline.
