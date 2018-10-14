
'''
Name                  := Space Yard III
Description           := Ship construction component which can work on one ship at a time.
Pic Num               := 49
Tonnage Space Taken   := 400
Tonnage Structure     := 200
Cost Minerals         := 4000
Cost Organics         := 0
Cost Radioactives     := 500
Vehicle Type          := Ship\Base
Supply Amount Used    := 0
Restrictions          := None
General Group         := Construction
Family                := 6
Roman Numeral         := 3
Custom Group          := 0
Number of Tech Req    := 1
Tech Area Req 1       := Space Yards
Tech Level Req 1      := 3
Number of Abilities   := 4
Ability 1 Type        := Space Yard
Ability 1 Descr       := Can construct with 2000 minerals per turn.
Ability 1 Val 1       := 1
Ability 1 Val 2       := 2000
Ability 2 Type        := Space Yard
Ability 2 Descr       := Can construct with 2000 organics per turn.
Ability 2 Val 1       := 2
Ability 2 Val 2       := 2000
Ability 3 Type        := Space Yard
Ability 3 Descr       := Can construct with 2000 radioactives per turn.
Ability 3 Val 1       := 3
Ability 3 Val 2       := 2000
Ability 4 Type        := Component Repair
Ability 4 Descr       := Can repair 8 components per turn.
Ability 4 Val 1       := 8
Ability 4 Val 2       := 0
Weapon Type           := None
'''

BASE_COMPONENT = '''
Name                  := {name}
Description           := Ship construction component which can work on one ship at a time.
Pic Num               := 49
Tonnage Space Taken   := {tonnage}
Tonnage Structure     := {structure}
Cost Minerals         := {cost_minerals}
Cost Organics         := 0
Cost Radioactives     := {cost_radioactives}
Vehicle Type          := Ship\Base
Supply Amount Used    := 0
Restrictions          := None
General Group         := Construction
Family                := 6
Roman Numeral         := 0
Custom Group          := 0
Number of Tech Req    := 1
Tech Area Req 1       := Space Yards
Tech Level Req 1      := {tech_level}
Number of Abilities   := 4
Ability 1 Type        := Space Yard
Ability 1 Descr       := Can construct with {construct} minerals per turn.
Ability 1 Val 1       := 1
Ability 1 Val 2       := {construct}
Ability 2 Type        := Space Yard
Ability 2 Descr       := Can construct with {construct} organics per turn.
Ability 2 Val 1       := 2
Ability 2 Val 2       := {construct}
Ability 3 Type        := Space Yard
Ability 3 Descr       := Can construct with {construct} radioactives per turn.
Ability 3 Val 1       := 3
Ability 3 Val 2       := {construct}
Ability 4 Type        := Component Repair
Ability 4 Descr       := Can repair {repair} components per turn.
Ability 4 Val 1       := {repair}
Ability 4 Val 2       := 0
Weapon Type           := None
'''


class ship_yard:
    def __init__(self, name, tech_level, scale):
        self.base_tech_level = 3
        self.base_repair = 8
        self.base_construct = 2000
        self.base_cost_minerals = 4000
        self.base_cost_radioactives = 500
        self.base_tonnage = 400
        self.base_structure = int(self.base_tonnage / 2)

        self.name = name
        self.scale = scale
        self.tech_level = tech_level

    def __str__(self):
        return BASE_COMPONENT.format(
            name = self.name,
            tonnage = self.base_tonnage * self.scale,
            construct = self.base_construct * self.scale,
            structure = self.base_structure * self.scale,
            cost_minerals = self.base_cost_minerals * self.scale,
            cost_radioactives = self.base_cost_radioactives * self.scale,
            repair = self.base_repair * self.scale,
            tech_level = self.base_tech_level + self.tech_level
            )


items = [
    ship_yard("Medium Space Yard", 1, 2),
    ship_yard("Large Space Yard", 2, 5),
    ship_yard("Industrial Complex", 3, 10),
    ship_yard("Massive Industrial Complex", 4, 20),
]


t = "c"

import helpers
helpers.write_data_file(items, __file__, t)

