Random VCard-Generator
======================

Generiert `VCards <https://de.wikipedia.org/wiki/VCard>`_ mit zufälligen, aber plausiblen Daten.

Die so generierten VCards können z.B. benutzt werden, um Software zu testen, die VCards importiert.

Das in Python geschriebene Kommandozeilen-Tool ist Open Source und steht unter der `GPL Version 3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Installation
------------

Lade `die neuste Version <https://github.com/davidak/random-vcard-generator/releases>`_ herunter und entpacke sie, z.B. in deinem Benutzerordner.

Für die Generierung zufälliger Daten wird `PyZufall <https://pyzufall.readthedocs.org/>`_ verwendet.

Wie du PyZufall installierst, erfährst du in dessen `Dokumentation <https://pyzufall.readthedocs.org/de/latest/installation.html>`_.

Eine VCard erzeugen
-------------------
::

	$ ./vcard-generator.py

100 VCards erzeugen und als 100_VCards.vcf speichern
----------------------------------------------------

::

	$ ./vcard-generator.py -c 100 -o 100_VCards.vcf

Hilfe
-----

::

	$ ./vcard-generator.py -h


Beispiel
--------
::

	BEGIN:VCARD
	VERSION:3.0
	N:Metzler;Lorena;;;
	FN:Lorena Metzler
	BDAY;VALUE=DATE:1935-05-03
	TITLE:Rentnerin
	CATEGORIES:Sportverein
	NOTE:Lieblingsessen: Champignon mit Soße\n\nMotto: Lachen ist die beste Medizin.
	END:VCARD
