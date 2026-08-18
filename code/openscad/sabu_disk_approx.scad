// Sabu disk — APPROXIMATE printable model from published measurements
// Sources: Emery 1949 Fig. 58; diameter 61 cm, height 10.6 cm, hole ~8 cm
// JE 71295, Egyptian Museum Cairo
//
// This is NOT a museum laser scan. Wall thickness and lobe curvature are
// simplified for FDM strength. Log any deviations when you publish results.
//
// Units: millimetres at scale_factor = 1.0 (full scale)

scale_factor = 0.25;  // 0.25 = 1:4 desk scale (~152.5 mm diameter)

D     = 610 * scale_factor;   // outer diameter
H     = 106 * scale_factor;   // max height
HOLE  =  80 * scale_factor;   // central hole diameter
WALL  =  10 * scale_factor;   // simplified wall (original is thinner in places)
HUB_H =  90 * scale_factor;   // hub / socket height (approx bowl depth)
HUB_OD = 110 * scale_factor;  // hub outer diameter (approx)

module lobe_cut(angle) {
    rotate([0, 0, angle])
        translate([D * 0.22, 0, H * 0.35])
            rotate([0, 25, 0])
                scale([1.1, 0.55, 0.35])
                    sphere(d = D * 0.55, $fn = 64);
}

module sabu_approx() {
    difference() {
        // outer bowl blank
        union() {
            difference() {
                cylinder(h = H * 0.35, d = D, $fn = 128);
                translate([0, 0, WALL])
                    cylinder(h = H, d = D - 2 * WALL, $fn = 128);
            }
            // raised rim
            difference() {
                cylinder(h = H * 0.2, d = D, $fn = 128);
                cylinder(h = H, d = D - 2 * WALL, $fn = 128);
            }
            // central hub
            cylinder(h = HUB_H, d = HUB_OD, $fn = 96);
        }
        // central bore
        translate([0, 0, -1])
            cylinder(h = HUB_H + 2, d = HOLE, $fn = 96);
        // three inward lobe voids (simplified)
        lobe_cut(0);
        lobe_cut(120);
        lobe_cut(240);
        // hollow bowl interior
        translate([0, 0, WALL])
            cylinder(h = H, d = D - 2.5 * WALL, $fn = 128);
    }
}

sabu_approx();

// Print tips:
// - Prefer scale_factor 0.25 or 0.5 for desktop beds
// - Measure finished diameter; do not claim museum-exact
// - Build a null twin (no lobe_cut calls) for acoustic tests
