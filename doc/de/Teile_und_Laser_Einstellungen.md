Beginne hier zu lesen.

Übersicht der Bauteile
======================

Die Teile der Maschine gliedern sich in fünf Gruppen:

* Speicherwerk (memory unit)
* Addierwerk (adder unit)
* Multiplikationswerk (napier unit)
* Seitenwände
* Übrige und optionale Teile

Die drei Werke und die Seitenwände sollten aus 3.2mm Birken-Sperrholz gefertigt werden.
Die Datei src/BOM.txt (billl of materials) listet alle benötigten Materialen.
Am wichtigsten davon sind drei Sperrholzplatten 76cm x 50cm. Aller lasergeschnittenen Teile 
werden daraus gemacht.

Achte beim Holzeinkauf auf die exakte Dicke. Die Platten sollten maximal 3.2mm dick sein. Manche Hersteller verkaufen bis zu 3.5mm dicke Platten als 3mm (funktioniert hier nicht!). Manche Hersteller halten exakt 3.0mm ein (das funkioniert, baucht aber mehr Holzleim). Mit 3.2mm Holz funktionieren viele Verbindungen als stramme Steckverbindungen, die oft keinen Leim benötigen.
Birkensperrholz sollte in guter Qualität gekauft werden. Astfrei, glatt, absolut eben. Frage nach "Laserqualität". 
Beim Zuschnitt muss die Holzmaserung in Längsrichtung verlaufen. (Holzfedern quer zur Maserung funktionieren nicht!)

Buchensperrholz ist auch eine gute Wahl. Es ist deutlich härter, aber auch teurer.
Billiges Pappelsperrholz sollte vermieden werden. Es ist zu weich für Zahnräder.

Die drei Dateien schickard_napiers.svg, schickard_adder.svg und schickard_memory.svg im Unterverzeichnis src ergeben die komplette Maschine. In jeder der Dateien sollte die Ebene 'laser' sichtbar sein. Dies ergibt einer 76cm x 50cm 
Platte pro Datei.  Alle weiteren Dateien enthalten optionale Teile oder Hilfskonstruktionen aus denen die drei schickard_*.svg Dateien erzeugt wurden.

Im Folgenden wird beschrieben, was in den drei Platten enthalten ist. Die Teile sollten man streng nach Werken 
sortiert werden. Du kannst die Platten nacheinander schneiden und zusammenbauen, wenn du dich an die Reihenfolge hier hältst. Das Multiplizierwerk (napier unit) wird zuletzt gebaut, da es die übrigbleibende Teile von den anderen Platten verwendet.


Speicherwerk
------------
Dieses Werk ist einfacher als die anderen, und sollte zuerst zusammengebaut werden.
Das Speicherwerk ist eine flache Kiste (ca. 33cm lang, 3cm hoch, 7cm tief) am unteren Ende der Maschine.
Auf der Oberseite sind sechs Drehknöpfe und sechs Fenster, die je eine Ziffer zeigen. Zu Beginn einer Multiplikation wird hier eine der beiden Zahlen durch die Drehknöpfe eingestellt.
Die Unterseite hat Aussparungen, um einen Blick in den Mechanismus zu erlauben.


Alle Teile des Speicherwerks finden auf der linken Hälfte der Datei schickard_memory.svg platz -- die rechte Hälfte enthält eine der Seitenwände und einige Teile des Multiplizierwerks.
Von einem Typ Ring sind 9 Exemplare vorhanden. Sechs davon werden für das Speicherwerk benötigt, drei gehören zum Multiplizierwerk.


Ausserdem befinden sich 13 Teile für Positionierhilfen auf der Platte, die nur während der Montage benutzt werden. Diese sind nicht Teil der Maschine.

 * Finde fünf kleine Rechtecke 32mm x 14mm mit gezahnten Aussparungen, die mit "Positioning Aid Knob Assembly" beschriftet sind. Weiter fünf dieser Teile sind unbeschriftet. (Nur je vier beschriftete und unbeschriftete werden benötigt. Falls eines verloren geht oder bricht, benutze das fünfte.)
 * Finde zwei gewinkelte Teile mit Innekurve ca. 6cm x 5cm mit der Beschriftung "Napier - Positioning Aid Side Connectors". Lege sie zur Seite, sie werden später bei den Seitenwänden benutzt.
 * Finde ein rechteckiges Teil ca. 7cm x 3cm mit der Beschriftung "Positioning Aid Side Connectors Memory". Lege es zur Seite, es wird später bei den Seitenwänden benutzt.

Ausserdem sind zwei Sätze Ringe auf der Platte. Ein Satz ist am unteren Rand und hat 14.4mm Aussendurchmesser. Der andere Satz ist am rechten Rand und hat 14.3mm. Benutze den einen Satz, der die bessere Presspassung bietet. Optional können Ringe aus stärkerem Material, beispielsweise Kraftplex gelasert werden.
Lege die Ringe zur Seite, sie werden später beim Addierwerk und Multiplizierwerk benutzt.



