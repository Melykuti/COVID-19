## Analyse der Verbreitung der SARS-CoV-2 Coronavirus-Pandemie in Deutschland und in den deutschen Bundesländern

> * Auf dieser Seite untersuche ich die gesamte oder kumulierte Anzahl der Coronavirus-Fälle und nicht die Anzahl der zur Zeit infizierten.

Zusammenfassung am Samstag, 23 Mai 2020:

* Die Anzahl der neuen Coronavirus-Infektionen ist in jedem Bundesland niedrig.
* Die höchsten Werte an Neuinfektionen weisen Bremen (1,7 Fälle pro Tag pro 100.000 EinwohnerInnen), Hessen, Niedersachsen (jeweils 1,1) und Berlin (1,0) auf. In Baden-Württemberg ist dieser Wert 0,4.
* Bund und Länder haben vereinbart, Beschränkungen für die Bevölkerung in einzelnen Landkreisen oder kreisfreien Städten zu verschärfen, wenn die Anzahl der Neuinfektionen pro Woche pro 100.000 EinwohnerInnen auf 50 steigt. Einige Bundesländer haben diese Grenze gesenkt: in Berlin und Niedersachsen gilt 30, in Bayern und Brandenburg gilt 35.

16 März 2020 (aktualisiert am 23 Mai 2020), Freiburg i. Br. – In der Anfangsphase der Verbreitung der Epidemie ist fast die ganze Bevölkerung empfindlich und jeder Erkrankte kann eine erhebliche Anzahl von gesunden Menschen anstecken. So kann die Anzahl der Infizierten Schritt für Schritt immer ein Faktor größer werden. Dieser Verlauf ist exponentielles Wachstum.

Bis die allgemeinen Ausgangsbeschränkungen angefangen haben ihre Wirkung zu zeigen, stimmten die beobachteten Coronavirus-Fallzahlen mit diesem Verlauf überein, sowohl in vielen europäischen Ländern als auch in Deutschland und in jedem einzigen Bundesland. Freiburg war die erste deutsche Großstadt, die solch einen Lockdown am 21.03.2020 angeordnet hat.

In dieser Analyse versuche ich es in begreifbarer Form zu beantworten, wie schnell die COVID-19-Pandemie sich zur Zeit ausbreitet. Da ich die älteren Resultate unten immer behalte, ist es möglich, mit dem früheren Ablauf einen Vergleich zu machen.

### Analyse

