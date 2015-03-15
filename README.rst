Random VCard-Generator
======================

Generiert `VCards <https://de.wikipedia.org/wiki/VCard>`_ mit zufälligen, aber plausiblen Daten.

Diese VCards können z.B. benutzt werden, um Software zu testen, die VCards importiert oder verarbeitet.

Das in Python geschriebene Kommandozeilen-Tool ist Open Source und steht unter der `GPLv3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Installation
------------

::

	# pip install vcardgen

Für die Installation brauchst du Admin-Rechte. Wenn du nicht root bist benutze sudo oder wende dich an den Administrator.

Eine VCard erzeugen
-------------------
::

	$ vcardgen Kontakt.vcf

Sie wird als Kontakt.vcf im aktuellen Verzeichnis gespeichert.

1000 VCards erzeugen
--------------------
::

	$ vcardgen -c 1000 Kontakte.vcf

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
	N:Metzler;Lorena;;;
	FN:Lorena Metzler
	BDAY;VALUE=DATE:1935-05-03
	TITLE:Rentnerin
	CATEGORIES:Sportverein
	NOTE:Lieblingsessen: Champignon mit Soße\n\nMotto: Lachen ist die beste Medizin.
	END:VCARD
