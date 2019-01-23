'''
Long Name                      := Large Ship Mount
Short Name                     := Large Mount
Description                    := Larger sized weapon mount which increases damage from the weapon by 2 times. Requires a vehicle size of at least 400kT. Can only be used on Direct Fire weapons. 
Code                           := L
Cost Percent                   := 150
Tonnage Percent                := 150
Tonnage Structure Percent      := 200
Damage Percent                 := 200
Supply Percent                 := 200
Range Modifier                 := 0
Weapon To Hit Modifier         := 0
Vehicle Size Minimum           := 400
Weapon Type Requirement        := Direct Fire
Vehicle Type                   := Ship
'''

MOUNT = '''
Long Name                      := {name} Mount
Short Name                     := {name}
Description                    := {name} Mount. Requires a vehicle size of at least {size_minimum}kT. Can only be used on Direct Fire weapons. 
Code                           := {code}
Cost Percent                   := {size_percent}
Tonnage Percent                := {size_percent}
Tonnage Structure Percent      := {damage_percent}
Damage Percent                 := {damage_percent}
Supply Percent                 := {damage_percent}
Range Modifier                 := {range_modifier}
Weapon To Hit Modifier         := {hit_mod}
Vehicle Size Minimum           := {size_minimum}
Weapon Type Requirement        := Direct Fire
Vehicle Type                   := Ship
'''

class mount:
    def __init__(self, name, code, size_multiplier, damage_multiplier, range_modifier):
        self.name = name
        self.code = code
        self.damage_multiplier = damage_multiplier
        self.size_multiplier = size_multiplier
        self.size_minimum = 50 * size_multiplier
        self.range_modifier = range_modifier

    def __str__(self):
        return MOUNT.format(
            name = self.name,
            code = self.code,
            size_percent = self.size_multiplier * 100,
            damage_percent = self.damage_multiplier * 100,
            size_minimum = self.size_minimum,
            range_modifier = self.range_modifier,
            hit_mod = self.range_modifier * 20
        )


items = [
    mount("Spinal", "S", 10, 15, 1),
    mount("Massive Spinal", "SM", 20, 30, 2),
]

t = "c"

import helpers
helpers.write_data_file(items, __file__, t)