Addierwerk
----------
The adder unit is a box (ca. 33cm x 8cm x 8cm) in the center of the machine. It has six wheels with knobs on its front, each wheel has 10 holes that can be operated with a 6mm rod or the end of a pen.
The top surface features six windows, where the result is displayed.
The back of the box is open and shows the most complex part of the machine: the gears. This mechanism performs correct carry-over to neigbouring digits. [Wilhelm Schickard](https://en.wikipedia.org/wiki/Wilhelm_Schickard Wikipedia article on Wilhelm Schickard) was most likely the first to design and document such a mechanism.

The result of all computations are displayed in this unit. To start multiplying, turn the wheels so that 000000 is displayed.

All parts fit on schickard_adder.svg using ca. two third of a 76 x 50 board. The right hand third of this file contains one set of side wall parts, and three sets of shafts for the napier drums. 

Also on this board are 12 parts that positioning aids used during assembly. They are not part of the machine.
Locate two rectangles ca 11cm x 5cm labeled "Positioning Aid Carry Wheels". Locate five small 32mm x 14mm rectangles with a toothed cut out. They are labeled "Positioning Aid Knob Assembly". There are five more unlabled parts very similar to the labeled ones. You can re-use the knob assembly aids from the memory unit and discard these 10 parts found here.
All knobs are identical.


Napier Unit
-----------
This is the upper part of the machine, where multiplications are done. It is named after [John Napier](https://en.wikipedia.org/wiki/John_Napier "Wikipedia Article on John Napier"), who invented the "[Napier's Bones](https://en.wikipedia.org/wiki/Napier%27s_bones)" giving the layout of the numbers on the drums.

The Napier unit consists of a box (ca. 33cm x 21cm x 6cm) with 6 drums standing upright. The back side of the box is open, to allow studying the interier, 
the front has 8 sliders that can cover one row each of the multiplication table. Row "1" is always visible.
On the top are 6 knobs. To start multiplying, close all slides and enter one of the two numbers here by turing the knobs, so that it is shown in Row "1".

All parts for the box and most parts of the drums are in the schickard_napiers.svg file.
The layout fills one 76cm x 50 cm board. Two sets of napiers bones and several rings and shafts for the drums are 
on the lower right hand side of the schickard_memory.svg. Three sets of shaft parts are on the right hand side 
of schickard_adder.svg.


Side Walls
----------
The machine has a modular design. Each of the three units as its own enclosure. The left and right sides of the 
machine are the two walls that hold the three modules in place. Each wall consits of two layer of plywood
 * the outer layer with only openings for the 8 slides,
 * the inner layer with openings for also the sides of the three units.

The memory unit is locked into the side walls using one connector on each side.
The napiers unit has two connectors (top and bottom) on each side.
The adder unit has none.

A wall connector is 30mm long, 6mm wide (two layers of plywood glued together), and in the middle 13mm high.
A rectanglar hole 4mm x 6mm goes across the connector.
Wall connectors are glued with their flat surface into the sidewalls. Their curved part extends into the sides of the memor or napier box. In this position a slim wedge can be inserted in to the hole of the connector locking the box in place.


Miscellaneous
-------------

The file schickard_misc_construction.svg has an additional set of rings (replacing the ones found in schickard_memory.svg). There are three different outer diameters 14.3mm, 14.4mm, and 14.5mm here. You can optionally cut these rings out of harder material like acrylic or kraftplex. The rings server as bearings for the shafts of napier and adder unit.

The file schickard_sign.svg has a wooden sign with two feet, for display with the machine. The sign is optional, it is not a part of the machine. This is designed for a 4mm plywood board.

There are also arrays of red lines, 90mm apart and 13mm apart. These can be used to cut the needed 4mm and 6mm 
shafts from beech wood rods with a lasercutter.



Laser Settings
==============
To cut the parts from the boards you need access to a laser cutter with a bed of at least 76cm x 50cm size.
Find a machine large enough at your nearest FabLab or hacker space.
A machine with ca. 60-80 Watts is recommended. Expect ca. two hours cutting time and another two hours handling time
for collecting the parts from the machine and sort them into suitable containers. In total, there are ca. 600 parts.

The source files are are SVG format. These files can be processed with VisiCut (or converted with inkscape to PDF or other formats needed for your laser machine). Please re-check the dimensions (76 x 50) of the drawings after conversion.

The line colors (stroke or outline color) used in the SVG files have different meaning. 

 * Red. These lines cut through the board. (E.g an 80W Thunderlaser may use speed 30, power 70/50 to cut through 3mm birchwood.)
 * Green. These lines are superficial markings. (E.g an 80W Thunderlaser may use speed 200, power 8/35 on birchwood.)
   Engraving mode (rasterization) may also work for green, but is not recommended, as it may be much slower.
 * Blue and other colors (if any) are to be ignored.

Several different fill colors were used during constructions, some parts have no fill. 
These colors have no meaning for laser cutting. 
Line width (stroke thickness) is typically 0.1 or 0.2mm. This also has no meaning for laser cutting.

Expect that some of the smaller parts may fall through the grid of the laser bed. It is recomended to clean any previous waste from the machine before starting. Most of the smaller parts come larger numbers than actually needed to save you from collecting each and every dropped piece.

A large table surface helps to keep the parts arranged into small piles. If needed, use containers like cardboard boxes or transparent zip bags for handling the parts between cutting and assembly.


Next steps
==========
Next read 'Adjustments and Maintenance' before assembly. 
You learn there where to apply grease before a part becomes inaccessible.
Do not forget check out the assembly gallery in the photos folder before you start.


