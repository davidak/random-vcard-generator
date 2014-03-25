Random VCard-Generator
======================

Generiert `VCards <https://de.wikipedia.org/wiki/VCard>`_ mit zufälligen, aber plausiblen Daten.

Die so generierten VCards können z.B. benutzt werden, um Software zu testen, die VCards importiert.

Das in Python geschriebene Kommandozeilen-Tool ist Open Source und steht unter der `GPL Version 3 <http://www.gnu.org/licenses/gpl-3.0.html>`_.

Installation
------------

Mit der Paketverwaltung `pip <http://www.pip-installer.org/en/latest/>`_ lassen sich Python-Pakete aus dem `Python Package Index <https://pypi.python.org/pypi/vcardgen/>`_ (PyPI) installieren.
::

	$ pip install vcardgen

Da vcardgen derzeit nur auf Python 3 getestet ist, muss das und `pip` für diese Version auf deinem System installiert sein. Zudem braucht man für die Installation neuer Pakete Administratorrechte.

Der Befehl sieht dann z.B. so aus:
::

	$ sudo pip-3.2 install vcardgen

Deinstallation
--------------

Beim Entfernen gilt das gleiche wie bei der Installation. Wenn du root bist und Python 3 auf deinem System das Standard-Python ist, kannst du einfach diesen Befehl nutzen:
::

	$ pip uninstall vcardgen

Ansonsten nutze `sudo`, um das Programm `pip` für Python 3 mit Administratorrechten auszuführen.
::

	$ sudo pip-3.2 uninstall vcardgen

Um alle installierten Abhängigkeiten zu deinstallieren, füge dem Befehl `PyZufall` und `frogress` getrennt durch Leerzeichen an.

Eine VCard erzeugen
-------------------
::

	$ vcardgen Kontakt.vcf

Sie wird als `Kontakt.vcf` im aktuellen Verzeichnis gespeichert.

1000 VCards erzeugen
--------------------
::

	$ vcardgen -c 1000 Kontakte.vcf

Die Anzahl wird mit dem Parameter `-c` angegeben.

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
