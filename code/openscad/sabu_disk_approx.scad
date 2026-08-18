// Sabu disk — APPROXIMATE printable model (refined lobe curvature)
// Sources: Emery 1949 Fig. 58; Ø 61 cm, H 10.6 cm, hole ~8 cm
// Egyptian Museum Cairo JE 71295
//
// Geometry intent (museum plan-view):
//   - Shallow bowl, slightly raised outer rim
//   - Three WIDE spokes / lobes running rim → hub (steering-wheel look)
//   - Between spokes: smooth kidney openings (not gear teeth, not sphere bites)
//   - Lobes fold inward: upper surface rises then meets the central socket
//   - Outer rim survives as three narrow arches between openings
//
// NOT a laser scan. Wall thickness thickened for FDM. Log deviations.
// Units: mm at scale_factor = 1.0 (full scale)

$fn = 96;

scale_factor = 0.25;  // 0.25 → ~152.5 mm diameter (desk)

// --- published-class dimensions ---
D      = 610 * scale_factor;  // outer diameter
R      = D / 2;
H      = 106 * scale_factor;  // max height (hub / bowl depth class)
HOLE   =  80 * scale_factor;  // central bore
HUB_OD = 110 * scale_factor;  // hub outer diameter
WALL   =  max(2.4, 8 * scale_factor);  // printable wall (original thinner)
RIM_H  =  18 * scale_factor;  // rim lip height
FLOOR  =  max(1.6, 6 * scale_factor);  // bowl floor thickness

// lobe / opening tuning (plan view)
OPEN_R0    = R * 0.30;   // inner radius of kidney (near hub)
OPEN_R1    = R * 0.78;   // outer radius of kidney (near rim)
OPEN_HALF  = 28;         // half-angle of each opening (deg); 3× leaves wide spokes
OPEN_BULGE = 1.15;       // radial elongation of kidney
SPOKE_RISE = H * 0.55;   // how far lobe upper surface rises

// ---------------------------------------------------------------------------
// Kidney opening in plan: smooth void between two spokes
// ---------------------------------------------------------------------------
module kidney_2d() {
    // stadium / kidney in polar band OPEN_R0..OPEN_R1, angular width 2*OPEN_HALF
    hull() {
        // outer rounded end (near rim)
        for (a = [-OPEN_HALF, OPEN_HALF])
            rotate(a)
                translate([OPEN_R1, 0])
                    circle(r = R * 0.07);
        // mid bulge
        for (a = [-OPEN_HALF * 0.55, OPEN_HALF * 0.55])
            rotate(a)
                translate([(OPEN_R0 + OPEN_R1) * 0.52 * OPEN_BULGE / 1.15, 0])
                    circle(r = R * 0.10);
        // inner rounded end (near hub)
        for (a = [-OPEN_HALF * 0.35, OPEN_HALF * 0.35])
            rotate(a)
                translate([OPEN_R0, 0])
                    circle(r = R * 0.055);
    }
}

module kidney_void(angle) {
    rotate([0, 0, angle])
        linear_extrude(height = H * 1.4, center = true)
            kidney_2d();
}

// ---------------------------------------------------------------------------
// Bowl shell: floor + outer rim wall + gentle dish
// ---------------------------------------------------------------------------
module bowl_shell() {
    difference() {
        // solid blank
        union() {
            // floor disk
            cylinder(h = FLOOR, r = R, $fn = 128);
            // outer rim wall
            translate([0, 0, 0])
                difference() {
                    cylinder(h = RIM_H, r = R, $fn = 128);
                    translate([0, 0, -0.1])
                        cylinder(h = RIM_H + 0.2, r = R - WALL, $fn = 128);
                }
            // slight dish fill (solid that openings will cut)
            translate([0, 0, FLOOR])
                cylinder(h = SPOKE_RISE * 0.85, r1 = R - WALL * 0.3, r2 = R * 0.42, $fn = 128);
        }
        // inner cavity above floor (keep spokes by only cutting center later via kidneys)
        translate([0, 0, FLOOR + SPOKE_RISE * 0.15])
            cylinder(h = H, r = R * 0.20, $fn = 64);
    }
}

