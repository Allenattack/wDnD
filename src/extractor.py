#!/bin/python3
# -*- coding: utf8 -*-

import PyPDF2
import json

sheet = open('DnD_5E_CharacterSheet-Zen.pdf', 'rb')

reader = PyPDF2.PdfFileReader(sheet)

fields = reader.getFormTextFields()

data = json.dumps(fields)

print(fields)

json.dump(fields, open("fieldstext.txt", "w"), sort_keys=True, indent=4)
