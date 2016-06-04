Random VCard-Generator
======================

.. image:: https://travis-ci.org/davidak/random-vcard-generator.svg?branch=master
    :target: https://travis-ci.org/davidak/random-vcard-generator

.. image:: https://badge.fury.io/py/vcardgen.svg
    :target: https://badge.fury.io/py/vcardgen

Generiert `VCards <https://de.wikipedia.org/wiki/VCard>`_ mit zufälligen, aber plausiblen Daten.

Diese können z.B. genutzt werden, um Software zu testen, die VCards importiert oder verarbeitet.

Das in Python geschriebene Kommandozeilen-Tool ist Open Source und steht unter der `GPLv3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Installation
------------

::

	# pip install vcardgen

Für die Installation brauchst du Admin-Rechte. Wenn du nicht root bist benutze sudo oder wende dich an den Administrator.

Kompatibel mit Python 2.7, Python 3.3+ sowie `PyPy <http://pypy.org/>`_.

Eine VCard erzeugen
-------------------

::

	$ vcardgen -f Kontakt.vcf

Sie wird als Kontakt.vcf im aktuellen Verzeichnis gespeichert.

1000 VCards erzeugen
--------------------
::

	$ vcardgen -c 1000 -f Kontakte.vcf

Die Anzahl wird mit dem Parameter -c angegeben.

Hilfe
-----
::

	$ vcardgen -h

Beispiel
--------
::

	BEGIN:VCARD
	VERSION:3.0
	PRODID:-//davidak//Random VCard-Generator 0.8//DE
	FN:Sara Hufnagel
	N:Hufnagel;Sara;;;
	BDAY:2003-11-02
	BIRTHPLACE:Luckau
	CATEGORIES:Freunde
	TZ:+0100
	EMAIL;TYPE=INTERNET;TYPE=HOME;TYPE=PREF:sarhuf@yahoo.com.au
	URL;TYPE=HOME:http://sara.hufnagel.org/
	NOTE:Lieblingsfarbe: Grau
	END:VCARD
