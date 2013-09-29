Python Random VCard-Generator
=============================

Generiert `VCards <https://de.wikipedia.org/wiki/VCard>`_ mit zufälligen, aber plausiblen Daten.

Die so generierten VCards können z.B. benutzt werden, um Software zu testen, die VCards importiert.

Der Python Random VCard-Generator ist Open Source und steht unter der `GPL Version 3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Installation
------------

Lade `die neuste Version <https://github.com/davidak/python-random-vcard-generator/releases>`_ herunter und entpacke sie, z.B. in deinem Benutzerordner.

Für die Generierung zufälliger Daten wird `PyZufall <https://pyzufall.readthedocs.org/>`_ verwendet.

Wie du PyZufall installierst, erfährst du in dessen `Dokumentation <https://pyzufall.readthedocs.org/de/latest/installation.html>`_.

Eine VCard erzeugen
-------------------
::

	$ python3 vcard_generator.py > VCard.vcf

5 VCards in einer Datei erzeugen
--------------------------------

Für die Erzeugung mehrerer VCards in einer Datei kann die `Shell <http://de.wikipedia.org/wiki/Bourne-again_shell>`_ benutzt werden.
Das Funktioniert auf Unix (z.B. OS X) und Linux.
::

	for i in {1..5} ; do python3 vcard_generator.py >> Kontakte.vcf ; done

Natürlich kannst du statt 5 auch 10000 eingeben.

Beispiele
---------
::

	BEGIN:VCARD
	VERSION:3.0
	N:Ramm;Ulrich;;;
	FN:Ulrich Ramm
	BDAY;VALUE=DATE:1966-03-30
	CATEGORIES:Arbeit
	NOTE:
	END:VCARD

	BEGIN:VCARD
	VERSION:3.0
	N:Höpfner;Lutz;;;
	FN:Lutz Höpfner
	BDAY;VALUE=DATE:1925-03-29
	CATEGORIES:CCC
	NOTE:Interessen: Tennis\nLieblingsfarbe: Grün\nLieblingsessen: Pilz mit Thunfischsoße
	END:VCARD

	BEGIN:VCARD
	VERSION:3.0
	N:Joswig;Wilhelm;;;
	FN:Wilhelm Joswig
	BDAY;VALUE=DATE:2005-02-04
	CATEGORIES:Piratenpartei
	NOTE:Interessen: Fotografie, lesen, telefonieren\nLieblingsessen: Kohl mit Gemüse\n\nMotto: Abwarten und Tee trinken.
	END:VCARD

	BEGIN:VCARD
	VERSION:3.0
	N:Staab;Marina;;;
	FN:Marina Staab
	BDAY;VALUE=DATE:1973-11-24
	TITLE:Notarin
	CATEGORIES:CCC
	NOTE:Interessen: Münzen sammeln, Selbstverteidigung
	END:VCARD

	BEGIN:VCARD
	VERSION:3.0
	N:Holle;Paul;;;
	FN:Paul Holle
	BDAY;VALUE=DATE:2001-12-24
	TITLE:Schüler
	CATEGORIES:Familie
	NOTE:Lieblingsessen: Rettich mit Ketchup\n\nMotto: Auch Wasser wird zum edlen Tropfen, mischt man es mit Malz und Hopfen!
	END:VCARD
