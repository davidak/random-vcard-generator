Changelog
=========

Version 0.9
-----------

Veröffentlicht am 05.06.2016

- Parameter -f ist nun optional, Ausgabe in Terminal möglich
- Weitere Encoding-Probleme mit Python 2.7 behoben
- Problem beim Speichern von mehr als 6.000.000 VCards behoben
- Performance enorm gesteigert (nur noch 4,7 statt 19 Sekunden für 10.000 VCards)
- RAM-Nutzung verringert auf 6 MB (vorher je nach Anzahl VCards, 100 MB bei 10.000)
- Prüfung, ob genug Speicherplatz verfügbar ist
- Spätere Dateigröße anzeigen

Version 0.8.3
-------------

Veröffentlicht am 23.05.2016

- Unicode Fehler behoben, Kompatibilität mit Python 2/3 verbessert
- Python 3.2 wird nicht mehr unterstützt

Version 0.8.2
-------------

Veröffentlicht am 07.07.2015

- Fehler bei Installation mit Python 3 behoben

Version 0.8.1
-------------

Veröffentlicht am 15.03.2015

- Fehler in Paket auf PyPI behoben

Version 0.8
-----------

Veröffentlicht am 15.03.2015

- läuft jetzt auch mit Python 2.7
- Geburtsname und Geburtsort hinzugefügt
- E-Mail, Nickname und Homepage hinzugefügt
- Kennung der Software, die die VCard erzeugt hat, hinzugefügt
- Motto entfernt, unrealistisch

Version 0.7
-----------

Veröffentlicht am 02.03.2014

- Fortschrittsanzeige mit vergangener und verbleibender Zeit
- Benutzung vereinfacht

Version 0.6
-----------

Veröffentlicht am 01.03.2014

- jetzt auch mit pip installierbar und auf PyPI gehostet
- Dokumentation entsprechend angepasst

Version 0.5
-----------

Veröffentlicht am 09.01.2014

- Kommandozeilen-Interface (CLI) hinzugefügt
- viele Verbesserungen am Code

Version 0.4
-----------

Veröffentlicht am 24.09.2013

- kompletter Rewrite. benutzt nun die Klasse Person von PyZufall
- PyZufall git Submodul gelöscht, da es nun über PyPI installierbar ist
- CHANGELOG hinzugefügt
- viele kleine Änderungen

Version 0.3
-----------

Veröffentlicht am 23.07.2013

- README und LICENSE hinzugefügt

Version 0.2
-----------

Veröffentlicht am 23.07.2013

- PyZufall als git Submodul eingebunden
- Docstring hinzugefügt

Version 0.1
-----------

Veröffentlicht am 23.07.2013

- einfacher VCard-Generator, der PyZufall benutzt
