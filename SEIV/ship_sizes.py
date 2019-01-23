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

'''

Name                          := Barge
Short Name                    := Barge
Description                   := Massive slow moving hull with vehicle control and engines built in. Designed for moving Ring and Sphere world components into place, but useable for other non-combat tasks.
Code                          := MB
Primary Bitmap Name           := Barge
Alternate Bitmap Name         := TransportLarge
Vehicle Type                  := Base
Tonnage                       := 2000
Cost Minerals                 := 10000
Cost Organics                 := 0
Cost Radioactives             := 0
Engines Per Move              := 1
Number of Tech Req            := 4
Tech Area Req 1               := Ship Construction
Tech Level Req 1              := 11
Tech Area Req 2               := Base Construction
Tech Level Req 2              := 4
Tech Area Req 3               := Cargo
Tech Level Req 3              := 3
Tech Area Req 4               := Stellar Manipulation
Tech Level Req 4              := 5
Number of Abilities           := 3
Ability 1 Type                := Combat To Hit Defense Minus
Ability 1 Descr               := Bulk and Massive size makes MB 99% easier to hit in combat.
Ability 1 Val 1               := 99
Ability 1 Val 2               := 0
Ability 2 Type                := Combat To Hit Offense Minus
Ability 2 Descr               := Bulk and Massive size makes MB 99% less likely to hit in combat.
Ability 2 Val 1               := 99
Ability 2 Val 2               := 0
Ability 3 Type                := Standard Ship Movement
Ability 3 Descr               := Generates 1 standard movement.
Ability 3 Val 1               := 1
Ability 3 Val 2               := 0
Requirement Must Have Bridge  := False
Requirement Can Have Aux Con  := False
Requirement Min Life Support  := 0
Requirement Min Crew Quarters := 0
Requirement Uses Engines      := False
Requirement Max Engines       := 0
Requirement Pct Fighter Bays  := 0
Requirement Pct Colony Mods   := 0
Requirement Pct Cargo         := 0
'''

TECH = ['''
Name                  := Massive Ship Construction
Group                 := Applied Science
Description           := Technology to construct Massive Ships.
Maximum Level         := 3
Level Cost            := 100000
Start Level           := 0
Raise Level           := 0
Racial Area           := 0
Unique Area           := 0
Can Be Removed        := False
Number of Tech Req    := 3
Tech Area Req 1       := Construction
Tech Level Req 1      := 1
Tech Area Req 2       := Base Construction 
Tech Level Req 2      := 3
Tech Area Req 3       := Ship Construction
Tech Level Req 3      := 9
'''
]

VEHICLE = '''
Name                          := {name}
Short Name                    := {name}
Description                   := {description}
Code                          := {code}
Primary Bitmap Name           := Starbase
Alternate Bitmap Name         := Starbase
Vehicle Type                  := Ship
Tonnage                       := {tonnage}
Cost Minerals                 := {tonnage}
Cost Organics                 := 0
Cost Radioactives             := 0
Engines Per Move              := 1
Number of Tech Req            := 1
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
Requirement Must Have Bridge  := False
Requirement Can Have Aux Con  := True
Requirement Min Life Support  := 0
Requirement Min Crew Quarters := 0
Requirement Uses Engines      := False
Requirement Max Engines       := 0
Requirement Pct Fighter Bays  := 0
Requirement Pct Colony Mods   := 0
Requirement Pct Cargo         := 0
'''

class vehicle_size:

    def __init__(self, name, code, tonnage, tech_level, hit_mod, description = ""):
        self.name = name
        self.code = code
        self.tonnage = tonnage
        self.tech = "Massive Ship Construction"
        self.tech_level = tech_level
        self.hit_mod = hit_mod
        self.crew = int(tonnage / 1250) * 3
        self.description = description
 
    def __str__(self):
        return VEHICLE.format(
            name = self.name,
            code = self.code,
            tonnage = self.tonnage,
            tech = self.tech,
            tech_level = self.tech_level,
            hit_mod = self.hit_mod,
            crew = self.crew,
            description = self.description
        )

BARGE_DESCRIPTION = "Massive slow moving hull with vehicle control and engines built in. Designed for moving Ring and Sphere world components into place, but useable for other non-combat tasks."

items = [
    vehicle_size("Barge", "B", 2000, 1, 50, BARGE_DESCRIPTION),
    vehicle_size("Star Fortress", "SF", 5000, 2, 100),
    vehicle_size("Artificial Moon", "AM", 10000, 3, 150),
]


t = "v"

import helpers
helpers.write_data_file(items, __file__, t)

t = "t"
helpers.write_data_file(TECH, __file__, t)