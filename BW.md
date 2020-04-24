## Analyse der Verbreitung der SARS-CoV-2 Coronavirus-Pandemie in Baden-Württemberg und in den einzelnen Landkreisen

> * Auf dieser Seite untersuche ich die gesamte oder kumulierte Anzahl der Coronavirus-Fälle und nicht die Anzahl der zur Zeit infizierten.

15 April 2020 (aktualisiert am 23 April 2020), Freiburg i. Br. -- In dieser Analyse versuche ich es in begreifbarer Form zu beantworten, wie schnell die COVID-19-Pandemie sich zur Zeit ausbreitet.

### Analyse

Meine Methodologie habe ich [auf Englisch im Detail beschrieben.](https://github.com/Melykuti/COVID-19/blob/master/global.md) Eine Übersicht auf Deutsch gibt es samt Datenanalyse [für Deutschland und für die Bundesländer](https://github.com/Melykuti/COVID-19/blob/master/Deutschland.md).

Ich nehme den Logarithmus auf Basis 2 der Anzahl der Fälle. Wenn diese Zahl tatsächlich exponentiell wächst, ist daran erkennbar, dass der Logarithmus nicht unter einer geraden Linie mit einer positiven Steigung fällt. Mit linearer Regression bestimme ich eine annährende Linie, und von deren Steigung kann ich vieles ausrechnen. Ich kann sagen, mit welchem Faktor die Anzahl von einem Tag bis zum nächsten wächst. Eng verbunden damit ist die Verdopplungszeit: wie lange es dauert, bis die Anzahl der Infekten sich verdoppelt.

Ich verwende jedoch lineare Regression nicht nur auf den Logarithmus (was ich exponentielle Annäherung nenne mit Bezug auf exponentielles Wachstum) sondern auf die ursprünglichen Zahlen auch (was ich lineare Annäherung nenne, da sie einem linearen Wachstum entspricht).

Ich wähle immer die letzten 4-14 Tage aus, um die lineare Regression durchzuführen. Mit der Wahl der Länge des Zeitintervals versuche ich die beste Anpassung zu erreichen, gemessen an R^2 und an der Differenz zwischen dem letzten Tag in der geraden Strecke und dem letzten Datenpunkt. Diese Optimierung ist automatisiert.

Nachdem die optimale Fenstergröße für sowohl das exponentielle als auch das lineare Modell ausgewählt wurde, vergleiche ich die beiden. Von den beiden Modellen wähle ich das bessere aus.

Auch wenn die tägliche Differenz schon ziemlich stabil ist und das Wachstum sichtbar nur linear ist, kann es immer wieder vereinzelt vorkommen, wenn beide Modelle im Zeitfenster sehr gut sind, dass die Optimierung die exponentielle Annäherung genauer findet als die lineare Annäherung. _Man darf dem Vorzug des exponentiellen Modells vor dem linearen nicht allzu viel Bedeutung beimessen._

Man kann die beiden Arten der linearen Regression einfach als _Glättung der Zeitreihen_ sehen. So rechne ich den täglichen Zuwachs von der Annäherung aus und nicht von dem letzten beiden Datenpunkten, was sehr empfindlich auf zufällige Effekte reagieren würde.

### Hinweis zur Interpretation

**Ich würde gerne schätzen können, wie hoch die Wahrscheinlichkeit ist, dass ich mit einem Infizierten in Kontakt komme, wenn ich meine Wohnung verlasse.** Diese Wahrscheinlichkeit wächst ungefähr proportional zur Gesamtanzahl der derzeit Infizierten (sie sind ansteckend). Seit Kontaktsperren in Kraft sind ist es nicht mehr ganz so, da die Straßen und Geschäfte viel leerer sind als am Anfang März.

Die Anzahl der Ansteckenden ist die kumulierte Anzahl der Fälle minus Anzahl der Genesenen minus Anzahl der Tode. Doch die Anzahl der Genesenen wird leider nicht veröffentlicht oder offiziell geschätzt. (Das Robert Koch Institut hat Ende März angefangen, diese Zahlen für die gesamte Bundesrepublik zu schätzen.)

Man könnte sie eigentlich einfach grob annähern, wenn man annimmt, dass jeder Patient in z.&nbsp;B. 21&nbsp;Tagen entweder sich erholt oder stirbt. Dann würde man von der heutigen kumulierten Fallzahl die kumulierte Fallzahl vor 21&nbsp;Tagen subtrahieren um die aktiven Fällen zu bekommen.

Eine alternative Betrachtung ist es zu argumentieren, dass **man es vermeiden will, in den täglichen Zuwachs zu geraten**. Am informativsten dafür ist der tägliche Zuwachs pro 100.000 EinwohnerInnen. Da die Inkubationszeit der Coronavirus-Infektion im Schnitt fünf Tage beträgt, und da es noch weiter Tage braucht getestet zu werden und die Daten zu melden, entspricht der heutige Zuwachs Infektionen von vor mindestens einer Woche oder mehr.

### Datenquelle

Die Daten werden täglich durch das [Ministerium für Soziales und Integration Baden-Württemberg](https://sozialministerium.baden-wuerttemberg.de/de/gesundheit-pflege/gesundheitsschutz/infektionsschutz-hygiene/informationen-zu-coronavirus/lage-in-baden-wuerttemberg/) in einer [XLSX-Datei](https://sozialministerium.baden-wuerttemberg.de/fileadmin/redaktion/m-sm/intern/downloads/Downloads_Gesundheitsschutz/Tabelle_Coronavirus-Faelle-BW.xlsx) veröffentlicht.

Die zu den relativen Fallzahlen verwendeten Bevölkerungsgrößen und die Bevölkerungsdichten stammen aus dem [Statistischen Landesamt Baden-Württemberg](https://www.statistikportal.de/de/bevoelkerung/flaeche-und-bevoelkerung). Die Datei ist [hier erreichbar](https://www.statistik-bw.de/BevoelkGebiet/Bevoelk_I_Flaeche_j.csv).

### Programmdateien

* **download_BW.py** ist das Skript um die Daten vom [Ministerium für Soziales und Integration Baden-Württemberg](https://sozialministerium.baden-wuerttemberg.de/de/gesundheit-pflege/gesundheitsschutz/infektionsschutz-hygiene/informationen-zu-coronavirus/lage-in-baden-wuerttemberg/) herunterzuladen.

* **BW.py** ist das für Baden-Württemberg spezifische Skript, das hauptsächlich für die Vorbereitung der Daten zuständig ist. Es enthält auch die Visualisation.

* **utils.py** hat die gemeinsamen Funktionen, die die Analyse durchführen.

### Schaubilder für das gesamte Land Baden-Württemberg

Die Schaubilder zeigen die Coronavirus-Fälle, bzw. die Todesfälle für alle Landkreise (blaue Punkte) und für das gesamte Land Baden-Württemberg (gelb-schwarzer Punkt). Meine Heimatstadt Freiburg im Breisgau zeichnete ich mit Verweis auf unser Wappen mit rotem Kreuz.

Für die andere Achse hatte ich die Bevölkerungsdichte des Landkreises gewählt. Ich hatte vermutet, je dichter ein Kreis besiedelt ist, desto höhere Fallzahlen ich finden werde. Meine Vermutung war total falsch!

So war der Korrelationskoeffizient am 14.04.2020 zwischen Bevölkerungsdichte (Einwohner/km²) und Fallzahl auf 100.000 Einwohner -0.275, während zwischen Bevölkerungsdichte (Einwohner/km²) und Todesfälle auf 100.000 Einwohner -0.262.

Viele Landkreise markierte ich mit dem zu ihm gehörenden Kfz-Kennzeichen. Wo zwei Landkreise das gleiche Kennzeichen haben (wie Freiburg im Breisgaus und Breisgau-Hochschwarzwald _FR_ oder Heidelberg und Rhein-Neckar-Kreis _HD_) kennzeichnete ich den ländlichen Kreis mit Sternchen.

Es ist zu beachten, dass es auch in einem Bundesland Unterschiede geben kann, wieviele Tests in den einzelnen Landkreisen durchgeführt werden. Wenn man zu wenig Tests durchführt, dann detektiert man automatisch auch weniger Neuinfektionen. Ich weiß es auch nicht, zu welchem Landkreis ein Infekt oder ein Todesfall zugeordnet wird wenn der Patient in einem ländlichen Kreis wohnt aber in einer großstädtischen Universitätsklinik behandelt wird.

![Baden-Württemberg, Populationsdichte abgebildet auf Coronavirus-Fallzahlen](https://github.com/Melykuti/COVID-19/blob/master/plots/BW_population_density_scatter_confirmed_2020-04-22.png)

![Baden-Württemberg, Populationsdichte abgebildet auf Coronavirus-Todesfälle](https://github.com/Melykuti/COVID-19/blob/master/plots/BW_population_density_scatter_deaths_2020-04-22.png)

Warum Freiburg solch eine merkwürdige Position in der Grafik hat weiß ich nicht. Das Universitätsklinikum hat einen ausgezeichneten Ruf und es kann sein, dass viele Schwerkranke hierher gebracht werden. Gegen Ende März boten Freiburg, Karlsruhe, Mannheim und Heidelberg an, Corona-PatientInnen aus der schwer betroffenen Grenzenregion Frankreichs, Region Grand Est zu übernehmen. Dies mag die Lage in Freiburg erklären, jedoch sieht man keine ähnliche Wirkung in den anderen drei Städten. Eventuell hat es mit der Grenzennähe und GrenzgängerInnen zu tun, die von Freiburg nach Basel und die aus dem Elsass hierher pendeln. Basel hat mehr Fälle pro 100.000 EinwohnerInnen als zum Beispiel das Grenzengebiet gegenüber Konstanz.

Eine andere Erklärung ist auch wohl möglich, die mit meinem früheren Forschungsgebiet zu tun hat: dass es eine Erklärung gibt, die aber nicht nützt. Wir sind in der Anfangsphase – ich meine es nicht zeitlich sondern daran gemessen, dass z.B. nur 500-1000 von 100.000 sich angesteckt haben und keine 10.000. In der Anfangsphase haben zufällige, stochastische Effekte sehr große Wirkung. Unter dem Namen Superspreader (Personen und Ereignisse) meint man in der Epidemiologie solche Effekte. Wenn es früh einen Coronavirus-Fall in Freiburg gab, der weitere zehn Personen angesteckt hat, dann hätte Freiburg einen Frühstart in der Epidemie im Verglech mit anderen Landkreisen gehabt. Solche Ereignisse sind zufällig und man könnte von denen nicht schlussfolgern, dass etwas in einigen Landkreisen systematisch anders läuft.


### Resultate

Diese Resultate sind die direkte numerische Folge der linearen Anpassungen.

**Ich mache eine grobe Schätzung, wie hoch die wahre kumulierte Fallzahl zur Zeit sein kann.** Meine Annahme ist es, dass die gemeldeten Zahlen nur diejenigen zeigen, die schon getestet worden sind. Aber die Inkubationszeit der COVID-19 Krankheit beträgt im Schnitt fünf Tage (von 1 Tag bis 14 Tage), deshalb werden sich die heute infizierten erst in ungefähr fünf Tagen melden und testen lassen, sogar später. Aber sie sind bereits unumkehrbar infiziert.

Die Spalten haben die folgende Bedeutung:

* Die Gesamtanzahl der Infekten wächst täglich um diese Zahl

* Die Gesamtanzahl der Infekten pro 100.000 Einwohner wächst täglich um diese Zahl

* Die Gesamtanzahl der Infekten wächst täglich um diesen Faktor (prozentual ausgedrückt)

* Die Zeitdauer bis die Anzahl der Infekten sich verdoppelt. Dies ist ein Begriff, der zum exponentiellen Wachstum natürlich passt, aber bei nur linearem Wachstum nicht mehr so aussagekräftig ist. Bei exponentiellem Wachstum ist die Fallzahl nach 2 Verdopplungszeiten _viermal_ so hoch wie am Anfang. Bei linearem Wachstum ist sie nur _dreimal_ so hoch. Im Allgemeinen, nach `n` mal der Verdopplungszeit wird die Fallzahl bei exponentiellem Wachstum auf `2^n` mal die ursprüngliche gestiegen sein, bei linearem Wachstum nur auf `n+1` mal die ursprüngliche.

* Die letzte gemeldete Anzahl der Fälle.

* Die letzte gemeldete Anzahl der Coronavirus-Fälle pro 100.000 Einwohner.

* Meine Schätzung der derzeitigen Fallzahl (auf 100.000 Einwohner). Konkret, die Extrapolation der angepassten exponentiellen oder linearen Kurve auf 4, beziehungsweise, 6 Tage voraus. (Ich zeige die Schätzung wenn R^2 nicht kleiner als 0,95 und die vorletzte Spalte nicht größer als 0,5 ist, oder wenn die vorletzte Spalte in [-0,2;&nbsp; 0,1] ist.) Für Todesfälle mache ich diese Extrapolation nicht.

* R^2 oder Bestimmtheitsmaß oder Determinationskoeffizient der Anpassungsgüte der linearen Regression. Je näher es an 1 ist, desto besser ist die Anpassung.

* Differenz zwischen der linearen Annäherung und der wahren Beobachtung in logarithmischem Raum für den letzten Datenpunkt (für den letzten Tag). Man kann es als Exponent einer Potenz auf Basis 2 interpretieren für die Quote zwischen Schätzung und der letzten Beobachtung. Wenn diese Nummer groß ist, dann ist die Annäherung wenig gut. Wenn sie sogar negativ ist, dann ist die Annäherung viel zu niedrig und die Anzahl der Fälle wird unterschätzt.

* Die Anzahl der Tage im Zeitfenster, in dem die lineare Regression stattfindet. Sie wird automatisch optimiert, so dass der Vektor (10 * (1-R^2), Differenz) in l_2 kleinstmöglich ist.)

* e wenn das exponentielle Modell, l wenn das lineare Modell die bessere Annäherung gab und die Zahlen in der dazugehörenden Reihe der Tabelle lieferte. Man darf dem Vorzug des exponentiellen Modells vor dem linearen nicht allzu viel Bedeutung beimessen wenn beides im Zeitfenster sehr genau ist.

&nbsp;
#### Infizierte

    Landkreis                Zu- Zuwachs Wachst.- Verdoppl.  Gesamte   pro     Schätzung   R^2  Diff. Fenster Exp/Lin
                           wachs   pro    rate      zeit      Fälle  100.000                          größe
                                 100.000

Stand 23.04.2020

    Alb-Donau-Kreis            7,3  3,7   1,5%   134,3 Tage     501    256     [264, 271] 0,94 -0,02  14  l
    Baden-Baden (Stadtkreis    2,9  5,3   1,8%   112,1 Tage     164    298     [323, 334] 0,98  0,02  14  l
    Biberach                   6,4  3,2   1,4%    51,3 Tage     472    236     [248, 255] 0,97 -0,01  14  e
    Böblingen                   15  3,8   1,2%   172,4 Tage    1272    325     [343, 350] 0,97  0,01  13  l
    Bodenseekreis              1,7  0,8   0,6%   331,8 Tage     276    128     [132, 133] 0,91  0,01  14  l
    Breisgau-Hochschwarzwal     17  6,3   1,7%   120,7 Tage    1019    388     [409, 421] 0,97 -0,01  14  l
    Calw                        12  7,8   2,0%    34,3 Tage     610    385     [418, 435] 0,98  0,00  10  e
    Emmendingen                4,3  2,6   0,8%    83,0 Tage     507    307     [322, 327] 0,92  0,02  13  e
    Enzkreis                    21   11   4,6%    15,4 Tage     473    238     [280, 307] 0,97 -0,02   5  e
    Esslingen                   16  3,0   1,0%   196,8 Tage    1563    293     [305, 311] 0,97  0,00   9  l
    Freiburg im Breisgau (S    9,6  4,2   1,1%   190,4 Tage     921    400     [417, 425] 0,99  0,00  12  l
    Freudenstadt                13   11   2,4%    28,7 Tage     522    443     [489, 513] 0,97  0,00  13  e
    Göppingen                  8,3  3,2   1,2%   166,6 Tage     700    272     [283, 289] 0,96 -0,01  13  l
    Heidelberg (Stadtkreis)   -7,7 -4,8  -2,9%     nan Tage     267    167                0,71 -0,03   6  l
    Heidenheim                 3,5  2,6   0,9%   232,6 Tage     409    309     [319, 325] 0,98  0,00   4  l
    Heilbronn                   18  5,2   2,3%    88,5 Tage     800    233     [257, 267] 0,97  0,01   9  l
    Heilbronn (Stadtkreis)     5,9  4,7   1,5%    45,6 Tage     386    306     [331, 341] 0,97  0,02  14  e
    Hohenlohekreis             5,7  5,1   0,8%   249,7 Tage     717    640     [660, 670] 0,97 -0,00  13  l
    Karlsruhe                   12  2,8   1,5%   134,6 Tage     838    189     [201, 207] 0,98  0,01  10  l
    Karlsruhe (Stadtkreis)     3,1  1,0   1,0%   203,7 Tage     322    103     [107, 109] 0,96 -0,00  12  l
    Konstanz                   6,1  2,1   1,5%   129,6 Tage     397    139     [150, 154] 0,97  0,02  14  l
    Lörrach                   10,0  4,4   1,9%   103,7 Tage     526    230     [246, 255] 0,98 -0,01   9  l
    Ludwigsburg                 20  3,7   1,4%    49,7 Tage    1461    269     [284, 292] 0,97  0,00  13  e
    Main-Tauber-Kreis          4,6  3,4   1,4%   142,5 Tage     329    249     [263, 269] 0,97  0,00  13  l
    Mannheim (Stadtkreis)      2,2  0,7   0,5%   379,2 Tage     424    137     [140, 141] 0,97 -0,00   6  l
    Neckar-Odenwald-Kreis      6,0  4,2   2,0%   100,1 Tage     300    209     [227, 236] 0,98  0,01   6  l
    Ortenaukreis                14  3,2   1,5%   136,4 Tage     936    218     [230, 237] 0,98 -0,00  13  l
    Ostalbkreis                 41   13   4,0%    50,2 Tage    1031    328     [388, 414] 0,97  0,02   8  l
    Pforzheim (Stadtkreis)     9,4  7,5   4,7%    15,0 Tage     209    166     [196, 215] 0,96 -0,03   6  e
    Rastatt                    6,0  2,6   1,3%   156,3 Tage     473    205     [217, 223] 0,98  0,01  14  l
    Ravensburg                 5,3  1,9   1,0%   193,0 Tage     511    180     [188, 192] 0,96  0,00  14  l
    Rems-Murr-Kreis             16  3,8   1,5%    46,9 Tage    1106    260     [269, 277] 0,94 -0,04  13  e
    Reutlingen                  22  7,6   1,7%   120,2 Tage    1314    458     [489, 504] 0,99  0,00   8  l
    Rhein-Neckar-Kreis          14  2,5   1,6%   121,9 Tage     856    156     [166, 171] 0,93 -0,00  12  l
    Rottweil                    12  8,4   2,2%    91,7 Tage     542    389     [430, 446] 0,96  0,02  13  l
    Schwäbisch Hall             12  6,1   1,7%   120,2 Tage     726    371     [397, 409] 0,98  0,00  10  l
    Schwarzwald-Baar-Kreis     7,8  3,7   1,8%   112,9 Tage     445    210     [225, 232] 0,98  0,00  13  l
    Sigmaringen                 12  9,1   1,6%    42,4 Tage     734    561     [597, 617] 0,99 -0,00   4  e
    Stuttgart                   13  2,0   1,0%   193,7 Tage    1262    199     [208, 212] 0,97  0,00  10  l
    Tübingen                    11  4,7   0,9%   221,2 Tage    1180    519     [538, 547] 0,96  0,00  12  l
    Tuttlingen                 5,5  3,9   1,4%    50,6 Tage     402    287     [307, 315] 0,94  0,02  13  e
    Ulm (Stadtkreis)           1,4  1,1   0,6%   117,4 Tage     233    184     [187, 190] 0,95 -0,01  11  e
    Waldshut                   6,7  3,9   2,4%    83,4 Tage     284    166     [185, 193] 0,94  0,02  14  l
    Zollernalbkreis             19   10   2,1%    94,4 Tage     930    492     [527, 548] 0,98 -0,01  14  l
    
    Baden-Württemberg          408  3,7   1,4%    49,7 Tage   29350    265     [280, 288] 0,99 -0,00   6  e

Stand 19.04.2020

    Alb-Donau-Kreis            5,7  2,9   1,3%    54,9 Tage     455    232     [244, 250] 0,98 -0,00   5  e
    Baden-Baden (Stadtkreis    3,2  5,8   2,1%    96,0 Tage     154    279     [307, 318] 0,98  0,01  11  l
    Biberach                   6,1  3,0   1,4%    51,3 Tage     446    223     [236, 242] 0,94 -0,00  10  e
    Böblingen                   18  4,5   1,4%   139,4 Tage    1229    314     [334, 343] 0,97  0,01   9  l
    Bodenseekreis              4,1  1,9   1,5%    46,6 Tage     274    127     [135, 139] 0,93  0,01   4  e
    Breisgau-Hochschwarzwal     16  6,0   1,7%   119,3 Tage     947    360     [380, 392] 0,95 -0,01  11  l
    Calw                        12  7,7   2,2%    90,9 Tage     561    354     [387, 403] 0,97  0,01  14  l
    Emmendingen                7,9  4,8   1,6%   126,7 Tage     505    305     [328, 338] 0,93  0,01  14  l
    Enzkreis                    15  7,4   3,8%    52,9 Tage     392    197     [226, 240] 0,97 -0,01  14  l
    Esslingen                   20  3,7   1,3%   152,3 Tage    1508    282     [298, 305] 0,99  0,00   5  l
    Freiburg im Breisgau (S    9,4  4,1   1,1%   187,1 Tage     885    384     [399, 408] 0,97 -0,00   8  l
    Freudenstadt                10  8,5   2,1%    93,4 Tage     470    399     [435, 452] 0,95  0,01   9  l
    Göppingen                   13  5,1   2,0%   101,1 Tage     663    258     [284, 294] 0,96  0,02  14  l
    Heidelberg (Stadtkreis)   0,70  0,4   0,2%   842,9 Tage     295    184     [186, 187] 0,89  0,00   4  l
    Heidenheim                  17   13   4,3%    16,4 Tage     391    295     [364, 396] 0,96  0,06  14  e
    Heilbronn                   20  5,8   2,7%    26,0 Tage     738    215     [239, 252] 0,97  0,00   5  e
    Heilbronn (Stadtkreis)     4,7  3,8   1,3%    53,2 Tage     363    288     [306, 314] 0,96  0,01   9  e
    Hohenlohekreis             7,2  6,4   1,0%    67,8 Tage     700    625     [651, 664] 0,99 -0,00   9  e
    Karlsruhe                   14  3,2   1,8%    38,7 Tage     801    180     [193, 200] 0,99 -0,01   6  e
    Karlsruhe (Stadtkreis)     3,6  1,2   1,2%   168,7 Tage     308     98     [104, 106] 0,91  0,01   9  l
    Konstanz                   7,7  2,7   2,0%    98,4 Tage     381    134     [145, 150] 0,98  0,00   5  l
    Lörrach                     13  5,6   2,7%    74,5 Tage     486    213     [236, 247] 0,99  0,00   4  l
    Ludwigsburg                 19  3,6   1,4%    49,7 Tage    1384    254     [269, 276] 0,94 -0,00   9  e
    Main-Tauber-Kreis          6,8  5,1   2,2%    32,0 Tage     315    238     [259, 271] 1,00 -0,00   4  e
    Mannheim (Stadtkreis)      5,7  1,8   1,4%   145,3 Tage     416    134     [142, 146] 0,99  0,00   4  l
    Neckar-Odenwald-Kreis       28   19  10,1%    19,7 Tage     278    194     [279, 318] 0,93  0,04   5  l
    Ortenaukreis                21  4,9   2,4%    29,5 Tage     895    208     [228, 239] 0,97 -0,01   4  e
    Ostalbkreis                 78   25   9,0%    22,1 Tage     897    286     [396, 446] 0,93  0,04   7  l
    Pforzheim (Stadtkreis)      10  8,3   6,2%    11,5 Tage     171    136                0,89 -0,21  14  e
    Rastatt                    7,4  3,2   1,6%   124,0 Tage     457    198     [211, 218] 0,98  0,00  14  l
    Ravensburg                 8,1  2,8   1,6%   123,1 Tage     498    175     [187, 193] 0,97  0,00   6  l
    Rems-Murr-Kreis             13  3,2   1,3%    52,1 Tage    1002    235     [249, 256] 0,97  0,01   7  e
    Reutlingen                  71   25   5,8%    12,3 Tage    1228    428     [561, 628] 0,96  0,06  14  e
    Rhein-Neckar-Kreis         5,7  1,0   0,7%   277,9 Tage     792    145     [149, 151] 0,90  0,00   4  l
    Rottweil                    17   12   3,3%    21,6 Tage     515    369     [424, 452] 0,97  0,01   8  e
    Schwäbisch Hall             15  7,8   2,2%    31,3 Tage     687    351     [383, 400] 0,96 -0,00   5  e
    Schwarzwald-Baar-Kreis     8,6  4,1   2,1%    96,3 Tage     421    198     [213, 221] 0,99 -0,01  14  l
    Sigmaringen                 14   11   2,1%    97,3 Tage     695    531     [581, 602] 0,97  0,01  14  l
    Stuttgart                   23  3,6   1,9%   105,2 Tage    1223    193     [210, 217] 0,98  0,01  14  l
    Tübingen                    17  7,3   1,5%   137,7 Tage    1152    507     [536, 551] 0,96  0,00   5  l
    Tuttlingen                  10  7,4   2,6%    26,5 Tage     394    281     [313, 330] 0,99  0,00   5  e
    Ulm (Stadtkreis)           1,7  1,4   0,8%    91,1 Tage     227    180     [185, 188] 0,94 -0,00   5  e
    Waldshut                   9,5  5,6   3,6%    19,9 Tage     272    159     [181, 194] 0,96 -0,02  14  e
    Zollernalbkreis             19 10,0   2,3%    88,2 Tage     839    444     [485, 505] 0,97  0,00  10  l
    
    Baden-Württemberg          592  5,4   2,2%    32,5 Tage   27710    250     [273, 285] 1,00  0,00   9  e


Stand 15.04.2020

    Alb-Donau-Kreis             10  5,4   2,4%    83,0 Tage     439    224     [250, 261] 0,96  0,02  11  l
    Baden-Baden (Stadtkreis    4,2  7,5   2,9%    69,9 Tage     145    263     [301, 316] 0,99  0,03  14  l
    Biberach                    13  6,6   3,1%    64,2 Tage     418    209     [250, 263] 0,93  0,07  14  l
    Böblingen                   35  8,9   3,0%    67,6 Tage    1186    303     [349, 367] 0,97  0,03  13  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     263    122                1,00  0,00   4  l
    Breisgau-Hochschwarzwal    8,2  3,1   0,9%    74,4 Tage     882    336     [348, 354] 0,96 -0,00   4  e
    Calw                        15  9,4   2,8%    24,8 Tage     528    333     [379, 401] 0,97  0,02  13  e
    Emmendingen                 10  6,3   2,2%    92,8 Tage     482    291     [327, 340] 0,95  0,04  14  l
    Enzkreis                    14  7,3   4,3%    46,2 Tage     339    170     [204, 218] 0,98  0,02  14  l
    Esslingen                   38  7,2   2,7%    75,4 Tage    1454    272     [303, 317] 0,99  0,01  14  l
    Freiburg im Breisgau (S    8,2  3,6   1,0%    72,2 Tage     856    372     [386, 393] 0,98 -0,00   4  e
    Freudenstadt                21   18   4,9%    41,0 Tage     442    375     [471, 507] 0,98  0,06  14  l
    Göppingen                   14  5,5   2,2%    31,3 Tage     645    251     [273, 286] 0,99 -0,00   4  e
    Heidelberg (Stadtkreis)    9,2  5,8   3,2%    61,9 Tage     293    183     [216, 228] 0,78  0,06  14  l
    Heidenheim                  14   11   4,0%    17,7 Tage     362    273     [311, 336] 0,95 -0,04  13  e
    Heilbronn                   17  4,9   2,5%    80,5 Tage     683    199     [223, 233] 0,97  0,02  14  l
    Heilbronn (Stadtkreis)     4,3  3,4   1,2%    56,9 Tage     351    279     [292, 299] 0,94 -0,00   6  e
    Hohenlohekreis             5,2  4,6   0,8%    90,9 Tage     677    604     [623, 632] 0,98 -0,00   4  e
    Karlsruhe                   32  7,1   4,2%    47,6 Tage     759    171     [210, 224] 0,94  0,06  14  l
    Karlsruhe (Stadtkreis)      11  3,4   3,6%    56,3 Tage     303     97     [114, 121] 0,96  0,04  14  l
    Konstanz                   9,6  3,4   2,7%    73,8 Tage     358    125     [143, 149] 0,95  0,03  12  l
    Lörrach                    9,9  4,3   2,2%    90,7 Tage     447    196     [221, 230] 0,94  0,04  13  l
    Ludwigsburg                 35  6,4   2,7%    75,0 Tage    1317    242     [275, 288] 0,96  0,03  13  l
    Main-Tauber-Kreis          6,6  5,0   2,3%    88,5 Tage     295    223     [247, 257] 0,95  0,02  11  l
    Mannheim (Stadtkreis)       12  3,9   3,1%    64,4 Tage     399    129     [148, 155] 0,96  0,02  14  l
    Neckar-Odenwald-Kreis      5,5  3,8   2,9%    67,9 Tage     191    133     [149, 156] 0,97  0,00  14  l
    Ortenaukreis               8,5  2,0   1,0%    67,8 Tage     835    194     [202, 206] 0,98 -0,00   4  e
    Ostalbkreis                104   33  15,8%     4,7 Tage     747    238     [403, 541] 0,86 -0,09   4  e
    Pforzheim (Stadtkreis)     4,4  3,5   4,0%    49,7 Tage     111     88     [104, 111] 0,98  0,02  14  l
    Rastatt                    4,8  2,1   1,1%   177,5 Tage     429    186     [195, 199] 0,98  0,00   7  l
    Ravensburg                 7,9  2,8   1,7%   119,0 Tage     478    168     [181, 186] 0,95  0,01  14  l
    Rems-Murr-Kreis             11  2,5   1,1%    62,7 Tage     966    227     [236, 242] 0,96 -0,00   4  e
    Reutlingen                  65   23   5,8%    12,2 Tage    1159    404     [477, 535] 0,95 -0,09  14  e
    Rhein-Neckar-Kreis          19  3,4   2,5%    27,7 Tage     776    142     [153, 161] 0,64 -0,03   4  e
    Rottweil                    21   15   4,4%    45,2 Tage     465    333     [406, 435] 0,97  0,04  13  l
    Schwäbisch Hall            7,3  3,7   1,1%   174,6 Tage     641    327     [342, 350] 0,94 -0,00   7  l
    Schwarzwald-Baar-Kreis     9,7  4,6   2,5%    28,0 Tage     397    187     [205, 215] 0,98 -0,01  11  e
    Sigmaringen                 16   12   2,4%    83,8 Tage     676    517     [555, 579] 0,97 -0,02  14  l
    Stuttgart                   24  3,8   2,1%    96,6 Tage    1177    185     [201, 209] 0,99  0,00  14  l
    Tübingen                   7,6  3,3   0,7%   287,4 Tage    1097    483     [496, 503] 0,93  0,00   5  l
    Tuttlingen                 9,4  6,7   2,6%    76,8 Tage     365    260     [295, 309] 0,90  0,03  11  l
    Ulm (Stadtkreis)           6,3  5,0   2,9%    24,5 Tage     222    176     [202, 214] 0,94  0,04  12  e
    Waldshut                   7,2  4,2   3,1%    64,0 Tage     232    136     [158, 167] 0,96  0,04  12  l
    Zollernalbkreis             25   13   3,3%    61,0 Tage     763    404     [474, 500] 0,96  0,04  14  l
    
    Baden-Württemberg          521  4,7   2,0%    34,5 Tage   26050    235     [254, 264] 0,99 -0,01   6  e

Stand 14.04.2020

    Alb-Donau-Kreis             12  6,1   2,8%    72,6 Tage     432    220     [250, 263] 0,96  0,03  11  l
    Baden-Baden (Stadtkreis    4,3  7,8   3,0%    66,8 Tage     145    263     [297, 313] 0,99  0,01  14  l
    Biberach                    15  7,3   3,4%    58,1 Tage     423    212     [251, 266] 0,96  0,05  14  l
    Böblingen                   37  9,4   3,2%    63,3 Tage    1172    299     [346, 364] 0,97  0,03  12  l
    Bodenseekreis              0,0  0,0   0,0%     inf Tage     263    122                1,00  0,00   4  l
    Breisgau-Hochschwarzwal     27   10   3,2%    63,2 Tage     869    331     [386, 407] 0,96  0,04  13  l
    Calw                        15  9,5   2,9%    24,2 Tage     524    331     [372, 394] 0,97  0,00  12  e
    Emmendingen                 10  6,3   2,2%    91,9 Tage     480    290     [323, 335] 0,96  0,03  12  l
    Enzkreis                    15  7,4   4,5%    44,3 Tage     328    165     [198, 213] 0,98  0,02  14  l
    Esslingen                   39  7,2   2,7%    72,9 Tage    1429    268     [296, 311] 0,99 -0,00  13  l
    Freiburg im Breisgau (S     24   10   2,8%    71,3 Tage     844    367     [419, 440] 0,96  0,03  12  l
    Freudenstadt                22   19   5,1%    39,3 Tage     435    369     [461, 498] 0,99  0,05  14  l
    Göppingen                   16  6,1   2,5%    78,8 Tage     627    244     [272, 285] 0,98  0,02  14  l
    Heidelberg (Stadtkreis)     10  6,3   3,6%    54,9 Tage     279    174     [217, 229] 0,82  0,10  14  l
    Heidenheim                  12  9,0   3,7%    19,1 Tage     336    254     [291, 313] 0,95 -0,01  14  e
    Heilbronn                   18  5,3   2,7%    73,5 Tage     665    194     [222, 232] 0,97  0,04  14  l
    Heilbronn (Stadtkreis)      11  8,6   3,2%    63,2 Tage     344    273     [320, 337] 0,93  0,04  13  l
    Hohenlohekreis              14   13   2,1%    93,6 Tage     670    598     [665, 690] 0,98  0,03  13  l
    Karlsruhe                   34  7,7   4,6%    43,3 Tage     741    167     [209, 225] 0,96  0,07  14  l
    Karlsruhe (Stadtkreis)      11  3,5   3,8%    53,3 Tage     298     95     [113, 120] 0,97  0,03  14  l
    Konstanz                    10  3,6   2,9%    69,1 Tage     352    123     [141, 149] 0,96  0,03  11  l
    Lörrach                     11  4,7   2,4%    83,4 Tage     447    196     [221, 230] 0,96  0,03  12  l
    Ludwigsburg                 37  6,8   2,8%    70,4 Tage    1299    239     [273, 287] 0,96  0,03  12  l
    Main-Tauber-Kreis          7,0  5,3   2,4%    83,0 Tage     290    219     [245, 256] 0,95  0,02  10  l
    Mannheim (Stadtkreis)       13  4,1   3,4%    59,4 Tage     380    123     [146, 154] 0,97  0,05  14  l
    Neckar-Odenwald-Kreis      5,7  3,9   3,2%    63,2 Tage     179    125     [146, 154] 0,97  0,04  14  l
    Ortenaukreis                28  6,4   3,4%    59,3 Tage     823    192     [223, 236] 0,96  0,03  11  l
    Ostalbkreis                 14  4,6   2,7%    25,7 Tage     577    184     [186, 196] 0,89 -0,14  13  e
    Pforzheim (Stadtkreis)     4,5  3,6   4,2%    47,8 Tage     107     85     [102, 109] 0,99  0,02  14  l
    Rastatt                    5,3  2,3   1,2%    55,8 Tage     427    185     [194, 199] 0,99 -0,00   6  e
    Ravensburg                 8,4  2,9   1,8%   110,6 Tage     463    163     [179, 185] 0,95  0,03  14  l
    Rems-Murr-Kreis             40  9,3   4,2%    47,6 Tage     949    223     [276, 295] 0,95  0,07  14  l
    Reutlingen                  58   20   5,6%    12,7 Tage    1072    374     [438, 489] 0,94 -0,08  13  e
    Rhein-Neckar-Kreis         3,4  0,6   0,5%   422,4 Tage     718    131     [134, 136] 0,63  0,01   8  l
    Rottweil                    23   17   5,2%    38,4 Tage     463    332     [409, 442] 0,97  0,03  14  l
    Schwäbisch Hall             14  7,4   2,3%    87,1 Tage     631    322     [360, 375] 0,94  0,03  11  l
    Schwarzwald-Baar-Kreis     8,4  3,9   2,2%    90,1 Tage     380    179     [196, 204] 0,98  0,01  10  l
    Sigmaringen                 15   12   2,4%    82,9 Tage     625    478     [539, 562] 0,97  0,03  13  l
    Stuttgart                   25  3,9   2,1%    93,2 Tage    1154    182     [198, 206] 0,99  0,00  14  l
    Tübingen                    29   13   2,7%    73,8 Tage    1087    478     [554, 580] 0,94  0,05  14  l
    Tuttlingen                  15   11   4,2%    47,7 Tage     356    254     [319, 340] 0,92  0,09  14  l
    Ulm (Stadtkreis)           6,6  5,3   3,0%    23,3 Tage     220    174     [200, 212] 0,94  0,03  11  e
    Waldshut                   9,2  5,4   4,0%    17,7 Tage     230    135     [164, 178] 0,97  0,06  11  e
    Zollernalbkreis             27   14   3,5%    56,4 Tage     756    400     [471, 500] 0,97  0,04  14  l
    
    Baden-Württemberg          458  4,1   1,8%   109,5 Tage   25289    228     [245, 254] 1,00  0,00   5  l


Stand 01.04.2020

    Alb-Donau-Kreis             45   23  20,3%     3,8 Tage     228    116     [278, 403] 0,98  0,19  14  e
    Baden-Baden (Stadtkreis    9,6   17  12,2%    16,4 Tage      84    152     [221, 256] 1,00 -0,00   5  l
    Biberach                    22   11   9,5%    21,0 Tage     236    118     [167, 189] 0,97  0,05  11  l
    Böblingen                   24  6,0   5,6%    12,8 Tage     432    110     [137, 153] 0,99  0,00   4  e
    Bodenseekreis              3,8  1,8   2,0%    98,9 Tage     190     88       [95, 99] 0,96  0,00   5  l
    Breisgau-Hochschwarzwal     47   18  11,6%     6,3 Tage     419    159     [256, 319] 0,99  0,05  12  e
    Calw                        21   13   6,9%    29,0 Tage     308    194     [250, 276] 0,99  0,02  12  l
    Emmendingen                 27   16   9,7%     7,5 Tage     287    174     [237, 285] 0,97 -0,09  11  e
    Enzkreis                    20   10  16,7%     4,5 Tage     125     63     [126, 172] 0,99  0,12  13  e
    Esslingen                   49  9,2   6,2%    32,3 Tage     833    156     [192, 211] 0,99 -0,01  14  l
    Freiburg im Breisgau (S     31   14   7,3%    27,3 Tage     442    192     [247, 275] 1,00  0,01   8  l
    Freudenstadt                19   16  11,3%    17,7 Tage     174    148     [215, 247] 0,98  0,03  10  l
    Göppingen                   30   12   8,2%    24,3 Tage     371    144     [199, 223] 0,98  0,06  11  l
    Heidelberg (Stadtkreis)     13  7,8   8,3%     8,7 Tage     154     96     [134, 157] 0,98  0,02   5  e
    Heidenheim                  11  8,3   6,9%    29,0 Tage     160    121     [152, 169] 0,97 -0,02  14  l
    Heilbronn                   31  9,0   7,6%     9,5 Tage     427    124     [166, 192] 0,99 -0,01   4  e
    Heilbronn (Stadtkreis)      14   11   9,1%    21,9 Tage     168    133     [173, 196] 0,99 -0,04  11  l
    Hohenlohekreis              26   23   5,6%    35,5 Tage     453    404     [502, 547] 0,98  0,01  14  l
    Karlsruhe                   18  4,1   6,6%    30,5 Tage     305     69       [82, 90] 0,97 -0,05  14  l
    Karlsruhe (Stadtkreis)      19  6,1  13,9%     5,3 Tage     159     51      [88, 115] 0,96  0,05  14  e
    Konstanz                    11  4,0   7,5%    26,8 Tage     162     57       [73, 81] 0,98 -0,00  11  l
    Lörrach                     25   11  10,6%     6,9 Tage     251    110     [161, 197] 0,99 -0,03   7  e
    Ludwigsburg                 57   11   8,4%    23,9 Tage     698    128     [176, 197] 0,97  0,04  11  l
    Main-Tauber-Kreis           18   14  14,8%     5,0 Tage     135    102     [178, 234] 0,98  0,00   8  e
    Mannheim (Stadtkreis)       16  5,3   7,5%     9,6 Tage     226     73      [97, 112] 0,98 -0,02   8  e
    Neckar-Odenwald-Kreis       13  9,4  14,6%     5,1 Tage      99     69     [126, 165] 0,99  0,08  14  e
    Ortenaukreis                31  7,3   9,9%    20,2 Tage     316     74     [106, 121] 0,98  0,05   8  l
    Ostalbkreis                 20  6,3   6,9%    29,1 Tage     298     95     [120, 133] 0,97  0,00  14  l
    Pforzheim (Stadtkreis)     7,1  5,7  16,7%     4,5 Tage      46     37       [68, 93] 1,00  0,01   5  e
    Rastatt                     19  8,0   6,6%    30,4 Tage     286    124     [158, 174] 0,99  0,02   9  l
    Ravensburg                  24  8,6   7,4%    27,0 Tage     340    120     [164, 181] 0,93  0,08  14  l
    Rems-Murr-Kreis             23  5,5   6,9%    28,9 Tage     392     92     [103, 114] 0,94 -0,11  14  l
    Reutlingen                  21  7,4   7,3%    27,5 Tage     325    113     [134, 149] 0,96 -0,08  14  l
    Rhein-Neckar-Kreis          39  7,1   6,8%    29,5 Tage     590    108     [136, 150] 0,99 -0,00  10  l
    Rottweil                    18   13  13,7%    14,6 Tage     152    109     [155, 181] 0,96 -0,05   9  l
    Schwäbisch Hall             26   13   7,8%    25,6 Tage     343    175     [228, 254] 0,98  0,00  11  l
    Schwarzwald-Baar-Kreis      15  6,9   7,8%    25,7 Tage     187     88     [121, 135] 0,98  0,06  13  l
    Sigmaringen                 31   24   9,5%    21,0 Tage     341    261     [364, 412] 0,98  0,03  10  l
    Stuttgart                   46  7,3   6,2%    32,1 Tage     784    123     [153, 168] 0,98  0,01  14  l
    Tübingen                    65   29  10,1%    19,8 Tage     655    288     [428, 486] 0,95  0,09  11  l
    Tuttlingen                  19   14  12,6%    15,9 Tage     167    119     [175, 203] 0,99  0,00   9  l
    Ulm (Stadtkreis)           8,4  6,6   7,3%    27,5 Tage     118     93     [122, 136] 0,99  0,03  13  l
    Waldshut                   8,7  5,1   9,2%    21,7 Tage      98     57       [77, 87] 0,98 -0,01  11  l
    Zollernalbkreis             33   17   9,5%    21,1 Tage     349    185     [273, 308] 0,95  0,10  11  l
    
    Baden-Württemberg          903  8,2   7,1%    10,1 Tage   13313    120     [157, 180] 0,99 -0,01   4  e

#### Todesfälle

    Landkreis               Zuwachs Zuwachs Wachst.- Verdoppl.  Gesamte   pro     R^2  Diff. Fenster Exp/Lin
                                      pro    rate      zeit      Fälle  100.000              größe
                                    100.000

Stand 23.04.2020

    Alb-Donau-Kreis            0,60   0,31   7,1%    28,3 Tage     9,0    4,6    0,90 -0,01   4  l
    Baden-Baden (Stadtkreis)   0,73    1,3   5,4%    36,9 Tage      14     25    0,96  0,02  13  l
    Biberach                    1,1   0,56   7,0%    28,7 Tage      16    8,0    0,94  0,10  14  l
    Böblingen                   1,4   0,35   3,9%    18,1 Tage      36    9,2    0,97 -0,01   4  e
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     7,0    3,2    1,00  0,00   4  l
    Breisgau-Hochschwarzwald    2,8    1,1   7,1%    10,2 Tage      44     17    0,98 -0,08  14  e
    Calw                       0,72   0,46   5,6%    12,8 Tage      13    8,2    0,90 -0,02  14  e
    Emmendingen                0,66   0,40   1,9%   106,2 Tage      35     21    0,94  0,00  14  l
    Enzkreis                   0,70   0,35   5,9%    34,1 Tage      12    6,0    0,97  0,02  12  l
    Esslingen                   2,7   0,51   4,2%    17,0 Tage      67     13    0,98  0,00  14  e
    Freiburg im Breisgau (St    2,2   0,98   3,9%    50,8 Tage      60     26    0,97 -0,03  14  l
    Freudenstadt                1,4    1,2   6,1%    32,6 Tage      24     20    0,96  0,02  14  l
    Göppingen                  0,64   0,25   2,4%    29,5 Tage      28     11    0,92 -0,08  13  e
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     6,0    3,7    1,00  0,00   4  l
    Heidenheim                 0,94   0,71   3,1%    63,6 Tage      30     23    0,92  0,02   6  l
    Heilbronn                   1,2   0,34   4,9%    41,0 Tage      25    7,3    0,94  0,01  13  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      10    7,9    1,00  0,00   4  l
    Hohenlohekreis             0,86   0,77   2,5%    78,7 Tage      34     30    0,89  0,05  14  l
    Karlsruhe                   2,2   0,50   5,0%    39,9 Tage      45     10    0,92  0,06  14  l
    Karlsruhe (Stadtkreis)     0,20   0,06   4,5%    15,8 Tage     5,0    1,6    0,81 -0,12  12  e
    Konstanz                   0,00   0,00   0,0%     inf Tage     8,0    2,8    1,00  0,00   4  l
    Lörrach                     1,9   0,83   5,8%    34,7 Tage      34     15    0,96  0,00   4  l
    Ludwigsburg                 2,4   0,45   5,2%    13,6 Tage      47    8,6    0,98  0,00  13  e
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage     7,0    5,3    1,00  0,00   4  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage     6,0    1,9    1,00  0,00   4  l
    Neckar-Odenwald-Kreis       1,7    1,2  14,8%    13,5 Tage      12    8,4    0,98  0,03   4  l
    Ortenaukreis                2,5   0,58   3,2%    61,6 Tage      77     18    0,98  0,01  14  l
    Ostalbkreis                 1,1   0,36   6,2%    32,1 Tage      18    5,7    0,93  0,02  14  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     4,0    3,2    1,00  0,00   4  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      11    4,8    1,00  0,00   4  l
    Ravensburg                 0,27   0,09   4,4%    16,0 Tage     6,0    2,1    0,86 -0,02  11  e
    Rems-Murr-Kreis             1,4   0,33   3,5%    57,1 Tage      40    9,4    0,92  0,01   9  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      16    5,6    1,00  0,00   4  l
    Rhein-Neckar-Kreis          1,4   0,26   5,5%    36,4 Tage      26    4,7    0,98  0,00   4  l
    Rottweil                   0,53   0,38   4,8%    41,7 Tage      11    7,9    0,96  0,04  14  l
    Schwäbisch Hall             1,1   0,54   2,7%    73,6 Tage      39     20    0,97  0,03  13  l
    Schwarzwald-Baar-Kreis     0,88   0,41   6,8%    29,6 Tage      13    6,1    0,96  0,07  14  l
    Sigmaringen                0,47   0,36   1,6%   122,7 Tage      29     22    0,90  0,01  13  l
    Stuttgart                   2,3   0,36   5,2%    38,8 Tage      45    7,1    0,99 -0,01  14  l
    Tübingen                    1,9   0,82   5,3%    13,5 Tage      36     16    0,97  0,04  14  e
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      10    7,1    1,00  0,00   4  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     3,0    2,4    1,00  0,00   4  l
    Waldshut                    1,7   0,97   5,4%    36,7 Tage      32     19    0,98 -0,05  14  l
    Zollernalbkreis             2,0    1,1   3,8%    52,7 Tage      53     28    0,95  0,01  14  l
    
    Baden-Württemberg            46   0,42   4,3%    46,9 Tage    1103   10,0    1,00  0,00   4  l

Stand 19.04.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     7,0    3,6    1,00  0,00   4  l
    Baden-Baden (Stadtkreis)    1,1    2,0   9,8%     7,4 Tage      12     22    0,94 -0,01   9  e
    Biberach                    1,8   0,91  13,0%     5,7 Tage      14    7,0    0,94  0,06   5  e
    Böblingen                   1,5   0,38   4,6%    43,0 Tage      32    8,2    0,97  0,05  14  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     6,0    2,8    1,00  0,00   4  l
    Breisgau-Hochschwarzwald    2,4   0,91   7,6%     9,5 Tage      33     13    0,99 -0,02  14  e
    Calw                       0,00   0,00   0,0%     inf Tage     9,0    5,7    1,00  0,00   4  l
    Emmendingen                0,96   0,58   3,0%    66,8 Tage      32     19    0,95  0,05  14  l
    Enzkreis                   0,98   0,49  10,3%     7,1 Tage      10    5,0    0,93 -0,06   8  e
    Esslingen                   2,1   0,38   3,5%    56,5 Tage      58     11    0,98 -0,01  14  l
    Freiburg im Breisgau (St    2,7    1,2   5,5%    36,1 Tage      51     22    0,98  0,01  14  l
    Freudenstadt                1,2    1,0   7,0%    28,5 Tage      17     14    0,94  0,03  14  l
    Göppingen                  0,62   0,24   2,6%    27,3 Tage      24    9,3    0,94  0,01   7  e
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     6,0    3,7    1,00  0,00   4  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      26     20    1,00  0,00   4  l
    Heilbronn                   2,2   0,63   9,8%     7,4 Tage      22    6,4    0,95  0,03   8  e
    Heilbronn (Stadtkreis)      2,0    1,6  20,6%     3,7 Tage      10    7,9    0,94  0,17  14  e
    Hohenlohekreis              1,0   0,89   3,0%    67,0 Tage      34     30    1,00  0,00   4  l
    Karlsruhe                   4,6    1,0  11,3%     6,5 Tage      41    9,2    0,97  0,12  14  e
    Karlsruhe (Stadtkreis)     0,26   0,08   6,4%    31,1 Tage     4,0    1,3    0,77  0,04   6  l
    Konstanz                    1,2   0,42  15,0%    13,3 Tage     8,0    2,8    0,80  0,04   4  l
    Lörrach                     1,3   0,56   4,6%    43,1 Tage      28     12    0,96  0,00  14  l
    Ludwigsburg                 1,8   0,33   4,7%    42,4 Tage      38    7,0    0,97  0,02  13  l
    Main-Tauber-Kreis          0,57   0,43   8,2%    24,4 Tage     7,0    5,3    0,95 -0,00  12  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage     6,0    1,9    1,00  0,00   4  l
    Neckar-Odenwald-Kreis      0,26   0,18   3,7%    54,4 Tage     7,0    4,9    0,77  0,02   6  l
    Ortenaukreis                3,1   0,72   4,6%    15,6 Tage      68     16    0,98  0,02  11  e
    Ostalbkreis                 2,3   0,73  16,3%     4,6 Tage      14    4,5    0,97  0,21  14  e
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     4,0    3,2    1,00  0,00   4  l
    Rastatt                     1,2   0,51  11,2%    17,9 Tage      11    4,8    0,97  0,01   6  l
    Ravensburg                 0,16   0,06   3,2%    62,3 Tage     5,0    1,8    0,85 -0,01  14  l
    Rems-Murr-Kreis             2,2   0,51   6,2%    32,3 Tage      35    8,2    0,93  0,01  14  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      16    5,6    1,00  0,00   4  l
    Rhein-Neckar-Kreis          1,9   0,35   8,7%    23,0 Tage      22    4,0    0,93  0,04   6  l
    Rottweil                   0,53   0,38   5,9%    34,1 Tage     9,0    6,5    0,96  0,05  14  l
    Schwäbisch Hall             1,3   0,66   3,6%    55,5 Tage      36     18    0,97  0,02   8  l
    Schwarzwald-Baar-Kreis     0,92   0,43   9,7%    20,6 Tage      10    4,7    0,92  0,05  10  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      27     21    1,00  0,00   4  l
    Stuttgart                   2,5   0,40   7,4%    27,1 Tage      36    5,7    0,99  0,00   8  l
    Tübingen                    1,3   0,59   4,5%    44,3 Tage      32     14    0,96 -0,06  14  l
    Tuttlingen                 0,48   0,34   5,0%    39,7 Tage      10    7,1    0,92 -0,02  14  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     3,0    2,4    1,00  0,00   4  l
    Waldshut                    2,3    1,3   9,8%     7,4 Tage      25     15    0,97 -0,05  12  e
    Zollernalbkreis             2,2    1,2   4,7%    42,5 Tage      47     25    0,95 -0,02  14  l
    
    Baden-Württemberg            44   0,40   4,7%    42,8 Tage     952    8,6    0,99 -0,00  14  l


Stand 15.04.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     7,0    3,6    1,00  0,00   4  l
    Baden-Baden (Stadtkreis)   0,35   0,63   4,3%    46,1 Tage     8,0     15    0,95 -0,00  14  l
    Biberach                    1,7   0,84  17,6%     4,3 Tage      10    5,0    0,83 -0,07   9  e
    Böblingen                   2,4   0,61   8,0%     9,0 Tage      31    7,9    0,99  0,01  14  e
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     6,0    2,8    1,00  0,00   4  l
    Breisgau-Hochschwarzwald    1,9   0,73   7,6%     9,5 Tage      27     10    0,98 -0,05  12  e
    Calw                       0,48   0,30   5,3%    37,8 Tage     9,0    5,7    0,95  0,02   8  l
    Emmendingen                 1,4   0,85   4,5%    15,7 Tage      31     19    0,98  0,06  14  e
    Enzkreis                   0,35   0,18   5,0%    39,8 Tage     7,0    3,5    0,91 -0,03  13  l
    Esslingen                   2,1   0,40   4,4%    45,8 Tage      50    9,4    0,98  0,02  14  l
    Freiburg im Breisgau (St    2,9    1,3   6,7%    29,9 Tage      45     20    0,98 -0,00   8  l
    Freudenstadt                1,1   0,94   7,7%    26,1 Tage      16     14    0,91 -0,16  13  l
    Göppingen                  0,99   0,39   4,5%    44,3 Tage      22    8,6    0,95  0,07  14  l
    Heidelberg (Stadtkreis)    0,77   0,48  11,9%     6,2 Tage     6,0    3,7    0,62  0,66  13  e
    Heidenheim                  1,9    1,4   7,2%    27,7 Tage      26     20    0,98  0,04  12  l
    Heilbronn                  0,97   0,28   6,1%    11,7 Tage      18    5,2    0,93 -0,16  14  e
    Heilbronn (Stadtkreis)      1,0   0,83  19,8%     3,8 Tage     7,0    5,6    0,91 -0,16  12  e
    Hohenlohekreis              1,4    1,3   4,8%    41,3 Tage      31     28    0,93 -0,01  14  l
    Karlsruhe                   1,9   0,44   6,7%    30,0 Tage      31    7,0    0,97 -0,04  13  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     3,0   0,96    1,00  0,00   4  l
    Konstanz                   0,00   0,00   0,0%     inf Tage     5,0    1,8    1,00  0,00   4  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      22    9,6    1,00  0,00   4  l
    Ludwigsburg                 1,8   0,32   5,6%    36,0 Tage      33    6,1    0,95 -0,00  10  l
    Main-Tauber-Kreis           1,0   0,77  20,4%     3,7 Tage     5,0    3,8    0,90  0,10  11  e
    Mannheim (Stadtkreis)      0,37   0,12   6,8%    29,4 Tage     6,0    1,9    0,90 -0,03  12  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     6,0    4,2    1,00  0,00   4  l
    Ortenaukreis                3,6   0,83   6,0%    12,0 Tage      62     14    0,97 -0,02   5  e
    Ostalbkreis                 1,6   0,51  16,3%     4,6 Tage      12    3,8    0,97 -0,22  12  e
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     4,0    3,2    1,00  0,00   4  l
    Rastatt                    0,54   0,24   7,8%    25,7 Tage     7,0    3,0    0,92  0,00  13  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     4,0    1,4    1,00  0,00   4  l
    Rems-Murr-Kreis             3,7   0,86  12,2%     6,0 Tage      31    7,3    0,93 -0,07  14  e
    Reutlingen                 0,60   0,21   3,9%    51,3 Tage      16    5,6    0,93  0,02  14  l
    Rhein-Neckar-Kreis         0,44   0,08   2,8%    70,9 Tage      17    3,1    0,71 -0,06  14  l
    Rottweil                   0,82   0,59  10,3%     7,1 Tage     8,0    5,7    0,95  0,01  12  e
    Schwäbisch Hall             1,7   0,87   5,2%    38,2 Tage      33     17    0,98  0,01   4  l
    Schwarzwald-Baar-Kreis      1,6   0,75  18,8%    10,6 Tage     9,0    4,2    0,98  0,02   5  l
    Sigmaringen                 1,3    1,0   5,0%    39,9 Tage      27     21    0,97  0,05  14  l
    Stuttgart                   3,0   0,47  10,9%    18,3 Tage      29    4,6    1,00  0,00   4  l
    Tübingen                    1,3   0,59   5,5%    36,4 Tage      25     11    0,98  0,04  14  l
    Tuttlingen                 0,48   0,34   6,0%    33,2 Tage     9,0    6,4    0,85 -0,07  11  l
    Ulm (Stadtkreis)           0,60   0,47  24,0%     8,3 Tage     3,0    2,4    0,90 -0,03   4  l
    Waldshut                    1,3   0,76   7,4%    27,0 Tage      20     12    0,95 -0,10  14  l
    Zollernalbkreis             2,0    1,1   5,8%    34,6 Tage      36     19    0,95  0,07  14  l
    
    Baden-Württemberg            40   0,37   5,1%    38,9 Tage     820    7,4    1,00 -0,02  14  l


Stand 14.04.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     7,0    3,6    1,00  0,00   4  l
    Baden-Baden (Stadtkreis)   0,35   0,63   4,7%    42,9 Tage     8,0     15    0,95 -0,05  14  l
    Biberach                    2,0    1,0  22,2%     9,0 Tage     9,0    4,5    0,80  0,06   4  l
    Böblingen                   2,3   0,59   8,2%     8,8 Tage      29    7,4    0,99  0,00  14  e
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     6,0    2,8    1,00  0,00   4  l
    Breisgau-Hochschwarzwald    1,2   0,48   5,5%    36,0 Tage      24    9,1    0,98 -0,02  10  l
    Calw                       0,60   0,38   7,1%    10,1 Tage     9,0    5,7    0,95 -0,02   7  e
    Emmendingen                 1,4   0,86   4,7%    15,2 Tage      31     19    0,98  0,01  13  e
    Enzkreis                   0,32   0,16   5,0%    40,2 Tage     7,0    3,5    0,90 -0,10  14  l
    Esslingen                   2,2   0,41   4,7%    42,9 Tage      47    8,8    0,98  0,05  14  l
    Freiburg im Breisgau (St    3,1    1,4   7,7%    26,0 Tage      41     18    0,97  0,03   9  l
    Freudenstadt               1,00   0,84   9,1%    22,1 Tage      13     11    0,92 -0,11  12  l
    Göppingen                   1,0   0,40   4,8%    41,8 Tage      22    8,6    0,96  0,04  14  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    1,00  0,00   4  l
    Heidenheim                  1,9    1,5   8,0%    24,9 Tage      26     20    0,98 -0,02  11  l
    Heilbronn                  0,61   0,18   4,3%    46,0 Tage      14    4,1    0,95  0,02  12  l
    Heilbronn (Stadtkreis)     0,40   0,32  10,0%    20,0 Tage     4,0    3,2    0,92  0,10  10  l
    Hohenlohekreis              1,4    1,2   5,1%    39,3 Tage      28     25    0,92  0,03  14  l
    Karlsruhe                   1,8   0,41   7,1%    28,2 Tage      27    6,1    0,96  0,01  13  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     3,0   0,96    1,00  0,00   4  l
    Konstanz                   0,00   0,00   0,0%     inf Tage     5,0    1,8    1,00  0,00   4  l
    Lörrach                     1,8   0,79   8,3%     8,7 Tage      22    9,6    0,96  0,14  14  e
    Ludwigsburg                 1,4   0,26   4,7%    42,3 Tage      30    5,5    0,93  0,01  14  l
    Main-Tauber-Kreis          0,81   0,61  20,9%     3,6 Tage     5,0    3,8    0,87 -0,12  10  e
    Mannheim (Stadtkreis)      0,34   0,11   6,8%    29,5 Tage     5,0    1,6    0,87  0,06  12  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     6,0    4,2    1,00  0,00   4  l
    Ortenaukreis                2,0   0,47   3,6%    19,5 Tage      58     14    0,95 -0,05   9  e
    Ostalbkreis                 1,2   0,37  15,4%     4,8 Tage     8,0    2,5    0,97  0,07  11  e
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     4,0    3,2    1,00  0,00   4  l
    Rastatt                    0,55   0,24   9,1%    22,0 Tage     7,0    3,0    0,91 -0,07  12  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     4,0    1,4    1,00  0,00   4  l
    Rems-Murr-Kreis             2,9   0,69  12,5%     5,9 Tage      29    6,8    0,93 -0,14  14  e
    Reutlingen                 0,00   0,00   0,0%     inf Tage      15    5,2    1,00  0,00   4  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      14    2,6    1,00  0,00   4  l
    Rottweil                   0,71   0,51  10,3%     7,1 Tage     8,0    5,7    0,95 -0,12  14  e
    Schwäbisch Hall             1,7   0,85   5,4%    37,2 Tage      32     16    0,96  0,02  14  l
    Schwarzwald-Baar-Kreis      2,8    1,3  39,8%     2,1 Tage     8,0    3,8    1,00  0,02   4  e
    Sigmaringen                 1,4    1,1   5,3%    37,7 Tage      26     20    0,98  0,05  13  l
    Stuttgart                   2,1   0,33   8,5%     8,5 Tage      26    4,1    0,97 -0,06  14  e
    Tübingen                    1,4   0,61   5,8%    34,5 Tage      24     11    0,98  0,05  13  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage     7,0    5,0    1,00  0,00   4  l
    Ulm (Stadtkreis)           0,40   0,32  20,0%    10,0 Tage     2,0    1,6    0,80  0,05   4  l
    Waldshut                    1,2   0,73   8,3%     8,7 Tage      15    8,8    0,96  0,06   8  e
    Zollernalbkreis             2,1    1,1   6,3%    31,9 Tage      34     18    0,96  0,09  14  l
    
    Baden-Württemberg            40   0,36   5,4%    36,8 Tage     756    6,8    1,00 -0,00  14  l

Stand 01.04.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Baden-Baden (Stadtkreis)   0,29   0,52   9,5%    21,0 Tage     3,0    5,4    0,86  0,00   8  l
    Biberach                   0,00   0,00   0,0%     inf Tage     2,0    1,0    1,00  0,00   4  l
    Böblingen                   1,3   0,34  14,7%    13,6 Tage      10    2,6    0,86  0,01   7  l
    Bodenseekreis              0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Breisgau-Hochschwarzwald    1,3   0,48  16,8%    11,9 Tage     8,0    3,0    0,94  0,06   6  l
    Calw                       0,00   0,00   0,0%     inf Tage     2,0    1,3    1,00  0,00   4  l
    Emmendingen                 4,1    2,5  30,9%     2,6 Tage      15    9,1    0,97  0,00   4  e
    Enzkreis                   0,30   0,15  20,0%    10,0 Tage     2,0    1,0    0,60 -0,15   4  l
    Esslingen                   6,4    1,2  45,5%     1,8 Tage      18    3,4    0,96 -0,10   4  e
    Freiburg im Breisgau (St    3,5    1,5  30,4%     2,6 Tage      12    5,2    0,94  0,04   8  e
    Freudenstadt               0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Göppingen                   3,1    1,2  34,0%     2,4 Tage     9,0    3,5    0,87 -0,07   9  e
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Heidenheim                -0,40  -0,30 -13,3%     nan Tage     3,0    2,3    0,80 -0,03   4  l
    Heilbronn                  0,42   0,12   6,5%    30,8 Tage     8,0    2,3    0,89 -0,18  14  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Hohenlohekreis              1,6    1,4  17,8%    11,2 Tage     9,0    8,0    0,94  0,07   5  l
    Karlsruhe                  0,54   0,12  15,3%    13,1 Tage     4,0   0,90    0,85 -0,03   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Konstanz                   0,30   0,11  20,0%    10,0 Tage     2,0   0,70    0,60 -0,15   4  l
    Lörrach                    0,60   0,26  15,0%    13,3 Tage     5,0    2,2    0,60 -0,12   4  l
    Ludwigsburg                 1,4   0,26  21,5%     9,3 Tage     7,0    1,3    0,98  0,01   4  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Neckar-Odenwald-Kreis      0,40   0,28  20,0%    10,0 Tage     2,0    1,4    0,80  0,05   4  l
    Ortenaukreis                3,7   0,86  22,5%     3,4 Tage      18    4,2    0,98 -0,01   5  e
    Ostalbkreis                0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Rastatt                    0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Ravensburg                 0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage     3,0   0,70    1,00  0,00   4  l
    Reutlingen                 0,57   0,20   9,5%    21,0 Tage     6,0    2,1    0,93  0,05  11  l
    Rhein-Neckar-Kreis         0,61   0,11  15,2%    13,2 Tage     4,0   0,73    0,90  0,13   7  l
    Rottweil                   0,23   0,17   9,5%     7,6 Tage     2,0    1,4    0,77  0,37  13  e
    Schwäbisch Hall             1,1   0,55  11,3%    17,7 Tage      10    5,1    0,89  0,07   8  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage     2,0   0,94    1,00  0,00   4  l
    Sigmaringen                0,90   0,69  21,1%     3,6 Tage     6,0    4,6    0,80 -0,34   6  e
    Stuttgart                  0,88   0,14  12,6%    15,8 Tage     7,0    1,1    0,94  0,11   9  l
    Tübingen                    2,1   0,94  47,9%     1,8 Tage     5,0    2,2    0,94  0,07   5  e
    Tuttlingen                 0,00   0,00   0,0%     inf Tage     3,0    2,1    1,00  0,00   4  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     0,0 Tage    0,00   0,00    0,00 100,00  -1  l
    Waldshut                   0,00   0,00   0,0%     inf Tage     1,0   0,59    1,00  0,00   4  l
    Zollernalbkreis            0,39   0,21   8,7%    22,9 Tage     5,0    2,6    0,80 -0,02   7  l
    
    Baden-Württemberg            22   0,20  12,1%    16,6 Tage     196    1,8    0,98 -0,05   8  l

### Bitte um Spenden

Wenn Sie meine Arbeit unterstützen können, dann bitte ich Sie, mein [Ocean Plastic Detector](https://www.gofundme.com/OceanPlasticDetector) Projekt aufzusuchen und dort eine Spende durchzuführen. Danke!

Finden Sie mich auf [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), auf meiner Webseite/Blog: [Melykuti.me](https://melykuti.me), oder folgen Sie mir auf [Facebook](https://www.facebook.com/bence.melykuti) für meine öffentlichen Posts.

Ich arbeite als selbständiger Data Scientist. Sie können mich mit Ihrem Projekt beauftragen.
