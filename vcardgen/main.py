#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Copyright (C) 2013 - 2016 davidak
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see {http://www.gnu.org/licenses/}.

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

from os import (statvfs, path)
import sys
import ctypes
import platform
import argparse
import frogress
import random as r
from datetime import datetime
from pyzufall.person import Person
from .version import __version__

if sys.version_info[0] == 2:
    from kitchen.text.converters import getwriter
    UTF8Writer = getwriter('utf8')
    sys.stdout = UTF8Writer(sys.stdout)

name = "Random VCard-Generator"

parser = argparse.ArgumentParser()
parser.add_argument('-V', '--version', action='version', version=name + ' ' + __version__)
parser.add_argument("-q", "--quiet", action="store_true", help="no output on screen")
parser.add_argument("-c", "--count", type=int, default=1, help="number of vcards to generate")
parser.add_argument('-f', '--file', help='filename or path, typical with .vcf extension')
args = parser.parse_args()

vcard_size = 312  # Bytes
total_vcard_size = vcard_size * args.count

widgets = [frogress.BarWidget, frogress.PercentageWidget, frogress.ProgressWidget('VCard: '), frogress.TimerWidget, frogress.EtaWidget]
gruppen = ['Arbeit', 'Kunden', 'Freunde', 'Familie', 'Sportverein', 'Ärzte', 'Piratenpartei', 'CCC', 'Bekannte aus dem Internet']


def sizeof_fmt(num, suffix='B'):
    """Dateigröße menschenlesbar ausgeben"""
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.2f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f %s%s" % (num, 'Yi', suffix)


def get_free_space(path):
    """Gibt den freien Speicherplatz im angegebenen Verzeichnis in Bytes zurück"""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(path), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value
    else:
        st = statvfs(path)
        return st.f_bavail * st.f_frsize


def check_available_storage():
    free_space = get_free_space(path.dirname(path.realpath(args.file)))
    if total_vcard_size > free_space:
        print('Fehler: {} Speicherplatz benötigt, aber nur {} frei'.format(sizeof_fmt(total_vcard_size), sizeof_fmt(free_space)))
        sys.exit(1)


def generate_vcard():
    _p = Person()

    _s = "BEGIN:VCARD\n"
    _s += "VERSION:3.0\n"
    _s += "PRODID:-//davidak//{} {}//DE\n".format(name, __version__)
    _s += "FN:{}\n".format(_p.name)
    _s += "N:{};{};;;\n".format(_p.nachname, _p.vorname)
    if r.randint(0,1):
        _s+= "NICKNAME:{}\n".format(_p.nickname)
    if _p.geburtsname != _p.nachname:
        _s += "X-MAIDENNAME:{}\n".format(_p.geburtsname)
    _bday = datetime.strptime(_p.geburtsdatum, "%d.%m.%Y").date()
    _s += "BDAY:{}\n".format(_bday)
    if r.randint(0,1):
        _s += "BIRTHPLACE:{}\n".format(_p.geburtsort)
    #_s = "ORG:" + z.firma() + ";Abteilung\n"
    if _p.beruf != 'kein' and r.randint(0,1):
        _s += "TITLE:{}\n".format(_p.beruf)
    _s += "CATEGORIES:{}\n".format(r.choice(gruppen))
    _s += "TZ:+0100\n"
    #_s += "ADR;TYPE=WORK:;;Plorach Straße 27;Klostein;;46587;Deutschland\n"
    if _p.alter < 80 and r.randint(1,100) < 85:
        _s += "EMAIL;TYPE=INTERNET;TYPE=HOME;TYPE=PREF:{}\n".format(_p.email)
    if _p.alter < 50 and r.randint(0,1):
        _s += "URL;TYPE=HOME:{}\n".format(_p.homepage)

    # Notiz zusammensetzen
    _note = ''
    if r.randint(0,1):
        _note += 'Interessen: ' + _p.interessen
    if r.randint(0,1):
        if _note:
            _note += '\\n'
        _note += 'Lieblingsfarbe: ' + _p.lieblingsfarbe
    if r.randint(0,1):
        if _note:
            _note += '\\n'
        _note += 'Lieblingsessen: ' + _p.lieblingsessen
    if _note:
        _s += "NOTE:{}\n".format(_note)

    _s += "END:VCARD\n\n"

    del _p
    return _s


def main():
    if args.file:
        check_available_storage()
        output = ''
        if not args.quiet:
            print('{} {}'.format(name, __version__))
            print('Generiere {} ({})'.format(args.file, sizeof_fmt(total_vcard_size)))
            for i in frogress.bar(range(args.count), steps=args.count, widgets=widgets):
                output += generate_vcard()
                if (i % 250) == 0 or i == args.count - 1: # schreibe immer 250 vcards in datei
                    with open(args.file, mode='a', encoding='utf-8') as f:
                        f.write(output)
                        output = ''
            print("\n")
        else:
            for i in range(args.count):
                output += generate_vcard()
                if (i % 250) == 0 or i == args.count - 1: # schreibe immer 250 vcards in datei
                    with open(args.file, mode='a', encoding='utf-8') as f:
                        f.write(output)
                        output = ''
    else:
        for i in range(args.count):
            print(generate_vcard(), end='')


if __name__ == "__main__":
    main()