// ---------------------------------------------------------------------------
// Central hub / socket
// ---------------------------------------------------------------------------
module hub() {
    difference() {
        cylinder(h = H * 0.92, r = HUB_OD / 2, $fn = 96);
        translate([0, 0, -0.2])
            cylinder(h = H * 1.2, r = HOLE / 2, $fn = 96);
        // soft inner chamfer
        translate([0, 0, H * 0.92 - WALL * 0.4])
            cylinder(h = WALL, r1 = HOLE / 2, r2 = HOLE / 2 + WALL * 0.35, $fn = 64);
    }
}

// ---------------------------------------------------------------------------
// Lobe upper surface: gentle inward fold (hull along spoke centreline)
// ---------------------------------------------------------------------------
module lobe_surface(angle) {
    rotate([0, 0, angle])
        hull() {
            // root at rim (low)
            translate([R - WALL * 0.8, 0, RIM_H * 0.5])
                scale([1.0, 0.55, 0.35])
                    sphere(r = WALL * 1.1);
            // mid-span (higher — the fold)
            translate([R * 0.58, 0, SPOKE_RISE])
                scale([1.2, 0.70, 0.45])
                    sphere(r = WALL * 1.6);
            // near hub (meet socket)
            translate([HUB_OD * 0.55, 0, H * 0.55])
                scale([0.9, 0.55, 0.40])
                    sphere(r = WALL * 1.2);
        }
}

module lobe_surfaces() {
    for (a = [0, 120, 240])
        lobe_surface(a + 60);  // spokes sit between openings
}

// ---------------------------------------------------------------------------
// Full approximate disk
// ---------------------------------------------------------------------------
module sabu_approx() {
    difference() {
        union() {
            bowl_shell();
            hub();
            lobe_surfaces();
        }
        // three kidney openings through the dish
        for (a = [0, 120, 240])
            kidney_void(a);
        // clean central bore through everything
        translate([0, 0, -1])
            cylinder(h = H * 1.5, r = HOLE / 2, $fn = 96);
        // trim anything above max envelope
        translate([0, 0, H])
            cylinder(h = H, r = R * 1.1);
        // trim below bed
        translate([0, 0, -H])
            cylinder(h = H, r = R * 1.1);
    }
}

// ---------------------------------------------------------------------------
// Null twin: same envelope, no lobes / no kidneys (for acoustic null test)
// ---------------------------------------------------------------------------
module null_twin() {
    difference() {
        union() {
            cylinder(h = FLOOR, r = R, $fn = 128);
            difference() {
                cylinder(h = RIM_H, r = R, $fn = 128);
                translate([0, 0, -0.1])
                    cylinder(h = RIM_H + 0.2, r = R - WALL, $fn = 128);
            }
            hub();
        }
        translate([0, 0, -1])
            cylinder(h = H * 1.5, r = HOLE / 2, $fn = 96);
    }
}

// --- render ---
sabu_approx();
// null_twin();  // uncomment to export the null object instead

// ---------------------------------------------------------------------------
// Support structure recommendations (FDM) — full detail in docs/REPLICA.md §5
// ---------------------------------------------------------------------------
// Orientation: bowl UP (floor on bed). Avoid on-edge.
// Need supports under: lobe undersides if SPOKE_RISE is high (tree/organic).
// Never plug: the three kidney openings or the hub bore.
// Workflow: auto supports → paint-exclude kidneys + bore → keep pillars under solid lobes only.
// Settings start: tree supports, density 10–15%, top Z gap ~0.25–0.35 mm, overhang ~50–55°.
// Null twin: usually support-free bowl-up.
// After print: cool fully; open kidneys to light; photo before acoustic runs.
// scale_factor 0.25 or 0.5 for desktop beds; measure finished Ø; do not claim museum-exact.
