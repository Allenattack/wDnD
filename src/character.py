#!/bin/python3
# -*- coding: utf8 -*-

class Fifth_ED_Character:
    xp = 0
    str = 0
    dex = 0
    const = 0
    intel = 0
    wis = 0
    cha = 0
    ac = 0

    # Saving throws
    st_chr = ""
    st_con = ""
    st_dex = ""
    st_int = ""
    st_str = ""
    st_wis = ""

    # Combat related
    hit_dice = ""
    hp_max = 0
    hp_current = 0
    hp_temp = 0

    # Character Physical Traits
    # we already know name
    age = 0
    height = ""
    weight = 0
    eyecolor = ""
    skin = ""
    hair = ""
    appearance = ""
    alliesAndOrg = ""
    backstory = ""
    FeatsTraits = ""
    addFeatsTraits = ""
    treasure = ""
    background = ""
    alignment = ""

    # Spells Header
    spellClass = ""
    spellAbil = ""
    spellSave = 0
    spellAttBonus = 0

    # Spells themselves
    cantrips = []
    spellSlots = 0
    # Debating what to do for each spell level

    def __init__(self, name, floc):
        # base stuff to know before we extract everything
        self.name = name
        self.file = floc
