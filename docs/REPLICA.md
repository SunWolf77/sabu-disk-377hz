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

---

## 3. Recommended print scales

Full scale (610 mm) needs a large-format printer or segmented print.

| Scale | Diameter | Height | Use |
| --- | --- | --- | --- |
| **1:1** | 610 mm | 106 mm | Museum-scale; specialist beds or multi-part |
| **1:2** | 305 mm | 53 mm | Serious acoustic / photo study |
| **1:4** | 152.5 mm | 26.5 mm | Desk acoustic null tests |
| **1:10** | 61 mm | 10.6 mm | Geometry check only |

OpenSCAD parameter `scale_factor` in `code/openscad/sabu_disk_approx.scad` sets this (1.0 = full scale).

---

## 4. Print settings (practical)

- **Material:** PLA or PETG for geometry tests. Stone-fill filaments are cosmetic only — density and stiffness ≠ siltstone.  
- **Orientation:** Flat on the bed (bowl opening up) unless you segment.  
- **Walls / infill:** High perimeter count; thin original walls are fragile — thicken slightly for PLA if needed, and **record the deviation**.  
- **Supports:** Likely under inward lobe undersides depending on model.  
- **Tolerance:** Central hole should stay circular; measure with calipers after print and log Ø.

---

## 5. Workflow

1. Open `code/openscad/sabu_disk_approx.scad`.  
2. Set `scale_factor` (e.g. `0.25` for 1:4).  
3. Render → export STL.  
4. Slice → print.  
5. Photograph next to a ruler; log actual diameter and height.  
6. For acoustic work: build a **null twin** (same mass class, no lobes or scrambled lobes) and follow `docs/NULL_TEST.md`.

---

## 6. What a successful print allows

| Allowed claim | Not allowed claim |
| --- | --- |
| “This PLA object approximates published Sabu disk dimensions at scale X.” | “This is the Sabu disk.” |
| “Under drive D, amplitude at 377 Hz differed from null by …” (if measured) | “Ancient 377 Hz modulator proven.” |
| “Form matches Emery plan-view features (3 inward lobes, central socket).” | “Museum-certified exact mesh.” |

---

## 7. Next upgrades (honest backlog)

- [ ] Replace approx SCAD with measurements from a licensed museum scan or measured replica.  
- [ ] Segmented 1:1 print plan (bolt circle, alignment pins).  
- [ ] Density-matched composite if acoustic mass loading matters.  
- [ ] Publish caliper sheet + photos with every acoustic CSV.
