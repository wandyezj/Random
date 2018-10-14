'''
Name                          := Starbase
Short Name                    := Starbase
Description                   := 
Code                          := SB
Primary Bitmap Name           := Starbase
Alternate Bitmap Name         := Starbase
Vehicle Type                  := Base
Tonnage                       := 2500
Cost Minerals                 := 2500
Cost Organics                 := 0
Cost Radioactives             := 0
Engines Per Move              := 0
Number of Tech Req            := 1
Tech Area Req 1               := Base Construction
Tech Level Req 1              := 3
Number of Abilities           := 2
Ability 1 Type                := Combat To Hit Defense Minus
Ability 1 Descr               := Large size makes base 60% easier to hit in combat.
Ability 1 Val 1               := 60
Ability 1 Val 2               := 0
Ability 2 Type                := Modified Maintenance Cost
Ability 2 Descr               := Reduced wear and tear allow for a decrease in maintenance cost of 50%.
Ability 2 Val 1               := -50
Ability 2 Val 2               := 0
Requirement Must Have Bridge  := True
Requirement Can Have Aux Con  := True
Requirement Min Life Support  := 6
Requirement Min Crew Quarters := 6
Requirement Uses Engines      := False
Requirement Max Engines       := 0
Requirement Pct Fighter Bays  := 0
Requirement Pct Colony Mods   := 0
Requirement Pct Cargo         := 0
'''

VEHICLE = '''
Name                          := {name}
Short Name                    := {name}
Description                   := 
Code                          := {code}
Primary Bitmap Name           := Starbase
Alternate Bitmap Name         := Starbase
Vehicle Type                  := Ship
Tonnage                       := {tonnage}
Cost Minerals                 := {tonnage}
Cost Organics                 := 0
Cost Radioactives             := 0
Engines Per Move              := 0
Number of Tech Req            := 2
Tech Area Req 1               := {tech}
Tech Level Req 1              := {tech_level}
Number of Abilities           := 3
Ability 1 Type                := Combat To Hit Defense Minus
Ability 1 Descr               := Large size makes base {hit_mod}% easier to hit in combat.
Ability 1 Val 1               := {hit_mod}
Ability 1 Val 2               := 0
Ability 2 Type                := Modified Maintenance Cost
Ability 2 Descr               := Reduced wear and tear allow for a decrease in maintenance cost of 50%.
Ability 2 Val 1               := -50
Ability 2 Val 2               := 0
Ability 3 Type                := Standard Ship Movement
Ability 3 Descr               := Built in engine allows for slow movement.
Ability 3 Val 1               := 1
Ability 3 Val 2               := 0
Requirement Must Have Bridge  := True
Requirement Can Have Aux Con  := True
Requirement Min Life Support  := {crew}
Requirement Min Crew Quarters := {crew}
Requirement Uses Engines      := True
Requirement Max Engines       := 0
Requirement Pct Fighter Bays  := 0
Requirement Pct Colony Mods   := 0
Requirement Pct Cargo         := 0
'''

class vehicle_size:

    def __init__(self, name, code, tonnage, tech_level, hit_mod):
        self.name = name
        self.code = code
        self.tonnage = tonnage
        self.tech = "Massive Construction"
        self.tech_level = tech_level
        self.hit_mod = hit_mod
        self.crew = int(tonnage / 2500) * 6
 
    def __str__(self):
        return VEHICLE.format(
            name = self.name,
            code = self.code,
            tonnage = self.tonnage,
            tech = self.tech,
            tech_level = self.tech_level,
            hit_mod = self.hit_mod,
            crew = self.crew
        )

items = {
    vehicle_size("Barge", "B", 2000, 1, 50),
    vehicle_size("Star Fortress", "SF", 5000, 2, 100),
    vehicle_size("Artificial Moon", "AM", 10000, 3, 150),
}


t = "v"

import helpers
helpers.write_data_file(items, __file__, t)