Meine Methodologie habe ich [auf Englisch in Detail beschrieben.](https://github.com/Melykuti/COVID-19/blob/master/global.md) Für Deutschland und für die Bundesländer melde ich seit 12.04.2020 die kumulativen (gesamten) bestätigten Coronavirus-Fallzahlen.

Bis 01.04.2020 rechnete ich für jeden Tag das Folgende aus: `Nr. der Ansteckenden = Nr. der Fälle - Nr. der Tode`. Da die Nummer der erholten PatientInnen das Robert Koch Institut lange nicht zur Verfügung stellte, war es nie möglich die aktuelle Anzahl der derzeit Infizierten auszurechnen. Denn es gibt immer mehr von den Genesenen und die Anzahl der Todesfälle ist vergleichsweise gering, macht es keinen Sinn mehr, diese ungenaue Annäherung zu machen. Deshalb bin ich auf die reine kumulative Fallzahl umgestiegen.

Seit 03.05.2020 bestimme ich eine annähernde Linie der täglich meldeten neuen Coronavirus-Fälle. (Davor hatte ich immer die kumulativen Zahlen angenähert.) Ich verwende lineare Regression auf diesen täglichen Zuwachs, und nenne dieses Modell das _lineare_ Modell. Ich wiederhole das gleiche mit dem Logarithmus des täglichen Zuwachses, und nenne das resultierende Modell das _exponentielle_ Model. Ich wähle die Fensterlänge (wieviele Tage, das heißt, wieviele Datenpunkte die beste Annäherung ergeben) und das bessere der beiden Modelle automatisiert aus. In der frühen, mit exponentiellem Wachstum gekennzeichneten Phase der Pandemie ist das exponentielle Modell genauer.

Auch wenn die tägliche Differenz schon ziemlich stabil ist und das Wachstum sichtbar nur linear ist, kann es immer wieder vereinzelt vorkommen wenn beide Modelle im Zeitfenster sehr gut sind, dass die Optimierung die exponentielle Annäherung genauer findet als die lineare Annäherung. Man darf dem Vorzug des exponentiellen Modells vor dem linearen nicht allzu viel Bedeutung beimessen.

Von der durch lineare Regression bestimmten annähernden Linie rechne ich vieles aus: den jetzigen täglichen Zuwachs; die Rate, wie lange es dauert, bis die Anzahl der Infekten sich verdoppelt; oder den Faktor, mit dem die Anzahl von einem Tag bis zum Nächsten wächst.

Mich interessiert sehr, **wie hoch die Wahrscheinlichkeit ist, dass ich mich mit dem SARS-CoV-2-Coronavirus infiziere**. Wenn wir die nicht bestätigten Fälle ignorieren, dann ist es unser Ziel, nicht in den täglichen Zuwachs der neu infizierten zu geraten. Ich drücke diesen Zuwachs pro 100.000 Einwohner aus, was ich am informativsten finde. Man kann diese Spalte durch die Zeit verfolgen oder die Zeitreihe direkt auf der Grafik sehen.

### Datenquelle

Die Daten werden durch das Robert Koch Institut gesammelt und [veröffentlicht](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html). Da ich auf der Webseite nur die aktuellen Fallzahlen finde, verwende ich [Wikipedia](https://de.wikipedia.org/wiki/COVID-19-Pandemie_in_Deutschland#Infektionsf%C3%A4lle_nach_Bundesl%C3%A4ndern), wo Freiwillige die ganzen Zeitreihen gespeichert haben.

Die zu den relativen Fallzahlen verwendeten Bevölkerungsgrößen stammen aus dem [Gemeinsamen Statistikportal der Statistischen Ämter des Bundes und der Länder](https://www.statistikportal.de/de/bevoelkerung/flaeche-und-bevoelkerung).

### Programmdateien

* **download_DEU.py** ist das Skript um die Daten von [Wikipedia](https://de.wikipedia.org/wiki/COVID-19-F%C3%A4lle_in_Deutschland) herunterzuladen.

* **DEU.py** ist das für Deutschland spezifische Skript, das hauptsächlich für die Vorbereitung der Daten von Wikipedia zuständig ist.

* **utils.py** hat die gemeinsamen Funktionen, die die Analyse und die Visualisierung durchführen.

* **comparison_joint.py** beinhaltet die für die Datenverarbeitung und Grafik notwendige Funktionen, um die Ländervergleiche herzustellen.

### Schaubilder

Die Schaubilder zeigen sowohl den täglichen Zuwachs der bestätigten COVID-19-Fälle als auch die gesamte Anzahl der Infekten, das heißt, die gesamte Anzahl der Fälle.

Auf der linken Seite ist die Zunahme gegenüber dem Vortag. In der Mitte ist die kumulierte Fallzahl auf normaler linearer Skala. Auf der rechten Seite ist sie auf logarithmischer Skala auf Basis&nbsp;10. Die blaue Kurve zeigt die Beobachtungen.

Ich wähle immer die letzten 7-14 Tage aus, um die lineare Regression durchzuführen. Mit der Wahl der Länge des Zeitintervalls versuche ich die beste Anpassung zu erreichen, gemessen an R^2 und an der Quote zwischen dem aus der Annäherung errechneten Zuwachs im Zeitfenster und dem wahren Zuwachs. Seit 18.03.2020 ist diese Optimierung automatisiert. Bis 7 Mai 2020 wurde das Zeitfenster mit einer Länge von 4-14 Tagen gewählt. Um den deutlichen Effekt der Wochenenden möglichst zu dämpfen habe ich mich entschieden, die Fenstergröße auf mindestens 7 Tage zu erhöhen.

Nachdem die optimale Fenstergröße für sowohl das exponentielle als auch das lineare Modell ausgewählt wurde, vergleiche ich die beiden. Wenn die exponentielle Annäherung besser ist als die lineare, dann markiere ich das Resultat mit einer orangenfarbigen Linie. Im umgekehrten Fall ist die Annäherung mit pinkfarbiger Linie markiert.


#### Die gesamte Bundesrepublik

![Deutschland](https://github.com/Melykuti/COVID-19/blob/master/plots/Deutschland_2020-05-23.png)

Auf diesen drei Schaubildern verwende ich nur das lineare Model. (Wenn ich das exponentielle Modell auch in das Rennen schicken würde, dann bekäme ich ein hin und her Schalten zwischen den beiden Modellen für jede Linie, was zu einer großen Varianz der Wachstumsraten führt.) [Eine Begründung der angewandten Methodik findet man hier.](https://github.com/Melykuti/COVID-19/blob/master/comparison.md)

![Täglicher relativer Zuwachs in Deutschland im Zeitablauf](https://github.com/Melykuti/COVID-19/blob/master/plots/Deutschland_DGR_2020-05-23_xy_-1_lin_date_incr_confirmed.png)

![Täglicher relativer Zuwachs in Deutschland als Funktion der Infekten pro 100.000 Einwohner](https://github.com/Melykuti/COVID-19/blob/master/plots/Deutschland_DGR_2020-05-23_xy_-1_lin_cases_incr_confirmed.png)

![Tägliche Wachstumsrate in Deutschland als Funktion der Infekten pro 100.000 Einwohner](https://github.com/Melykuti/COVID-19/blob/master/plots/Deutschland_DGR_2020-05-23_xy_-1_lin_cases_rate_confirmed.png)

#### Die einzelnen Bundesländer

![Baden-Württemberg](https://github.com/Melykuti/COVID-19/blob/master/plots/Baden-Württemberg_2020-05-23.png)

![Bayern](https://github.com/Melykuti/COVID-19/blob/master/plots/Bayern_2020-05-23.png)

![Berlin](https://github.com/Melykuti/COVID-19/blob/master/plots/Berlin_2020-05-23.png)

![Brandenburg](https://github.com/Melykuti/COVID-19/blob/master/plots/Brandenburg_2020-05-23.png)

![Bremen](https://github.com/Melykuti/COVID-19/blob/master/plots/Bremen_2020-05-23.png)

![Hamburg](https://github.com/Melykuti/COVID-19/blob/master/plots/Hamburg_2020-05-23.png)

![Hessen](https://github.com/Melykuti/COVID-19/blob/master/plots/Hessen_2020-05-23.png)

![Mecklenburg-Vorpommern](https://github.com/Melykuti/COVID-19/blob/master/plots/Mecklenburg-Vorpommern_2020-05-23.png)

![Niedersachsen](https://github.com/Melykuti/COVID-19/blob/master/plots/Niedersachsen_2020-05-23.png)

![Nordrhein-Westfalen](https://github.com/Melykuti/COVID-19/blob/master/plots/Nordrhein-Westfalen_2020-05-23.png)

![Rheinland-Pfalz](https://github.com/Melykuti/COVID-19/blob/master/plots/Rheinland-Pfalz_2020-05-23.png)

![Saarland](https://github.com/Melykuti/COVID-19/blob/master/plots/Saarland_2020-05-23.png)

![Sachsen](https://github.com/Melykuti/COVID-19/blob/master/plots/Sachsen_2020-05-23.png)

![Sachsen-Anhalt](https://github.com/Melykuti/COVID-19/blob/master/plots/Sachsen-Anhalt_2020-05-23.png)

![Schleswig-Holstein](https://github.com/Melykuti/COVID-19/blob/master/plots/Schleswig-Holstein_2020-05-23.png)

![Thüringen](https://github.com/Melykuti/COVID-19/blob/master/plots/Thüringen_2020-05-23.png)


### Resultate

Diese Resultate sind die direkte numerische Folge der linearen Anpassungen im vorherigen Abschnitt.

**Ich mache eine grobe Schätzung, wie hoch die wahre kumulierte Fallzahl zur Zeit sein kann.** Meine Annahme ist es, dass die gemeldeten Zahlen nur diejenigen zeigen, die schon getestet worden sind. Aber die Inkubationszeit der COVID-19 Krankheit beträgt im Schnitt fünf Tage (von 1 Tag bis 14 Tage), deshalb werden sich die heute infizierten erst in ungefähr fünf Tagen melden und testen lassen, sogar später. Aber sie sind bereits unumkehrbar infiziert.

Die Spalten haben die folgende Bedeutung:

* (Ab 15.04.2020) Die Gesamtanzahl der Infekten wächst täglich um diese Zahl. Sie wird aus der Annäherung errechnet und nicht direkt aus dem Zuwachs zwischen den letzten beiden Tagen.

* (Ab 15.04.2020) Die Gesamtanzahl der Infekten pro 100.000 Einwohner wächst täglich um diese Zahl. Sie wird aus der Annäherung errechnet und nicht direkt aus dem Zuwachs zwischen den letzten beiden Tagen.

* Die Gesamtanzahl der Infekten wächst täglich um diesen Faktor (prozentual ausgedrückt)

* Die Zeitdauer bis die Anzahl der Infekten sich verdoppelt. Seit 03.05.2020 wird sie anders berechnet: das Wachstum kann so langsam sein, dass laut Extrapolation es nicht mehr zu einer Verdoppelung kommen wird. In diesem Fall melde ich `inf` (unendlich).

* Die letzte gemeldete Anzahl der Fälle.

* (Ab 30.03.2020) Die letzte gemeldete Anzahl der Coronavirus-Fälle pro 100.000 Einwohner.

* Meine Schätzung der derzeitigen Fallzahl (ab 30.03.2020 auf 100.000 Einwohner). Konkret, die Extrapolation der angepassten Kurve auf 4, beziehungsweise, 6 Tage voraus. (Bis 16.03.2020, wenn R^2 kleiner als 0,945 oder die letzte Spalte größer als 0,5 ist, dann lasse ich diese Schätzung wegfallen, denn mein Vertrauen in ihr ist schwächer. Ab 18.03.2020 zeige ich die Schätzung wenn R^2 nicht kleiner als 0,95 und die `Diff.` Spalte nicht größer als 0,5 ist, oder wenn die `Diff.` Spalte in [-0,2;&nbsp; 0,1] ist. Ab 03.05.2020 zeige ich die Schätzung wenn R^2 nicht kleiner als 0,75 und die vorvorletzte Spalte nicht größer als 0,5 ist, oder wenn die vorvorletzte Spalte in [-0,3;&nbsp; 0,3] ist.)

* R^2 oder Bestimmtheitsmaß oder Determinationskoeffizient der Anpassungsgüte der linearen Regression. Je näher es an 1 ist, desto besser ist die Anpassung.

* Normalisierte Differenz zwischen Zuwachs im ausgewählten Zeitfenster aus der Annäherung und in den Daten. (Bis 27.04.2020 war es die Differenz der linearen Annäherung und der wahren Beobachtung in logarithmischem Raum für den letzten Datenpunkt (für den letzten Tag). Man konnte es als Exponent einer Potenz auf Basis 2 interpretieren für die Quote zwischen Schätzung und der letzten Beobachtung. Wenn diese Nummer groß ist, dann ist die Annäherung wenig gut. Wenn sie sogar negativ ist, dann ist die Annäherung viel zu niedrig und die Anzahl der Fälle wird unterschätzt.)

* (Ab 18.03.2020) Die Anzahl der Tage im Zeitfenster, in dem die lineare Regression stattfindet. Sie wird automatisch optimiert, so dass der Vektor (10 * (1-R^2), normalisierte Differenz) in l_2 kleinstmöglich ist.)

* (Ab 12 April 2020) e wenn das exponentielle Modell, l wenn das lineare Modell die bessere Annäherung gab und die Zahlen in der dazugehörenden Reihe der Tabelle lieferte. Man darf dem Vorzug des exponentiellen Modells vor dem linearen nicht allzu viel Bedeutung beimessen wenn beides im Zeitfenster sehr genau ist.

&nbsp;

    Bundesland               Zu- Zuwachs Wachst.- Verdoppl.  Gesamte   pro     Schätzung   R^2  Diff. Fenster Exp/Lin
                           wachs   pro    rate      zeit      Fälle  100.000                          größe
                                 100.000

Stand 23.05.2020

    Baden-Württemberg           46  0,4   0,1%     inf Tage   34345    310     [311, 311] 0,25  0,07  12  l
    Bayern                      93  0,7   0,2%     inf Tage   46132    353     [355, 356] 0,51  0,05  12  l
    Berlin                      38  1,0   3,2%    22,2 Tage    6614    181     [187, 192] 0,47 -0,10   7  e
    Brandenburg                4,5  0,2   0,1%     inf Tage    3213    128     [128, 128] 0,23  0,05  11  l
    Bremen                      11  1,7   0,9%     inf Tage    1296    190     [195, 197] 0,16 -0,16  10  e
    Hamburg                   0,00  0,0   0,0%     inf Tage    5063    275                0,43  0,56   8  l
    Hessen                      68  1,1   1,1%    62,2 Tage    9670    154     [159, 162] 0,11 -0,06  13  l
    Mecklenburg-Vorpommern     1,4  0,1   0,2%     inf Tage     763     47       [48, 48] 0,15  0,18   8  l
    Niedersachsen               91  1,1   1,8%    39,1 Tage   11521    144     [150, 153] 0,58 -0,11   8  l
    Nordrhein-Westfalen        120  0,7   0,3%     inf Tage   37139    207     [210, 211] 0,17 -0,04  12  e
    Rheinland-Pfalz             15  0,4   0,2%     inf Tage    6582    161     [162, 162] 0,14  0,05   9  l
    Saarland                  0,71  0,1   0,0%     inf Tage    2709    273     [274, 274] 0,54  0,18  10  l
    Sachsen                     11  0,3   0,2%     inf Tage    5219    128     [128, 128] 0,32  0,23  10  l
    Sachsen-Anhalt             1,2  0,1   0,1%     inf Tage    1692     77       [77, 77] 0,22  0,05  10  l
    Schleswig-Holstein          20  0,7   2,0%    35,9 Tage    3062    106     [109, 112] 0,79 -0,12   7  l
    Thüringen                   14  0,6   0,5%     inf Tage    2830    132     [134, 135] 0,21 -0,05  11  e
    
    Deutschland                521  0,6   0,3%     inf Tage  177850    214     [216, 217] 0,32  0,03  12  l

Stand 19.05.2020

    Baden-Württemberg           35  0,3   0,1%     inf Tage   34034    307     [308, 308] 0,77  0,02   8  e
    Bayern                      95  0,7   0,2%     inf Tage   45639    349     [351, 351] 0,67  0,06   8  l
    Berlin                      16  0,4   0,2%     inf Tage    6478    178     [179, 179] 0,38 -0,11   7  e
    Brandenburg                2,1  0,1   0,1%     inf Tage    3185    127     [127, 127] 0,34  0,05  14  l
    Bremen                      36  5,2   3,9%    18,2 Tage    1237    181     [206, 222] 0,27 -0,05   9  l
    Hamburg                   0,00  0,0   0,0%     inf Tage    5042    274                0,33  1,80   8  l
    Hessen                      28  0,5   0,3%     inf Tage    9368    150     [151, 151] 0,44 -0,03   7  e
    Mecklenburg-Vorpommern     1,4  0,1   0,2%     inf Tage     752     47       [47, 47] 0,29  0,23   7  l
    Niedersachsen               23  0,3   0,2%     inf Tage   11207    140     [141, 141] 0,28  0,08  13  l
    Nordrhein-Westfalen        123  0,7   0,3%     inf Tage   36485    203     [206, 206] 0,50  0,02  14  l
    Rheinland-Pfalz             32  0,8   1,2%    56,6 Tage    6520    160     [163, 166] 0,16 -0,12   7  l
    Saarland                   1,8  0,2   0,1%     inf Tage    2699    272     [273, 273] 0,13  0,04  14  l
    Sachsen                     11  0,3   0,2%     inf Tage    5133    126     [127, 127] 0,38 -0,21   7  e
    Sachsen-Anhalt             1,1  0,0   0,1%     inf Tage    1679     76       [76, 76] 0,35  0,07  13  l
    Schleswig-Holstein        0,00  0,0   0,0%     inf Tage    3002    104                0,84  0,31   7  l
    Thüringen                   12  0,5   0,4%     inf Tage    2750    128     [130, 130] 0,76  0,01   7  e
    
    Deutschland                431  0,5   0,2%     inf Tage  175210    211     [212, 212] 0,74  0,05   8  l

Stand 15.05.2020

    Baden-Württemberg          152  1,4   0,7%    95,8 Tage   33851    306     [312, 315] 0,03 -0,04  11  l
    Bayern                     151  1,2   0,3%     inf Tage   45143    345     [349, 351] 0,21  0,06   9  l
    Berlin                     7,6  0,2   0,1%     inf Tage    6342    174     [174, 174] 0,46  0,08  10  l
    Brandenburg                7,4  0,3   0,2%     inf Tage    3158    126     [126, 126] 0,23  0,06   9  l
    Bremen                      14  2,1   1,3%     inf Tage    1129    165     [171, 172] 0,26  0,14   9  l
    Hamburg                     39  2,1   1,3%    54,8 Tage    4981    271     [280, 285] 0,03 -0,06  14  l
    Hessen                      35  0,6   0,4%     inf Tage    9204    147     [148, 148] 0,30  0,07   9  l
    Mecklenburg-Vorpommern     1,7  0,1   0,2%     inf Tage     740     46       [46, 46] 0,31 -0,01  10  e
    Niedersachsen               45  0,6   0,4%     inf Tage   11087    139     [141, 141] 0,14  0,08   9  l
    Nordrhein-Westfalen        188  1,0   0,5%     inf Tage   35967    201     [204, 206] 0,25  0,01  10  l
    Rheinland-Pfalz             18  0,4   0,3%     inf Tage    6413    157     [159, 159] 0,04 -0,12  10  e
    Saarland                   6,8  0,7   1,1%    65,7 Tage    2684    271     [275, 277] 0,41 -0,07   7  l
    Sachsen                     49  1,2   5,2%    13,5 Tage    5061    124     [132, 140] 0,39 -0,26   8  e
    Sachsen-Anhalt             4,7  0,2   0,3%     inf Tage    1668     76       [76, 76] 0,17  0,05   9  l
    Schleswig-Holstein         5,9  0,2   0,2%     inf Tage    2998    103     [104, 104] 0,46  0,18   7  l
    Thüringen                   28  1,3   1,5%    45,9 Tage    2681    125     [131, 134] 0,15 -0,02   7  l
    
    Deutschland                730  0,9   0,4%     inf Tage  173152    209     [212, 213] 0,20  0,05   9  l


Stand 11.05.2020

    Baden-Württemberg           55  0,5   0,2%     inf Tage   33190    300     [301, 301] 0,38  0,07  12  l
    Bayern                     138  1,1   0,3%     inf Tage   44368    339     [343, 344] 0,38 -0,03  14  e
    Berlin                      22  0,6   0,3%     inf Tage    6272    172     [174, 175] 0,52 -0,03  13  e
    Brandenburg                7,3  0,3   0,2%     inf Tage    3106    124     [124, 124] 0,37 -0,22   7  e
    Bremen                      29  4,2   6,2%    11,6 Tage    1055    154                0,21 -0,30   9  e
    Hamburg                     14  0,8   0,3%     inf Tage    4780    260     [262, 262] 0,07 -0,09   7  l
    Hessen                      45  0,7   0,5%     inf Tage    9012    144     [146, 147] 0,22  0,10  13  l
    Mecklenburg-Vorpommern     2,6  0,2   0,4%     inf Tage     728     45       [46, 46] 0,42 -0,06   7  e
    Niedersachsen               40  0,5   0,4%     inf Tage   10854    136     [137, 138] 0,23 -0,17   7  e
    Nordrhein-Westfalen        197  1,1   0,6%     inf Tage   35132    196     [200, 202] 0,11  0,02  14  l
    Rheinland-Pfalz             16  0,4   0,2%     inf Tage    6313    155     [156, 156] 0,36  0,05  14  l
    Saarland                   2,2  0,2   0,1%     inf Tage    2665    269     [270, 270] 0,58 -0,04  12  e
    Sachsen                     18  0,5   0,4%     inf Tage    4915    121     [122, 122] 0,25  0,07   7  l
    Sachsen-Anhalt             5,1  0,2   0,3%     inf Tage    1643     74       [75, 76] 0,09 -0,11  12  e
    Schleswig-Holstein          34  1,2   4,0%    17,6 Tage    2957    102     [109, 114] 0,47 -0,14   7  e
    Thüringen                   37  1,7   3,6%    19,4 Tage    2585    121     [129, 135] 0,32 -0,16  10  e
    
    Deutschland                662  0,8   0,4%     inf Tage  169575    204     [207, 208] 0,30 -0,03  13  e

Stand 07.05.2020

    Baden-Württemberg           87  0,8   0,3%     inf Tage   32762    296     [297, 297] 0,55  0,08   8  l
    Bayern                     264  2,0   3,3%    21,3 Tage   43658    334     [345, 354] 0,73 -0,09   5  e
    Berlin                      56  1,5   2,2%    31,7 Tage    6149    169     [177, 182] 0,85 -0,07   4  l
    Brandenburg                 33  1,3   2,8%    25,5 Tage    2999    119     [127, 132] 0,75 -0,17   4  l
    Bremen                      36  5,3   6,4%    11,2 Tage     963    141     [173, 196] 0,61 -0,16   5  l
    Hamburg                     39  2,1  11,7%     6,2 Tage    4704    255     [304, 470] 0,99 -0,29   4  e
    Hessen                      91  1,5   8,5%     8,5 Tage    8736    139     [155, 183] 1,00 -0,19   4  e
    Mecklenburg-Vorpommern     7,0  0,4   8,9%     8,1 Tage     715     44                0,52 -0,31   4  e
    Niedersachsen              106  1,3   6,6%    10,9 Tage   10564    132     [143, 157] 0,99 -0,14   4  e
    Nordrhein-Westfalen        280  1,6   2,2%    31,8 Tage   34249    191     [199, 205] 0,96 -0,11   4  l
    Rheinland-Pfalz             15  0,4   0,2%     inf Tage    6213    152     [153, 153] 0,60  0,08  12  l
    Saarland                    25  2,5  11,3%     6,5 Tage    2655    268     [318, 465] 0,87 -0,30   4  e
    Sachsen                     55  1,4   3,1%    23,1 Tage    4836    119     [127, 133] 0,74 -0,22   4  l
    Sachsen-Anhalt              11  0,5   8,5%     8,5 Tage    1602     73       [79, 93] 0,75 -0,26   4  e
    Schleswig-Holstein          11  0,4   0,4%     inf Tage    2834     98                0,41  0,57   4  l
    Thüringen                   34  1,6   5,9%    12,1 Tage    2452    114     [125, 136] 0,53 -0,17   6  e
    
    Deutschland               1213  1,5   4,6%    15,5 Tage  166091    200     [210, 219] 0,90 -0,09   4  e

Stand 03.05.2020

    Baden-Württemberg          165  1,5   0,5%     inf Tage   32291    292     [296, 297] 0,74  0,03   4  e
    Bayern                     146  1,1   0,3%     inf Tage   42792    327     [330, 331] 0,68  0,09   5  e
    Berlin                      35  1,0   0,6%     inf Tage    5976    164     [166, 167] 0,93  0,18   4  e
    Brandenburg                 10  0,4   0,4%     inf Tage    2905    116     [116, 116] 0,83  0,39   4  l
    Bremen                     6,0  0,9   0,7%     inf Tage     875    128     [128, 128] 0,88  0,19   5  l
    Hamburg                     13  0,7   0,3%     inf Tage    4631    252     [252, 252] 0,61  0,13  11  l
    Hessen                      50  0,8   0,6%     inf Tage    8524    136     [137, 137] 0,74  0,17   5  l
    Mecklenburg-Vorpommern     1,9  0,1   0,3%     inf Tage     698     43                0,53  0,42   5  e
    Niedersachsen               46  0,6   0,4%     inf Tage   10283    129     [130, 130] 0,67  0,08  13  l
    Nordrhein-Westfalen        192  1,1   0,6%     inf Tage   33428    186     [190, 192] 0,55 -0,02  14  e
    Rheinland-Pfalz             30  0,7   0,5%     inf Tage    6133    150     [152, 153] 0,44  0,07   8  l
    Saarland                   7,3  0,7   0,3%     inf Tage    2605    263     [263, 263] 0,99  0,29   4  l
    Sachsen                     60  1,5   2,7%    26,0 Tage    4696    115     [123, 128] 0,36 -0,12   5  l
    Sachsen-Anhalt             4,7  0,2   0,3%     inf Tage    1576     71       [72, 72] 0,98  0,31   4  e
    Schleswig-Holstein          10  0,4   0,4%     inf Tage    2738     95       [96, 96] 0,48  0,06  12  e
    Thüringen                  1,9  0,1   0,1%     inf Tage    2345    109     [109, 109] 0,88  0,44   4  l
    
    Deutschland                808  1,0   0,5%     inf Tage  162496    196     [198, 199] 0,80  0,05   4  e

Stand 27.04.2020

    Baden-Württemberg          329  3,0   1,1%     inf Tage   31043    280     [290, 294] 0,30  0,04  11  l
    Bayern                     209  1,6   0,5%     inf Tage   41070    314     [315, 315] 0,80  0,11   4  l
    Berlin                      41  1,1   0,7%     inf Tage    5638    155     [157, 157] 0,83  0,25   4  e
    Brandenburg                 37  1,5   1,4%     inf Tage    2721    108     [110, 110] 0,83  0,11   4  l
    Bremen                     9,8  1,4   1,3%     inf Tage     754    110     [111, 111] 0,71  0,27   5  l
    Hamburg                     31  1,7   0,7%     inf Tage    4475    243     [245, 245] 0,68  0,15   5  l
    Hessen                      46  0,7   0,6%     inf Tage    7979    127     [128, 128] 0,84  0,24   5  l
    Mecklenburg-Vorpommern     2,1  0,1   0,3%     inf Tage     674     42       [42, 42] 0,15  0,24  10  l
    Niedersachsen               65  0,8   0,7%     inf Tage    9847    123     [124, 124] 0,93  0,13   4  l
    Nordrhein-Westfalen        183  1,0   0,6%     inf Tage   31879    178     [180, 180] 0,88  0,21   4  e
    Rheinland-Pfalz             39  0,9   0,7%     inf Tage    5879    144     [146, 147] 0,52  0,05  13  l
    Saarland                    13  1,3   0,5%     inf Tage    2503    253                0,61  0,40   4  l
    Sachsen                     22  0,5   0,5%     inf Tage    4458    109     [110, 110] 0,73  0,13   5  l
    Sachsen-Anhalt              17  0,8   1,1%     inf Tage    1515     69       [71, 73] 0,11 -0,07  11  e
    Schleswig-Holstein          12  0,4   0,4%     inf Tage    2638     91       [92, 92] 0,69  0,17   6  e
    Thüringen                   22  1,0   1,0%     inf Tage    2120     99     [101, 101] 0,81  0,35   4  e
    
    Deutschland               1146  1,4   0,7%     inf Tage  155193    187     [189, 189] 0,94  0,11   4  l

In den nachfolgenden Tabellen wurden die kumulativen Fallzahlen und nicht die täglichen Zuwächse für die Annäherungen verwendet.


    Bundesland               Zu- Zuwachs Wachst.- Verdoppl.  Gesamte   pro     Schätzung   R^2  Diff. Fenster Exp/Lin
                           wachs   pro    rate      zeit      Fälle  100.000                          größe
                                 100.000

Stand 27.04.2020

    Baden-Württemberg          422  3.8   1.4%    51.1 Tage   31043    280     [296, 304] 1.00  0.00   9  e
    Bayern                     492  3.8   1.2%   166.6 Tage   41070    314     [331, 339] 0.99  0.01  10  l
    Berlin                      68  1.9   1.2%    58.0 Tage    5638    155     [162, 166] 0.98  0.00  10  e
    Brandenburg                 75  3.0   2.8%    25.4 Tage    2721    108     [122, 129] 0.99  0.01  14  e
    Bremen                      17  2.4   2.2%    31.4 Tage     754    110     [121, 126] 0.99  0.00   4  e
    Hamburg                     38  2.1   0.9%    80.6 Tage    4475    243     [251, 256] 0.99 -0.00   4  e
    Hessen                     142  2.3   1.8%   112.3 Tage    7979    127     [138, 143] 0.99  0.02  14  l
    Mecklenburg-Vorpommern     4.0  0.2   0.6%   116.9 Tage     674     42       [43, 43] 0.97  0.00   6  e
    Niedersachsen              144  1.8   1.5%   136.4 Tage    9847    123     [132, 135] 0.99  0.01  11  l
    Nordrhein-Westfalen        533  3.0   1.7%   119.3 Tage   31879    178     [193, 199] 0.98  0.02  14  l
    Rheinland-Pfalz             55  1.3   0.9%   214.7 Tage    5879    144     [149, 152] 0.99  0.00   9  l
    Saarland                    19  1.9   0.8%   265.2 Tage    2503    253     [260, 264] 0.99 -0.00   4  l
    Sachsen                     27  0.7   0.6%   115.5 Tage    4458    109     [112, 113] 1.00 -0.00   4  e
    Sachsen-Anhalt              24  1.1   1.6%   125.9 Tage    1515     69       [73, 75] 0.99  0.00  14  l
    Schleswig-Holstein          32  1.1   1.2%   162.6 Tage    2638     91       [96, 98] 0.98  0.01  13  l
    Thüringen                   48  2.3   2.3%    87.3 Tage    2120     99     [109, 113] 0.99  0.01  14  l
    
    Deutschland               2041  2.5   1.3%   151.6 Tage  155193    187     [198, 203] 1.00  0.01  10  l

Stand 22.04.2020

    Baden-Württemberg          510  4.6   1.8%   112.9 Tage   28898    261     [282, 291] 0.99  0.01  12  l
    Bayern                     477  3.6   1.2%    56.4 Tage   38814    297     [312, 319] 1.00 -0.00   4  e
    Berlin                      82  2.2   1.6%   129.0 Tage    5312    146     [156, 160] 0.99  0.01  13  l
    Brandenburg                 55  2.2   2.3%    85.3 Tage    2389     95     [103, 107] 0.99 -0.01  13  l
    Bremen                      14  2.0   2.2%    89.0 Tage     624     91     [100, 104] 0.98  0.00   6  l
    Hamburg                     60  3.3   1.4%   138.9 Tage    4204    228     [244, 251] 0.98  0.01  12  l [1 Tag früher]
    Hessen                     150  2.4   2.1%    97.4 Tage    7380    118     [128, 133] 0.99  0.01  13  l
    Mecklenburg-Vorpommern     1.7  0.1   0.3%   771.2 Tage     656     41       [41, 41] 0.98  0.00   4  l
    Niedersachsen              172  2.2   1.9%   106.5 Tage    9236    116     [125, 129] 1.00  0.00  12  l
    Nordrhein-Westfalen        593  3.3   2.0%   100.5 Tage   30185    168     [181, 188] 1.00 -0.00  13  l
    Rheinland-Pfalz             94  2.3   1.7%   118.3 Tage    5593    137     [148, 153] 0.99  0.01  12  l
    Saarland                    33  3.3   1.4%   143.2 Tage    2367    239     [254, 261] 0.97  0.01  12  l
    Sachsen                     27  0.7   0.6%   312.3 Tage    4273    105     [108, 109] 0.97  0.00   4  l
    Sachsen-Anhalt              25  1.1   1.8%   112.0 Tage    1395     63       [68, 71] 0.99  0.01  14  l
    Schleswig-Holstein          41  1.4   1.7%   119.0 Tage    2496     86       [93, 95] 0.97  0.01  14  l
    Thüringen                   46  2.1   2.5%    28.2 Tage    1872     87      [96, 101] 0.99 -0.00  14  e
    
    Deutschland               1955  2.4   1.4%    51.6 Tage  145694    175     [185, 190] 1.00 -0.00   4  e

Stand 18.04.2020

    Baden-Württemberg          538  4.9   2.0%    35.0 Tage   27258    246     [265, 276] 0.99 -0.01   8  e
    Bayern                     865  6.6   2.4%    84.3 Tage   36881    282     [308, 322] 1.00  0.00   4  l
    Berlin                     113  3.1   2.3%    88.7 Tage    5066    139     [151, 158] 1.00 -0.00   4  l
    Brandenburg                 69  2.7   3.2%    62.0 Tage    2161     86      [98, 104] 0.98  0.02  14  l
    Bremen                      16  2.3   2.8%    25.3 Tage     567     83       [91, 96] 0.97 -0.02  14  e
    Hamburg                     78  4.3   1.9%    36.3 Tage    4118    224     [241, 250] 0.99 -0.01   5  e
    Hessen                     193  3.1   2.8%    24.8 Tage    6916    110     [123, 130] 0.99 -0.00   5  e
    Mecklenburg-Vorpommern     6.0  0.4   0.9%   212.3 Tage     645     40       [41, 42] 0.97 -0.00   8  l
    Niedersachsen              223  2.8   2.6%    26.9 Tage    8649    108     [120, 126] 1.00 -0.00   4  e
    Nordrhein-Westfalen        644  3.6   2.3%    29.9 Tage   28006    156     [170, 178] 0.99 -0.01   9  e
    Rheinland-Pfalz            114  2.8   2.2%    32.3 Tage    5324    130     [142, 148] 1.00 -0.00   5  e
    Saarland                    46  4.7   2.0%    98.1 Tage    2289    231     [250, 260] 0.99  0.00   5  l
    Sachsen                    105  2.6   2.6%    27.4 Tage    4140    102     [112, 118] 1.00  0.00   6  e
    Sachsen-Anhalt              32  1.4   2.5%    28.6 Tage    1315     60       [65, 69] 1.00 -0.00   4  e
    Schleswig-Holstein          48  1.7   2.0%    98.5 Tage    2387     82       [89, 93] 1.00  0.00   4  l
    Thüringen                   60  2.8   3.5%    20.0 Tage    1717     80       [92, 99] 0.99  0.01   5  e
    
    Deutschland               3417  4.1   2.5%    27.9 Tage  137439    166     [183, 192] 1.00 -0.00   4  e


Stand 17.04.2020

    Baden-Württemberg          500  4.5   1.9%    36.7 Tage   26543    240     [258, 268] 1.00 -0.00   7  e
    Bayern                     851  6.5   2.4%    29.3 Tage   36027    276     [303, 317] 1.00 -0.00   4  e
    Berlin                      84  2.3   1.7%    40.6 Tage    4945    136     [145, 150] 0.98 -0.01   8  e
    Brandenburg                 71  2.8   3.4%    59.0 Tage    2120     84      [97, 102] 0.99  0.01  14  l
    Bremen                      13  1.9   2.4%    82.3 Tage     556     81       [86, 90] 0.96 -0.03  14  l
    Hamburg                     68  3.7   1.7%   117.9 Tage    4005    218     [232, 240] 0.99  0.00   4  l
    Hessen                     175  2.8   2.7%    26.4 Tage    6705    107     [118, 125] 0.99 -0.01   4  e
    Mecklenburg-Vorpommern      11  0.7   1.7%   118.7 Tage     634     39       [43, 44] 0.96  0.03  14  l
    Niedersachsen              178  2.2   2.1%    93.5 Tage    8442    106     [114, 119] 0.99 -0.00   8  l
    Nordrhein-Westfalen        592  3.3   2.2%    31.6 Tage   27030    151     [164, 172] 1.00 -0.00   4  e
    Rheinland-Pfalz            101  2.5   2.0%    35.7 Tage    5211    128     [137, 143] 1.00 -0.00   7  e
    Saarland                    50  5.0   2.2%    31.4 Tage    2254    228     [248, 259] 0.99 -0.00   4  e
    Sachsen                    104  2.6   2.6%    26.9 Tage    4048     99     [110, 116] 0.99 -0.00   5  e
    Sachsen-Anhalt              22  1.0   1.7%   114.4 Tage    1279     58       [62, 64] 0.99 -0.00   8  l
    Schleswig-Holstein          60  2.1   2.6%    77.2 Tage    2348     81       [90, 94] 0.99  0.00   4  l
    Thüringen                   62  2.9   3.7%    18.8 Tage    1682     78       [90, 97] 0.98 -0.01   4  e

    Deutschland               2774  3.3   2.1%    33.4 Tage  133830    161     [175, 182] 1.00 -0.00   7  e


Stand 15.04.2020

    Baden-Württemberg          460  4,2   1,8%   109,6 Tage   25438    230     [247, 255] 1,00  0,00   5  l
    Bayern                     659  5,0   1,9%   103,0 Tage   34294    262     [282, 292] 1,00 -0,00   4  l
    Berlin                      54  1,5   1,2%    60,5 Tage    4722    130     [136, 139] 0,99 -0,00   4  e
    Brandenburg                 32  1,3   1,7%    41,9 Tage    1950     78       [83, 86] 0,99 -0,00   4  e
    Bremen                     6,7  1,0   1,4%    51,4 Tage     500     73       [77, 79] 1,00 -0,00   4  e
    Hamburg                     48  2,6   1,2%   160,6 Tage    3869    210     [220, 226] 0,97 -0,00   5  l
    Hessen                     203  3,2   3,2%    61,7 Tage    6347    101     [116, 123] 0,98  0,02  14  l
    Mecklenburg-Vorpommern      12  0,7   1,9%   105,5 Tage     624     39       [42, 44] 0,97  0,02  12  l
    Niedersachsen              145  1,8   1,8%    38,3 Tage    8019    100     [108, 112] 1,00  0,00   4  e
    Nordrhein-Westfalen        561  3,1   2,2%    91,2 Tage   25835    144     [157, 163] 1,00  0,00   6  l
    Rheinland-Pfalz             94  2,3   1,9%    36,6 Tage    5004    123     [132, 137] 0,99 -0,00   5  e
    Saarland                    31  3,1   1,5%   136,4 Tage    2145    217     [229, 235] 0,99 -0,00   5  l
    Sachsen                     78  1,9   2,1%    34,1 Tage    3819     94     [102, 106] 0,99  0,00   4  e
    Sachsen-Anhalt              34  1,5   2,8%    72,3 Tage    1223     55       [63, 66] 0,99  0,03  14  l
    Schleswig-Holstein          69  2,4   3,1%    64,1 Tage    2245     78       [89, 94] 0,98  0,02  14  l
    Thüringen                   27  1,2   1,8%    40,0 Tage    1550     72       [77, 80] 0,98 -0,01   6  e
    
    Deutschland               2340  2,8   1,9%   108,0 Tage  127584    154     [165, 171] 1,00 -0,00   4  l


&nbsp;

    Bundesland           Wachstums-  Verdoppl.   Gesamte   pro      Schätzung   R^2   Diff. Fenster Exp/Lin
                            rate       zeit       Fälle  100.000                            größe

Stand 12.04.2020

    Baden-Württemberg        3,8%    18,5 Tage    24078    218      [254, 274]  1,00  0,01   8  e
    Bayern                   3,9%    51,5 Tage    32282    247      [287, 307]  1,00  0,01   8  l
    Berlin                   2,6%    75,9 Tage     4567    125      [139, 145]  0,99  0,00   4  l
    Brandenburg              5,2%    38,8 Tage     1857     74        [89, 97]  1,00  0,00   6  l
    Bremen                   2,6%    26,7 Tage      480     70        [78, 82]  0,99  0,00   4  e
    Hamburg                  3,5%    57,1 Tage     3742    203      [233, 247]  0,99  0,00  14  l
    Hessen                   3,8%    52,6 Tage     5859     94      [110, 117]  0,99  0,02  14  l
    Mecklenburg-Vorpommern   2,2%    90,0 Tage      605     38        [41, 43]  0,98  0,01   9  l
    Niedersachsen            3,5%    58,0 Tage     7602     95      [108, 115]  1,00  0,00   4  l
    Nordrhein-Westfalen      3,4%    59,1 Tage    24267    135      [154, 164]  1,00  0,01   9  l
    Rheinland-Pfalz          3,3%    61,1 Tage     4734    116      [132, 139]  1,00  0,01  10  l
    Saarland                 5,2%    38,4 Tage     2058    208      [253, 275]  0,99  0,01  14  l
    Sachsen                  3,6%    55,6 Tage     3600     88      [102, 109]  0,99  0,01   9  l
    Sachsen-Anhalt           3,2%    61,9 Tage     1166     53        [60, 64]  0,99  0,01  12  l
    Schleswig-Holstein       3,8%    53,2 Tage     2118     73        [85, 91]  0,99  0,02  12  l
    Thüringen                4,0%    49,7 Tage     1464     68        [82, 87]  0,99  0,03  14  l
    
    Deutschland              3,6%    55,2 Tage   120479    145      [167, 178]  1,00  0,01   9  l

&nbsp;

Die nachfolgenden Tabellen zeigen Rechnungen ausschließlich mit `Nr. der Fälle - Nr. der Tode`.

    Bundesland           Wachstums-  Verdoppl.   Aktive    pro      Schätzung   R^2   Diff. Fenster Exp/Lin
                            rate       zeit       Fälle  100.000                            größe

Stand 01.04.2020

    Baden-Württemberg        9,0%    22,2 Tage    13213    119      [162, 184]  1,00  0,00   4  l
    Bayern                   8,4%    23,9 Tage    16272    124      [166, 187]  0,99  0,01   9  l
    Berlin                   6,4%    31,3 Tage     2738     75       [95, 104]  0,99  0,01  14  l
    Brandenburg              7,6%    26,4 Tage      877     34        [45, 51]  0,99  0,01  10  l
    Bremen                   5,1%    39,4 Tage      306     44        [54, 59]  0,99  0,02  13  l
    Hamburg                  6,5%    30,8 Tage     2297    124      [157, 174]  0,99  0,01  14  l
    Hessen                   6,4%    31,4 Tage     3424     54        [68, 75]  0,99 -0,00  14  l
    Mecklenburg-Vorpommern   6,4%    31,0 Tage      403     25        [31, 34]  0,98  0,00  10  l
    Niedersachsen            8,2%     8,8 Tage     4340     54        [74, 87]  1,00  0,00   4  e
    Nordrhein-Westfalen      7,8%     9,3 Tage    14217     79      [106, 123]  1,00 -0,01   5  e
    Rheinland-Pfalz          5,8%    34,4 Tage     2876     70        [86, 95]  1,00  0,00   5  l
    Saarland                11,7%     6,3 Tage      821     82      [132, 164]  0,98  0,04   9  e
    Sachsen                  7,6%    26,2 Tage     2017     49        [65, 72]  1,00  0,02  10  l
    Sachsen-Anhalt           6,8%    29,2 Tage      743     33        [41, 46]  0,98 -0,04  12  l
    Schleswig-Holstein       7,5%    26,8 Tage     1236     42        [55, 61]  0,99  0,00  11  l
    Thüringen                7,6%    26,2 Tage      854     39        [52, 58]  1,00  0,00  11  l
    
    Deutschland              8,4%     8,6 Tage    66634     80      [110, 130]  1,00 -0,00   5  e

&nbsp;

In den nachfolgenden Tabellen haben alle Annäherungen ausschließlich das exponentielle Modell benutzt.

    Bundesland     Wachstumsrate Verdoppl.zeit AktiveFälle pro100000 Schätzung  R^2  Diff. Fenstergröße

Stand 01.04.2020

    Baden-Württemberg       11,0%     6,6 Tage    13213    119      [183, 225]  0,99  0,01   4
    Bayern                   8,1%     8,9 Tage    16272    124      [168, 196]  0,99 -0,01   4
    Berlin                   5,1%    13,8 Tage     2738     75       [91, 100]  0,99 -0,01   4
    Brandenburg              7,4%     9,7 Tage      877     34        [46, 53]  0,98 -0,01   5
    Bremen                   4,1%    17,3 Tage      306     44        [52, 56]  0,98 -0,00   5
    Hamburg                  7,2%     9,9 Tage     2297    124      [166, 191]  0,98  0,01   5
    Hessen                  11,6%     6,3 Tage     3424     54       [92, 115]  0,98  0,13  12
    Mecklenburg-Vorpommern   9,6%     7,5 Tage      403     25        [37, 45]  0,98  0,06  13
    Niedersachsen            8,2%     8,8 Tage     4340     54        [74, 87]  1,00  0,00   4
    Nordrhein-Westfalen      7,8%     9,3 Tage    14217     79      [106, 123]  1,00 -0,01   5
    Rheinland-Pfalz          6,4%    11,2 Tage     2876     70       [90, 102]  1,00  0,00   4
    Saarland                11,7%     6,3 Tage      821     82      [132, 164]  0,98  0,04   9
    Sachsen                 10,1%     7,2 Tage     2017     49        [74, 90]  0,98  0,05   7
    Sachsen-Anhalt          10,7%     6,8 Tage      743     33        [50, 61]  0,98  0,00   9
    Schleswig-Holstein       7,4%     9,7 Tage     1236     42        [55, 64]  0,98 -0,02   5
    Thüringen               10,4%     7,0 Tage      854     39        [60, 73]  0,98  0,03   7
    
    Deutschland              8,4%     8,6 Tage    66634     80      [110, 130]  1,00 -0,00   5

Stand 30.03.2020

    Baden-Württemberg       15,8%     4,7 Tage    10824     97      [195, 261]  0,97  0,15  12
    Bayern                  16,9%     4,4 Tage    13862    106      [208, 285]  0,99  0,08   8
    Berlin                  13,3%     5,5 Tage     2453     67      [120, 154]  0,99  0,12  11
    Brandenburg             14,8%     5,0 Tage      759     30        [56, 73]  0,99  0,10  11
    Bremen                   8,0%     9,0 Tage      284     41        [58, 68]  0,99  0,05  10
    Hamburg                 11,9%     6,1 Tage     2048    111      [181, 227]  0,97  0,05   9
    Hessen                  12,6%     5,8 Tage     3078     49       [81, 103]  0,98  0,04  10
    Mecklenburg-Vorpommern  11,2%     6,5 Tage      355     22        [35, 43]  0,99  0,06   8
    Niedersachsen            9,7%     7,5 Tage     3706     46        [67, 81]  0,99  0,01   4
    Nordrhein-Westfalen     12,2%     6,0 Tage    12077     67      [111, 140]  0,99  0,06   8
    Rheinland-Pfalz          9,3%     7,8 Tage     2566     62       [90, 108]  0,99  0,01   5
    Saarland                11,7%     6,3 Tage      699     70      [106, 132]  0,97 -0,05   7
    Sachsen                 11,4%     6,4 Tage     1786     43        [67, 83]  1,00 -0,00   4
    Schleswig-Holstein      16,0%     4,7 Tage     1042     35        [72, 97]  0,99  0,16  11
    Thüringen               17,7%     4,3 Tage      714     33       [73, 101]  0,98  0,19  11
    
    Deutschland             13,3%     5,6 Tage    56843     68      [117, 151]  0,99  0,06   7
    

&nbsp;

    Bundesland      Wachstumsrate Verdoppl.zeit Aktive Fälle  Schätzung    R^2  Diff. Fenstergröße

Stand 29.03.2020

    Bayern                  17,2%     4,4 Tage    12774    [24262, 33313]  1,00  0,01   4
    Berlin                  14,0%     5,3 Tage     2351      [4090, 5311]  0,99  0,04  10
    Brandenburg             14,4%     5,2 Tage      720      [1232, 1611]  0,99  0,00   5
    Bremen                   8,5%     8,5 Tage      273        [383, 451]  0,99  0,02   7
    Hamburg                 17,1%     4,4 Tage     1842      [4093, 5610]  0,98  0,24  14
    Mecklenburg-Vorpommern  11,9%     6,2 Tage      347        [534, 669]  0,99 -0,03   7
    Niedersachsen           15,4%     4,8 Tage     3429      [6371, 8480]  0,99  0,07   8
    Nordrhein-Westfalen     12,9%     5,7 Tage    11302    [18756, 23899]  1,00  0,03   7
    Rheinland-Pfalz          9,9%     7,4 Tage     2384      [3486, 4207]  0,99  0,01   4
    Sachsen                 12,1%     6,1 Tage     1608      [2535, 3184]  1,00 -0,00   4
    Sachsen-Anhalt          15,9%     4,7 Tage      590      [1089, 1464]  0,97  0,03  12
    Schleswig-Holstein      16,8%     4,5 Tage      999      [1953, 2666]  0,99  0,07  10
    Thüringen               18,8%     4,0 Tage      692      [1454, 2051]  0,99  0,08  10
    
    Deutschland             14,3%     5,2 Tage    52158   [91799, 119863]  0,99  0,05   6


Stand 28.03.2020

    Baden-Württemberg       16,1%     4,6 Tage     9680    [17397, 23444]  1,00 -0,01   5
    Bayern                  18,0%     4,2 Tage    11073    [21439, 29872]  1,00 -0,00   6
    Berlin                  15,4%     4,8 Tage     2153      [3892, 5186]  1,00  0,03   6
    Brandenburg             16,9%     4,4 Tage      644      [1206, 1648]  0,99  0,00   6
    Bremen                   8,8%     8,2 Tage      258        [359, 425]  0,99 -0,01   6
    Hamburg                 17,8%     4,2 Tage     1763      [3778, 5246]  0,98  0,15  13
    Hessen                  14,0%     5,3 Tage     2595      [4490, 5840]  0,99  0,03   8
    Mecklenburg-Vorpommern  11,5%     6,4 Tage      308        [465, 579]  0,99 -0,03   6
    Niedersachsen           16,2%     4,6 Tage     3138      [5830, 7867]  0,99  0,03   7
    Nordrhein-Westfalen     13,4%     5,5 Tage    10527    [17158, 22055]  1,00 -0,02   6
    Rheinland-Pfalz         13,6%     5,4 Tage     2201      [3767, 4861]  1,00  0,04   9
    Saarland                12,8%     5,8 Tage      548       [901, 1146]  0,98  0,02   5
    Sachsen                 16,5%     4,5 Tage     1423      [2729, 3703]  0,99  0,06   7
    Sachsen-Anhalt          16,1%     4,7 Tage      456       [952, 1283]  0,96  0,20  11
    Schleswig-Holstein      17,8%     4,2 Tage      911      [1792, 2488]  1,00  0,03   5
    Thüringen               19,3%     3,9 Tage      579      [1279, 1820]  0,99  0,13   9
    
    Deutschland             15,4%     4,8 Tage    48257   [85618, 113948]  1,00  0,00   5


Stand 27.03.2020

    Baden-Württemberg       15,5%     4,8 Tage     8091    [14527, 19374]  0,99  0,01   4
    Bayern                  17,9%     4,2 Tage     9426    [18062, 25126]  1,00 -0,01   5
    Berlin                  16,8%     4,5 Tage     1947      [3610, 4924]  1,00 -0,00   4
    Brandenburg             17,0%     4,4 Tage      536      [1036, 1419]  0,98  0,05   5
    Bremen                   8,6%     8,4 Tage      240        [327, 386]  0,98 -0,03   5
    Hamburg                 18,4%     4,1 Tage     1691      [3387, 4748]  0,98  0,03  12
    Hessen                  14,4%     5,1 Tage     2316      [4040, 5289]  0,99  0,03   7
    Mecklenburg-Vorpommern   9,5%     7,7 Tage      259        [376, 450]  0,99  0,02   4
    Niedersachsen           16,6%     4,5 Tage     2800      [5172, 7035]  0,99 -0,00   6
    Nordrhein-Westfalen     12,9%     5,7 Tage     9163    [14726, 18774]  1,00 -0,02   5
    Rheinland-Pfalz         13,9%     5,3 Tage     1963      [3400, 4414]  1,00  0,04   8
    Saarland                13,7%     5,4 Tage      503       [837, 1081]  0,98 -0,01   4
    Sachsen                 17,2%     4,4 Tage     1298      [2473, 3398]  1,00  0,01   4
    Sachsen-Anhalt          12,3%     6,0 Tage      456        [736, 929]  0,98  0,02   4
    Schleswig-Holstein      19,1%     4,0 Tage      808      [1620, 2297]  1,00 -0,00   4
    Thüringen               18,2%     4,1 Tage      538      [1060, 1481]  1,00  0,02   4
    
    Deutschland             15,5%     4,8 Tage    42035    [74587, 99432]  1,00 -0,00   4


Stand 25.03.2020

    Baden-Württemberg       21,4%     3,6 Tage     6032    [14160, 20865]  0,97  0,11  11
    Bayern                  23,0%     3,3 Tage     6521    [15128, 22905]  0,99  0,02  14
    Berlin                  13,5%     5,5 Tage     1426      [2346, 3020]  0,98 -0,01   6
    Brandenburg             21,2%     3,6 Tage      428       [968, 1423]  0,96  0,07  14
    Bremen                  15,1%     4,9 Tage      200        [377, 499]  0,96  0,11  14
    Hamburg                 19,7%     3,9 Tage     1262      [2693, 3858]  0,99  0,06  10
    Hessen                  13,8%     5,4 Tage     1750      [2967, 3840]  0,98  0,02   5
    Mecklenburg-Vorpommern  19,1%     4,0 Tage      218                    0,94  0,22  14
    Niedersachsen           21,3%     3,6 Tage     2133      [4715, 6941]  0,99  0,03   7
    Nordrhein-Westfalen     18,0%     4,2 Tage     7154    [14111, 19661]  0,98  0,02  13
    Rheinland-Pfalz         14,2%     5,2 Tage     1586      [2668, 3483]  1,00 -0,02   6
    Saarland                22,9%     3,4 Tage      401       [858, 1297]  0,96 -0,09   9
    Sachsen                 24,1%     3,2 Tage      953      [2495, 3842]  0,98  0,14  13
    Sachsen-Anhalt          21,6%     3,5 Tage      374       [843, 1248]  0,97  0,04  14
    Schleswig-Holstein      19,2%     4,0 Tage      574      [1161, 1649]  0,99  0,01  11
    Thüringen               21,0%     3,6 Tage      393       [827, 1210]  0,99 -0,02   6
    
    Deutschland             17,9%     4,2 Tage    31405    [60836, 84523]  1,00  0,01   6

Stand 24.03.2020

    Baden-Württemberg       24,4%     3,2 Tage     5348    [14069, 21761]  0,98  0,14  13
    Bayern                  25,4%     3,1 Tage     5754    [14455, 22723]  0,99  0,02   5
    Berlin                  20,7%     3,7 Tage     1220      [2928, 4268]  0,99  0,18  13
    Brandenburg             22,2%     3,5 Tage      343       [858, 1282]  0,96  0,17  14
    Bremen                  15,4%     4,8 Tage      183        [339, 451]  0,96  0,06  13
    Hamburg                 20,1%     3,8 Tage     1043      [2319, 3344]  0,98  0,10   9
    Hessen                  18,4%     4,1 Tage     1620      [3222, 4519]  0,98  0,02   6
    Mecklenburg-Vorpommern  20,6%     3,7 Tage      199                    0,95  0,21  14
    Niedersachsen           21,9%     3,5 Tage     1764      [4015, 5964]  0,99  0,05   6
    Nordrhein-Westfalen     18,9%     4,0 Tage     6318    [12712, 17983]  0,98  0,01  13
    Rheinland-Pfalz         13,9%     5,3 Tage     1370      [2290, 2972]  1,00 -0,01   5
    Saarland                22,1%     3,5 Tage      337        [660, 984]  0,95 -0,18   8
    Sachsen                 24,7%     3,1 Tage      811      [2117, 3290]  0,98  0,11  12
    Sachsen-Anhalt          21,8%     3,5 Tage      321       [702, 1042]  0,96 -0,01  13
    Schleswig-Holstein      19,2%     3,9 Tage      478       [980, 1393]  0,99  0,02  10
    Thüringen               20,4%     3,7 Tage      327        [664, 963]  0,99 -0,05   5
    
    Deutschland             21,4%     3,6 Tage    27436    [61174, 90222]  0,99  0,04  10

Stand 23.03.2020

    Baden-Württemberg       24,9%     3,1 Tage     3790    [11880, 18535]  0,98  0,37  12
    Bayern                  30,6%     2,6 Tage     4866    [14334, 24459]  0,99  0,02   6
    Berlin                  21,4%     3,6 Tage     1076      [2582, 3806]  0,99  0,14  12
    Brandenburg             22,8%     3,4 Tage      288       [740, 1116]  0,95  0,18  13
    Bremen                  20,5%     3,7 Tage      170        [396, 576]  0,96  0,15   8
    Hamburg                 21,0%     3,6 Tage      943      [2055, 3007]  0,98  0,03   8
    Hessen                  24,8%     3,1 Tage     1344      [3639, 5666]  0,98  0,16  11
    Mecklenburg-Vorpommern  22,0%     3,5 Tage      172        [452, 674]  0,95  0,25  14
    Niedersachsen           23,0%     3,3 Tage     1479      [3508, 5310]  0,99  0,05   5
    Nordrhein-Westfalen     20,4%     3,7 Tage     5587    [11769, 17066]  0,97  0,00  14
    Rheinland-Pfalz         13,5%     5,5 Tage     1175      [1970, 2538]  0,99  0,01   4
    Saarland                19,9%     3,8 Tage      200                    0,93  0,18   7
    Sachsen                 25,2%     3,1 Tage      653      [1777, 2786]  0,98  0,15  11
    Sachsen-Anhalt          21,8%     3,5 Tage      212                    0,95  0,31  12
    Schleswig-Holstein      12,9%     5,7 Tage      382        [628, 801]  0,99  0,02   4
    Thüringen               18,3%     4,1 Tage      249        [496, 696]  0,99  0,02   4
    
    Deutschland             22,1%     3,5 Tage    22586    [52387, 78048]  0,99  0,06  10
    

Stand 20.03.2020

    Baden-Württemberg       25,5%     3,0 Tage     2736     [6703, 10562]  0,98 -0,02   5
    Bayern                  26,5%     3,0 Tage     2389      [5784, 9249]  0,98 -0,08   9
    Berlin                  21,6%     3,5 Tage      731      [1458, 2155]  0,98 -0,13   9
    Brandenburg             38,8%     2,1 Tage      192       [695, 1339]  0,99 -0,03   4
    Bremen                  27,2%     2,9 Tage      121        [295, 477]  0,94 -0,10   4
    Hamburg                 29,1%     2,7 Tage      586      [1676, 2795]  0,98  0,04   8
    Hessen                  34,1%     2,4 Tage      812      [2723, 4898]  0,99  0,05   7
    Mecklenburg-Vorpommern  45,7%     1,8 Tage      131       [598, 1270]  0,97  0,02   4
    Niedersachsen           28,7%     2,7 Tage      803      [2175, 3602]  0,99 -0,02   8
    Nordrhein-Westfalen     21,5%     3,6 Tage     3491     [7782, 11482]  0,99  0,03   8
    Rheinland-Pfalz         24,2%     3,2 Tage      800      [1873, 2890]  0,98 -0,02   5
    Saarland                23,6%     3,3 Tage      146        [316, 483]  0,93 -0,11   4
    Sachsen                 35,0%     2,3 Tage      394      [1302, 2374]  0,97 -0,01   9
    Sachsen-Anhalt          47,5%     1,8 Tage      180       [935, 2036]  0,98  0,13   5
    Schleswig-Holstein      27,7%     2,8 Tage      265       [696, 1135]  1,00 -0,02   4
    Thüringen               41,8%     2,0 Tage      149       [588, 1184]  1,00 -0,03   5
    
    Deutschland             26,8%     2,9 Tage    13926    [35907, 57751]  1,00 -0,00   8
    
Stand 19.03.2020

    Baden-Württemberg       34,6%     2,3 Tage     2149     [7415, 13425]  0,97  0,07   9
    Bayern                  20,7%     3,7 Tage     1684      [3432, 4998]  0,98 -0,06   6
    Berlin                  20,4%     3,7 Tage      573      [1102, 1597]  0,98 -0,13   8
    Brandenburg             27,1%     2,9 Tage      134        [327, 529]  0,94 -0,10   4
    Bremen                  10,9%     6,7 Tage       80        [116, 143]  0,95 -0,05   8
    Hamburg                 18,8%     4,0 Tage      432       [858, 1212]  1,00 -0,00   4
    Hessen                  39,3%     2,1 Tage      682      [2559, 4964]  0,99 -0,00   8
    Mecklenburg-Vorpommern  27,3%     2,9 Tage       98        [212, 344]  0,97 -0,28   9
    Niedersachsen           36,1%     2,2 Tage      669      [2238, 4148]  0,98 -0,04   4
    Nordrhein-Westfalen     22,8%     3,4 Tage     3027     [6869, 10351]  0,99 -0,00   8
    Rheinland-Pfalz         42,5%     2,0 Tage      637      [3075, 6248]  0,97  0,23   8
    Saarland                40,2%     2,1 Tage       99                    0,88  0,29   9
    Sachsen                 35,0%     2,3 Tage      275       [958, 1746]  0,96  0,07   8
    Sachsen-Anhalt          54,5%     1,6 Tage      140       [836, 1998]  0,98  0,07   4
    Schleswig-Holstein      24,8%     3,1 Tage      202        [485, 756]  1,00 -0,01   4
    Thüringen               40,2%     2,1 Tage       98        [386, 760]  1,00  0,03   4
    
    Deutschland             26,8%     2,9 Tage    10979    [28209, 45329]  1,00 -0,01   7
    

Stand 18.03.2020

    Baden-Württemberg       35,3%    2,3 Tage     1609     [5780, 10580]  0,96  0,10  8
    Bayern                  15,8%    4,7 Tage     1243      [2265, 3035]  0,99  0,02  4
    Berlin                  14,0%    5,3 Tage      391        [660, 857]  1,00  0,00  4
    Brandenburg             17,4%    4,3 Tage       92        [170, 234]  0,98 -0,04  4
    Freie Hansestadt Bremen 10,4%    7,0 Tage       69        [101, 123]  0,93 -0,02  7
    Hamburg                 32,1%    2,5 Tage      358      [1189, 2076]  0,98  0,12  6
    Hessen                  35,7%    2,3 Tage      432      [1587, 2924]  0,98  0,11  6
    Mecklenburg-Vorpommern  22,7%    3,4 Tage       56        [126, 190]  0,99 -0,00  7
    Niedersachsen           26,2%    3,0 Tage      478      [1141, 1819]  0,98 -0,09  6
    Nordrhein-Westfalen     22,8%    3,4 Tage     2372      [5604, 8448]  0,99  0,06  7
    Rheinland-Pfalz         45,8%    1,8 Tage      474      [2582, 5487]  0,97  0,27  7
    Saarland                53,1%    1,6 Tage       88                    0,88  0,35  9
    Sachsen                 40,7%    2,0 Tage      198       [924, 1830]  0,95  0,25  8
    Sachsen-Anhalt          39,7%    2,1 Tage      105        [386, 754]  0,87 -0,05  8
    Schleswig-Holstein      25,8%    3,0 Tage      159        [401, 636]  1,00  0,01  4
    Thüringen               32,8%    2,4 Tage       74        [227, 401]  0,96 -0,02  8
    
    Deutschland             27,4%    2,9 Tage     8198    [22821, 37052]  1,00  0,08  9


Stand 16.03.2020

    Baden-Württemberg      28,5%    2,77 Tage     1102      [2839, 4686]  0,97 -0,08
    Bayern                 25,1%    3,09 Tage     1062      [2725, 4267]  0,99  0,07
    Berlin                 22,0%    3,49 Tage      300       [692, 1030]  0,99  0,06
    Brandenburg            34,1%    2,37 Tage       94        [334, 601]  0,97  0,14
    Bremen                 37,3%    2,19 Tage       56                    0,91  0,38
    Hamburg                41,3%    2,00 Tage      260      [1058, 2113]  0,97  0,03
    Hessen                 41,6%    1,99 Tage      342      [1445, 2895]  0,97  0,07
    Mecklenburg-Vorpommern 29,3%    2,70 Tage       51        [174, 292]  0,99  0,30
    Niedersachsen          38,4%    2,13 Tage      391      [1547, 2964]  0,96  0,11
    Nordrhein-Westfalen    22,6%    3,40 Tage     1536      [3856, 5798]  0,96  0,15
    Rheinland-Pfalz        60,3%    1,47 Tage      325      [2100, 5396]  0,96 -0,03
    Saarland               43,3%    1,93 Tage       85        [310, 636]  0,95 -0,21
    Sachsen                40,4%    2,04 Tage      140       [668, 1317]  0,95  0,30
    Sachsen-Anhalt         32,7%    2,45 Tage       77                    0,90 -0,02
    Schleswig-Holstein     48,7%    1,75 Tage      123       [694, 1534]  0,96  0,21
    Thüringen              49,0%    1,74 Tage       55        [329, 730]  0,95  0,28
    
    Deutschland            28,2%    2,79 Tage     5999    [16760, 27532]  0,98  0,05


Stand 15.03.2020

    Baden-Württemberg      23,5%    3,28 Tage      824      [1732, 2644]  0,96 -0,15
    Bayern                 25,6%    3,04 Tage      882      [2253, 3554]  0,99  0,04
    Berlin                 34,3%    2,35 Tage      265       [928, 1674]  0,97  0,11
    Brandenburg            37,9%    2,16 Tage       84        [301, 574]  1,00 -0,01
    Bremen                 40,8%    2,02 Tage       53                    0,84  0,20
    Hamburg                41,5%    2,00 Tage      162       [759, 1521]  0,96  0,23
    Hessen                 42,0%    1,98 Tage      286      [1056, 2130]  0,96 -0,14
    Mecklenburg-Vorpommern 30,5%    2,61 Tage       50        [150, 256]  0,99  0,05
    Niedersachsen          39,0%    2,11 Tage      287      [1168, 2256]  0,95  0,13
    Nordrhein-Westfalen    23,0%    3,34 Tage     1402      [3285, 4974]  0,95  0,03
    Rheinland-Pfalz        41,4%    2,00 Tage      168       [649, 1299]  0,96 -0,05
    Saarland               42,0%    1,98 Tage       32                    0,95  0,60
    Sachsen                49,1%    1,73 Tage      130       [719, 1599]  0,98  0,16
    Sachsen-Anhalt         46,1%    1,83 Tage       47                    0,87  0,46
    Schleswig-Holstein     51,8%    1,66 Tage      103       [549, 1266]  0,95  0,01
    Thüringen              55,4%    1,57 Tage       51        [312, 754]  0,95  0,07
    
    Deutschland            28,4%    2,78 Tage     4826    [13312, 21938]  0,98  0,02




### Konklusion

Unsere Intuition kann mit nichtlinearen Effekten schwer umgehen. Exponentielles Wachstum ist solch ein Beispiel. **Das Risiko, dass man sich mit der Krankheit auf der Straße ansteckt, wuchs ursprünglich um den Faktor 25-50% täglich.** Es war zu erwarten, dass man über die Erkrankung zunächst nur aus den Nachrichten hören wird, dann plötzlich wird sie überall im Bekanntenkreis auftauchen, wenn die Eindämmung nicht erfolgt.

Wenn man die Ansteckung vermeiden will, dann war es besser eine Besorgung noch heute und nicht morgen zu machen, und es war besser morgen Vormittag als morgen Nachmittag das Zuhause zu verlassen. (Angenommen, dass genau so viele Leute sich auf den Straßen und in den Supermärkten befinden werden. Wenn deren Anzahl zurückgeht, dann sinkt die Kontaktwahrscheinlichkeit auch.)

Neben der Nichtlinearität ist die durch die Inkubationszeit ausgelöste Zeitverzögerung ein zweiter überraschender Aspekt der Pandemie. **Die Anzahl der heute ansteckenden Erkrankten ist so viel, wie die aktive Fallanzahl erst in ungefähr fünf Tagen (die durchschnittliche Inkubationszeit) gemeldet werden wird. Das Problem ist deshalb viel größer während der Ausbreitungsphase, als die aktuellen Fallzahlen es zeigen.**

Für das medizinische Personal war es zu erwarten, dass die Anzahl der neuen Patienten auch exponentiell mit der gleichen Rate wachsen wird. Wenn ein Tag schwierig war, dann wird der nächste z.B. 5-12% schwieriger, und der übernächste noch 5-12% schwieriger werden.

### Bitte um Spenden

Wenn Sie meine Arbeit unterstützen können, dann bitte ich Sie, mein [Ocean Plastic Detector](https://www.gofundme.com/OceanPlasticDetector) Projekt aufzusuchen und dort eine Spende durchzuführen. Danke!

Finden Sie mich auf [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), auf meiner Webseite/Blog: [Melykuti.me](https://melykuti.me), oder folgen Sie mir auf [Facebook](https://www.facebook.com/bence.melykuti) für meine öffentlichen Posts.

Ich arbeite als selbständiger Data Scientist. Sie können mich mit Ihrem Projekt beauftragen.

### Archiv

Zusammenfassung am Dienstag, 19 Mai 2020:

* Bremen ist das einzige Bundesland, wo die Anzahl der COVID-19 Neuinfektionen steigt. Ich finde es besonders schade, denn Bremen war am Anfang der Coronavirus-Pandemie, bis Anfang April, ziemlich verschont. Heute ist Bremen im Mittelfeld gemessen an bestätigten Fällen pro 100.000 Einwohner. Rein numerisch gesehen ist Bremen mit 5,2 Neuinfektionen pro Tag pro 100.000 noch unter der vom Bund und Ländern gesetzten Grenze von 50 pro Woche, aber ich weiß nicht, wo die neuen Infektionen herkommen.
* In allen anderen Ländern ist die Lage entspannt. In Baden-Württemberg ist es fast so ruhig geworden, wie in den östlichen ländlichen Bundesländern.

Zusammenfassung am Freitag, 15 Mai 2020:

* Die Anzahl der Neuinfektionen hat sich auf einem Niveau stabilisiert wo sie Anfang Mai war. Der Trend ist nicht, dass die COVID-19 aus Deutschland verschwinden würde. Eher würde ich die Lage so interpretieren, dass die Lockerungen der Schutzmaßnahmen keine Verschlechterung der Pandemie verursachten.
* Bremen und Hamburg zeigen den höchsten Zuwachs mit circa 2,1 neuen Coronavirus-Fällen pro 100.000 EinwohnerInnen pro Tag, oder ungefähr 15 pro Woche.

Zusammenfassung am Montag, 11 Mai 2020:

* Nach einem Wochenende sind die gemeldeten Fallzahlen der Neuinfektionen immer niedriger, wie es auch heute der Fall ist. Aber die heutigen Zahlen sind in den meisten Bundesländern niedriger als die von vor einer Woche, das unbedingt eine positive Entwicklung ist.
* Es gibt leider Ausnahmen: in Bremen, in Schleswig-Holstein und in Thüringen gibt es über die letzten Tagen mehr neue Infekte als vor einer Woche. Die aus Baden-Württemberg übermittelten Daten sind unzuverlässig, und das Robert-Koch-Institut ermittelt, warum sie sogar gesunken sind.
* 50 Neuinfektionen über eine Woche pro 100.000 Einwohner wurde als Grenze für Landkreise gesetzt, über die etliche Lockerungen müssen zurückgenommen werden. Ich melde diese Zahl nicht, jedoch gebe ich eine Schätzung für Neuinfektionen an einem Tag laut des angepassten Trends. Diese Zahl muss dann ungefähr unter 7 bleiben. Deutschlandweit ist sie nun 0,8, jedoch große Schwankungen sind für einzelne Landkreise zu erwarten.

Zusammenfassung am Donnerstag, 7 Mai 2020:

* Ein Anstieg der Infektionszahlen ist in der großen Mehrheit der Bundesländer zu beobachten, jedoch ist es unklar, ob er auf eine Verschlechterung der Situation hindeutet oder nur ein Nachholeffekt nach dem langen Wochenende 1-3 Mai ist. Z.B. in Berlin, Bremen und Thüringen gibt es eine wöchentliche Periodizität in der Zeitreihe, womit die jetztige Zunahme in Übereinstimmung ist.
* Ich rate zur Vorsicht. Lockerungen bedeuten nicht, dass man man sie umfangreich ausnutzen muss. Das neuartige Coronavirus kursiert immer noch in der Bevölkerung. Um die Gesundheit zu bewahren, muss man sich zunächst nicht alles gönnen was erlaubt ist.

Zusammenfassung am Sonntag, 3 Mai 2020:

* Wie man es von den Nachrichten auch spürt, ist die Lage ruhig in Deutschland.
* Die tägliche Anzahl der neuen bestätigten Infektionen ist unter 2 pro 100.000 EinwohnerInnen in jedem Bundesland. Die Anzahl der neuen Infekten pro Tag und Bevölkerung ist in Sachsen, in Baden-Württemberg (1,5), in Bayern, in Nordrhein-Westfalen (1,1) und in Berlin (1,0) am größten.
* Sachsen und Bremen zeigen gerade eine leichte Erhöhung der täglichen neuen Infekten.

Zusammenfassung am Montag, 27 April 2020:

* Wie man es von den Nachrichten auch spürt, ist die Lage ruhig in Deutschland.
* Die tägliche Anzahl der neuen bestätigten Infektionen ist unter 4 pro 100.000 EinwohnerInnen in jedem Bundesland. Die Anzahl der neuen Infekten pro Tag und Bevölkerung ist in Bayern, in Baden-Württemberg und in Nordrhein-Westfalen am größten.
* Mit der Ausnahme von Brandenburg und Thüringen ist die Anzahl der täglichen neuen Infekten pro 100.000 jetzt niedriger als am 23.03.2020, der Anfang der Kontaktbeschränkungen.

Zusammenfassung am Mittwoch, 22 April 2020:

* Aufgrund technischer Probleme wurden am 21.04.2020 am Robert Koch Institut keine Daten aus Hamburg empfangen.
* Die neuen Infektionszahlen gehen schön zurück. Bayern kann sich über eine deutlichere Senkung der täglichen neuen Fälle freuen. Damit ist die Anzahl der neuen Infekten pro Tag und Bevölkerung in Baden-Württemberg am größten.

Zusammenfassung am Freitag, 17 April 2020:

* In Bremen gab es einen Ausbruch in einem Flüchtlingsheim, wohin eine Person nach zweiwöchiger Isolation zurückkehrte, und offenbar immer noch ansteckend war.
* Ich beobachte eine kleine aber merkbare Beschleunigung im Zuwachs der Fallzahlen in fast jedem Bundesland. Was heute beobachtet wird sind Infektionen von vor einer Woche oder häufig mehr. Es könnte auf eine nachlassende Vorsichtigkeit der Bevölkerung hindeuten. Aber es könnte dadurch zu erklären sein, dass weniger Tests zu Ostern durchgeführt wurden, oder die Labors die Arbeit erst später in der Woche nachholen.

Zusammenfassung am Mittwoch, 1 April 2020:

* Die starken Beschränkungen des Alltagslebens zeigen ihre positive Wirkung. Die tägliche Wachstumsrate der Fallzahlen ist in jedem Bundesland auf 5-12% gesunken.
* Baden-Württemberg, Bayern, Hamburg sind die traurigen Vorreiter in Fallzahlen pro 100.000 Einwohner.
* In Bremen ist sowohl die Fallzahl als auch die Wachstumsrate im Vergleich mit Hamburg niedrig. Ich weiß es jedoch nicht, was sie anders machen.
* Berlin, Bremen, Rheinland-Pfalz haben ihre Verdopplungszeiten über 10 Tage gedrückt. Brandenburg, Hamburg, Nordrhein-Westfalen, Schleswig-Holstein sind fast da.

Zusammenfassung am Montag, 30 März 2020:

* Am 29.3.2020 wurden keine Daten aus Sachsen-Anhalt übermittelt. Ich aktualisiere dessen Grafik und Resultate nicht.
* Wie vor einer Woche sind die heute gemeldeten Daten und eventuelle Rückgänge der Wachstumsraten wegen des Wochenendes nicht besonder vertrauenswürdig (siehe Zusammenfassung am 23 März 2020).
* Es gibt Stimmen in der Politik, dass man mit der allmählichen Lockerung der Beschränkungen erst dann anfangen kann, wann die Verdopplungszeit 10 Tage erreicht. Dies entspricht eine tägliche Wachstumsrate von 7,2%.

Zusammenfassung am Sonntag, 29 März 2020:

* Am 28.3.2020 wurden keine Daten aus Baden-Württemberg, Hessen und dem Saarland an das Robert Koch Institut übermittelt. Ich aktualisiere deren Grafiken und Resultate nicht.
* Die Wachstumsraten zeigen zwar überall eine sinkende Tendenz, aber es war auch Samstag und die Vollständigkeit der Datenübergabe, wie vor einer Woche, auch heute suspekt ist.

Zusammenfassung am Samstag, 28 März 2020:

* Es überrascht mich, dass es **gar keine Verbesserung im Vergleich mit gestern** gibt: die täglichen Wachstumsraten sind nicht kleiner geworden.
* Sachsen-Anhalt hat seine Fallzahlen nicht aktualisiert. Es geht nicht um eine Pause in der Pandemie.

Zusammenfassung am Freitag, 27 März 2020:

* Wie Bundeskanzlerin Angela Merkel es [gestern erwähnt hat](https://www.faz.net/aktuell/politik/inland/angela-merkel-zu-shutdown-muss-deutsche-um-geduld-bitten-16698796.html), steht die Verdopplungszeit der Fallzahlen bei vier bis fünf Tagen. Sie hält die Ausgangsbeschränkungen nötig, bis diese Zeitspanne noch wesentlich länger gestreckt wird.
* Ich sehe auch positive Entwicklungen: die tägliche Wachstumrate der Fallzahlen sank auf 10-20%.
* In Freiburg ist heute der 7. Tag der Ausgangsbeschränkung. Mit einer Inkubationszeit von 5-7 Tagen im Schnitt (manchmal bis zu 14 Tagen), und mit weiteren 2-3 Tagen bis ein Kranker sich testen lässt und ein positives Resultat bei dem Robert Koch Institut eintrifft, ist es zu erwarten, dass die positive Wirkung der Ausgangssperren in den kommenden Tagen die Wachstumsraten weiter verringern.
* Ich würde Hamburg hervorheben, wo die Situation relativ schlechter ist. Die tägliche Wachstumsrate liegt jetzt bei 18%, aber mit einem kürzeren Zeitfenster von 5-6 Tagen bekomme ich 13-15%, die dem bundesweiten Durchschnitt entspricht. Die Fallzahl pro 100.000 Einwohner ist in Hamburg am größten.
* Laut der Grafik (besonders laut des rechten Schaubildes) ist Bremen in der schwieriger Situation, dass die Verbreitung der Pandemie über den letzten 6 Tagen sich noch weiter beschleunigt hat. Meine numerischen Schätzungen sind deswegen zu optimistisch.

Zusammenfassung am Mittwoch, 25 März 2020:

* In Baden-Württemberg, Bayern, Bremen, Mecklenburg-Vorpommern, Sachsen gibt es positive Zeichen, dass die Ausbreitung der Coronavirus-Pandemie sich einigermaßen verlangsamt.
* In Berlin, Brandenburg, Hamburg, Hessen, Niedersachsen, Nordrhein-Westfalen, Rheinland-Pfalz, Schleswig-Holstein, Thüringen gibt es leider kaum Veränderung der Anstiegsrate der Fallzahl. (Die Wachstumsraten hier sind jedoch im Schnitt sowieso niedriger.)
* Die Ausgangssperren und öffentliche Aufklärungsarbeit werden bald ihre positive Wirkung zeigen.

Zusammenfassung am Dienstag, 24 März 2020:

* Die Daten vom Wochenende sind angekommen. **Die Lage ist ernst, wie ich dies gestern vorhersah. Diejenigen, die heute positiv gemeldet sind, können möglicherweise Beatmung in ein paar Tagen brauchen. Die Nachfrage nach Intensivpflege steigt mit einer gewissen Verzögerung.**
* In vielen Bundesländern ist die tatsächliche Fallzahl ein bisschen niedgriger, als was meine beste exponentielle Annäherung vorhersagt. Siehe die Grafiken. Dies bedeutet, das die Ausbreitung immer noch exponentiell voranstreitet, aber ihre Rate sinkt ein wenig.
* Um den Effekt der Ausgangssperren zu sehen muss man ein paar Tage noch warten, da die Inkubationszeit der Coronavirus-Infektion ca. 5-7 Tage ist, und für Testen und Datenübergabe würde ich mindestens 1-2 Tage einrechnen.

Zusammenfassung am Montag, 23 März 2020:

*  Das Wochenende brachte eine eintägige Verzögerung im Berichten der Fallzahl in Nordrhein-Westfalen. (Die Zahl am 22.03.2020 war viel zu niedrig.) Mit dem letzten Datenpunkt ist keine Verbesserung in der Zeitreihe zu sehen.
* In Baden-Württemberg ist die heutige Zahl sehr suspekt. Im Fall BW rufe ich zu Geduld auf; ich denke nicht, dass die Lage sich so schnell entspannt hätte, wie dies zur Zeit aussieht. Warum sollte die Situation hier besser sein als in Bayern, wo die Wachstumsrate nicht nachlässt.
* In Mecklenburg-Vorpommern oder Sachsen-Anhalt sind große Schwankungen wegen der relativ geringen Fallzahl zu erwarten. Ich gebe auch hier keine Entwarnung wegen des Effekts des Wochenendes.
* In Baden-Württemberg, Berlin, Brandenburg, Bremen, Hamburg, Hessen, Mecklenburg-Vorpommern, Saarland, Sachsen, Sachsen-Anhalt war es schon vor sieben Tagen, am 16.03., eine nur vorübergehende Verlangsamung der Fallzahlen zu beobachten. Ich vermute, dass nur eine Verspätung der Datenübertragung am Wochenende deren zugrunde liegt.
* **Überall, wo die heutigen Daten auf eine Verlangsamung hinweisen, gab es vor einer Woche, nach dem Wochenende, schon eine ähnliche Verlangsamung, ohne langfristigen Effekt an der Ausbreitung der Coronavirus-Pandemie.**
* [Diese Vermutung bestätigt heute das Robert Koch Institut:](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html) „Am aktuellen Wochenende wurden nicht aus allen Ämtern Daten übermittelt, sodass der hier berichtete Anstieg der Fallzahlen nicht dem tatsächlichen Anstieg der Fallzahlen entspricht. Die Daten werden am Montag nachübermittelt und ab Dienstag auch in dieser Statistik verfügbar sein.“
