l_e=300; // largeur écran mm
jeu= 10;//jeu de chaque coté mm

pp= 400; // profondeur caisse mm

t1=18; // largeur tasseau 1 (carre)
t2=13;

p1l=28; //l planche1
p1h=9;//h planche1

p1l=28; //l planche1
p1h=9;//h planche1


ll=l_e+2*jeu+2*t1; //largeur ext structure


jj=400;
kk=200;
hh=jj+kk;

ee=6; //epaisseur plateau milieu

color("grey")
cube([ll,pp,ee]);

translate([0,0,hh-t1+ee]){
color("blue") {
    translate([t1,0,0])
    cube([ll-2*t1,t1,t1]);
    translate([t1,pp-t1,0])
    cube([ll-2*t1,t1,t1]);
    }
color("red") {
    translate([0,t1,0])
    cube([t1,pp-2*t1,t1]);
    translate([ll-t1,t1,0])
    cube([t1,pp-2*t1,t1]);
    }
}
translate([0,0,ee]){
color("green") {
    translate([0,0,0])
    cube([t1,t1,hh]);
    translate([ll-t1,0,0])
    cube([t1,t1,hh]);
    translate([0,pp-t1,0])
    cube([t1,t1,hh]);
    translate([ll-t1,pp-t1,0])
    cube([t1,t1,hh]);
    }
color("red") {
    translate([0,t1,0])
    cube([t1,pp-2*t1,t1]);
    translate([ll-t1,t1,0])
    cube([t1,pp-2*t1,t1]);
    }
color("blue") {
    translate([t1,pp-t1,0])
    cube([ll-2*t1,t1,t1]);
    }
color("blue",0.5) {
    translate([t1,0,0])
    cube([ll-2*t1,t2,t2]);
    }
}
// planches sur le cadre
translate([0,0,hh+ee]){
color("orange"){
    translate([0,0,0])
    cube([p1l,pp,p1h]);
    translate([ll-p1l,0,0])
    cube([p1l,pp,p1h]);
    }
}

