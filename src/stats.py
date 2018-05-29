#!/bin/python3
# -*- coding: utf8 -*-

import character
import PyPDF2
import json

name = "Zen"
s_loc = "DnD_5E_CharacterSheet-Zen.pdf"

pc = character.Fifth_ED_Character(name, s_loc)


def extractData(floc):
    s = open(floc, 'rb')
    r = PyPDF2.PdfFileReader(s)
    d = json.dumps(r.getFormTextFields())
    json.dump(r.getFormTextFields(), open("fieldstext_raw.txt", "w"))
    return json.loads(d)


def parseData(d):
    pc.xp = d['XP']
    pc.str = d['STR']
    pc.dex = d['DEX']
    pc.const = d['CON']
    pc.intel = d['INT']
    pc.wis = d['WIS']
    pc.cha = d['CHA']
    pc.ac = d['AC']
    # We will generate modifiers for each attribute in another file since we have the value
    #Attributes

    # Saving throws
    pc.st_chr = d['ST Sharisma']
    pc.st_con = d['ST Constitution']
    pc.st_dex = d['ST Dexterity']
    pc.st_int = d['ST Intelligence']
    pc.st_str = d['ST Strength']
    pc.st_wis = d['ST Wisdom']

    # Combat related
    pc.hit_dice = d['HDTotal']
    pc.hp_max = d['HPMAX']
    pc.hp_current = d['HPCurrent']
    pc.hp_temp = d['HPTEMP']

    # Character Physical Traits
    # we already know name
    pc.age = d['Age']
    pc.height = d['Height']
    pc.weight = d['Weight']
    pc.eyecolor = d['Eyes']
    pc.skin = d['Skin']
    pc.hair = d['Hair']
    pc.appearance = d['']
    pc.alliesAndOrg = d['Allies']
    pc.backstory = d['Backstory']
    pc.FeatsTraits = d['Features and Traits']
    pc.addFeatsTraits = d['Feat+Traits']
    pc.treasure = d['Treasure']
    pc.background = d['Background']
    pc.alignment = d['Alignment']



parseData(extractData(pc.file))
