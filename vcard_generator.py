#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Generiert eine VCard mit zufälligen, aber plausiblen Daten.

https://de.wikipedia.org/wiki/VCard

Für die Erzeugung zufälliger Daten wird pyzufall benutzt.
https://github.com/davidak/pyzufall
"""

from pyzufall import pyzufall as z
import random as r

geschlecht = r.randint(0,1)

if geschlecht:
	vname = z.vorname_m() + z.e16("-" + z.vorname_m()) #16% Wahrscheinlichkeit ein Doppelname
else:
	vname = z.vorname_w() + z.e16("-" + z.vorname_w())

nname = z.nachname()

bday = str(r.randint(1950,2012)) + "-" + str(r.randint(1,12)).zfill(2) + "-" + str(r.randint(1,31)).zfill(2)

print("BEGIN:VCARD")
print("VERSION:3.0")
print("N:" + nname + ";" + vname)
print("FN:" + vname + " " + nname)
#print("NICKNAME:Broho")
if r.randint(1,5) == 1:
	print("X-MAIDENNAME:" + z.nachname())
if r.randint(0,1):
	print("BDAY;VALUE=DATE:" + bday)
#print("ORG:" + z.firma() + ";Abteilung")
if r.randint(1,4) == 1:
	if geschlecht:
		berufsbez = z.beruf_m()
	else:
		berufsbez = z.beruf_w()
	print("TITLE:" + berufsbez)
	print("CATEGORIES:Arbeit")
else:
	print("CATEGORIES:" + r.choice(['Ärzte', 'Piratenpartei', 'CCC', 'Freunde', 'Familie']))
if r.randint(0,2):
	print("EMAIL;TYPE=INTERNET:" + vname.lower() + "." + nname.lower() + "@" + r.choice(['gmx.de', 'web.de', 't-online.de', 'gmail.com', 'hotmail.com']))
#print("ADR;TYPE=WORK:;;Plorach Straße 27;Klostein;;46587;Deutschland")
if r.randint(1,8) == 1:
	print("URL;TYPE=WORK:http://" + r.choice([vname.lower() + "-" + nname.lower(), nname.lower()]) + r.choice(['.de', '.net', '.org', '.me', '.com']) + "/")
if r.randint(0,1):
	print("NOTE:Motto: " + z.sprichwort())
print("END:VCARD")
print() #Zeilenumbruch
