#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Der Python Random VCard-Generator generiert VCards mit zufälligen, aber plausiblen Daten.

Copyright (C) 2013 davidak

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see {http://www.gnu.org/licenses/}.
"""

import random as r
from datetime import datetime as date
from pyzufall.person import Person

__version__ = '0.4'

gruppen = ['Arbeit', 'Freunde', 'Familie', 'Sportverein', 'Ärzte', 'Piratenpartei', 'CCC', 'Bekannte aus dem Internet', 'Kegelclub', 'Mafia', 'Expartner', 'Prostituierte']


p = Person()

print("BEGIN:VCARD")
print("VERSION:3.0")
print("N:" + p.nachname + ";" + p.vorname + ";;;")
print("FN:" + p.name)
#print("NICKNAME:Broho")
#if r.randint(1,5) == 1:
#	print("X-MAIDENNAME:" + z.nachname())
bday = date.strptime(p.geburtsdatum, "%d.%m.%Y").date()
print("BDAY;VALUE=DATE:" + date.strftime(bday, "%Y-%m-%d"))
#print("ORG:" + z.firma() + ";Abteilung")
if r.randint(1,4) == 1: # jeder 5. Kontakt von Arbeit
	print("TITLE:" + p.beruf)
print("CATEGORIES:" + r.choice(gruppen))
#print("ADR;TYPE=WORK:;;Plorach Straße 27;Klostein;;46587;Deutschland")
#print("EMAIL;TYPE=INTERNET:" + p.email)
#print("URL;TYPE=WORK:" + p.webseite)
note = ''
if r.randint(0,1):
	note += 'Interessen: ' + p.interessen
if r.randint(0,1):
	if note:
		note += '\\n'
	note += 'Lieblingsfarbe: ' + p.lieblingsfarbe
if r.randint(0,1):
	if note:
		note += '\\n'
	note += 'Lieblingsessen: ' + p.lieblingsessen
if r.randint(0,1):
	if note:
		note += '\\n\\n'
	note += 'Motto: ' + p.motto
print("NOTE:" + note)
print("END:VCARD")
print('') #Zeilenumbruch
