python-random-vcard-generator
=============================

Generiert eine VCard mit zufälligen, aber plausiblen Daten.

https://de.wikipedia.org/wiki/VCard

Für die Erzeugung zufälliger Daten wird pyzufall benutzt.
https://github.com/davidak/pyzufall

Für die Erzeugung mehrerer VCards in einer Datei kann die Shell benutzt werden.
Das Funktioniert auf Unix (z.B. OS X) und Linux.

	for i in {1..5} ; do python3 vcard_generator.py >> Kontakte.vcf ; done

Beispiel
--------

	BEGIN:VCARD
	VERSION:3.0
	N:Reisner;Armin
	FN:Armin Reisner
	X-MAIDENNAME:Gerk
	BDAY;VALUE=DATE:1954-03-24
	CATEGORIES:Freunde
	EMAIL;TYPE=INTERNET:armin.reisner@web.de
	END:VCARD
	 
	BEGIN:VCARD
	VERSION:3.0
	N:Senn;Anica
	FN:Anica Senn
	CATEGORIES:Freunde
	EMAIL;TYPE=INTERNET:anica.senn@gmail.com
	URL;TYPE=WORK:http://anica-senn.net/
	NOTE:Motto: Auf Donner folgt gern Regen.
	END:VCARD
	 
	BEGIN:VCARD
	VERSION:3.0
	N:Johannes;Georg
	FN:Georg Johannes
	CATEGORIES:Familie
	EMAIL;TYPE=INTERNET:georg.johannes@web.de
	END:VCARD
	 
	BEGIN:VCARD
	VERSION:3.0
	N:Mucha;Sergej
	FN:Sergej Mucha
	CATEGORIES:Familie
	EMAIL;TYPE=INTERNET:sergej.mucha@hotmail.com
	NOTE:Motto: Betrunkene und Kinder sagen die Wahrheit.
	END:VCARD
	 
	BEGIN:VCARD
	VERSION:3.0
	N:Kehrer;Kaan
	FN:Kaan Kehrer
	X-MAIDENNAME:Pavlovic
	TITLE:Vermessungsingenieur
	CATEGORIES:Arbeit
	EMAIL;TYPE=INTERNET:kaan.kehrer@gmx.de
	NOTE:Motto: Alle Wege führen nach Rom.
	END:VCARD
