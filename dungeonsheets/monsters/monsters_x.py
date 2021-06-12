"""
A collection of monsters from D&D 5e's SRD

This file was autogenerated by https://github.com/stravajiaxen/5e-srd-to-py
"""

from dungeonsheets.monsters.monsters import Monster
from dungeonsheets.stats import Ability


class Xorn(Monster):
    """
    **Earth Glide**: The xorn can burrow through nonmagical, unworked earth and stone. While doing so, the xorn doesn't disturb the material it moves through.

    **Stone Camouflage**: The xorn has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.

    **Treasure Sense**: The xorn can pinpoint, by scent, the location of precious metals and stones, such as coins and gems, within 60 ft. of it.

    **Multiattack**: The xorn makes three claw attacks and one bite attack.

    **Bite**: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (3d6 + 3) piercing damage.

    **Claw**: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.
    """

    name = "Xorn"
    description = "Medium elemental, neutral"
    challenge_rating = 5
    armor_class = 19
    skills = "Perception +6, Stealth +3"
    senses = "Darkvision 60 ft., Tremorsense 60 ft., Passive Perception 16"
    languages = "Terran"
    strength = Ability(17)
    dexterity = Ability(10)
    constitution = Ability(22)
    intelligence = Ability(11)
    wisdom = Ability(10)
    charisma = Ability(11)
    speed = 20
    swim_speed = 0
    fly_speed = 0
    climb_speed = 0
    hp_max = 73
    hit_dice = "7d8"