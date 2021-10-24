## Analyse der Verbreitung der SARS-CoV-2 Coronavirus-Pandemie in Baden-Württemberg und in dessen einzelnen Landkreisen

> * Auf dieser Seite untersuche ich die gesamte oder kumulierte Anzahl der bestätigten Coronavirus-Fälle und nicht die Anzahl der zur Zeit infizierten.
> * Zusätzlich präsentiere ich die Anzahl der Todesfälle, sowohl grafisch als auch numerisch.

15 April 2020 (aktualisiert am 24 Oktober 2021), Freiburg i. Br. – In dieser Analyse versuche ich es in begreifbarer Form zu beantworten, wie schnell die COVID-19-Pandemie sich zur Zeit ausbreitet.

### Analyse

Meine Methodologie habe ich [auf Englisch im Detail beschrieben.](https://github.com/Melykuti/COVID-19/blob/master/global.md) Eine Übersicht auf Deutsch gibt es samt Datenanalyse [für Deutschland und für die Bundesländer](https://github.com/Melykuti/COVID-19/blob/master/Deutschland.md).

Seit 4 Mai 2020 nehme ich den täglichen Zuwachs der bestätigten Fallzahlen und Todesfälle als Startpunkt für meine Analyse (und nicht mehr die _kumulierten_ Zahlen). (Um die beiden vergleichen zu können, melde ich die Zahlen für 23.04.2020 mit beiden Methodologien.) Ich nähere den Trend mit linearer Regression an. Ich fitte ein _lineares_ und ein _exponentielles_ Modell: beim exponentiellen ist das Objekt der linearen Annäherung nicht die täglichen Zuwächse sondern ihre Logarithmen. Wenn die Pandemie sich exponentiell verbreitet, dann ist dieses Modell meiner Erwartung nach besser als das lineare.

Den täglichen Zuwachs pro 100.000 Bevölkerung leite ich von dem Fit ab und nicht direkt durch das Subtrahieren der letzten beiden kumulierten Fallzahlen, weil die Differenz unter Anderem durch den Effekt der Wochenenden sehr stark schwanken kann.

Von der annähernden Linie rechne ich aus, wie lange es dauern würde, bis die Fallzahl (oder Todeszahl) sich verdoppelt im Vergleich mit dem heutigen Stand. Es kann durchaus sein, dass eine Verdopplung unter dem jetzigen Trend nicht mehr zu erwarten ist. In diesem Fall melde ich `inf` (unendlich) als Verdopplungszeit. Von der Verdopplungszeit wird die tägliche Wachstumsrate in Prozent errechnet: ich teile das Zeitintervall uniform nach geometrischer Reihe auf. Nur wenn die Verdopplungszeit als unendlich errechnet wurde kalkuliere ich die tägliche Wachstumsrate aus der letzten kumulierten Anzahl. (Auch dann nehme ich einen Durchschnitt der letzten beiden für Glättung.)

Ich wähle immer die letzten 7-14 Tage aus, um die beiden linearen Regressionen (ohne und mit Logarithmusnahme) durchzuführen. (Bis 8 Mai 2020 wurde das Zeitfenster mit einer Länge von 4-14 Tagen gewählt. Um den deutlichen Effekt der Wochenenden möglichst zu dämpfen habe ich mich entschieden, die Fenstergröße auf mindestens 7 Tage zu erhöhen.) Mit der Wahl der Länge des Zeitintervalls versuche ich die beste Anpassung zu erreichen, gemessen an R^2 und an der normalisierten Differenz zwischen Zuwachs im ausgewählten Zeitfenster aus der Annäherung und in den Daten. Diese Optimierung ist automatisiert.

Nachdem die optimale Fenstergröße für sowohl das exponentielle als auch das lineare Modell ausgewählt wurde, vergleiche ich die beiden. Von den beiden Modellen wähle ich das bessere aus.

Auch wenn die tägliche Differenz schon ziemlich stabil ist und das Wachstum sichtbar nur linear ist, kann es besonders mit kurzen Zeitfenstern immer wieder vereinzelt vorkommen, wenn beide Modelle im Zeitfenster sehr gut sind, dass die Optimierung die exponentielle Annäherung genauer findet als die lineare Annäherung. _Man darf dem Vorzug des exponentiellen Modells vor dem linearen nicht allzu viel Bedeutung beimessen._

Man kann die beiden Arten der linearen Regression einfach als _Glättung der Zeitreihen_ sehen. So rechne ich den täglichen Zuwachs von der Annäherung aus und nicht von den letzten beiden Datenpunkten, was sehr empfindlich auf zufällige Effekte reagieren würde.

### Hinweis zur Interpretation

**Ich würde gerne schätzen können, wie hoch die Wahrscheinlichkeit ist, dass ich mit einem Infizierten in Kontakt komme, wenn ich meine Wohnung verlasse.** Diese Wahrscheinlichkeit wächst ungefähr proportional zur Gesamtanzahl der derzeit Infizierten (sie sind ansteckend). Seit Kontaktsperren in Kraft sind ist es nicht mehr ganz so, da die Straßen und Geschäfte viel leerer sind als am Anfang März.

Die Anzahl der Ansteckenden ist die kumulierte Anzahl der Fälle minus Anzahl der Genesenen minus Anzahl der Tode. Doch die Anzahl der Genesenen wird leider nicht veröffentlicht oder offiziell geschätzt. (Das Robert Koch Institut hat Ende März angefangen, diese Zahlen für die gesamte Bundesrepublik zu schätzen. Ab ca. 15 Mai müssen die Gesundheitsämter diese Zahlen, samt Anzahl der negativ ausgefallenen Tests, melden.)

Man könnte sie eigentlich einfach grob annähern, wenn man annimmt, dass jeder Patient in z.&nbsp;B. 21&nbsp;Tagen entweder sich erholt oder stirbt. Dann würde man von der heutigen kumulierten Fallzahl die kumulierte Fallzahl vor 21&nbsp;Tagen subtrahieren um die aktiven Fällen zu bekommen.

Eine alternative Betrachtung ist es zu argumentieren, dass **man es vermeiden will, in den täglichen Zuwachs zu geraten**. Am informativsten dafür ist der tägliche Zuwachs pro 100.000 EinwohnerInnen. Da die Inkubationszeit der Coronavirus-Infektion im Schnitt fünf Tage beträgt, und da es noch weitere Tage braucht getestet zu werden und die Daten zu melden, entspricht der heutige Zuwachs Infektionen von vor mindestens einer Woche oder mehr.

### Datenquelle

Die Daten werden täglich durch das [Ministerium für Soziales und Integration Baden-Württemberg](https://sozialministerium.baden-wuerttemberg.de/de/gesundheit-pflege/gesundheitsschutz/infektionsschutz-hygiene/informationen-zu-coronavirus/lage-in-baden-wuerttemberg/) in einer [XLSX-Datei](https://sozialministerium.baden-wuerttemberg.de/fileadmin/redaktion/m-sm/intern/downloads/Downloads_Gesundheitsschutz/Tabelle_Coronavirus-Faelle-BW.xlsx) veröffentlicht.

Die zu den relativen Fallzahlen verwendeten Bevölkerungsgrößen und die Bevölkerungsdichten stammen vom [Statistischen Landesamt Baden-Württemberg](https://www.statistikportal.de/de/bevoelkerung/flaeche-und-bevoelkerung). Die Datei ist [hier erreichbar](https://www.statistik-bw.de/BevoelkGebiet/Bevoelk_I_Flaeche_j.csv).

### Programmdateien

* **download_BW.py** ist das Skript um die Daten vom [Ministerium für Soziales und Integration Baden-Württemberg](https://sozialministerium.baden-wuerttemberg.de/de/gesundheit-pflege/gesundheitsschutz/infektionsschutz-hygiene/informationen-zu-coronavirus/lage-in-baden-wuerttemberg/) herunterzuladen.

* **BW.py** ist das für Baden-Württemberg spezifische Skript, das hauptsächlich für die Vorbereitung der Daten zuständig ist. Es enthält auch die Visualisation.

* **utils.py** hat die gemeinsamen Funktionen, die die Analyse durchführen.

### Schaubilder für das gesamte Land Baden-Württemberg

Die Schaubilder zeigen die Coronavirus-Fälle, bzw. die Todesfälle für alle Landkreise (blaue Punkte) und für das gesamte Land Baden-Württemberg (gelb-schwarzer Punkt). Meine Heimatstadt Freiburg im Breisgau zeichnete ich mit Verweis auf unser Wappen mit rotem Kreuz.

Für die andere Achse hatte ich die Bevölkerungsdichte des Landkreises gewählt. Ich hatte vermutet, je dichter ein Kreis besiedelt ist, desto höhere Fallzahlen ich finden werde. Meine Vermutung war total falsch!

So war der Korrelationskoeffizient zwischen Bevölkerungsdichte (Einwohner/km²) und Fallzahl auf 100.000 Einwohner  
am 22.10.2021  0,100,  
am 16.07.2021  0,043,  
am 04.06.2021  0,035,  
am 25.04.2021  0,058,  
am 16.04.2021  0,069,  
am 03.04.2021  0,082,  
am 09.03.2021  0,155,  
am 16.02.2021  0,166,  
am 29.01.2021  0,190,  
am 23.01.2021  0,194,  
am 16.01.2021  0,200,  
am 04.01.2021  0,237,  
am 19.12.2020  0,305,  
am 24.11.2020  0,357,  
am 13.11.2020  0,296,  
am 06.11.2020  0,245,  
am 08.10.2020 -0,108,  
am 09.09.2020 -0,233,  
am 26.08.2020 -0,288,  
am 04.08.2020 -0,330,  
am 29.07.2020 -0,333,  
am 23.07.2020 -0,332,  
am 03.07.2020 -0,338,  
am 19.06.2020 -0,345,  
am 12.06.2020 -0,349,  
am 05.06.2020 -0,354,  
am 29.05.2020 -0,356,  
am 23.05.2020 -0,359,  
am 19.05.2020 -0,362,  
am 15.05.2020 -0,363,  
am 11.05.2020 -0,363,  
am 07.05.2020 -0,361,  
am 03.05.2020 -0,359,  
am 14.04.2020 -0,275,  
während zwischen Bevölkerungsdichte (Einwohner/km²) und Todesfälle auf 100.000 Einwohner  
am 22.10.2021 -0,232,  
am 16.07.2021 -0,246,  
am 04.06.2021 -0,287,  
am 25.04.2021 -0,269,  
am 16.04.2021 -0,269,  
am 03.04.2021 -0,246,  
am 09.03.2021 -0,233,  
am 16.02.2021 -0,258,  
am 29.01.2021 -0,308,  
am 23.01.2021 -0,302,  
am 16.01.2021 -0,304,  
am 04.01.2021 -0,321,  
am 19.12.2020 -0,316,  
am 24.11.2020 -0,324,  
am 13.11.2020 -0,347,  
am 06.11.2020 -0,336,  
am 08.10.2020 -0,360,  
am 09.09.2020 -0,354,  
am 26.08.2020 -0,356,  
am 04.08.2020 -0,353,  
am 29.07.2020 -0,351,  
am 23.07.2020 -0,353,  
am 03.07.2020 -0,351,  
am 19.06.2020 -0,353,  
am 12.06.2020 -0,346,  
am 05.06.2020 -0,348,  
am 29.05.2020 -0,349,  
am 23.05.2020 -0,343,  
am 19.05.2020 -0,343,  
am 15.05.2020 -0,335,  
am 11.05.2020 -0,321,  
am 07.05.2020 -0,316,  
am 03.05.2020 -0,306,  
am 14.04.2020 -0,262.

Viele Landkreise markierte ich mit dem zu ihnen gehörenden Kfz-Kennzeichen. Wo zwei Landkreise das gleiche Kennzeichen haben (wie Freiburg im Breisgaus und Breisgau-Hochschwarzwald _FR_ oder Heidelberg und Rhein-Neckar-Kreis _HD_) kennzeichnete ich den ländlichen Kreis mit Sternchen.

Es ist zu beachten, dass es auch in einem Bundesland Unterschiede geben kann, wieviele Tests in den einzelnen Landkreisen durchgeführt werden. Wenn man zu wenig Tests durchführt, dann detektiert man automatisch auch wenigere Neuinfektionen. Ein Infekt oder ein Todesfall wird dem Wohnort zugeordnet auch wenn der Patient zum Beispiel in einem ländlichen Kreis wohnt aber in einer großstädtischen Universitätsklinik behandelt wird.

![Baden-Württemberg, Populationsdichte abgebildet auf Coronavirus-Fallzahlen](https://github.com/Melykuti/COVID-19/blob/master/plots/BW_population_density_scatter_confirmed_2021-10-22.png)

![Baden-Württemberg, Populationsdichte abgebildet auf Coronavirus-Todesfälle](https://github.com/Melykuti/COVID-19/blob/master/plots/BW_population_density_scatter_deaths_2021-10-22.png)

### Resultate

Diese Resultate sind die direkte numerische Folge der linearen Anpassungen.

**Ich mache eine grobe Schätzung, wie hoch die wahre kumulierte Fallzahl zur Zeit sein kann.** Meine Annahme ist es, dass die gemeldeten Zahlen nur diejenigen zeigen, die schon getestet worden sind. Aber die Inkubationszeit der COVID-19 Krankheit beträgt im Schnitt fünf Tage (von 1 Tag bis 14 Tage), deshalb werden sich die heute infizierten erst in ungefähr fünf Tagen melden und testen lassen, sogar später. Aber sie sind bereits unumkehrbar infiziert.

Die Spalten haben die folgende Bedeutung:

* Die Gesamtanzahl der Infekten wächst täglich um diese Zahl. Sie wird aus der Annäherung errechnet und nicht direkt aus dem Zuwachs zwischen den letzten beiden Tagen.

* Die Gesamtanzahl der Infekten pro 100.000 Einwohner wächst täglich um diese Zahl. Sie wird aus der Annäherung errechnet und nicht direkt aus dem Zuwachs zwischen den letzten beiden Tagen. (Der in Deutschland häufig verwendete _7-Tage-Inzidenzwert_ ist im Prinzip der siebenfache dieser Zahl. Während die 7-Tage-Inzidenz eine Summe über die letzten sieben Tage ist, rechne ich von einer Annäherung über 7 bis 14 Tagen den Trend aus und melde den Wert für den letzten Tag. Mein Indikator reagiert schneller auf schnell wachsende oder fallende Fallzahlen.)

* Die Gesamtanzahl der Infekten wächst täglich um diesen Faktor (prozentual ausgedrückt)

* Die Zeitdauer bis die Anzahl der Infekten sich verdoppelt. Seit 04.05.2020 wird sie anders berechnet: das Wachstum kann so langsam sein, dass laut Extrapolation es nicht mehr zu einer Verdoppelung kommen wird. In diesem Fall melde ich `inf` (unendlich).

* Die letzte gemeldete Anzahl der Fälle.

* Die letzte gemeldete Anzahl der Coronavirus-Fälle pro 100.000 Einwohner.

* Meine Schätzung der derzeitigen Fallzahl (auf 100.000 Einwohner). Konkret, die Extrapolation der angepassten exponentiellen oder linearen Kurve auf 4, beziehungsweise, 6 Tage voraus. (Bis 23.04.2020 zeigte ich die Schätzung wenn R^2 nicht kleiner als 0,95 und die `Diff.` Spalte nicht größer als 0,5 ist, oder wenn die `Diff.` Spalte in [-0,2;&nbsp; 0,1] ist. Ab 04.05.2020 zeige ich die Schätzung wenn R^2 nicht kleiner als 0,75 und die vorvorletzte Spalte nicht größer als 0,5 ist, oder wenn die vorvorletzte Spalte in [-0,3;&nbsp; 0,3] ist.) Für Todesfälle mache ich diese Extrapolation nicht.

* R^2 oder Bestimmtheitsmaß oder Determinationskoeffizient der Anpassungsgüte der linearen Regression. Je näher es an 1 ist, desto besser ist die Anpassung.

* Normalisierte Differenz zwischen Zuwachs im ausgewählten Zeitfenster aus der Annäherung und in den Daten. (Bis 23.04.2020 war es die Differenz der linearen Annäherung und der wahren Beobachtung in logarithmischem Raum für den letzten Datenpunkt (für den letzten Tag). Man konnte es als Exponent einer Potenz auf Basis 2 interpretieren für die Quote zwischen Schätzung und der letzten Beobachtung. Wenn diese Nummer groß ist, dann ist die Annäherung wenig gut. Wenn sie sogar negativ ist, dann ist die Annäherung viel zu niedrig und die Anzahl der Fälle wird unterschätzt.)

* Die Anzahl der Tage im Zeitfenster, in dem die lineare Regression stattfindet. Sie wird automatisch optimiert, so dass der Vektor (10 * (1-R^2), normalisierte Differenz) in l_2 kleinstmöglich ist.)

* e wenn das exponentielle Modell, l wenn das lineare Modell die bessere Annäherung gab und die Zahlen in der dazugehörenden Reihe der Tabelle lieferte. Man darf dem Vorzug des exponentiellen Modells vor dem linearen nicht allzu viel Bedeutung beimessen wenn beides im Zeitfenster sehr genau ist.

[Direkt zu den Todesfällen.](#todesfaelle)

&nbsp;
#### Infizierte

    Landkreis                Zu- Zuwachs Wachst.- Verdoppl.  Gesamte   pro     Schätzung   R^2  Diff. Fenster Exp/Lin
                           wachs   pro    rate      zeit      Fälle  100.000                          größe
                                 100.000

Stand 22.10.2021

    Alb-Donau-Kreis             68   35   1,6%    42,7 Tage   10556   5384   [5557, 5669] 0,36 -0,05   7  l
    Baden-Baden (Stadtkreis     24   44   1,9%    36,4 Tage    2772   5029   [5245, 5385] 0,48 -0,04   7  l
    Biberach                    97   49   5,5%    13,0 Tage   10897   5456   [5800, 6166] 0,63 -0,16   7  e
    Böblingen                  109   28   1,5%    46,5 Tage   20844   5322   [5464, 5557] 0,20  0,01   7  l
    Bodenseekreis               83   38   1,8%    38,3 Tage    9924   4590   [4777, 4896] 0,28 -0,01   7  l
    Breisgau-Hochschwarzwal     51   19   3,7%    19,1 Tage   10454   3978   [4095, 4199] 0,29 -0,17   7  e
    Calw                        20   13   0,2%     inf Tage    9748   6154   [6198, 6216] 0,08  0,04  12  l
    Emmendingen                 40   24   1,5%    47,8 Tage    7590   4589   [4711, 4790] 0,48 -0,03   7  l
    Enzkreis                    77   39   4,4%    16,0 Tage   11590   5827   [6075, 6309] 0,57 -0,16   7  e
    Esslingen                  135   25   1,3%    55,5 Tage   31398   5881   [6006, 6085] 0,38 -0,03   7  l
    Freiburg im Breisgau (S     63   27   1,3%    52,5 Tage    9662   4196   [4321, 4396] 0,50 -0,06  13  l
    Freudenstadt                28   24   0,9%    77,8 Tage    6524   5532   [5637, 5697] 0,25 -0,03  14  l
    Göppingen                   73   28   1,3%    55,7 Tage   15734   6116   [6253, 6339] 0,38  0,01   7  l
    Heidelberg (Stadtkreis)     27   17   1,3%    54,6 Tage    6132   3824   [3906, 3958] 0,76 -0,10   8  l
    Heidenheim                  63   47   1,4%    48,3 Tage    7796   5885   [6099, 6224] 0,38 -0,05  14  l
    Heilbronn                  103   30   1,1%    65,8 Tage   19954   5816   [5951, 6028] 0,33 -0,06  13  l
    Heilbronn (Stadtkreis)      50   39   1,3%    55,2 Tage   10720   8511   [8702, 8822] 0,50 -0,06   8  l
    Hohenlohekreis              32   29   1,4%    49,7 Tage    6708   5989   [6133, 6227] 0,63 -0,04   7  l
    Karlsruhe                  129   29   1,1%    64,3 Tage   23232   5230   [5359, 5434] 0,29 -0,06  13  l
    Karlsruhe (Stadtkreis)      69   22   1,0%    69,2 Tage   13373   4271   [4369, 4424] 0,27 -0,06  13  l
    Konstanz                    66   23   1,4%    48,5 Tage   13707   4804   [4922, 5000] 0,55 -0,06   7  l
    Lörrach                     54   24   1,3%    53,3 Tage   11826   5172   [5289, 5364] 0,17 -0,06   8  l
    Ludwigsburg                168   31   4,4%    16,3 Tage   32188   5917   [6123, 6325] 0,57 -0,15   7  e
    Main-Tauber-Kreis           20   15   1,2%    57,4 Tage    6168   4661   [4741, 4795] 0,67 -0,07   7  l
    Mannheim (Stadtkreis)       65   21   0,7%   105,8 Tage   20208   6532   [6622, 6671] 0,30 -0,02  14  l
    Neckar-Odenwald-Kreis       23   16   0,8%    92,0 Tage    7443   5185   [5256, 5297] 0,23 -0,06  13  l
    Ortenaukreis               107   25   1,3%    54,5 Tage   23375   5443   [5565, 5642] 0,35 -0,04   7  l
    Ostalbkreis                 97   31   1,4%    50,0 Tage   18368   5850   [6000, 6097] 0,35 -0,03   7  l
    Pforzheim (Stadtkreis)      65   52   3,9%    18,0 Tage   10008   7972   [8282, 8551] 0,45 -0,15   7  e
    Rastatt                     59   25   1,3%    52,7 Tage   12091   5234   [5358, 5437] 0,31 -0,05   7  l
    Ravensburg                  80   28   1,6%    44,1 Tage   13482   4742   [4884, 4976] 0,65 -0,05   7  l
    Rems-Murr-Kreis            135   32   4,0%    17,8 Tage   25028   5873   [6070, 6249] 0,23 -0,21   7  e
    Reutlingen                 113   39   1,6%    43,3 Tage   16804   5860   [6053, 6176] 0,31 -0,02   7  l
    Rhein-Neckar-Kreis         103   19   1,1%    66,2 Tage   27231   4973   [5061, 5116] 0,34 -0,01   7  l
    Rottweil                    25   18   0,7%   104,8 Tage    9410   6748   [6827, 6871] 0,29 -0,03  14  l
    Schwäbisch Hall             38   20   1,1%    64,8 Tage   12768   6519   [6617, 6681] 0,46 -0,03   7  l
    Schwarzwald-Baar-Kreis      62   29   1,0%    73,0 Tage   12717   5988   [6115, 6188] 0,15 -0,07  13  l
    Sigmaringen                 74   56   2,1%    33,4 Tage    7254   5543   [5821, 6000] 0,35 -0,02   7  l
    Stuttgart                  218   34   1,6%    43,2 Tage   37287   5874   [6048, 6164] 0,71 -0,11   7  l
    Tübingen                    47   21   5,0%    14,2 Tage   11384   5008                0,24 -0,32   7  e
    Tuttlingen                  49   35   1,3%    54,6 Tage    9106   6497   [6661, 6761] 0,55 -0,08  12  l
    Ulm (Stadtkreis)            52   41   3,3%    21,3 Tage    7290   5771   [5991, 6158] 0,36 -0,21  13  e
    Waldshut                    24   14   3,5%    20,4 Tage    8789   5151   [5241, 5324] 0,66 -0,15   7  e
    Zollernalbkreis             31   16   1,9%    36,8 Tage   11100   5875   [5954, 6007] 0,08 -0,25   8  e
    
    Baden-Württemberg         3124   28   1,4%    51,4 Tage  610640   5516   [5654, 5741] 0,44 -0,03   7  l


Stand 16.07.2021

    Alb-Donau-Kreis           0,00  0,0   0,0%     inf Tage    8859   4519                0,51  0,11  10  l
    Baden-Baden (Stadtkreis   0,40  0,7   0,0%     inf Tage    2113   3833   [3835, 3835] 0,13  0,27  14  l
    Biberach                  0,75  0,4   0,2%   399,0 Tage    8830   4421   [4423, 4424] 0,19 -0,14   7  l
    Böblingen                  7,3  1,9   0,3%   245,5 Tage   17020   4346   [4354, 4359] 0,36 -0,04  13  l
    Bodenseekreis              1,2  0,6   0,0%     inf Tage    7814   3614   [3615, 3615] 0,19  0,12  11  l
    Breisgau-Hochschwarzwal    5,5  2,1   0,5%   132,6 Tage    8582   3266   [3277, 3284] 0,64 -0,10   7  l
    Calw                       3,5  2,2   0,3%   206,2 Tage    8301   5241   [5251, 5258] 0,41 -0,08  13  l
    Emmendingen                4,5  2,7   0,6%   110,9 Tage    6204   3751   [3767, 3778] 0,88 -0,21   7  l
    Enzkreis                   4,0  2,0   0,4%   195,7 Tage    9735   4894   [4904, 4911] 0,30 -0,26  13  l
    Esslingen                  2,4  0,5   0,0%     inf Tage   26375   4940   [4942, 4942] 0,17  0,04  11  l
    Freiburg im Breisgau (S     11  4,8   0,8%    87,8 Tage    7568   3287   [3312, 3329] 0,63 -0,02   7  l
    Freudenstadt              0,86  0,7   0,3%   268,3 Tage    5372   4555   [4559, 4562] 0,33 -0,14   7  l
    Göppingen                   17  6,6   1,3%    55,2 Tage   12956   5036                0,37 -2,64   7  l
    Heidelberg (Stadtkreis)    3,5  2,2   0,3%   218,6 Tage    5172   3225   [3235, 3240] 0,13 -0,10  14  l
    Heidenheim                 7,9  6,0   0,7%   101,5 Tage    6196   4677   [4707, 4727] 0,23 -0,07   8  l
    Heilbronn                  6,0  1,8   0,2%   289,8 Tage   16056   4680   [4688, 4692] 0,06 -0,08  13  l
    Heilbronn (Stadtkreis)     2,6  2,1   0,3%   217,2 Tage    8826   7007   [7018, 7024] 0,34 -0,11   9  l
    Hohenlohekreis             4,1  3,6   0,5%   131,5 Tage    5681   5072   [5091, 5103] 0,53 -0,12   8  l
    Karlsruhe                  9,1  2,1   0,4%   184,1 Tage   18629   4194   [4204, 4210] 0,16 -0,03   7  l
    Karlsruhe (Stadtkreis)      13  4,3   0,5%   142,4 Tage   10882   3476   [3495, 3507] 0,44 -0,08  13  l
    Konstanz                   6,6  2,3   0,5%   143,9 Tage   11542   4045   [4057, 4066] 0,67 -0,12   8  l
    Lörrach                    7,9  3,5   0,5%   138,3 Tage    9963   4358   [4375, 4386] 0,46 -0,09  11  l
    Ludwigsburg                 12  2,2   2,7%    26,1 Tage   26978   4959   [4974, 4989] 0,93 -0,11   7  e
    Main-Tauber-Kreis         0,69  0,5   0,2%   348,9 Tage    5136   3881   [3884, 3886] 0,22 -0,08  12  l
    Mannheim (Stadtkreis)      2,3  0,8   0,0%     inf Tage   16391   5298   [5300, 5300] 0,18  0,07   8  l
    Neckar-Odenwald-Kreis     0,00  0,0   0,0%     inf Tage    6356   4428                0,15  1,25  10  l
    Ortenaukreis               6,7  1,6   2,5%    27,9 Tage   19217   4474   [4485, 4495] 0,41 -0,23   7  e
    Ostalbkreis                3,5  1,1   0,2%   353,6 Tage   15654   4985   [4990, 4993] 0,19 -0,04  13  l
    Pforzheim (Stadtkreis)     1,2  0,9   0,2%   308,8 Tage    7739   6164   [6169, 6172] 0,10 -0,12   8  l
    Rastatt                    5,9  2,6   0,4%   188,9 Tage   10035   4344   [4356, 4363] 0,34 -0,08  13  l
    Ravensburg                 3,3  1,2   0,3%   219,3 Tage   11061   3891                0,24 -0,44  12  l
    Rems-Murr-Kreis            6,1  1,4   0,2%   403,5 Tage   20369   4780   [4786, 4789] 0,12 -0,04  14  l
    Reutlingen                 5,7  2,0   0,3%   248,1 Tage   13765   4800   [4809, 4815] 0,16 -0,08  13  l
    Rhein-Neckar-Kreis         8,5  1,6   0,3%   235,8 Tage   22639   4134   [4141, 4146] 0,51 -0,08  13  l
    Rottweil                   2,9  2,0   0,4%   183,9 Tage    7769   5571   [5582, 5589] 0,53 -0,14   7  l
    Schwäbisch Hall            1,3  0,6   0,2%   321,8 Tage   11498   5870   [5874, 5876] 0,48 -0,12   8  l
    Schwarzwald-Baar-Kreis     3,3  1,6   0,3%   211,5 Tage   10022   4719   [4727, 4732] 0,49 -0,12   8  l
    Sigmaringen               0,50  0,4   0,2%   318,3 Tage    5586   4268                0,17 -0,56   8  l
    Stuttgart                   24  3,9   0,5%   134,1 Tage   29915   4712   [4731, 4744] 0,29 -0,10   7  l
    Tübingen                   2,1  0,9   0,0%     inf Tage    9436   4151   [4153, 4154] 0,15  0,07  10  l
    Tuttlingen                 2,1  1,5   0,4%   195,7 Tage    7699   5493   [5501, 5507] 0,53 -0,25   8  l
    Ulm (Stadtkreis)           5,3  4,2   0,4%   177,7 Tage    5944   4705   [4724, 4735] 0,09 -0,03  14  l
    Waldshut                   2,2  1,3   0,2%   293,3 Tage    7495   4393   [4399, 4402] 0,23 -0,08  13  l
    Zollernalbkreis            1,7  0,9   0,3%   274,8 Tage    9282   4913   [4917, 4920] 0,28 -0,11   9  l

    Baden-Württemberg          260  2,4   3,3%    21,6 Tage  502662   4541   [4559, 4580] 0,69 -0,18   7  e

Stand 04.06.2021

    Alb-Donau-Kreis            5,1  2,6   0,1%     inf Tage    8728   4452   [4455, 4455] 0,39  0,06  10  l
    Baden-Baden (Stadtkreis   0,50  0,9   0,0%     inf Tage    2097   3804   [3804, 3804] 0,44  0,28   8  l
    Biberach                   5,2  2,6   0,1%     inf Tage    8660   4336   [4343, 4345] 0,26 -0,16  10  e
    Böblingen                   17  4,5   0,1%     inf Tage   16819   4295   [4310, 4315] 0,07  0,05  10  l
    Bodenseekreis              1,6  0,8   0,0%     inf Tage    7670   3547   [3548, 3548] 0,32  0,29   9  l
    Breisgau-Hochschwarzwal    4,8  1,8   0,1%     inf Tage    8473   3224   [3226, 3226] 0,23  0,23   9  l
    Calw                       8,9  5,6   0,6%   109,0 Tage    8181   5165   [5194, 5212] 0,45 -0,07   7  l
    Emmendingen                3,0  1,8   0,0%     inf Tage    6142   3714   [3718, 3719] 0,23  0,05  10  l
    Enzkreis                   5,2  2,6   0,1%     inf Tage    9591   4822   [4829, 4832] 0,34 -0,08  10  e
    Esslingen                   14  2,6   0,1%     inf Tage   26035   4877   [4885, 4888] 0,47  0,11  10  e
    Freiburg im Breisgau (S    3,8  1,6   0,1%     inf Tage    7434   3229   [3231, 3231] 0,22  0,13   9  l
    Freudenstadt               8,0  6,7   0,1%     inf Tage    5318   4509   [4530, 4535] 0,10  0,05   9  l
    Göppingen                   12  4,5   0,1%     inf Tage   12564   4884   [4896, 4897] 0,18  0,12   9  l
    Heidelberg (Stadtkreis)    3,5  2,2   0,4%   188,1 Tage    5082   3169   [3179, 3185] 0,22 -0,03   8  l
    Heidenheim                 5,1  3,9   0,1%     inf Tage    6009   4536   [4543, 4543] 0,61  0,10   9  l
    Heilbronn                  7,1  2,1   0,0%     inf Tage   15988   4660   [4664, 4664] 0,17  0,11  10  l
    Heilbronn (Stadtkreis)     6,0  4,7   0,1%     inf Tage    8615   6839   [6848, 6848] 0,21  0,17   9  l
    Hohenlohekreis             4,0  3,6   0,1%     inf Tage    5646   5041   [5048, 5048] 0,32  0,05  10  l
    Karlsruhe                  7,3  1,6   0,0%     inf Tage   18367   4135   [4137, 4137] 0,34  0,05  10  l
    Karlsruhe (Stadtkreis)     7,9  2,5   0,1%     inf Tage   10697   3417   [3425, 3427] 0,21  0,08  10  l
    Konstanz                   6,7  2,4   0,1%     inf Tage   11390   3992   [3997, 3998] 0,26  0,10   9  l
    Lörrach                    5,4  2,4   0,1%     inf Tage    9844   4305   [4312, 4314] 0,47  0,02   9  e
    Ludwigsburg                 25  4,5   0,1%     inf Tage   26551   4881   [4892, 4893] 0,32  0,07  10  l
    Main-Tauber-Kreis          1,8  1,4   0,0%     inf Tage    5070   3832                0,22  0,53   9  l
    Mannheim (Stadtkreis)      5,6  1,8   0,0%     inf Tage   16270   5259   [5262, 5262] 0,27  0,12  10  l
    Neckar-Odenwald-Kreis      6,3  4,4   0,1%     inf Tage    6306   4393   [4408, 4414] 0,06  0,04  10  l
    Ortenaukreis                11  2,5   0,1%     inf Tage   18941   4410   [4417, 4419] 0,33  0,04  10  l
    Ostalbkreis                 15  4,9   0,1%     inf Tage   15416   4910   [4923, 4924] 0,25  0,19   9  l
    Pforzheim (Stadtkreis)     4,0  3,2   0,1%     inf Tage    7590   6046   [6055, 6057] 0,34 -0,05  10  e
    Rastatt                     10  4,4   0,1%     inf Tage    9938   4302   [4313, 4314] 0,22  0,07  10  l
    Ravensburg                  11  3,8   0,1%     inf Tage   10889   3830   [3839, 3839] 0,20  0,18   9  l
    Rems-Murr-Kreis             11  2,6   0,1%     inf Tage   19967   4685   [4689, 4689] 0,38  0,15  10  l
    Reutlingen                 5,4  1,9   0,0%     inf Tage   13551   4726                0,22  0,51   8  l
    Rhein-Neckar-Kreis          12  2,2   0,1%     inf Tage   22349   4081   [4088, 4089] 0,23  0,05  10  l
    Rottweil                   5,7  4,1   0,1%     inf Tage    7637   5476   [5483, 5483] 0,34  0,17  10  l
    Schwäbisch Hall            3,2  1,6   0,0%     inf Tage   11376   5808   [5809, 5809] 0,54  0,21   9  l
    Schwarzwald-Baar-Kreis      11  5,0   0,1%     inf Tage    9830   4628   [4637, 4637] 0,33  0,13   9  l
    Sigmaringen                3,9  3,0   0,1%     inf Tage    5559   4248   [4251, 4251] 0,28  0,27   9  l
    Stuttgart                   39  6,2   0,5%   133,1 Tage   29288   4614   [4642, 4658] 0,53 -0,01   7  l
    Tübingen                   7,0  3,1   0,1%     inf Tage    9313   4097   [4105, 4106] 0,30  0,10  10  l
    Tuttlingen                 6,2  4,4   0,1%     inf Tage    7552   5388   [5401, 5404] 0,42  0,04   9  e
    Ulm (Stadtkreis)           4,4  3,5   0,1%     inf Tage    5806   4596   [4603, 4603] 0,17  0,24  10  l
    Waldshut                   7,5  4,4   1,5%    47,1 Tage    7418   4348   [4369, 4383] 0,38 -0,11   7  e
    Zollernalbkreis            8,3  4,4   0,1%     inf Tage    9189   4864   [4877, 4881] 0,54  0,01  10  e

    Baden-Württemberg          375  3,4   0,1%     inf Tage  495156   4473   [4482, 4482] 0,39  0,05  10  l

Stand 25.04.2021

    Alb-Donau-Kreis             33   17   0,4%     inf Tage    7433   3791   [3833, 3836] 0,18 -0,08   7  l
    Baden-Baden (Stadtkreis    9,6   17   0,5%     inf Tage    1810   3284   [3326, 3327] 0,15 -0,08   7  l
    Biberach                    79   40   1,6%    43,7 Tage    7230   3620   [3795, 3894] 0,13 -0,04  10  l
    Böblingen                  100   25   0,7%     inf Tage   14689   3751   [3839, 3874] 0,03 -0,12   7  l
    Bodenseekreis               75   35   5,2%    13,6 Tage    6609   3057   [3281, 3495] 0,31 -0,28   8  e
    Breisgau-Hochschwarzwal     15  5,8   0,2%     inf Tage    7796   2967   [2987, 2995] 0,12 -0,15  13  e
    Calw                        71   45   4,9%    14,4 Tage    7130   4501                0,16 -0,41   8  e
    Emmendingen                8,9  5,4   0,2%     inf Tage    5652   3418   [3431, 3434] 0,29 -0,18   7  e
    Enzkreis                    75   38   2,0%    34,6 Tage    8228   4137   [4306, 4407] 0,15 -0,08   8  e
    Esslingen                  157   29   0,7%     inf Tage   22539   4222   [4328, 4373] 0,03 -0,08   7  l
    Freiburg im Breisgau (S     36   15   0,8%    92,0 Tage    6668   2896   [2961, 2995] 0,05 -0,04  14  l
    Freudenstadt                74   63   7,3%     9,9 Tage    4600   3900   [4388, 4967] 0,36 -0,28   7  e
    Göppingen                  109   42   2,5%    28,1 Tage   10491   4078   [4276, 4399] 0,24 -0,11   8  e
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage    4720   2943                0,64  0,19   9  l
    Heidenheim                  49   37   2,2%    32,4 Tage    4806   3628   [3795, 3895] 0,05 -0,20   8  e
    Heilbronn                   97   28   0,7%     inf Tage   14005   4082   [4172, 4199] 0,25  0,08  10  l
    Heilbronn (Stadtkreis)      37   29   0,5%     inf Tage    7454   5918   [6014, 6046] 0,14  0,04  12  l
    Hohenlohekreis              57   51   4,4%    16,1 Tage    4698   4194   [4485, 4720] 0,46 -0,16   8  e
    Karlsruhe                   85   19   0,5%     inf Tage   16223   3652   [3722, 3753] 0,05  0,04  13  l
    Karlsruhe (Stadtkreis)      48   15   0,5%     inf Tage    9338   2983   [3036, 3057] 0,12  0,05  13  l
    Konstanz                    98   35   1,7%    40,5 Tage   10306   3612   [3772, 3868] 0,30 -0,05   8  l
    Lörrach                     48   21   3,1%    22,6 Tage    8961   3919   [4034, 4123] 0,32 -0,18   8  e
    Ludwigsburg                117   22   0,5%     inf Tage   22772   4186   [4265, 4300] 0,08 -0,10  13  e
    Main-Tauber-Kreis          9,3  7,0   0,2%     inf Tage    4632   3501   [3523, 3531] 0,22 -0,21  13  e
    Mannheim (Stadtkreis)      114   37   2,3%    31,0 Tage   14560   4706   [4879, 4988] 0,41 -0,09   9  e
    Neckar-Odenwald-Kreis       72   50   8,0%     9,0 Tage    5506   3836                0,47 -0,31   8  e
    Ortenaukreis                84   20   0,5%     inf Tage   16979   3953   [4025, 4055] 0,07  0,02  13  l
    Ostalbkreis                 84   27   0,6%     inf Tage   13042   4153   [4244, 4279] 0,21 -0,09   7  e
    Pforzheim (Stadtkreis)      65   52   2,1%    33,4 Tage    6441   5131   [5387, 5552] 0,62 -0,10   7  l
    Rastatt                     48   21   0,5%     inf Tage    8716   3773   [3843, 3869] 0,14  0,04  13  l
    Ravensburg                  93   33   5,0%    14,1 Tage    9175   3227   [3439, 3639] 0,28 -0,28   8  e
    Rems-Murr-Kreis            166   39   3,2%    21,8 Tage   17224   4042   [4241, 4383] 0,14 -0,25   8  e
    Reutlingen                  99   34   2,8%    25,1 Tage   11947   4166   [4337, 4452] 0,09 -0,24   8  e
    Rhein-Neckar-Kreis         173   32   3,5%    20,2 Tage   20121   3674   [3844, 3972] 0,47 -0,12   8  e
    Rottweil                    38   27   0,6%     inf Tage    6548   4695   [4789, 4825] 0,08  0,05  11  l
    Schwäbisch Hall             59   30   0,6%     inf Tage   10025   5118   [5221, 5260] 0,08  0,02  12  l
    Schwarzwald-Baar-Kreis      96   45   5,3%    13,5 Tage    7947   3742                0,19 -0,32   7  e
    Sigmaringen                 45   34   3,5%    20,2 Tage    4781   3653   [3836, 3972] 0,17 -0,21   8  e
    Stuttgart                  106   17   0,4%     inf Tage   24878   3919   [3968, 3982] 0,38 -0,09   7  e
    Tübingen                    85   38   3,2%    22,1 Tage    8115   3570   [3759, 3889] 0,28 -0,15   8  e
    Tuttlingen                  38   27   0,6%     inf Tage    6322   4511   [4601, 4635] 0,20 -0,04   7  e
    Ulm (Stadtkreis)            22   17   0,5%     inf Tage    4781   3785                0,08 -0,31   7  e
    Waldshut                    19   11   0,3%     inf Tage    6484   3800   [3841, 3859] 0,07 -0,10  12  e
    Zollernalbkreis             86   46   2,0%    35,1 Tage    7310   3869   [4081, 4209] 0,12 -0,09   8  l

    Baden-Württemberg         3345   30   2,1%    33,3 Tage  429692   3882   [4021, 4106] 0,10 -0,16   8  e

Stand 16.04.2021

    Alb-Donau-Kreis             66   34   1,8%    38,2 Tage    7005   3573   [3732, 3831] 0,44 -0,07   8  l
    Baden-Baden (Stadtkreis     14   25   4,8%    14,8 Tage    1688   3062   [3227, 3386] 0,18 -0,18   7  e
    Biberach                    70   35   1,5%    45,3 Tage    6653   3331   [3484, 3571] 0,17 -0,06  13  l
    Böblingen                  122   31   1,4%    48,2 Tage   13712   3501   [3639, 3719] 0,21 -0,04  14  l
    Bodenseekreis               46   21   1,6%    43,1 Tage    6180   2858   [2961, 3024] 0,32 -0,02   7  l
    Breisgau-Hochschwarzwal     37   14   2,2%    32,0 Tage    7561   2877   [2946, 2991] 0,19 -0,03   7  e
    Calw                        53   33   1,9%    36,4 Tage    6652   4200   [4369, 4482] 0,47 -0,05   7  l
    Emmendingen                 28   17   3,0%    23,4 Tage    5429   3283   [3375, 3446] 0,16 -0,12   7  e
    Enzkreis                    74   37   1,6%    43,5 Tage    7645   3844   [4012, 4110] 0,54 -0,05  14  l
    Esslingen                  204   38   3,1%    22,8 Tage   21055   3944   [4136, 4270] 0,38 -0,17  14  e
    Freiburg im Breisgau (S     33   14   2,3%    30,8 Tage    6385   2773   [2843, 2890] 0,36 -0,05   7  e
    Freudenstadt                36   30   1,3%    51,8 Tage    4244   3599   [3732, 3807] 0,15 -0,05  14  l
    Göppingen                  136   53   4,1%    17,2 Tage    9696   3769   [4051, 4263] 0,35 -0,18  13  e
    Heidelberg (Stadtkreis)     26   16   1,4%    48,2 Tage    4569   2849   [2928, 2979] 0,32  0,01   7  l
    Heidenheim                  66   49   4,0%    17,6 Tage    4388   3312   [3571, 3759] 0,26 -0,26  14  e
    Heilbronn                  222   65   5,6%    12,7 Tage   12816   3736   [4132, 4486] 0,46 -0,22  12  e
    Heilbronn (Stadtkreis)      82   65   4,5%    15,9 Tage    7029   5580                0,26 -0,38  13  e
    Hohenlohekreis              75   67   6,1%    11,7 Tage    4634   4137                0,34 -0,35  13  e
    Karlsruhe                  132   30   1,4%    50,5 Tage   15383   3463   [3594, 3668] 0,25 -0,05  14  l
    Karlsruhe (Stadtkreis)      88   28   1,5%    45,6 Tage    8812   2815   [2938, 3009] 0,25 -0,04  14  l
    Konstanz                   107   37   2,2%    31,9 Tage    9667   3388   [3572, 3690] 0,25 -0,09   7  l
    Lörrach                     46   20   2,9%    24,2 Tage    8659   3787                0,17 -0,35  12  e
    Ludwigsburg                220   40   1,7%    42,1 Tage   21354   3925   [4107, 4213] 0,46 -0,05  14  l
    Main-Tauber-Kreis           46   35   1,7%    41,7 Tage    4469   3377   [3534, 3625] 0,41 -0,05  14  l
    Mannheim (Stadtkreis)      125   40   1,9%    36,2 Tage   13770   4451   [4649, 4775] 0,83 -0,09   7  l
    Neckar-Odenwald-Kreis       56   39   4,4%    15,9 Tage    5194   3619   [3849, 4043] 0,37 -0,29  14  e
    Ortenaukreis               154   36   3,3%    21,5 Tage   16150   3760   [3946, 4078] 0,35 -0,20  14  e
    Ostalbkreis                162   51   2,5%    28,0 Tage   12122   3860   [4116, 4280] 0,92 -0,07   7  l
    Pforzheim (Stadtkreis)      46   37   1,7%    40,6 Tage    6077   4841   [5020, 5135] 0,57 -0,05   7  l
    Rastatt                     91   40   4,3%    16,4 Tage    8168   3536                0,28 -0,38  14  e
    Ravensburg                  83   29   4,7%    15,1 Tage    8582   3019   [3200, 3365] 0,23 -0,16   7  e
    Rems-Murr-Kreis            173   41   2,1%    33,7 Tage   16037   3763   [3959, 4083] 0,46 -0,05   7  l
    Reutlingen                  86   30   1,7%    42,2 Tage   11187   3901   [4045, 4135] 0,45 -0,00   7  l
    Rhein-Neckar-Kreis         135   25   2,1%    33,1 Tage   19036   3476   [3590, 3662] 0,32 -0,12  14  e
    Rottweil                    80   57   5,9%    12,2 Tage    6103   4376   [4767, 5162] 0,40 -0,27  12  e
    Schwäbisch Hall            127   65   2,4%    29,8 Tage    9434   4817   [5128, 5323] 0,37  0,02   7  l
    Schwarzwald-Baar-Kreis      72   34   3,6%    19,7 Tage    7384   3477   [3658, 3794] 0,55 -0,17  14  e
    Sigmaringen                 46   35   4,1%    17,1 Tage    4467   3413                0,21 -0,37  12  e
    Stuttgart                  266   42   3,4%    20,6 Tage   23304   3671   [3885, 4036] 0,65 -0,11  12  e
    Tübingen                    77   34   2,1%    33,3 Tage    7533   3314   [3480, 3587] 0,73 -0,05   7  l
    Tuttlingen                  59   42   2,2%    31,6 Tage    5866   4185   [4401, 4542] 0,24 -0,00   7  l
    Ulm (Stadtkreis)            44   35   1,5%    46,4 Tage    4455   3527   [3679, 3766] 0,22 -0,07  14  l
    Waldshut                    21   12   0,3%     inf Tage    6245   3660   [3690, 3691] 0,29  0,05  10  l
    Zollernalbkreis             59   31   3,9%    18,0 Tage    6758   3577   [3754, 3898] 0,43 -0,11   7  e

    Baden-Württemberg         3764   34   1,8%    39,5 Tage  403557   3646   [3805, 3903] 0,45 -0,01   7  l

Stand 03.04.2021

    Alb-Donau-Kreis             43   22   1,3%    52,7 Tage    6467   3299   [3398, 3457] 0,24  0,02   7  l
    Baden-Baden (Stadtkreis     20   36   2,4%    29,2 Tage    1555   2821   [2998, 3112] 0,43 -0,08   7  l
    Biberach                    35   18   0,6%     inf Tage    5974   2991   [3049, 3069] 0,34  0,04  10  l
    Böblingen                  107   27   2,0%    35,6 Tage   12624   3223   [3361, 3451] 0,34 -0,03   7  l
    Bodenseekreis               41   19   1,4%    49,6 Tage    5717   2644   [2731, 2783] 0,23  0,01   7  l
    Breisgau-Hochschwarzwal     24  9,2   0,3%     inf Tage    7146   2719   [2743, 2745] 0,23  0,19   9  l
    Calw                        26   17   3,3%    21,4 Tage    6289   3970   [4067, 4147] 0,24 -0,20   7  e
    Emmendingen                 36   22   2,0%    34,5 Tage    5104   3086   [3187, 3249] 0,19 -0,17  13  e
    Enzkreis                    45   23   1,6%    44,4 Tage    7029   3534   [3645, 3716] 0,13 -0,10   7  l
    Esslingen                  126   24   1,3%    54,5 Tage   19350   3625   [3731, 3794] 0,20  0,01   7  l
    Freiburg im Breisgau (S     16  6,9   0,3%     inf Tage    6046   2626   [2641, 2641] 0,20  0,26   9  l
    Freudenstadt                42   35   2,4%    29,2 Tage    3907   3313   [3497, 3621] 0,45 -0,02   7  l
    Göppingen                   57   22   2,1%    33,7 Tage    8655   3364   [3467, 3531] 0,37 -0,08   7  e
    Heidelberg (Stadtkreis)     24   15   1,2%    60,5 Tage    4349   2712   [2781, 2821] 0,17 -0,01   7  l
    Heidenheim                  35   27   1,8%    38,2 Tage    3826   2888   [3016, 3095] 0,49 -0,05   7  l
    Heilbronn                  116   34   4,0%    17,6 Tage   11417   3328   [3518, 3670] 0,36 -0,22  13  e
    Heilbronn (Stadtkreis)      51   40   1,4%    50,4 Tage    6329   5025   [5205, 5309] 0,28 -0,04  14  l
    Hohenlohekreis              74   66   3,0%    23,3 Tage    4179   3731   [4060, 4273] 0,32  0,04   7  l
    Karlsruhe                  120   27   1,4%    50,7 Tage   14164   3188   [3308, 3377] 0,23 -0,07  13  l
    Karlsruhe (Stadtkreis)      65   21   1,3%    51,9 Tage    8009   2558   [2649, 2702] 0,24 -0,06  13  l
    Konstanz                    76   27   1,7%    41,4 Tage    8774   3075   [3200, 3276] 0,10  0,05   7  l
    Lörrach                     40   17   1,3%    55,4 Tage    8225   3597   [3680, 3732] 0,43  0,01   7  l
    Ludwigsburg                155   28   1,7%    40,8 Tage   19525   3589   [3726, 3813] 0,35  0,03   7  l
    Main-Tauber-Kreis           58   44   2,7%    25,6 Tage    4097   3096   [3321, 3470] 0,46 -0,06   7  l
    Mannheim (Stadtkreis)       48   16   0,4%     inf Tage   12725   4113   [4167, 4188] 0,19 -0,07  11  e
    Neckar-Odenwald-Kreis       43   30   1,7%    41,5 Tage    4789   3336   [3476, 3560] 0,63 -0,08  13  l
    Ortenaukreis               136   32   1,9%    36,1 Tage   14868   3462   [3617, 3715] 0,39 -0,14   7  l
    Ostalbkreis                 88   28   2,3%    31,0 Tage   10878   3464   [3595, 3676] 0,19 -0,17  13  e
    Pforzheim (Stadtkreis)      31   25   1,4%    50,0 Tage    5725   4560   [4680, 4756] 0,22 -0,06   8  l
    Rastatt                    113   49   2,8%    24,9 Tage    7390   3199   [3446, 3607] 0,61 -0,09   7  l
    Ravensburg                  54   19   1,3%    52,8 Tage    7830   2754   [2841, 2891] 0,11  0,03   7  l
    Rems-Murr-Kreis            123   29   1,6%    43,0 Tage   14629   3433   [3567, 3649] 0,19  0,03   7  l
    Reutlingen                  98   34   2,0%    34,7 Tage   10402   3628   [3796, 3905] 0,78 -0,06   7  l
    Rhein-Neckar-Kreis          94   17   0,5%     inf Tage   17721   3236   [3298, 3323] 0,08  0,04   9  l
    Rottweil                    38   27   1,6%    43,6 Tage    5648   4050   [4184, 4269] 0,28 -0,06   7  l
    Schwäbisch Hall             81   41   1,0%     inf Tage    8269   4222   [4364, 4420] 0,80  0,02  10  e
    Schwarzwald-Baar-Kreis      47   22   1,6%    44,1 Tage    6850   3225   [3332, 3399] 0,35  0,02   7  l
    Sigmaringen                 63   48   2,8%    25,3 Tage    4078   3116   [3356, 3512] 0,14  0,02   7  l
    Stuttgart                  133   21   1,4%    49,6 Tage   21241   3346   [3445, 3505] 0,45 -0,05   7  l
    Tübingen                    59   26   1,5%    46,9 Tage    6932   3049   [3167, 3236] 0,72 -0,06  13  l
    Tuttlingen                  29   21   0,9%    73,5 Tage    5432   3876   [3966, 4016] 0,11 -0,07  12  l
    Ulm (Stadtkreis)            28   22   2,2%    31,7 Tage    4049   3205   [3308, 3374] 0,15 -0,24  13  e
    Waldshut                    38   22   3,0%    23,8 Tage    5826   3415   [3530, 3614] 0,19 -0,22   8  e
    Zollernalbkreis             51   27   2,5%    27,6 Tage    6267   3317   [3448, 3533] 0,21 -0,17  13  e

    Baden-Württemberg         2854   26   1,5%    46,2 Tage  370306   3345   [3465, 3536] 0,40 -0,00   7  l


Stand 09.03.2021

    Alb-Donau-Kreis             14  6,9   0,2%     inf Tage    5691   2903   [2925, 2932] 0,23 -0,06   8  e
    Baden-Baden (Stadtkreis    1,9  3,4   0,1%     inf Tage    1299   2357   [2362, 2362] 0,17  0,17   7  l
    Biberach                    12  6,1   0,2%     inf Tage    5116   2561   [2570, 2570] 0,38  0,15   7  l
    Böblingen                  9,1  2,3   0,1%     inf Tage   11501   2937   [2943, 2945] 0,17 -0,18   8  e
    Bodenseekreis              6,2  2,9   0,1%     inf Tage    5052   2336   [2338, 2338] 0,45  0,20   8  l
    Breisgau-Hochschwarzwal     36   14   3,2%    22,2 Tage    6386   2430   [2506, 2564] 0,29 -0,25  10  e
    Calw                        18   12   0,7%    94,0 Tage    5814   3671   [3722, 3751] 0,11 -0,03  13  l
    Emmendingen                 39   24   5,2%    13,6 Tage    4407   2665                0,37 -0,31  10  e
    Enzkreis                   6,9  3,5   0,1%     inf Tage    6484   3260   [3271, 3275] 0,23 -0,06   7  e
    Esslingen                   38  7,2   0,2%     inf Tage   17018   3188   [3209, 3213] 0,21  0,11   7  l
    Freiburg im Breisgau (S    6,6  2,9   0,1%     inf Tage    5500   2389   [2391, 2391] 0,53  0,17   7  l
    Freudenstadt                16   13   1,2%    58,1 Tage    3407   2889   [2952, 2991] 0,29 -0,06  10  l
    Göppingen                   36   14   1,1%    60,9 Tage    7526   2926   [2991, 3030] 0,28 -0,06  10  l
    Heidelberg (Stadtkreis)    6,8  4,2   0,2%     inf Tage    3937   2455   [2465, 2465] 0,15 -0,03   7  l
    Heidenheim                 4,2  3,1   0,1%     inf Tage    3383   2554   [2558, 2558] 0,35  0,26   8  l
    Heilbronn                   11  3,3   0,1%     inf Tage   10026   2922   [2932, 2935] 0,21 -0,08   8  e
    Heilbronn (Stadtkreis)     3,7  2,9   0,1%     inf Tage    5746   4562   [4570, 4572] 0,13  0,13  14  l
    Hohenlohekreis             6,9  6,2   0,2%     inf Tage    3289   2936   [2943, 2943] 0,34  0,11   7  l
    Karlsruhe                   17  3,8   0,1%     inf Tage   12282   2765                0,10 -0,33   8  e
    Karlsruhe (Stadtkreis)      46   15   1,3%    53,1 Tage    6874   2196   [2262, 2301] 0,15 -0,08  10  l
    Konstanz                    27  9,3   0,4%     inf Tage    7399   2593   [2622, 2632] 0,28  0,01   7  e
    Lörrach                     13  5,6   0,2%     inf Tage    7516   3287   [3298, 3298] 0,32  0,16   7  l
    Ludwigsburg                 25  4,6   0,1%     inf Tage   17423   3203   [3212, 3212] 0,34  0,16   7  l
    Main-Tauber-Kreis          6,2  4,7   0,2%     inf Tage    3330   2517   [2523, 2523] 0,24  0,21   7  l
    Mannheim (Stadtkreis)       25  8,1   0,2%     inf Tage   11124   3596   [3622, 3631] 0,17 -0,09   8  e
    Neckar-Odenwald-Kreis      4,0  2,8   0,1%     inf Tage    4370   3045   [3047, 3047] 0,36  0,05   7  l
    Ortenaukreis                23  5,3   0,2%     inf Tage   13038   3036   [3054, 3060] 0,08  0,08   8  l
    Ostalbkreis                 14  4,4   0,1%     inf Tage    9503   3026   [3040, 3045] 0,17  0,14   8  l
    Pforzheim (Stadtkreis)     2,5  2,0   0,0%     inf Tage    5328   4244   [4246, 4246] 0,49  0,29   7  l
    Rastatt                     16  6,8   0,3%     inf Tage    5902   2555   [2576, 2582] 0,15 -0,14   8  e
    Ravensburg                  10  3,5   0,1%     inf Tage    6902   2428   [2438, 2441] 0,21 -0,05   8  e
    Rems-Murr-Kreis             15  3,6   0,1%     inf Tage   13039   3060   [3065, 3065] 0,38  0,16   7  l
    Reutlingen                  15  5,1   0,2%     inf Tage    9167   3197   [3205, 3205] 0,32  0,08   7  l
    Rhein-Neckar-Kreis          16  2,9   0,1%     inf Tage   15657   2859   [2868, 2871] 0,21 -0,04   8  e
    Rottweil                   4,2  3,0   0,1%     inf Tage    5247   3763   [3769, 3771] 0,58 -0,05   8  e
    Schwäbisch Hall             26   13   0,4%     inf Tage    5885   3005   [3043, 3054] 0,39 -0,11   7  e
    Schwarzwald-Baar-Kreis     4,1  2,0   0,1%     inf Tage    6248   2942   [2947, 2949] 0,48 -0,09   7  e
    Sigmaringen                 14   10   0,4%     inf Tage    3182   2431   [2465, 2477] 0,08  0,07   8  l
    Stuttgart                   70   11   0,7%   101,8 Tage   19206   3025   [3072, 3098] 0,13 -0,02  12  l
    Tübingen                   7,8  3,4   0,1%     inf Tage    6229   2740   [2752, 2757] 0,19  0,01  14  l
    Tuttlingen                 5,6  4,0   0,1%     inf Tage    4871   3476   [3479, 3479] 0,61  0,06   7  l
    Ulm (Stadtkreis)           7,3  5,8   0,2%     inf Tage    3638   2880   [2895, 2897] 0,28  0,07   8  l
    Waldshut                   1,5  0,9   0,0%     inf Tage    5144   3015   [3015, 3015] 0,93  0,23   7  l
    Zollernalbkreis            8,0  4,2   0,1%     inf Tage    5598   2963   [2976, 2979] 0,34  0,10  14  l

    Baden-Württemberg          666  6,0   0,2%     inf Tage  325684   2942   [2962, 2968] 0,23 -0,02   7  e

Stand 16.02.2021

    Alb-Donau-Kreis            9,0  4,6   0,2%     inf Tage    5347   2727   [2742, 2746] 0,31 -0,06   8  e
    Baden-Baden (Stadtkreis    1,5  2,7   0,1%     inf Tage    1221   2215   [2219, 2219] 0,49  0,14   8  l
    Biberach                   3,5  1,8   0,1%     inf Tage    4677   2342   [2342, 2342] 0,33  0,29   7  l
    Böblingen                   16  4,2   0,1%     inf Tage   10904   2784   [2796, 2798] 0,16  0,17  13  l
    Bodenseekreis              2,6  1,2   0,1%     inf Tage    4675   2162                0,23  0,34  12  l
    Breisgau-Hochschwarzwal    3,9  1,5   0,1%     inf Tage    5948   2263   [2265, 2265] 0,70  0,17   8  l
    Calw                       1,4  0,9   0,0%     inf Tage    5546   3501                0,63  0,36   7  l
    Emmendingen                1,1  0,7   0,0%     inf Tage    4103   2481                0,65  0,32   7  l
    Enzkreis                   4,5  2,3   0,1%     inf Tage    6244   3139   [3141, 3141] 0,53  0,20   7  l
    Esslingen                   22  4,2   0,1%     inf Tage   16052   3007   [3020, 3024] 0,29  0,05  14  l
    Freiburg im Breisgau (S    4,2  1,8   0,1%     inf Tage    5240   2276   [2278, 2278] 0,51  0,15   8  l
    Freudenstadt               3,8  3,2   0,1%     inf Tage    3253   2758   [2769, 2773] 0,18 -0,11   8  e
    Göppingen                  7,2  2,8   0,1%     inf Tage    7101   2760   [2764, 2764] 0,44  0,10   7  l
    Heidelberg (Stadtkreis)    3,1  1,9   0,1%     inf Tage    3736   2330   [2335, 2335] 0,28  0,06  14  l
    Heidenheim                 2,9  2,2   0,1%     inf Tage    3209   2422   [2425, 2425] 0,32  0,21   7  l
    Heilbronn                  4,2  1,2   0,0%     inf Tage    9504   2770   [2771, 2771] 0,41  0,13  14  l
    Heilbronn (Stadtkreis)     1,5  1,2   0,0%     inf Tage    5588   4436                0,44  0,48   7  l
    Hohenlohekreis             2,6  2,4   0,1%     inf Tage    2985   2665   [2666, 2666] 0,57  0,12   7  l
    Karlsruhe                   14  3,2   0,1%     inf Tage   11345   2554   [2563, 2565] 0,19 -0,18   8  e
    Karlsruhe (Stadtkreis)     7,5  2,4   0,1%     inf Tage    6289   2009   [2011, 2011] 0,48  0,08   8  l
    Konstanz                    15  5,2   0,2%     inf Tage    6602   2314   [2328, 2329] 0,32  0,13   9  l
    Lörrach                    3,3  1,4   0,0%     inf Tage    7158   3131   [3131, 3131] 0,83  0,15   7  l
    Ludwigsburg                 11  2,0   0,1%     inf Tage   16647   3060   [3062, 3062] 0,45  0,09   8  l
    Main-Tauber-Kreis         0,54  0,4   0,0%     inf Tage    3099   2342   [2342, 2342] 0,95  0,15   7  l
    Mannheim (Stadtkreis)      9,1  2,9   0,1%     inf Tage   10414   3366   [3369, 3369] 0,77  0,17   8  l
    Neckar-Odenwald-Kreis      2,2  1,5   0,1%     inf Tage    4187   2917   [2918, 2918] 0,80  0,11   8  l
    Ortenaukreis               7,6  1,8   0,1%     inf Tage   12505   2912   [2913, 2913] 0,61  0,12  14  l
    Ostalbkreis                7,1  2,3   0,1%     inf Tage    9212   2934   [2936, 2936] 0,62  0,16   7  l
    Pforzheim (Stadtkreis)     2,3  1,8   0,0%     inf Tage    5164   4113   [4115, 4115] 0,56  0,06  11  l
    Rastatt                    5,3  2,3   0,1%     inf Tage    5385   2331   [2337, 2338] 0,25 -0,19   8  e
    Ravensburg                 8,2  2,9   0,1%     inf Tage    6527   2296   [2305, 2309] 0,21 -0,14  14  e
    Rems-Murr-Kreis             10  2,4   0,1%     inf Tage   12493   2932   [2935, 2935] 0,45  0,07   8  l
    Reutlingen                 7,9  2,7   0,1%     inf Tage    8702   3035   [3041, 3042] 0,23  0,11   7  l
    Rhein-Neckar-Kreis          27  4,9   0,2%     inf Tage   14878   2717   [2727, 2727] 0,49  0,10   8  l
    Rottweil                   3,8  2,7   0,1%     inf Tage    4881   3500   [3502, 3502] 0,31 -0,04   7  l
    Schwäbisch Hall             16  8,3   0,3%     inf Tage    5005   2555   [2567, 2567] 0,56  0,07   7  l
    Schwarzwald-Baar-Kreis     2,2  1,0   0,0%     inf Tage    6033   2841   [2841, 2841] 0,72  0,17   7  l
    Sigmaringen               0,59  0,5   0,0%     inf Tage    2913   2226   [2226, 2226] 0,42  0,21  13  l
    Stuttgart                   17  2,7   0,1%     inf Tage   18151   2859   [2864, 2864] 0,43  0,14   8  l
    Tübingen                    13  5,6   0,7%   103,8 Tage    5993   2636   [2662, 2677] 0,28 -0,09  10  l
    Tuttlingen                 2,8  2,0   0,1%     inf Tage    4611   3290   [3295, 3295] 0,57 -0,15   7  e
    Ulm (Stadtkreis)           3,3  2,6   0,1%     inf Tage    3420   2707   [2714, 2716] 0,24 -0,19   8  e
    Waldshut                   3,5  2,1   0,1%     inf Tage    4824   2827   [2829, 2829] 0,61  0,12  14  l
    Zollernalbkreis             19  9,9   0,7%    94,3 Tage    5319   2815   [2858, 2882] 0,05 -0,06   9  l
    
    Baden-Württemberg          414  3,7   0,1%     inf Tage  307090   2774   [2782, 2782] 0,56  0,05   8  l

Stand 29.01.2021

    Alb-Donau-Kreis             44   22   1,8%    39,3 Tage    5014   2558   [2664, 2731] 0,25  0,06   7  l
    Baden-Baden (Stadtkreis    3,2  5,8   1,2%    60,5 Tage    1172   2126   [2157, 2178] 0,69 -0,06   7  l
    Biberach                    26   13   2,7%    26,3 Tage    4315   2160   [2227, 2274] 0,12 -0,08   7  e
    Böblingen                   52   13   0,8%    86,2 Tage   10427   2662   [2718, 2749] 0,04 -0,06  13  l
    Bodenseekreis               45   21   2,2%    32,2 Tage    4386   2028   [2133, 2200] 0,55 -0,14   7  l
    Breisgau-Hochschwarzwal     37   14   1,6%    42,4 Tage    5655   2152   [2222, 2268] 0,40 -0,14   7  l
    Calw                        24   15   3,9%    18,3 Tage    5202   3284   [3380, 3468] 0,18 -0,19   7  e
    Emmendingen                 12  7,3   0,9%    73,7 Tage    3992   2414   [2448, 2470] 0,22  0,01   7  l
    Enzkreis                    13  6,8   0,2%     inf Tage    6015   3024   [3040, 3041] 0,24  0,15  11  l
    Esslingen                   82   15   2,1%    33,5 Tage   15326   2871   [2944, 2991] 0,28 -0,06   7  e
    Freiburg im Breisgau (S     14  6,2   0,3%     inf Tage    5014   2178   [2196, 2201] 0,19  0,07  10  l
    Freudenstadt               7,2  6,1   0,2%     inf Tage    3159   2679   [2696, 2698] 0,24  0,12  11  l
    Göppingen                   14  5,6   0,2%     inf Tage    6835   2657   [2672, 2675] 0,41  0,07  10  l
    Heidelberg (Stadtkreis)    9,2  5,7   0,3%     inf Tage    3610   2251   [2273, 2282] 0,03 -0,10  14  e
    Heidenheim                  12  8,9   1,7%    42,3 Tage    3107   2345   [2386, 2412] 0,10 -0,19   9  e
    Heilbronn                   66   19   1,8%    38,2 Tage    9020   2629   [2727, 2791] 0,62 -0,03   7  l
    Heilbronn (Stadtkreis)      51   41   2,1%    33,3 Tage    5299   4207   [4411, 4544] 0,39  0,01   7  l
    Hohenlohekreis             6,8  6,1   3,7%    19,1 Tage    2688   2400   [2441, 2481] 0,28 -0,22   7  e
    Karlsruhe                   69   15   1,4%    50,2 Tage   10611   2389   [2461, 2504] 0,27  0,01   7  l
    Karlsruhe (Stadtkreis)      35   11   3,4%    20,7 Tage    5937   1896   [1960, 2010] 0,17 -0,15   7  e
    Konstanz                    39   14   1,1%    60,9 Tage    6184   2167   [2228, 2263] 0,05 -0,03   8  l
    Lörrach                     19  8,4   0,3%     inf Tage    6813   2980   [3009, 3020] 0,19  0,01  10  e
    Ludwigsburg                 82   15   3,8%    18,4 Tage   16088   2957   [3050, 3133] 0,21 -0,13   7  e
    Main-Tauber-Kreis          5,4  4,1   0,2%     inf Tage    2922   2208   [2212, 2212] 0,51  0,14  11  l
    Mannheim (Stadtkreis)       29  9,4   0,3%     inf Tage    9946   3215   [3243, 3249] 0,42  0,09  11  l
    Neckar-Odenwald-Kreis       11  7,6   0,3%     inf Tage    3969   2765   [2776, 2776] 0,30  0,15  10  l
    Ortenaukreis               103   24   1,5%    45,2 Tage   11600   2701   [2809, 2873] 0,31  0,01   7  l
    Ostalbkreis                 53   17   1,4%    49,3 Tage    8849   2818   [2899, 2950] 0,29 -0,00   7  l
    Pforzheim (Stadtkreis)      29   23   2,9%    24,3 Tage    4940   3935   [4056, 4145] 0,34 -0,11   7  e
    Rastatt                     23  9,8   1,2%    57,8 Tage    5122   2217   [2264, 2294] 0,22  0,10   7  l
    Ravensburg                  28   10   0,5%     inf Tage    6116   2151   [2177, 2180] 0,31  0,06  11  l
    Rems-Murr-Kreis             22  5,1   0,2%     inf Tage   12086   2836   [2847, 2847] 0,47  0,04  11  l
    Reutlingen                  24  8,5   0,3%     inf Tage    8426   2938   [2965, 2973] 0,14  0,11  14  l
    Rhein-Neckar-Kreis          81   15   1,1%    64,6 Tage   14004   2557   [2623, 2660] 0,15 -0,04   8  l
    Rottweil                    13  9,5   0,3%     inf Tage    4633   3322   [3345, 3345] 0,15  0,17  10  l
    Schwäbisch Hall             38   19   2,0%    35,0 Tage    4593   2345   [2445, 2511] 0,66 -0,03   7  l
    Schwarzwald-Baar-Kreis      30   14   1,0%    67,2 Tage    5671   2670   [2733, 2769] 0,19 -0,07  13  l
    Sigmaringen                 11  8,5   0,4%     inf Tage    2723   2081   [2107, 2115] 0,11  0,09  10  l
    Stuttgart                   88   14   1,2%    57,5 Tage   17446   2748   [2813, 2852] 0,32  0,01   7  l
    Tübingen                    13  5,8   0,2%     inf Tage    5807   2554   [2573, 2579] 0,22  0,08   7  l
    Tuttlingen                  23   16   0,5%     inf Tage    4348   3102   [3158, 3179] 0,10  0,07  10  l
    Ulm (Stadtkreis)            15   12   1,0%    72,3 Tage    3236   2562   [2615, 2646] 0,16 -0,04   9  l
    Waldshut                    20   12   0,5%     inf Tage    4422   2592   [2629, 2640] 0,23  0,07  10  l
    Zollernalbkreis             19  9,8   0,4%     inf Tage    5026   2660   [2692, 2701] 0,14  0,13  10  l
    
    Baden-Württemberg         1559   14   1,1%    63,0 Tage  291754   2636   [2699, 2736] 0,18  0,03   7  l

Stand 23.01.2021

    Alb-Donau-Kreis             42   21   2,8%    24,9 Tage    4796   2446   [2552, 2623] 0,10 -0,11   7  e
    Baden-Baden (Stadtkreis    4,4  8,1   0,4%     inf Tage    1161   2106   [2133, 2142] 0,20  0,02  12  l
    Biberach                    19  9,4   0,5%     inf Tage    4160   2083   [2113, 2123] 0,14  0,11  10  l
    Böblingen                   29  7,3   0,3%     inf Tage   10087   2576   [2596, 2600] 0,18  0,07  10  l
    Bodenseekreis               31   14   0,7%     inf Tage    4189   1937   [1980, 1991] 0,39  0,05  11  l
    Breisgau-Hochschwarzwal     31   12   2,7%    25,6 Tage    5489   2089   [2149, 2192] 0,28 -0,11   7  e
    Calw                        10  6,6   0,2%     inf Tage    5074   3203   [3211, 3211] 0,33  0,05  11  l
    Emmendingen                 16 10,0   0,4%     inf Tage    3932   2378   [2411, 2422] 0,10  0,09  10  l
    Enzkreis                    35   18   1,1%    61,5 Tage    5879   2956   [3034, 3080] 0,07 -0,02   8  l
    Esslingen                   66   12   0,4%     inf Tage   14855   2783   [2822, 2835] 0,20  0,08  10  l
    Freiburg im Breisgau (S     37   16   1,7%    40,7 Tage    4896   2126   [2205, 2255] 0,72 -0,04   7  l
    Freudenstadt               7,7  6,5   0,2%     inf Tage    3085   2616   [2627, 2627] 0,33  0,19  10  l
    Göppingen                   24  9,4   0,4%     inf Tage    6701   2605   [2632, 2638] 0,30  0,11  10  l
    Heidelberg (Stadtkreis)    9,6  6,0   0,3%     inf Tage    3514   2191   [2210, 2217] 0,52  0,05  12  e
    Heidenheim                 7,2  5,4   0,2%     inf Tage    3031   2288   [2298, 2298] 0,26  0,09  11  l
    Heilbronn                   30  8,7   0,3%     inf Tage    8746   2549   [2574, 2578] 0,26  0,05  11  l
    Heilbronn (Stadtkreis)      46   37   1,8%    39,2 Tage    5075   4029   [4203, 4310] 0,25  0,02   7  l
    Hohenlohekreis             6,5  5,8   0,2%     inf Tage    2655   2370   [2386, 2389] 0,21  0,14  11  l
    Karlsruhe                   49   11   0,5%     inf Tage   10250   2307   [2343, 2354] 0,11  0,05  11  l
    Karlsruhe (Stadtkreis)      46   15   1,5%    46,7 Tage    5744   1835   [1901, 1941] 0,09 -0,12   8  l
    Konstanz                    20  7,2   0,3%     inf Tage    5953   2086   [2096, 2096] 0,37  0,26   9  l
    Lörrach                     27   12   0,4%     inf Tage    6628   2899   [2939, 2954] 0,10  0,13  10  l
    Ludwigsburg                120   22   1,8%    39,2 Tage   15682   2883   [2992, 3063] 0,25 -0,12   7  l
    Main-Tauber-Kreis           31   23   1,8%    39,0 Tage    2824   2134   [2240, 2303] 0,08 -0,04   7  l
    Mannheim (Stadtkreis)       52   17   0,5%     inf Tage    9669   3125   [3188, 3215] 0,06  0,02   9  l
    Neckar-Odenwald-Kreis       20   14   0,5%     inf Tage    3828   2667   [2716, 2736] 0,05 -0,23  11  e
    Ortenaukreis               114   26   2,0%    35,1 Tage   11025   2567   [2694, 2774] 0,38 -0,00   7  l
    Ostalbkreis                 94   30   2,3%    30,5 Tage    8582   2733   [2885, 2984] 0,64 -0,09   7  l
    Pforzheim (Stadtkreis)      28   23   0,6%     inf Tage    4786   3812   [3894, 3927] 0,06  0,07  10  l
    Rastatt                     17  7,3   0,3%     inf Tage    5012   2170   [2191, 2195] 0,28  0,02  12  l
    Ravensburg                  54   19   0,9%     inf Tage    5850   2058   [2117, 2135] 0,21  0,05  11  l
    Rems-Murr-Kreis             52   12   0,4%     inf Tage   11842   2779   [2824, 2844] 0,09  0,08  14  l
    Reutlingen                  18  6,4   0,2%     inf Tage    8172   2850   [2856, 2856] 0,34  0,21   7  l
    Rhein-Neckar-Kreis          62   11   0,5%     inf Tage   13522   2469   [2508, 2522] 0,18  0,02  11  l
    Rottweil                    38   27   1,7%    41,4 Tage    4510   3234   [3363, 3442] 0,13 -0,04   7  l
    Schwäbisch Hall             18  9,0   0,4%     inf Tage    4438   2266   [2292, 2297] 0,27  0,03  12  l
    Schwarzwald-Baar-Kreis      13  6,3   0,2%     inf Tage    5512   2595   [2607, 2607] 0,33  0,15  10  l
    Sigmaringen                 23   18   1,7%    40,5 Tage    2632   2011   [2094, 2145] 0,18  0,09   7  l
    Stuttgart                  106   17   2,7%    26,2 Tage   16991   2676   [2761, 2820] 0,67 -0,05   7  e
    Tübingen                   7,4  3,2   0,1%     inf Tage    5689   2503   [2506, 2506] 0,65  0,13  11  l
    Tuttlingen                  43   31   2,1%    33,9 Tage    4174   2978   [3128, 3223] 0,41 -0,05   7  l
    Ulm (Stadtkreis)            15   12   2,8%    25,0 Tage    3148   2492   [2554, 2600] 0,09 -0,24   7  e
    Waldshut                    31   18   2,7%    26,0 Tage    4233   2481   [2572, 2635] 0,14 -0,20   7  e
    Zollernalbkreis             22   12   0,4%     inf Tage    4868   2577   [2615, 2628] 0,17  0,02  12  l
    
    Baden-Württemberg         1424   13   0,5%     inf Tage  282889   2556   [2601, 2619] 0,19  0,02  11  l

Stand 16.01.2021

    Alb-Donau-Kreis             55   28   1,7%    40,9 Tage    4541   2316   [2439, 2509] 0,32 -0,07  14  l
    Baden-Baden (Stadtkreis    7,9   14   1,2%    59,6 Tage    1122   2035   [2098, 2134] 0,05 -0,08   9  l
    Biberach                    28   14   0,7%     inf Tage    4002   2004   [2052, 2070] 0,15  0,04  11  l
    Böblingen                   71   18   4,0%    17,6 Tage    9823   2508   [2616, 2709] 0,16 -0,13   7  e
    Bodenseekreis               72   33   2,7%    25,9 Tage    3909   1808   [1963, 2058] 0,32 -0,07   7  l
    Breisgau-Hochschwarzwal     45   17   1,9%    37,6 Tage    5324   2026   [2102, 2146] 0,13 -0,15  14  e
    Calw                        32   20   0,6%     inf Tage    4931   3113   [3172, 3186] 0,07  0,08  11  l
    Emmendingen                 22   13   0,6%     inf Tage    3790   2292   [2335, 2350] 0,34  0,08  10  l
    Enzkreis                    28   14   0,5%     inf Tage    5676   2854   [2895, 2903] 0,33  0,07  11  l
    Esslingen                  124   23   1,5%    48,0 Tage   14299   2678   [2782, 2842] 0,24 -0,03   7  l
    Freiburg im Breisgau (S     22  9,8   0,5%     inf Tage    4724   2052   [2082, 2090] 0,36  0,07  11  l
    Freudenstadt                26   22   1,4%    48,6 Tage    2994   2539   [2634, 2687] 0,05 -0,17  14  e
    Göppingen                   51   20   1,7%    41,0 Tage    6474   2517   [2604, 2654] 0,12 -0,16  14  e
    Heidelberg (Stadtkreis)     24   15   0,7%     inf Tage    3413   2128   [2182, 2203] 0,10  0,03  11  l
    Heidenheim                  26   20   1,2%    57,4 Tage    2942   2221   [2305, 2351] 0,08 -0,04  14  l
    Heilbronn                   85   25   3,9%    18,2 Tage    8487   2474   [2610, 2717] 0,45 -0,11   7  e
    Heilbronn (Stadtkreis)      55   44   3,4%    20,7 Tage    4841   3843   [4067, 4225] 0,22 -0,27  14  e
    Hohenlohekreis              11  9,5   0,4%     inf Tage    2597   2319   [2346, 2352] 0,19  0,10  11  l
    Karlsruhe                   62   14   0,6%     inf Tage    9781   2202   [2250, 2267] 0,15  0,04  11  l
    Karlsruhe (Stadtkreis)      20  6,4   0,4%     inf Tage    5472   1748   [1762, 1762] 0,39  0,07  11  l
    Konstanz                    47   17   0,8%     inf Tage    5670   1987   [2036, 2046] 0,09  0,12   8  l
    Lörrach                     36   16   0,6%     inf Tage    6407   2802   [2854, 2872] 0,14  0,11  10  l
    Ludwigsburg                147   27   2,8%    25,0 Tage   15138   2783   [2914, 3002] 0,21 -0,23  14  e
    Main-Tauber-Kreis           35   27   2,1%    33,8 Tage    2654   2006   [2128, 2201] 0,33 -0,10   9  l
    Mannheim (Stadtkreis)       74   24   1,3%    51,9 Tage    9292   3004   [3110, 3171] 0,14  0,05   7  l
    Neckar-Odenwald-Kreis       45   31   2,1%    32,6 Tage    3596   2505   [2653, 2744] 0,21  0,04   7  l
    Ortenaukreis                95   22   1,2%    59,4 Tage   10469   2438   [2531, 2581] 0,11 -0,03  14  l
    Ostalbkreis                115   37   2,4%    29,6 Tage    8180   2605   [2779, 2887] 0,30 -0,04   7  l
    Pforzheim (Stadtkreis)      43   34   1,8%    38,7 Tage    4572   3642   [3791, 3877] 0,17 -0,11  14  e
    Rastatt                     29   12   0,6%     inf Tage    4869   2108   [2144, 2151] 0,26  0,08  11  l
    Ravensburg                 101   36   3,4%    20,4 Tage    5377   1891   [2060, 2168] 0,16 -0,23  14  e
    Rems-Murr-Kreis             83   20   1,7%    41,9 Tage   11443   2685   [2771, 2821] 0,13 -0,15  14  e
    Reutlingen                  25  8,9   0,3%     inf Tage    7851   2738   [2756, 2756] 0,50  0,05  12  l
    Rhein-Neckar-Kreis          86   16   0,7%     inf Tage   13033   2380   [2438, 2463] 0,18  0,02  12  l
    Rottweil                    48   35   1,9%    37,2 Tage    4315   3094   [3253, 3349] 0,13 -0,04   7  l
    Schwäbisch Hall             33   17   0,8%     inf Tage    4282   2186   [2241, 2258] 0,31  0,05  11  l
    Schwarzwald-Baar-Kreis      50   24   1,6%    43,4 Tage    5368   2528   [2635, 2698] 0,22  0,00   7  l
    Sigmaringen                 17   13   0,7%     inf Tage    2515   1922                0,13  0,39   7  l
    Stuttgart                   95   15   0,6%     inf Tage   16441   2590   [2646, 2671] 0,32  0,01  12  l
    Tübingen                    28   12   0,5%     inf Tage    5583   2456   [2501, 2520] 0,12  0,06  13  l
    Tuttlingen                  39   28   1,7%    42,1 Tage    3971   2833   [2959, 3033] 0,16  0,04   7  l
    Ulm (Stadtkreis)            17   13   1,4%    51,0 Tage    3053   2417   [2481, 2522] 0,32  0,03   7  l
    Waldshut                    22   13   0,6%     inf Tage    4044   2370                0,17  0,31   9  l
    Zollernalbkreis             33   18   0,7%     inf Tage    4696   2486   [2543, 2563] 0,23  0,07   9  l
    
    Baden-Württemberg         1969   18   0,7%     inf Tage  271961   2457   [2523, 2552] 0,14  0,03  11  l

Stand 04.01.2021

    Alb-Donau-Kreis             16  8,1   0,4%     inf Tage    4059   2070   [2086, 2086] 0,25 -0,03   7  l
    Baden-Baden (Stadtkreis    2,9  5,3   0,3%     inf Tage    1038   1883                0,26 -0,33   7  e
    Biberach                    14  6,9   0,4%     inf Tage    3597   1801   [1809, 1809] 0,32 -0,02   7  l
    Böblingen                   24  6,1   0,3%     inf Tage    9044   2309   [2325, 2329] 0,25 -0,19   7  e
    Bodenseekreis               27   13   0,9%     inf Tage    3207   1483   [1524, 1538] 0,13  0,09  13  l
    Breisgau-Hochschwarzwal     13  4,9   0,3%     inf Tage    4852   1846   [1859, 1861] 0,73 -0,03   7  e
    Calw                       7,7  4,9   0,2%     inf Tage    4356   2750   [2759, 2761] 0,71 -0,16   7  e
    Emmendingen                 12  7,1   0,3%     inf Tage    3456   2090   [2097, 2097] 0,48  0,15   7  l
    Enzkreis                    16  8,2   0,3%     inf Tage    5159   2594   [2598, 2598] 0,58  0,09   7  l
    Esslingen                   50  9,4   0,4%     inf Tage   13082   2450   [2477, 2484] 0,60  0,10   7  e
    Freiburg im Breisgau (S    8,9  3,9   0,2%     inf Tage    4336   1883   [1885, 1885] 0,81  0,11   7  l
    Freudenstadt                13   11   0,5%     inf Tage    2688   2279   [2308, 2310] 0,24 -0,01   7  l
    Göppingen                   31   12   0,5%     inf Tage    5973   2322   [2360, 2372] 0,21  0,11  13  l
    Heidelberg (Stadtkreis)     16  9,9   0,5%     inf Tage    3069   1914   [1935, 1935] 0,21  0,16   9  l
    Heidenheim                 6,2  4,7   0,2%     inf Tage    2680   2023   [2028, 2028] 0,28  0,13   8  l
    Heilbronn                   49   14   0,6%     inf Tage    7750   2259   [2306, 2321] 0,09  0,20  13  l
    Heilbronn (Stadtkreis)     3,9  3,1   0,1%     inf Tage    4345   3450   [3455, 3455] 0,85 -0,09   7  e
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage    2401   2144                0,82  0,22   7  l
    Karlsruhe                   31  6,9   0,3%     inf Tage    8850   1992   [1998, 1998] 0,20  0,04   7  l
    Karlsruhe (Stadtkreis)     8,8  2,8   0,2%     inf Tage    5003   1598   [1599, 1599] 0,25  0,19   7  l
    Konstanz                    27  9,6   0,6%     inf Tage    4987   1748   [1759, 1759] 0,73  0,12   7  l
    Lörrach                     16  6,9   0,3%     inf Tage    5888   2575   [2590, 2593] 0,79 -0,05   7  e
    Ludwigsburg                 27  5,0   0,2%     inf Tage   13834   2543   [2546, 2546] 0,61  0,14   7  l
    Main-Tauber-Kreis           11  8,2   0,5%     inf Tage    2332   1762   [1770, 1770] 0,44 -0,04   7  l
    Mannheim (Stadtkreis)       33   11   0,4%     inf Tage    8518   2753   [2784, 2793] 0,79  0,07   8  e
    Neckar-Odenwald-Kreis      1,8  1,3   0,1%     inf Tage    3157   2199   [2200, 2200] 0,68  0,09   7  l
    Ortenaukreis                30  7,0   0,3%     inf Tage    9507   2214   [2230, 2234] 0,91  0,03   7  e
    Ostalbkreis                 34   11   0,5%     inf Tage    7232   2303   [2321, 2321] 0,24  0,10   8  l
    Pforzheim (Stadtkreis)      13   10   0,3%     inf Tage    4139   3297   [3319, 3323] 0,92  0,19   7  e
    Rastatt                    8,1  3,5   0,2%     inf Tage    4332   1875                0,46 -0,31   7  e
    Ravensburg                  16  5,5   0,4%     inf Tage    4361   1534   [1547, 1549] 0,57 -0,10   7  e
    Rems-Murr-Kreis             29  6,9   0,3%     inf Tage   10613   2490   [2499, 2499] 0,41  0,06   8  l
    Reutlingen                  32   11   0,4%     inf Tage    7231   2522   [2554, 2561] 0,22  0,05  14  l
    Rhein-Neckar-Kreis          79   14   0,7%     inf Tage   11898   2173   [2208, 2210] 0,25  0,05   7  l
    Rottweil                    11  8,2   0,3%     inf Tage    3867   2773   [2782, 2782] 0,36  0,12  13  l
    Schwäbisch Hall             17  8,8   0,5%     inf Tage    3728   1903   [1914, 1914] 0,40 -0,03   7  l
    Schwarzwald-Baar-Kreis      26   12   0,5%     inf Tage    4845   2281   [2317, 2327] 0,43 -0,10   7  e
    Sigmaringen               0,00  0,0   0,0%     inf Tage    2212   1690                0,61  0,08   7  l
    Stuttgart                   65   10   0,4%     inf Tage   15235   2400   [2426, 2429] 0,39  0,05   9  l
    Tübingen                    26   12   0,5%     inf Tage    5230   2301   [2331, 2335] 0,18  0,23  11  l
    Tuttlingen                  45   32   1,5%    47,5 Tage    3603   2571   [2707, 2780] 0,05 -0,09  11  l
    Ulm (Stadtkreis)           5,1  4,0   0,2%     inf Tage    2877   2277   [2280, 2280] 0,47  0,04   7  l
    Waldshut                    15  8,7   0,4%     inf Tage    3621   2122   [2132, 2132] 0,20 -0,06   7  l
    Zollernalbkreis            9,8  5,2   0,2%     inf Tage    4231   2239                0,17 -0,34   8  e
    
    Baden-Württemberg          973  8,8   0,4%     inf Tage  246423   2226   [2237, 2237] 0,72  0,06   7  l

Stand 19.12.2020

    Alb-Donau-Kreis             58   30   2,4%    28,9 Tage    3479   1775   [1911, 1992] 0,66 -0,05   7  l
    Baden-Baden (Stadtkreis     16   28   2,9%    24,3 Tage     886   1607   [1737, 1814] 0,20 -0,10   8  e
    Biberach                    86   43   4,1%    17,4 Tage    2848   1426   [1634, 1765] 0,55 -0,02   7  l
    Böblingen                  143   37   2,9%    24,2 Tage    7930   2025   [2203, 2315] 0,28  0,05   7  l
    Bodenseekreis               94   43   5,3%    13,4 Tage    2509   1160   [1386, 1538] 0,61 -0,08   7  l
    Breisgau-Hochschwarzwal     75   29   2,3%    30,6 Tage    4185   1592   [1719, 1791] 0,43 -0,05  13  l
    Calw                       121   76   4,7%    15,2 Tage    3554   2244   [2624, 2871] 0,34 -0,14   7  l
    Emmendingen                 67   40   3,7%    19,3 Tage    2850   1723   [1925, 2057] 0,76 -0,03   7  l
    Enzkreis                    72   36   1,8%     inf Tage    4162   2092   [2220, 2270] 0,09  0,06   9  l
    Esslingen                  174   33   2,0%    34,7 Tage   11240   2105   [2249, 2330] 0,10 -0,04   7  l
    Freiburg im Breisgau (S     62   27   2,4%    29,0 Tage    3702   1608   [1731, 1804] 0,47 -0,02   7  l
    Freudenstadt                29   25   1,3%     inf Tage    2274   1928   [1996, 2006] 0,33  0,13  10  l
    Göppingen                  104   40   3,2%    22,0 Tage    5119   1990   [2187, 2314] 0,56 -0,02   7  l
    Heidelberg (Stadtkreis)     50   31   2,9%    24,1 Tage    2536   1581   [1730, 1821] 0,53 -0,06   7  l
    Heidenheim                  14   10   0,6%     inf Tage    2314   1747   [1779, 1789] 0,50 -0,04  11  e
    Heilbronn                  171   50   5,9%    12,1 Tage    6335   1847   [2125, 2347] 0,66 -0,11   7  e
    Heilbronn (Stadtkreis)      89   71   4,1%    17,1 Tage    3662   2907   [3249, 3473] 0,23 -0,19  12  e
    Hohenlohekreis              44   39   6,2%    11,5 Tage    2034   1816   [2059, 2279] 0,56 -0,17   7  e
    Karlsruhe                  175   39   2,8%    25,4 Tage    7293   1642   [1815, 1914] 0,42 -0,05  13  l
    Karlsruhe (Stadtkreis)      83   27   2,7%    26,3 Tage    4290   1370   [1492, 1565] 0,23  0,02   7  l
    Konstanz                    93   33   3,4%    21,0 Tage    4107   1439   [1597, 1697] 0,30 -0,02   7  l
    Lörrach                    115   50   3,6%    19,8 Tage    4926   2154   [2387, 2530] 0,27 -0,12  13  e
    Ludwigsburg                208   38   2,6%    27,4 Tage   11848   2178   [2355, 2462] 0,12  0,09   7  l
    Main-Tauber-Kreis           51   38   6,7%    10,7 Tage    1898   1434   [1670, 1879] 0,53 -0,19   8  e
    Mannheim (Stadtkreis)      177   57   4,4%    16,2 Tage    7230   2337   [2618, 2808] 0,50 -0,08   7  e
    Neckar-Odenwald-Kreis      102   71   5,2%    13,6 Tage    2399   1671   [2016, 2234] 0,65 -0,02   7  l
    Ortenaukreis               193   45   3,4%    20,6 Tage    7940   1849   [2063, 2196] 0,53 -0,00   7  l
    Ostalbkreis                117   37   3,2%    22,3 Tage    6191   1972   [2158, 2278] 0,63 -0,14   7  l
    Pforzheim (Stadtkreis)      67   53   2,2%    31,2 Tage    3371   2685   [2915, 3042] 0,09  0,01   7  l
    Rastatt                     59   26   1,8%    39,4 Tage    3641   1576   [1685, 1744] 0,03  0,04   7  l
    Ravensburg                 100   35   4,2%    17,0 Tage    3413   1201   [1375, 1487] 0,65 -0,02   7  l
    Rems-Murr-Kreis            161   38   3,6%    19,5 Tage    9129   2142   [2326, 2447] 0,12 -0,04   7  e
    Reutlingen                 144   50   3,5%    20,4 Tage    6106   2129   [2372, 2526] 0,26 -0,14   7  l
    Rhein-Neckar-Kreis         247   45   2,8%    25,0 Tage    9580   1749   [1946, 2056] 0,52 -0,02  14  l
    Rottweil                   110   79   5,1%    13,9 Tage    2996   2148   [2552, 2819] 0,47 -0,11   7  l
    Schwäbisch Hall             74   38   3,5%    20,3 Tage    3121   1593   [1776, 1892] 0,59 -0,01   7  l
    Schwarzwald-Baar-Kreis      93   44   2,5%    27,6 Tage    3967   1868   [2057, 2162] 0,19 -0,04  13  l
    Sigmaringen                 58   44   9,0%     8,0 Tage    1919   1466   [1805, 2200] 0,47 -0,25   7  e
    Stuttgart                  156   25   1,2%     inf Tage   13346   2102   [2192, 2231] 0,30  0,03   9  l
    Tübingen                    99   43   4,0%    17,9 Tage    4354   1915   [2124, 2260] 0,47 -0,11  13  e
    Tuttlingen                  50   35   2,4%    28,9 Tage    2826   2016   [2171, 2258] 0,09 -0,09   7  e
    Ulm (Stadtkreis)            38   30   4,0%    17,9 Tage    2536   2007   [2164, 2277] 0,26 -0,14   7  e
    Waldshut                    58   34   2,2%    31,6 Tage    2920   1711   [1858, 1939] 0,15 -0,07  14  l
    Zollernalbkreis             71   37   2,4%    28,6 Tage    3421   1811   [1974, 2067] 0,46 -0,05  12  l
    
    Baden-Württemberg         4391   40   2,9%    24,1 Tage  206387   1864   [2048, 2159] 0,68 -0,02   7  l

Stand 24.11.2020

    Alb-Donau-Kreis             18  9,2   0,7%     inf Tage    2484   1267   [1282, 1282] 0,67  0,07   7  l
    Baden-Baden (Stadtkreis    6,4   12   1,1%     inf Tage     604   1096   [1120, 1120] 0,11  0,06   7  l
    Biberach                    26   13   2,0%    35,8 Tage    1698    850     [907, 939] 0,10 -0,05  11  l
    Böblingen                   22  5,5   0,4%     inf Tage    5749   1468   [1480, 1483] 0,64 -0,04   7  e
    Bodenseekreis               20  9,1   1,3%     inf Tage    1538    711     [733, 734] 0,18  0,10   7  l
    Breisgau-Hochschwarzwal     17  6,4   0,5%     inf Tage    3082   1173   [1191, 1196] 0,81  0,06   7  e
    Calw                        19   12   0,9%     inf Tage    2112   1333   [1359, 1359] 0,31  0,12   7  l
    Emmendingen                 15  9,0   0,8%     inf Tage    1987   1201   [1214, 1214] 0,60  0,06   7  l
    Enzkreis                    24   12   1,0%     inf Tage    2522   1268   [1287, 1287] 0,60  0,10   7  l
    Esslingen                   81   15   1,1%     inf Tage    7733   1449   [1497, 1513] 0,07  0,06   9  l
    Freiburg im Breisgau (S     19  8,4   0,7%     inf Tage    2671   1160   [1183, 1187] 0,49  0,07   7  l
    Freudenstadt                11  8,9   0,7%     inf Tage    1426   1209   [1235, 1243] 0,23 -0,16   7  e
    Göppingen                   38   15   1,1%     inf Tage    3512   1365   [1410, 1425] 0,35 -0,07   7  e
    Heidelberg (Stadtkreis)     18   11   1,1%     inf Tage    1709   1066   [1098, 1104] 0,39  0,12   9  l
    Heidenheim                 9,4  7,1   0,6%     inf Tage    1643   1240                0,49  0,30   7  l
    Heilbronn                   38   11   1,0%     inf Tage    3951   1152   [1170, 1170] 0,60  0,04   7  l
    Heilbronn (Stadtkreis)      13   10   0,6%     inf Tage    2304   1829   [1835, 1835] 0,75  0,08   7  l
    Hohenlohekreis              11   10   0,7%     inf Tage    1548   1382   [1397, 1397] 0,35  0,08   8  l
    Karlsruhe                   33  7,5   0,7%     inf Tage    4657   1048   [1058, 1058] 0,49  0,18   7  l
    Karlsruhe (Stadtkreis)      26  8,3   0,9%     inf Tage    2918    932     [943, 943] 0,45  0,09   7  l
    Konstanz                    33   12   1,2%     inf Tage    2843    996   [1022, 1022] 0,24  0,16   9  l
    Lörrach                     19  8,3   0,6%     inf Tage    2971   1299   [1304, 1304] 0,80  0,10   7  l
    Ludwigsburg                 48  8,9   0,6%     inf Tage    8409   1546   [1554, 1554] 0,54  0,13   7  l
    Main-Tauber-Kreis           11  8,2   0,9%     inf Tage    1254    948     [961, 961] 0,39  0,16   7  l
    Mannheim (Stadtkreis)       94   30   2,1%     inf Tage    4489   1451   [1563, 1613] 0,05 -0,03   8  e
    Neckar-Odenwald-Kreis      9,4  6,6   0,7%     inf Tage    1271    885     [892, 892] 0,66  0,17   7  l
    Ortenaukreis                52   12   1,0%     inf Tage    5186   1208   [1231, 1231] 0,16  0,02   7  l
    Ostalbkreis                 31  9,8   0,8%     inf Tage    4105   1307   [1337, 1346] 0,27 -0,03   9  e
    Pforzheim (Stadtkreis)      22   17   1,1%     inf Tage    1997   1591   [1648, 1670] 0,13 -0,12   9  e
    Rastatt                     25   11   1,0%     inf Tage    2456   1063   [1086, 1086] 0,17  0,07   7  l
    Ravensburg                  40   14   2,1%    33,6 Tage    2134    751     [811, 844] 0,01 -0,08   9  l
    Rems-Murr-Kreis             55   13   0,9%     inf Tage    6136   1440   [1463, 1463] 0,35  0,15   7  l
    Reutlingen                  38   13   0,9%     inf Tage    4031   1406   [1448, 1463] 0,37 -0,03   8  e
    Rhein-Neckar-Kreis          78   14   1,3%     inf Tage    5828   1064   [1094, 1094] 0,71  0,04   7  l
    Rottweil                    17   12   0,9%     inf Tage    1827   1310   [1330, 1330] 0,20  0,19   7  l
    Schwäbisch Hall            1,1  0,6   0,1%     inf Tage    2202   1124   [1124, 1124] 0,79  0,13   7  l
    Schwarzwald-Baar-Kreis      38   18   1,7%     inf Tage    2257   1063   [1122, 1144] 0,23 -0,02   7  e
    Sigmaringen                5,5  4,2   0,4%     inf Tage    1432   1094   [1097, 1097] 0,49  0,29   7  l
    Stuttgart                  202   32   2,5%    27,8 Tage    9513   1499   [1639, 1718] 0,09 -0,03  11  l
    Tübingen                    36   16   1,7%    41,3 Tage    3152   1387   [1456, 1497] 0,08 -0,08  10  l
    Tuttlingen                  22   16   1,3%     inf Tage    1696   1210   [1234, 1234] 0,23  0,00   7  l
    Ulm (Stadtkreis)            14   11   0,8%     inf Tage    1708   1352   [1386, 1397] 0,25 -0,11   8  e
    Waldshut                    25   15   1,4%     inf Tage    1807   1059   [1104, 1116] 0,32  0,11  13  l
    Zollernalbkreis             15  8,1   0,6%     inf Tage    2378   1259   [1276, 1277] 0,31  0,17   7  l
    
    Baden-Württemberg         1446   13   1,1%     inf Tage  136930   1237   [1269, 1270] 0,68  0,06   7  l

Stand 13.11.2020

    Alb-Donau-Kreis             40   21   3,4%    20,9 Tage    2141   1092   [1189, 1249] 0,12 -0,00   7  e
    Baden-Baden (Stadtkreis    6,2   11   1,3%     inf Tage     491    891     [926, 939] 0,83  0,03   8  e
    Biberach                    19  9,3   1,3%     inf Tage    1475    738     [770, 782] 0,10  0,04  10  l
    Böblingen                  135   34   3,5%    20,1 Tage    4990   1274   [1435, 1533] 0,36 -0,02   7  l
    Bodenseekreis               44   20   4,4%    16,2 Tage    1223    566     [661, 719] 0,10 -0,14   7  l
    Breisgau-Hochschwarzwal     46   17   2,2%    31,7 Tage    2755   1048   [1126, 1170] 0,27 -0,01   7  l
    Calw                        48   30   2,9%    24,4 Tage    1815   1146   [1278, 1352] 0,18 -0,07  14  l
    Emmendingen                 26   16   1,6%     inf Tage    1684   1018   [1070, 1088] 0,34  0,02  12  l
    Enzkreis                    21   11   1,1%     inf Tage    2032   1022   [1046, 1047] 0,71  0,06  11  l
    Esslingen                  148   28   2,3%    30,3 Tage    6652   1246   [1364, 1428] 0,08 -0,01  14  l
    Freiburg im Breisgau (S     21  9,1   0,9%     inf Tage    2376   1032   [1061, 1069] 0,28  0,10  12  l
    Freudenstadt                35   30   3,4%    20,5 Tage    1207   1023   [1158, 1237] 0,57 -0,08  12  l
    Göppingen                   78   30   2,6%    27,3 Tage    2857   1111   [1237, 1304] 0,43 -0,02  14  e
    Heidelberg (Stadtkreis)     55   34   4,8%    14,6 Tage    1409    879   [1044, 1148] 0,54 -0,09   7  l
    Heidenheim                  30   22   3,3%    21,5 Tage    1322    998   [1099, 1160] 0,07 -0,30  12  e
    Heilbronn                  119   35   4,3%    16,4 Tage    3310    965   [1127, 1225] 0,19 -0,12   8  l
    Heilbronn (Stadtkreis)      56   44   3,8%    18,7 Tage    1890   1500   [1708, 1835] 0,25  0,05   7  l
    Hohenlohekreis              35   31   4,4%    16,2 Tage    1324   1182   [1348, 1462] 0,70 -0,07   7  l
    Karlsruhe                   93   21   2,4%     inf Tage    3923    883     [960, 993] 0,08  0,04  10  l
    Karlsruhe (Stadtkreis)      53   17   2,2%     inf Tage    2390    763     [823, 848] 0,23  0,03  12  l
    Konstanz                    37   13   1,7%     inf Tage    2181    764     [799, 803] 0,29  0,08  11  l
    Lörrach                     83   36   3,5%    19,9 Tage    2256    987   [1142, 1228] 0,26 -0,03  14  l
    Ludwigsburg                182   34   3,5%    20,0 Tage    7084   1302   [1461, 1560] 0,31  0,01   7  l
    Main-Tauber-Kreis           28   21   3,8%    18,5 Tage    1078    815     [919, 986] 0,35 -0,14   7  l
    Mannheim (Stadtkreis)      122   40   4,7%    15,0 Tage    3329   1076   [1268, 1390] 0,71 -0,03   7  l
    Neckar-Odenwald-Kreis       16   11   3,1%    23,1 Tage    1053    734     [787, 821] 0,11 -0,29  13  e
    Ortenaukreis               135   31   3,8%    18,5 Tage    4212    981   [1125, 1211] 0,27  0,04   7  l
    Ostalbkreis                100   32   4,9%    14,6 Tage    3402   1083   [1242, 1349] 0,47 -0,13  14  e
    Pforzheim (Stadtkreis)      53   42   3,5%    20,2 Tage    1626   1295   [1481, 1587] 0,09  0,03   7  l
    Rastatt                     37   16   1,9%     inf Tage    1995    864     [918, 939] 0,40  0,05   7  e
    Ravensburg                  43   15   3,2%    22,1 Tage    1726    607     [677, 719] 0,22  0,03   7  l
    Rems-Murr-Kreis            140   33   4,1%    17,4 Tage    5121   1202   [1356, 1452] 0,14 -0,03   7  e
    Reutlingen                  73   25   2,5%    28,3 Tage    3384   1180   [1291, 1353] 0,13 -0,02  13  l
    Rhein-Neckar-Kreis         146   27   4,9%    14,4 Tage    4462    815    [944, 1030] 0,27 -0,12   7  e
    Rottweil                    63   45   5,4%    13,1 Tage    1529   1096   [1324, 1473] 0,43 -0,05   7  l
    Schwäbisch Hall             28   14   2,6%    26,9 Tage    1968   1005   [1076, 1122] 0,57 -0,09   7  l
    Schwarzwald-Baar-Kreis      76   36   9,4%     7,7 Tage    1725    812                0,24 -0,32   9  e
    Sigmaringen                 18   14   2,0%    35,4 Tage    1287    983   [1045, 1080] 0,08  0,02   7  l
    Stuttgart                  277   44   7,8%     9,3 Tage    7843   1235   [1508, 1758] 0,53 -0,13   7  e
    Tübingen                    32   14   1,2%     inf Tage    2831   1245   [1294, 1312] 0,15  0,06  10  l
    Tuttlingen                  52   37   5,4%    13,1 Tage    1260    899   [1085, 1206] 0,40  0,00   7  l
    Ulm (Stadtkreis)            49   38   4,7%    15,1 Tage    1407   1114   [1305, 1428] 0,76 -0,06   7  l
    Waldshut                    96   56  15,8%     4,7 Tage    1394    817                0,32 -0,37   7  e
    Zollernalbkreis             45   24   3,3%    21,4 Tage    2116   1120   [1236, 1310] 0,35 -0,01   7  l
    
    Baden-Württemberg         2992   27   3,2%    22,2 Tage  113535   1026   [1148, 1219] 0,48  0,00   7  l

Stand 06.11.2020

    Alb-Donau-Kreis             50   25   3,2%    21,9 Tage    1897    968   [1083, 1151] 0,33  0,03   7  l
    Baden-Baden (Stadtkreis    5,2  9,4   1,2%     inf Tage     425    771     [803, 816] 0,12 -0,11  10  e
    Biberach                    34   17   4,1%    17,2 Tage    1327    664     [746, 798] 0,38 -0,12  14  e
    Böblingen                  171   44   4,4%    16,1 Tage    4285   1094   [1293, 1411] 0,73 -0,06  13  l
    Bodenseekreis               44   20   5,6%    12,6 Tage    1000    462     [564, 631] 0,19 -0,06   7  l
    Breisgau-Hochschwarzwal     53   20   4,5%    15,9 Tage    2490    948   [1051, 1124] 0,23 -0,18   7  e
    Calw                        56   36   5,3%    13,5 Tage    1552    980   [1166, 1292] 0,70 -0,14   7  l
    Emmendingen                 49   30   3,3%    21,6 Tage    1463    885   [1012, 1082] 0,23 -0,03  14  l
    Enzkreis                    69   35   4,7%    15,0 Tage    1803    906   [1072, 1176] 0,48 -0,02   7  l
    Esslingen                  134   25   3,1%    23,0 Tage    5744   1076   [1192, 1261] 0,62 -0,01   7  l
    Freiburg im Breisgau (S     30   13   1,4%     inf Tage    2191    952    [992, 1003] 0,30  0,08  10  l
    Freudenstadt                20   17   2,1%    33,2 Tage    1016    861     [934, 973] 0,09 -0,01  14  l
    Göppingen                   68   26   2,9%    23,9 Tage    2338    909   [1021, 1082] 0,26 -0,03   7  e
    Heidelberg (Stadtkreis)     53   33   5,8%    12,3 Tage    1143    713     [877, 984] 0,72 -0,10   7  l
    Heidenheim                  17   13   1,6%     inf Tage    1076    812     [854, 868] 0,15  0,10  10  l
    Heilbronn                   52   15   1,9%     inf Tage    2647    772     [820, 836] 0,09  0,16   9  l
    Heilbronn (Stadtkreis)      65   51   5,0%    14,1 Tage    1601   1271   [1520, 1678] 0,46 -0,01   7  l
    Hohenlohekreis              27   24   2,8%    25,3 Tage    1203   1074   [1182, 1245] 0,50 -0,03  14  l
    Karlsruhe                  148   33   5,5%    12,9 Tage    3240    729     [892, 994] 0,45 -0,01   7  l
    Karlsruhe (Stadtkreis)      86   27   4,7%    15,1 Tage    1981    633     [757, 831] 0,16 -0,00   7  l
    Konstanz                    88   31   5,0%    14,3 Tage    1803    632     [771, 851] 0,30 -0,08  13  l
    Lörrach                     65   29   4,6%    15,4 Tage    1752    766     [897, 977] 0,57 -0,06  14  e
    Ludwigsburg                257   47   5,4%    13,2 Tage    6167   1134   [1369, 1521] 0,22 -0,00   7  l
    Main-Tauber-Kreis           18   13   2,9%    24,6 Tage     951    719     [782, 822] 0,58 -0,02   7  l
    Mannheim (Stadtkreis)       82   26   4,9%    14,4 Tage    2750    889   [1020, 1109] 0,13 -0,09   7  e
    Neckar-Odenwald-Kreis       14  9,6   1,5%     inf Tage     951    663     [696, 709] 0,07  0,04  10  l
    Ortenaukreis               134   31   4,6%    15,4 Tage    3480    810    [958, 1048] 0,44  0,02   7  l
    Ostalbkreis                 83   27   4,4%    16,0 Tage    2883    918   [1055, 1146] 0,55 -0,08   7  l
    Pforzheim (Stadtkreis)      59   47   5,1%    14,0 Tage    1314   1047   [1267, 1400] 0,48 -0,04   9  l
    Rastatt                     42   18   2,6%     inf Tage    1639    709     [779, 810] 0,09  0,01  10  l
    Ravensburg                  42   15   4,0%    17,7 Tage    1488    523     [592, 634] 0,54 -0,07  14  e
    Rems-Murr-Kreis            127   30   3,7%    19,1 Tage    4281   1005   [1138, 1216] 0,46 -0,06  13  e
    Reutlingen                  36   13   1,2%     inf Tage    2944   1027   [1068, 1082] 0,30  0,05  10  l
    Rhein-Neckar-Kreis         172   31   5,8%    12,2 Tage    3648    666     [822, 923] 0,68 -0,06   7  l
    Rottweil                    52   37   5,7%    12,5 Tage    1260    904   [1097, 1227] 0,47 -0,05   7  l
    Schwäbisch Hall             34   17   1,9%    36,7 Tage    1841    940   [1012, 1051] 0,31 -0,01  14  l
    Schwarzwald-Baar-Kreis      55   26   4,7%    15,0 Tage    1419    668     [791, 868] 0,26 -0,06   8  l
    Sigmaringen                 24   19   3,0%    23,2 Tage    1183    904    [993, 1047] 0,17 -0,12   8  l
    Stuttgart                  233   37   4,3%    16,6 Tage    6651   1048   [1220, 1325] 0,50  0,01   7  l
    Tübingen                    61   27   3,1%    22,6 Tage    2573   1132   [1256, 1330] 0,43 -0,06   7  l
    Tuttlingen                  31   22   4,0%    17,7 Tage    1041    743     [849, 915] 0,65 -0,05   7  l
    Ulm (Stadtkreis)            43   34   7,1%    10,2 Tage    1190    942   [1139, 1301] 0,83 -0,10   7  e
    Waldshut                    50   29   5,1%    13,9 Tage    1055    618     [753, 833] 0,43 -0,04   8  l
    Zollernalbkreis             44   23   2,9%    24,3 Tage    1910   1011   [1116, 1178] 0,57 -0,05  13  l
    
    Baden-Württemberg         3119   28   4,0%    17,7 Tage   96596    873   [1004, 1084] 0,70 -0,02   7  l

Stand 08.10.2020

    Alb-Donau-Kreis             10  5,3   7,6%     9,5 Tage     957    488     [537, 608] 0,96 -0,18   7  e
    Baden-Baden (Stadtkreis    1,6  2,9   2,0%    35,5 Tage     236    428     [444, 455] 0,67 -0,14   7  l
    Biberach                   5,7  2,9   0,6%     inf Tage     900    451     [460, 463] 0,35  0,04  13  l
    Böblingen                   22  5,7   2,1%    33,9 Tage    2260    577     [605, 623] 0,29 -0,02   7  l
    Bodenseekreis             1,00  0,5   0,2%     inf Tage     570    264                0,35  0,34   8  l
    Breisgau-Hochschwarzwal     12  4,5   3,1%    22,8 Tage    1560    594     [617, 634] 0,33 -0,20  12  e
    Calw                        10  6,3   2,4%    29,6 Tage     968    611     [644, 667] 0,31 -0,04   7  l
    Emmendingen                9,1  5,5   2,3%    30,9 Tage     732    443     [469, 486] 0,69 -0,10  10  l
    Enzkreis                   5,1  2,6   0,5%     inf Tage     936    471     [480, 483] 0,08  0,08  14  l
    Esslingen                   52  9,7   2,2%    31,5 Tage    3067    574     [617, 642] 0,26 -0,04  14  l
    Freiburg im Breisgau (S    9,9  4,3   1,4%    49,3 Tage    1321    574     [593, 605] 0,23 -0,04  12  l
    Freudenstadt              0,54  0,5   0,1%     inf Tage     669    567     [568, 568] 0,13 -0,04   7  l
    Göppingen                   18  7,0   4,6%    15,3 Tage    1269    493     [533, 565] 0,67 -0,18  12  e
    Heidelberg (Stadtkreis)    6,9  4,3   2,5%    27,7 Tage     562    350     [372, 387] 0,57 -0,14   7  l
    Heidenheim                 3,0  2,2   1,5%    47,9 Tage     638    482     [493, 501] 0,41 -0,11   9  l
    Heilbronn                   15  4,2   2,1%    33,6 Tage    1436    419     [439, 453] 0,25 -0,12   8  l
    Heilbronn (Stadtkreis)     8,1  6,5   1,6%    42,5 Tage     780    619     [648, 665] 0,10 -0,09  11  l
    Hohenlohekreis             2,9  2,6   0,9%    77,9 Tage     881    787     [798, 805] 0,08 -0,06   9  l
    Karlsruhe                   24  5,4   2,8%    25,2 Tage    1539    346     [373, 391] 0,37 -0,08   7  l
    Karlsruhe (Stadtkreis)     8,7  2,8   2,1%    32,8 Tage     746    238     [252, 260] 0,17  0,02   7  l
    Konstanz                    20  6,9   4,3%    16,3 Tage     811    284     [322, 349] 0,61 -0,14   7  l
    Lörrach                    1,5  0,7   0,2%     inf Tage     920    402     [404, 404] 0,15  0,14  14  l
    Ludwigsburg                 52  9,5   3,1%    22,5 Tage    2903    534     [582, 614] 0,49  0,01   7  l
    Main-Tauber-Kreis          4,7  3,6   1,5%    47,1 Tage     582    440     [456, 466] 0,20 -0,08  13  l
    Mannheim (Stadtkreis)       20  6,4   1,9%    36,2 Tage    1248    403     [431, 446] 0,08 -0,07  14  l
    Neckar-Odenwald-Kreis      6,1  4,2   1,7%    40,4 Tage     566    394     [413, 425] 0,34 -0,07  14  l
    Ortenaukreis                35  8,0   3,1%    22,6 Tage    1749    407     [446, 471] 0,79 -0,08  10  l
    Ostalbkreis                3,1  1,0   0,2%     inf Tage    1913    609     [611, 611] 0,11  0,23  10  l
    Pforzheim (Stadtkreis)     7,1  5,7   2,5%    27,8 Tage     654    521     [551, 572] 0,43 -0,14   7  l
    Rastatt                    6,2  2,7   1,9%    37,6 Tage     769    333     [346, 355] 0,47 -0,09   8  l
    Ravensburg                 5,6  2,0   1,4%    50,8 Tage     932    328     [337, 343] 0,17 -0,01   7  l
    Rems-Murr-Kreis             20  4,7   1,9%    36,3 Tage    2427    570     [593, 608] 0,30 -0,13   8  l
    Reutlingen                 2,7  0,9   0,1%     inf Tage    2010    701     [702, 702] 0,24  0,18   8  l
    Rhein-Neckar-Kreis          19  3,4   1,7%    41,6 Tage    1744    318     [334, 342] 0,17 -0,06  11  l
    Rottweil                  0,75  0,5   0,1%     inf Tage     786    564     [564, 564] 0,19  0,14   8  l
    Schwäbisch Hall             17  8,8   2,9%    24,5 Tage    1195    610     [656, 686] 0,63 -0,04   7  l
    Schwarzwald-Baar-Kreis     8,6  4,1   2,7%    25,6 Tage     725    341     [363, 379] 0,73 -0,14   7  l
    Sigmaringen                4,1  3,1   1,2%    59,5 Tage     912    697     [712, 721] 0,46 -0,08  12  l
    Stuttgart                   66   10   3,3%    21,5 Tage    3156    497     [548, 581] 0,43 -0,02   7  l
    Tübingen                    13  5,6   2,0%    35,4 Tage    1601    704     [733, 752] 0,30 -0,13   8  l
    Tuttlingen                  11  8,0   3,5%    20,3 Tage     653    466     [510, 541] 0,48 -0,14   7  l
    Ulm (Stadtkreis)           6,5  5,1   2,0%    34,6 Tage     631    499     [524, 540] 0,19 -0,05   7  l
    Waldshut                  1,00  0,6   0,2%     inf Tage     457    268     [268, 268] 0,27  0,20   8  l
    Zollernalbkreis            3,1  1,6   0,6%   112,5 Tage    1435    760     [767, 771] 0,15 -0,07  14  l
    
    Baden-Württemberg          564  5,1   2,1%    33,8 Tage   52806    477     [502, 517] 0,54 -0,03   7  l

Stand 09.09.2020

    Alb-Donau-Kreis            5,7  2,9   1,5%    46,4 Tage     813    415     [428, 437] 0,20 -0,10  10  l
    Baden-Baden (Stadtkreis    1,3  2,3   2,1%    34,1 Tage     210    381     [394, 404] 0,62 -0,14   7  l
    Biberach                   1,4  0,7   0,2%     inf Tage     747    374     [375, 375] 0,16  0,07   9  l
    Böblingen                   11  2,7   0,6%     inf Tage    1889    482     [491, 494] 0,28  0,04   9  l
    Bodenseekreis              2,6  1,2   0,6%     inf Tage     444    205     [208, 209] 0,11  0,26   8  l
    Breisgau-Hochschwarzwal     11  4,3   4,6%    15,5 Tage    1318    502     [528, 553] 0,69 -0,12   7  e
    Calw                       7,2  4,6   1,6%    44,6 Tage     867    547     [568, 581] 0,13 -0,06  13  l
    Emmendingen                1,5  0,9   0,2%     inf Tage     630    381     [382, 382] 0,55  0,07   8  l
    Enzkreis                   5,8  2,9   1,7%    41,1 Tage     781    393     [407, 416] 0,38  0,01   7  l
    Esslingen                   21  3,9   1,3%    52,0 Tage    2331    437     [453, 463] 0,05 -0,05  12  l
    Freiburg im Breisgau (S    1,3  0,5   0,1%     inf Tage    1133    492     [492, 492] 0,41  0,08   7  l
    Freudenstadt              0,83  0,7   0,1%     inf Tage     638    541     [542, 542] 0,39  0,08   8  l
    Göppingen                  6,8  2,6   1,1%    61,3 Tage    1046    407     [418, 425] 0,12 -0,06  11  l
    Heidelberg (Stadtkreis)    2,2  1,4   0,5%     inf Tage     439    274                0,18  0,58   7  l
    Heidenheim                 3,1  2,3   1,2%    59,6 Tage     589    445     [455, 462] 0,19 -0,07  14  l
    Heilbronn                   11  3,3   1,7%    40,7 Tage    1231    359     [374, 384] 0,15 -0,14   7  l
    Heilbronn (Stadtkreis)     2,9  2,3   0,4%     inf Tage     654    519     [527, 530] 0,24 -0,06  13  e
    Hohenlohekreis             2,6  2,4   0,9%    78,9 Tage     830    741     [752, 758] 0,17 -0,09  11  l
    Karlsruhe                  2,6  0,6   0,2%     inf Tage    1281    288                0,13  0,44   7  l
    Karlsruhe (Stadtkreis)    0,29  0,1   0,0%     inf Tage     588    188                0,30  0,66   7  l
    Konstanz                   2,2  0,8   0,3%     inf Tage     654    229     [232, 233] 0,07  0,08  14  l
    Lörrach                    1,5  0,7   0,2%     inf Tage     809    354     [354, 354] 0,42  0,22   7  l
    Ludwigsburg                 13  2,5   0,6%     inf Tage    2293    422     [430, 433] 0,30  0,04   9  l
    Main-Tauber-Kreis         0,82  0,6   0,2%     inf Tage     518    391     [392, 392] 0,08 -0,14   7  l
    Mannheim (Stadtkreis)      6,8  2,2   0,8%     inf Tage     854    276     [282, 284] 0,10  0,11   7  l
    Neckar-Odenwald-Kreis      2,3  1,6   1,1%    62,4 Tage     502    350     [357, 362] 0,16 -0,08  12  l
    Ortenaukreis               2,5  0,6   0,2%     inf Tage    1412    329     [330, 330] 0,10  0,26  13  l
    Ostalbkreis                4,9  1,6   0,7%    98,2 Tage    1710    545     [551, 555] 0,02 -0,09  11  l
    Pforzheim (Stadtkreis)     4,7  3,7   1,5%    47,6 Tage     573    456     [473, 483] 0,06 -0,10  10  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     664    287                0,67  0,34   8  l
    Ravensburg                 9,6  3,4   2,0%    35,1 Tage     805    283     [299, 308] 0,16 -0,07  12  l
    Rems-Murr-Kreis             20  4,7   1,7%    41,7 Tage    2140    502     [524, 537] 0,08 -0,06   9  l
    Reutlingen                 4,6  1,6   0,3%     inf Tage    1753    611                0,14  0,67   7  l
    Rhein-Neckar-Kreis          16  2,9   2,5%    27,8 Tage    1440    263     [279, 289] 0,52 -0,20   7  l
    Rottweil                  0,20  0,1   0,0%     inf Tage     733    526     [526, 526] 0,47  0,23   9  l
    Schwäbisch Hall            4,6  2,3   1,2%    58,7 Tage     986    503     [514, 521] 0,07 -0,09   8  l
    Schwarzwald-Baar-Kreis     1,9  0,9   1,1%    65,1 Tage     653    307     [312, 315] 0,06 -0,02   7  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     852    651                0,29  2,50   8  l
    Stuttgart                   36  5,7   2,7%    25,6 Tage    2292    361     [389, 407] 0,17  0,02   7  l
    Tübingen                    11  4,8   1,9%    37,6 Tage    1449    637     [662, 678] 0,36 -0,12   7  l
    Tuttlingen                0,00  0,0   0,0%     inf Tage     586    418                0,60  0,24   8  l
    Ulm (Stadtkreis)           3,3  2,6   0,7%     inf Tage     495    392     [397, 397] 0,25  0,03   7  l
    Waldshut                  1,00  0,6   0,3%     inf Tage     388    227     [229, 229] 0,17  0,11   8  l
    Zollernalbkreis            1,2  0,7   0,1%     inf Tage    1368    724     [725, 725] 0,45  0,13   9  l
    
    Baden-Württemberg          263  2,4   1,1%    64,8 Tage   44388    401     [411, 416] 0,14 -0,04  12  e

Stand 26.08.2020

    Alb-Donau-Kreis            1,2  0,6   0,2%     inf Tage     752    384     [384, 384] 0,34  0,11   7  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     197    357                0,80  0,43   7  l
    Biberach                  0,00  0,0   0,0%     inf Tage     701    351                0,70  0,18   7  l
    Böblingen                   17  4,4   2,1%    33,8 Tage    1686    430     [452, 466] 0,32 -0,01   7  l
    Bodenseekreis              6,8  3,1   2,9%    24,3 Tage     396    183     [199, 209] 0,21 -0,05   7  l
    Breisgau-Hochschwarzwal     10  4,0   2,3%    30,2 Tage    1225    466     [488, 504] 0,39 -0,08   7  l
    Calw                      0,42  0,3   0,1%     inf Tage     811    512     [512, 512] 0,38  0,29   8  l
    Emmendingen                3,5  2,1   1,5%    47,8 Tage     585    354     [364, 371] 0,19 -0,09  11  l
    Enzkreis                   3,1  1,6   0,9%    74,9 Tage     731    368     [374, 378] 0,25 -0,07  14  l
    Esslingen                   16  2,9   1,3%    54,2 Tage    2112    396     [409, 416] 0,13 -0,07  14  l
    Freiburg im Breisgau (S    6,9  3,0   1,5%    46,1 Tage    1070    465     [479, 488] 0,33 -0,07  10  l
    Freudenstadt               1,2  1,0   0,2%     inf Tage     617    523                0,26  0,31   8  l
    Göppingen                  3,5  1,4   0,4%     inf Tage     959    373     [375, 375] 0,71  0,12   7  l
    Heidelberg (Stadtkreis)    2,1  1,3   0,6%     inf Tage     371    231     [234, 234] 0,17  0,07  10  l
    Heidenheim                 2,9  2,2   1,1%    64,5 Tage     567    428     [438, 444] 0,14 -0,04  13  l
    Heilbronn                  9,4  2,7   1,4%    48,4 Tage    1111    324     [336, 343] 0,17 -0,05  14  l
    Heilbronn (Stadtkreis)     9,2  7,3   2,2%    31,9 Tage     574    456     [488, 507] 0,24 -0,03  14  l
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage     805    719                0,37  0,19   9  l
    Karlsruhe                   11  2,4   1,6%    43,1 Tage    1201    270     [281, 288] 0,15 -0,09  11  l
    Karlsruhe (Stadtkreis)     7,2  2,3   1,9%    37,8 Tage     531    170     [180, 185] 0,08 -0,09  11  l
    Konstanz                   5,2  1,8   1,9%    36,0 Tage     605    212     [221, 227] 0,09 -0,14   7  l
    Lörrach                    4,7  2,1   1,1%    64,8 Tage     755    330     [339, 344] 0,08 -0,05  14  l
    Ludwigsburg                 17  3,1   1,5%    45,2 Tage    2069    380     [394, 403] 0,26 -0,09  11  l
    Main-Tauber-Kreis         0,39  0,3   0,1%     inf Tage     501    379     [379, 379] 0,56  0,18   7  l
    Mannheim (Stadtkreis)       22  7,1   4,7%    15,1 Tage     726    235     [272, 297] 0,21 -0,02   7  l
    Neckar-Odenwald-Kreis     0,50  0,3   0,1%     inf Tage     485    338     [338, 338] 0,20 -0,09   7  l
    Ortenaukreis                10  2,4   1,4%    50,2 Tage    1345    313     [324, 330] 0,12 -0,08  12  l
    Ostalbkreis                6,1  1,9   0,8%    83,8 Tage    1654    527     [535, 540] 0,11 -0,05  14  l
    Pforzheim (Stadtkreis)     1,5  1,2   0,3%     inf Tage     527    420     [423, 424] 0,17  0,12  10  l
    Rastatt                    5,9  2,5   1,6%    43,4 Tage     617    267     [279, 285] 0,19 -0,07  14  l
    Ravensburg                 3,9  1,4   0,5%     inf Tage     720    253     [256, 256] 0,18  0,08  10  l
    Rems-Murr-Kreis             15  3,6   1,7%    41,2 Tage    1932    453     [471, 481] 0,09 -0,09   8  l
    Reutlingen                 2,9  1,0   0,2%     inf Tage    1664    580     [582, 582] 0,24  0,06   7  l
    Rhein-Neckar-Kreis         6,4  1,2   0,5%     inf Tage    1275    233     [234, 234] 0,63  0,12   7  l
    Rottweil                  0,00  0,0   0,0%     inf Tage     707    507                0,66  0,22   7  l
    Schwäbisch Hall            4,3  2,2   1,0%    70,5 Tage     939    479     [489, 495] 0,16 -0,06  12  l
    Schwarzwald-Baar-Kreis    0,92  0,4   0,1%     inf Tage     630    297     [297, 297] 0,41  0,24   8  l
    Sigmaringen               0,16  0,1   0,0%     inf Tage     831    635     [635, 635] 0,44  0,17   9  l
    Stuttgart                   25  3,9   1,8%    38,7 Tage    1962    309     [326, 336] 0,15 -0,07  14  l
    Tübingen                   8,6  3,8   1,4%    48,5 Tage    1361    599     [617, 628] 0,29 -0,08  12  l
    Tuttlingen                 3,4  2,4   1,6%    43,6 Tage     556    397     [409, 417] 0,19  0,07   7  l
    Ulm (Stadtkreis)           7,9  6,3   2,5%    28,0 Tage     426    337     [366, 382] 0,10 -0,07  10  l
    Waldshut                   4,1  2,4   2,0%    34,4 Tage     364    213     [225, 232] 0,38 -0,08  12  l
    Zollernalbkreis            6,6  3,5   1,3%    54,4 Tage    1311    694     [711, 721] 0,46  0,01   7  l
    
    Baden-Württemberg          289  2,6   1,2%    59,1 Tage   40964    370     [381, 388] 0,38 -0,03  14  l

Stand 04.08.2020

    Alb-Donau-Kreis            2,3  1,2   1,2%    57,1 Tage     691    352     [359, 363] 0,17  0,27   7  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     187    339                1,00  0,00   7  l
    Biberach                  0,00  0,0   0,0%     inf Tage     634    317                0,27  0,57  14  l
    Böblingen                  6,3  1,6   1,1%    62,6 Tage    1528    390     [398, 402] 0,51  0,22   9  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     339    157                0,33  1,67  13  l
    Breisgau-Hochschwarzwal   0,00  0,0   0,0%     inf Tage    1167    444                0,69  1,03   8  l
    Calw                      0,67  0,4   0,4%   198,0 Tage     776    490                0,05  0,35  12  l
    Emmendingen               0,00  0,0   0,0%     inf Tage     555    336                0,66  1,19   7  l
    Enzkreis                  0,00  0,0   0,0%     inf Tage     695    349                0,49  1,38  11  l
    Esslingen                  1,1  0,2   0,1%     inf Tage    1946    365                0,15  0,80  10  l
    Freiburg im Breisgau (S    3,3  1,4   1,2%    60,2 Tage    1000    434                0,61  0,31   9  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     588    499                0,25  1,29  12  l
    Göppingen                  2,6  1,0   1,0%    71,5 Tage     847    329     [334, 337] 0,21  0,28  10  l
    Heidelberg (Stadtkreis)   0,96  0,6   0,9%    76,7 Tage     321    200                0,52  0,35  14  l
    Heidenheim                0,00  0,0   0,0%     inf Tage     539    407                0,52  0,58   8  l
    Heilbronn                  3,0  0,9   0,3%     inf Tage    1009    294     [296, 296] 0,05  0,30   7  l
    Heilbronn (Stadtkreis)    0,24  0,2   0,0%     inf Tage     491    390     [390, 390] 0,09  0,14   7  l
    Hohenlohekreis             1,4  1,3   0,6%   108,8 Tage     790    705                0,20  0,34  14  l
    Karlsruhe                  6,7  1,5   1,6%    43,2 Tage    1096    247     [254, 259] 0,33  0,27   8  l
    Karlsruhe (Stadtkreis)     1,2  0,4   0,8%    91,6 Tage     444    142                0,07  0,33  14  l
    Konstanz                   4,6  1,6   0,9%     inf Tage     536    188                0,09  0,60  10  l
    Lörrach                    2,8  1,2   1,3%    53,4 Tage     686    300     [306, 310] 0,76  0,28   8  l
    Ludwigsburg                5,8  1,1   0,9%    75,1 Tage    1894    348                0,23  0,32  12  l
    Main-Tauber-Kreis         0,11  0,1   0,0%     inf Tage     468    354                0,31  0,89  14  l
    Mannheim (Stadtkreis)      7,8  2,5   2,1%    33,8 Tage     573    185                0,36  0,37  14  l
    Neckar-Odenwald-Kreis     0,00  0,0   0,0%     inf Tage     460    320                0,38  4,00   8  l
    Ortenaukreis              0,78  0,2   0,4%   167,6 Tage    1237    288     [289, 289] 0,27  0,28  11  l
    Ostalbkreis                2,9  0,9   0,2%     inf Tage    1570    500                0,37  1,01   8  l
    Pforzheim (Stadtkreis)    0,00  0,0   0,0%     inf Tage     487    388                0,32  1,85  10  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     551    239                0,67  1,73   7  l
    Ravensburg                 1,7  0,6   0,3%     inf Tage     614    216                0,09  0,35   7  l
    Rems-Murr-Kreis            2,8  0,7   0,2%     inf Tage    1762    413                0,14  1,16   8  l
    Reutlingen                 5,4  1,9   0,9%    79,2 Tage    1596    557                0,19  0,38  13  l
    Rhein-Neckar-Kreis          14  2,5   2,3%    30,6 Tage    1087    198     [210, 218] 0,20  0,29   8  l
    Rottweil                  0,45  0,3   0,5%   130,9 Tage     684    490                0,25  0,34   8  l
    Schwäbisch Hall            1,7  0,9   0,8%    84,4 Tage     882    450                0,40  0,31  10  l
    Schwarzwald-Baar-Kreis    0,01  0,0   0,0%     inf Tage     591    278                0,19  1,03  10  l
    Sigmaringen                1,7  1,3   0,7%    97,6 Tage     790    604                0,16  0,33  12  l
    Stuttgart                  6,9  1,1   1,0%    69,2 Tage    1675    264                0,15  0,37  13  l
    Tübingen                   1,0  0,5   0,5%   131,7 Tage    1301    572     [575, 576] 0,15  0,25   7  l
    Tuttlingen                0,00  0,0   0,0%     inf Tage     525    375                0,51  1,64  10  l
    Ulm (Stadtkreis)          0,37  0,3   0,1%     inf Tage     332    263                0,31  1,60  12  l
    Waldshut                   1,5  0,9   1,1%    64,6 Tage     332    195                0,16  0,34  14  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1246    659                1,00  0,00   7  l
    
    Baden-Württemberg           86  0,8   0,2%     inf Tage   37522    339                0,05  0,39   8  e

Stand 29.07.2020

    Alb-Donau-Kreis           0,84  0,4   0,1%     inf Tage     685    349                0,09  0,79  13  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     187    339                1,00  0,00   7  l
    Biberach                  0,16  0,1   0,0%     inf Tage     633    317                0,26  0,56   8  l
    Böblingen                  1,3  0,3   0,1%     inf Tage    1506    385                0,36  0,52  11  l
    Bodenseekreis             0,60  0,3   0,2%     inf Tage     336    155                0,39  2,17   7  l
    Breisgau-Hochschwarzwal    3,0  1,1   1,1%    62,6 Tage    1166    444     [450, 454] 0,51  0,12   7  l
    Calw                      0,76  0,5   0,5%   151,7 Tage     774    489     [491, 492] 0,19  0,26  13  l
    Emmendingen               0,61  0,4   0,1%     inf Tage     554    335                0,15  0,63   7  l
    Enzkreis                   2,2  1,1   0,3%     inf Tage     690    347                0,07  0,31   7  l
    Esslingen                  3,3  0,6   0,2%     inf Tage    1939    363                0,35  0,46  11  e
    Freiburg im Breisgau (S   0,96  0,4   0,6%   115,4 Tage     993    431     [433, 435] 0,21  0,17   8  l
    Freudenstadt               3,3  2,8   1,5%    45,8 Tage     588    499     [513, 522] 0,29  0,19   9  l
    Göppingen                 0,02  0,0   0,0%     inf Tage     838    326                0,42  0,50   8  l
    Heidelberg (Stadtkreis)   0,49  0,3   0,9%    73,4 Tage     318    198     [200, 201] 0,37  0,07   7  l
    Heidenheim                 1,9  1,5   0,4%     inf Tage     538    406                0,11  1,19   7  l
    Heilbronn                  3,4  1,0   0,9%    74,0 Tage     983    287     [291, 294] 0,30  0,26  14  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     483    383                0,45  2,50   8  l
    Hohenlohekreis             1,2  1,1   0,9%    81,9 Tage     786    702     [708, 712] 0,50  0,17   8  l
    Karlsruhe                  2,1  0,5   0,2%     inf Tage    1078    243                0,06  0,66  11  l
    Karlsruhe (Stadtkreis)    0,03  0,0   0,0%     inf Tage     439    140                0,18  1,55  11  l
    Konstanz                   8,6  3,0   2,6%    26,8 Tage     519    182     [196, 205] 0,60  0,17   9  l
    Lörrach                   0,12  0,1   0,0%     inf Tage     678    297                0,25  0,66  14  l
    Ludwigsburg                1,2  0,2   0,1%     inf Tage    1874    344                0,17  0,50   9  l
    Main-Tauber-Kreis         0,50  0,4   0,1%     inf Tage     457    345                0,43  1,24   8  l
    Mannheim (Stadtkreis)      5,5  1,8   2,5%    28,2 Tage     546    176     [186, 193] 0,74  0,12   7  l
    Neckar-Odenwald-Kreis      2,9  2,1   1,6%    44,4 Tage     458    319     [329, 336] 0,12  0,18   9  l
    Ortenaukreis              0,00  0,0   0,0%     inf Tage    1234    287                0,43  0,81  14  l
    Ostalbkreis                 18  5,6   2,1%    32,8 Tage    1532    488     [515, 532] 0,25  0,21  11  l
    Pforzheim (Stadtkreis)     2,1  1,7   0,4%     inf Tage     483    385                0,13  0,30  10  l
    Rastatt                    2,2  0,9   0,9%    74,0 Tage     549    238     [242, 244] 0,22  0,27  14  l
    Ravensburg                0,77  0,3   0,1%     inf Tage     601    211                0,27  0,99  11  l
    Rems-Murr-Kreis            7,5  1,8   1,2%    59,4 Tage    1745    409     [418, 423] 0,13  0,25   9  l
    Reutlingen                 4,4  1,5   4,0%    17,7 Tage    1580    551     [562, 573] 0,83  0,12   7  e
    Rhein-Neckar-Kreis         6,1  1,1   1,1%    64,6 Tage    1047    191                0,07  0,35   8  l
    Rottweil                  0,25  0,2   0,0%     inf Tage     683    490     [490, 490] 0,06  0,23   7  l
    Schwäbisch Hall           0,49  0,3   0,6%   125,0 Tage     878    448     [450, 451] 0,37  0,07   7  l
    Schwarzwald-Baar-Kreis    0,15  0,1   0,0%     inf Tage     590    278                0,18  1,51   7  l
    Sigmaringen               0,44  0,3   0,1%     inf Tage     784    599                0,18  0,57   9  l
    Stuttgart                  5,9  0,9   1,4%    50,9 Tage    1655    261     [266, 269] 0,52  0,20   7  l
    Tübingen                  0,22  0,1   0,0%     inf Tage    1298    571                0,40  0,88   7  l
    Tuttlingen                 1,0  0,7   0,7%   102,2 Tage     525    375     [378, 380] 0,11  0,16   9  l
    Ulm (Stadtkreis)           1,2  1,0   0,4%     inf Tage     321    254     [255, 255] 0,16  0,26   7  l
    Waldshut                  0,12  0,1   0,0%     inf Tage     327    192                0,29  1,10  11  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1246    659                0,86  0,75   8  l
    
    Baden-Württemberg          101  0,9   0,9%    75,9 Tage   37124    335     [339, 341] 0,29  0,26   9  e

Stand 23.07.2020

    Alb-Donau-Kreis           0,00  0,0   0,0%     inf Tage     678    346                0,93  2,06   7  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     187    339                1,00  0,00   7  l
    Biberach                   1,3  0,7   1,1%    61,4 Tage     632    316     [320, 323] 0,57 -0,15   7  l
    Böblingen                  4,2  1,1   0,7%   101,6 Tage    1494    381     [386, 389] 0,15  0,25  12  l
    Bodenseekreis              6,0  2,8   2,6%    26,6 Tage     330    153     [166, 173] 0,32  0,18  14  l
    Breisgau-Hochschwarzwal    1,9  0,7   0,7%   101,0 Tage    1158    441     [444, 446] 0,12  0,11   8  l
    Calw                      0,83  0,5   0,8%    88,3 Tage     772    487     [490, 493] 0,57 -0,12   7  l
    Emmendingen               0,79  0,5   0,7%   102,2 Tage     551    333     [336, 337] 0,09  0,10   8  l
    Enzkreis                   2,4  1,2   0,8%    86,2 Tage     674    339     [344, 347] 0,15  0,16  12  l
    Esslingen                  4,5  0,8   0,2%     inf Tage    1921    360                0,31  0,57   7  e
    Freiburg im Breisgau (S   0,37  0,2   0,0%     inf Tage     990    430                0,34  0,69  10  l
    Freudenstadt              0,21  0,2   0,0%     inf Tage     577    489                0,09  0,86   8  l
    Göppingen                  3,5  1,4   2,9%    24,6 Tage     836    325     [332, 338] 0,57  0,10   8  e
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     317    198                1,00  0,00   7  l
    Heidenheim                 2,8  2,1   1,2%    56,4 Tage     529    399     [409, 415] 0,21  0,17  14  l
    Heilbronn                  1,7  0,5   0,9%    77,5 Tage     971    283     [286, 288] 0,18  0,04   8  l
    Heilbronn (Stadtkreis)     2,1  1,6   1,5%    47,9 Tage     482    383     [391, 397] 0,36  0,04   8  l
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage     783    699                0,69  2,11   7  l
    Karlsruhe                  2,7  0,6   0,9%    80,7 Tage    1066    240     [243, 245] 0,09  0,12   9  l
    Karlsruhe (Stadtkreis)    0,19  0,1   0,0%     inf Tage     437    140                0,20  0,91   7  l
    Konstanz                   4,1  1,4   1,8%    39,7 Tage     490    172     [179, 183] 0,31  0,19  10  l
    Lörrach                   0,27  0,1   0,0%     inf Tage     677    296                0,24  0,85  14  l
    Ludwigsburg                3,8  0,7   0,9%    81,2 Tage    1869    344     [347, 349] 0,65  0,09   8  l
    Main-Tauber-Kreis          3,5  2,7   0,8%     inf Tage     447    338                0,36  1,28   7  l
    Mannheim (Stadtkreis)      2,7  0,9   1,3%    54,9 Tage     532    172     [176, 179] 0,16  0,12  10  l
    Neckar-Odenwald-Kreis      1,5  1,0   1,0%    68,1 Tage     450    314     [318, 322] 0,31  0,16  12  l
    Ortenaukreis              0,79  0,2   0,1%     inf Tage    1234    287                0,16  0,62   8  l
    Ostalbkreis                7,2  2,3   1,3%    53,5 Tage    1482    472     [483, 490] 0,35  0,04  14  l
    Pforzheim (Stadtkreis)     5,7  4,6   2,4%    29,3 Tage     471    375     [398, 413] 0,43  0,09   8  l
    Rastatt                    2,1  0,9   1,4%    49,2 Tage     542    235     [240, 243] 0,63  0,03   8  l
    Ravensburg                 3,5  1,2   1,3%    55,7 Tage     591    208     [214, 217] 0,09  0,20  14  l
    Rems-Murr-Kreis            2,2  0,5   0,1%     inf Tage    1719    403                0,26  0,84   7  l
    Reutlingen                 1,9  0,7   0,6%   117,5 Tage    1568    547     [550, 552] 0,39  0,12  10  l
    Rhein-Neckar-Kreis         7,4  1,3   4,0%    17,5 Tage    1026    187     [195, 202] 0,66  0,03  10  e
    Rottweil                  0,00  0,0   0,0%     inf Tage     681    488                0,25  0,34   8  l
    Schwäbisch Hall           0,00  0,0   0,0%     inf Tage     877    448                1,00  0,00   7  l
    Schwarzwald-Baar-Kreis    0,58  0,3   0,6%   119,2 Tage     589    277     [279, 280] 0,29  0,12  10  l
    Sigmaringen                1,7  1,3   0,9%    73,8 Tage     782    598     [604, 608] 0,64  0,09   9  l
    Stuttgart                  2,9  0,5   0,2%     inf Tage    1641    258                0,42  0,59   7  e
    Tübingen                  0,34  0,1   0,5%   133,0 Tage    1296    570                0,21   nan   7  l
    Tuttlingen                0,73  0,5   0,7%   106,8 Tage     521    372     [374, 376] 0,10  0,11   9  l
    Ulm (Stadtkreis)           2,1  1,7   1,5%    45,4 Tage     303    240     [248, 253] 0,13  0,14  12  l
    Waldshut                  0,55  0,3   0,2%     inf Tage     324    190                0,19  0,67   9  l
    Zollernalbkreis            2,9  1,5   1,0%    68,0 Tage    1244    658     [666, 672] 0,40  0,15   7  l
    
    Baden-Württemberg           99  0,9   1,5%    46,3 Tage   36741    332     [336, 339] 0,35  0,15  10  e

Stand 04.07.2020

    Alb-Donau-Kreis            2,5  1,3   1,3%    52,5 Tage     661    337     [344, 348] 0,49 -0,11   9  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     185    336                1,00  0,00   7  l
    Biberach                   3,5  1,8   1,3%    53,6 Tage     622    311     [320, 325] 0,25 -0,08  13  l
    Böblingen                 0,00  0,0   0,0%     inf Tage    1452    371                0,40 -0,03   7  l
    Bodenseekreis             0,07  0,0   0,0%     inf Tage     297    137                0,13  0,33   9  l
    Breisgau-Hochschwarzwal    1,1  0,4   1,1%    61,1 Tage    1135    432     [435, 438] 0,23 -0,14   7  l
    Calw                      0,92  0,6   0,8%    84,7 Tage     761    480                0,16 -0,42   8  l
    Emmendingen               0,46  0,3   0,7%    95,5 Tage     533    322     [324, 325] 0,38 -0,14   7  l
    Enzkreis                  0,04  0,0   1,4%    49,5 Tage     658    331     [333, 336] 0,16 -0,14   7  l
    Esslingen                  3,2  0,6   0,6%   122,2 Tage    1867    350     [352, 354] 0,10 -0,04  13  l
    Freiburg im Breisgau (S   0,00  0,0   0,0%     inf Tage     972    422                1,00  0,00   7  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     570    483                1,00  0,00   7  l
    Göppingen                  1,6  0,6   0,2%     inf Tage     811    315     [317, 317] 0,10  0,06   9  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     316    197                0,08  0,35  10  l
    Heidenheim                0,71  0,5   0,6%   114,6 Tage     515    389     [391, 393] 0,06 -0,07  14  l
    Heilbronn                  1,1  0,3   1,0%    68,2 Tage     961    280                0,14 -1,58   8  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     472    375                0,74  0,29   7  l
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage     779    695                0,76  0,26  10  l
    Karlsruhe                  8,1  1,8   1,5%    46,4 Tage    1044    235     [243, 248] 0,12 -0,07  14  l
    Karlsruhe (Stadtkreis)     5,3  1,7   2,1%    34,1 Tage     427    136     [144, 149] 0,15 -0,07  14  l
    Konstanz                  0,20  0,1   0,3%   207,9 Tage     469    164     [165, 165] 0,10 -0,07  14  l
    Lörrach                   0,74  0,3   0,7%    93,7 Tage     668    292                0,43  0,86  14  l
    Ludwigsburg                4,6  0,9   0,7%    97,9 Tage    1824    335     [339, 341] 0,15 -0,08  13  l
    Main-Tauber-Kreis         0,00  0,0   0,0%     inf Tage     399    302                1,00  0,00   7  l
    Mannheim (Stadtkreis)      3,3  1,1   1,7%    41,7 Tage     514    166     [172, 175] 0,43 -0,11   9  l
    Neckar-Odenwald-Kreis     0,46  0,3   0,8%    86,7 Tage     443    309     [311, 312] 0,38 -0,14   7  l
    Ortenaukreis              0,69  0,2   0,3%   206,1 Tage    1215    283     [284, 284] 0,11 -0,07  14  l
    Ostalbkreis               0,00  0,0   0,0%     inf Tage    1450    462                0,67  0,44   8  l
    Pforzheim (Stadtkreis)    0,79  0,6   0,2%     inf Tage     425    339     [339, 339] 0,10 -0,14   7  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     527    228                0,17 -0,14   7  l
    Ravensburg                 3,5  1,2   2,2%    31,9 Tage     567    199                0,52 -0,43   7  l
    Rems-Murr-Kreis            1,7  0,4   0,1%     inf Tage    1657    389                0,22  0,31   7  l
    Reutlingen                0,00  0,0   0,0%     inf Tage    1555    542                0,41  0,62  10  l
    Rhein-Neckar-Kreis         1,7  0,3   0,8%    84,2 Tage     971    177     [179, 180] 0,17 -0,11   9  l
    Rottweil                  0,00  0,0   0,0%     inf Tage     679    487                0,26  0,20  10  l
    Schwäbisch Hall           0,00  0,0   0,0%     inf Tage     873    446                0,38  0,31   8  l
    Schwarzwald-Baar-Kreis    0,00  0,0   0,0%     inf Tage     587    276                0,30  0,91  10  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     776    593                1,00  0,00   7  l
    Stuttgart                  1,6  0,3   0,1%     inf Tage    1546    244     [244, 244] 0,13  0,09  11  l
    Tübingen                  0,69  0,3   0,4%   171,1 Tage    1295    570     [571, 572] 0,22 -0,08  12  l
    Tuttlingen                0,47  0,3   0,1%     inf Tage     515    367     [368, 368] 0,08  0,14   9  l
    Ulm (Stadtkreis)          0,82  0,7   1,3%    52,6 Tage     290    230     [233, 236] 0,62 -0,14   7  l
    Waldshut                  0,00  0,0   0,0%     inf Tage     311    182                0,01 -1,00   8  l
    Zollernalbkreis           0,17  0,1   0,0%     inf Tage    1223    647                0,26  0,46   8  l

    Baden-Württemberg           40  0,4   0,1%     inf Tage   35817    324     [325, 325] 0,09  0,00  10  e

Stand 20.06.2020

    Alb-Donau-Kreis            3,8  2,0   1,9%    36,5 Tage     650    332                0,34 -0,48   9  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     185    336                1,00  0,00   7  l
    Biberach                  0,33  0,2   0,6%   116,1 Tage     600    300                0,21 -1,00   9  l
    Böblingen                 0,00  0,0   0,0%     inf Tage    1416    362                0,53  0,21   8  l
    Bodenseekreis             0,69  0,3   1,0%    67,4 Tage     294    136                0,18 -0,40  10  l
    Breisgau-Hochschwarzwal    1,5  0,6   0,6%   112,1 Tage    1139    433     [436, 438] 0,09 -0,09  11  l
    Calw                      1,00  0,6   0,7%    96,3 Tage     758    479     [482, 484] 0,15 -0,14   7  l
    Emmendingen                3,6  2,2   2,2%    32,3 Tage     528    319     [332, 341] 0,44 -0,14   7  l
    Enzkreis                   2,9  1,4   1,6%    43,6 Tage     667    335     [343, 349] 0,54 -0,14   7  l
    Esslingen                 0,00  0,0   0,0%     inf Tage    1844    345                0,32  0,19  13  l
    Freiburg im Breisgau (S   0,33  0,1   0,4%   175,0 Tage     970    421     [422, 423] 0,17 -0,13   8  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     570    483                1,00  0,00   7  l
    Göppingen                 0,40  0,2   0,1%     inf Tage     785    305     [306, 306] 0,07  0,07   9  l
    Heidelberg (Stadtkreis)   0,46  0,3   0,1%     inf Tage     313    195     [195, 195] 0,04 -0,14   7  l
    Heidenheim                0,00  0,0   0,0%     inf Tage     511    386                1,00  0,00   7  l
    Heilbronn                 0,00  0,0   0,0%     inf Tage     949    277                0,24  1,22   9  l
    Heilbronn (Stadtkreis)     1,1  0,9   0,2%     inf Tage     460    365                0,11  0,64   7  l
    Hohenlohekreis            0,07  0,1   0,0%     inf Tage     772    689     [689, 689] 0,04 -0,14   7  l
    Karlsruhe                 0,07  0,0   0,0%     inf Tage     988    222     [222, 222] 0,12 -0,14   7  l
    Karlsruhe (Stadtkreis)     2,0  0,6   1,7%    42,3 Tage     396    126     [130, 132] 0,45 -0,26   9  l
    Konstanz                  0,00  0,0   0,0%     inf Tage     468    164                1,00  0,00   7  l
    Lörrach                   0,00  0,0   0,0%     inf Tage     667    292                0,30 -1,89   9  l
    Ludwigsburg               0,00  0,0   0,0%     inf Tage    1789    329                0,44  0,63   7  l
    Main-Tauber-Kreis         0,00  0,0   0,0%     inf Tage     399    302                0,17 -0,12   8  l
    Mannheim (Stadtkreis)     0,00  0,0   0,0%     inf Tage     495    160                0,35  1,07   9  l
    Neckar-Odenwald-Kreis     0,00  0,0   0,0%     inf Tage     441    307                0,02  0,85  13  l
    Ortenaukreis              0,91  0,2   0,7%    99,0 Tage    1210    282     [283, 284] 0,27  0,06  14  l
    Ostalbkreis                6,4  2,0   1,2%    57,5 Tage    1400    446     [456, 462] 0,50 -0,08  12  l
    Pforzheim (Stadtkreis)    0,22  0,2   0,1%     inf Tage     406    323     [324, 324] 0,11  0,23  13  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     522    226                0,17 -0,12   8  l
    Ravensburg                0,00  0,0   0,0%     inf Tage     559    197                0,54  0,31   8  l
    Rems-Murr-Kreis            5,5  1,3   1,3%    54,3 Tage    1616    379     [386, 391] 0,39 -0,14   7  l
    Reutlingen                0,97  0,3   0,4%   159,2 Tage    1546    539     [541, 542] 0,46 -0,26  13  l
    Rhein-Neckar-Kreis         1,2  0,2   0,7%    96,3 Tage     960    175     [176, 177] 0,12 -0,28  10  l
    Rottweil                  0,00  0,0   0,0%     inf Tage     675    484                0,26 -0,14   7  l
    Schwäbisch Hall           0,82  0,4   0,7%    94,2 Tage     869    444     [446, 448] 0,26 -0,14   7  l
    Schwarzwald-Baar-Kreis    0,00  0,0   0,0%     inf Tage     570    268                0,40 -0,02   7  l
    Sigmaringen               0,32  0,2   0,6%   117,4 Tage     776    593                0,16   nan   7  l
    Stuttgart                  4,6  0,7   1,0%    69,1 Tage    1515    239     [242, 244] 0,20 -0,14   7  l
    Tübingen                  0,00  0,0   0,0%     inf Tage    1292    568     [568, 568] 0,33  0,29   7  l
    Tuttlingen                0,00  0,0   0,0%     inf Tage     505    360                0,13  1,77  13  l
    Ulm (Stadtkreis)          0,00  0,0   0,0%     inf Tage     288    228                0,29 -0,12   8  l
    Waldshut                  0,00  0,0   0,0%     inf Tage     311    182                0,17 -0,14   7  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1208    639                0,31  0,85  13  l
    
    Baden-Württemberg           29  0,3   0,1%     inf Tage   35282    319     [320, 320] 0,27  0,07   7  l

Stand 13.06.2020

    Alb-Donau-Kreis           0,00  0,0   0,0%     inf Tage     639    326                0,08 -1,00  12  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     185    336                0,17 -0,12   8  l
    Biberach                  0,22  0,1   0,7%   100,1 Tage     599    300     [301, 302] 0,11 -0,10  10  l
    Böblingen                   11  2,8   1,9%    37,1 Tage    1409    360     [374, 383] 0,49 -0,09   8  l
    Bodenseekreis             0,34  0,2   0,5%   127,1 Tage     292    135     [136, 136] 0,04 -0,07  14  l
    Breisgau-Hochschwarzwal   0,00  0,0   0,0%     inf Tage    1131    430                0,39  0,78   9  l
    Calw                       1,1  0,7   0,6%   107,5 Tage     755    477     [480, 482] 0,13 -0,08  13  l
    Emmendingen               0,00  0,0   0,0%     inf Tage     519    314                0,25  0,78   9  l
    Enzkreis                  0,00  0,0   0,0%     inf Tage     658    331                0,27  1,19   8  l
    Esslingen                 0,00  0,0   0,0%     inf Tage    1837    344                0,48  0,24   8  l
    Freiburg im Breisgau (S   0,00  0,0   0,0%     inf Tage     969    421                0,36  2,50   8  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     570    483                0,17 -0,14   7  l
    Göppingen                  1,1  0,4   0,7%   102,7 Tage     783    304     [306, 308] 0,65 -0,09  11  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     300    187                0,19  0,38  13  l
    Heidenheim                0,36  0,3   1,0%    69,7 Tage     511    386                0,29  2,56   9  l
    Heilbronn                  1,2  0,3   0,5%   139,1 Tage     950    277     [278, 279] 0,08 -0,07  14  l
    Heilbronn (Stadtkreis)     2,5  2,0   1,3%    52,7 Tage     449    356     [366, 372] 0,13 -0,07  14  l
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage     770    687                1,00  0,00   7  l
    Karlsruhe                  1,2  0,3   0,4%   157,7 Tage     982    221     [222, 223] 0,07 -0,07  14  l
    Karlsruhe (Stadtkreis)    0,08  0,0   0,0%     inf Tage     391    125                0,07  0,75   8  l
    Konstanz                  0,20  0,1   0,3%   207,7 Tage     468    164     [164, 165] 0,10 -0,07  14  l
    Lörrach                   0,71  0,3   0,5%   132,0 Tage     669    293     [294, 295] 0,20 -0,07  14  l
    Ludwigsburg                3,6  0,7   0,9%    75,1 Tage    1780    327     [331, 333] 0,13 -0,14   7  l
    Main-Tauber-Kreis         0,33  0,3   0,6%   110,3 Tage     399    302     [303, 304] 0,17 -0,13   8  l
    Mannheim (Stadtkreis)     0,58  0,2   0,1%     inf Tage     493    159     [160, 160] 0,06  0,27   9  l
    Neckar-Odenwald-Kreis     0,11  0,1   0,0%     inf Tage     441    307                0,01  0,35  10  l
    Ortenaukreis               1,2  0,3   1,1%    65,1 Tage    1210    282     [284, 286] 0,42  0,02   9  l
    Ostalbkreis               0,00  0,0   0,0%     inf Tage    1369    436                0,21  0,57  10  l
    Pforzheim (Stadtkreis)    0,25  0,2   0,1%     inf Tage     404    322                0,16  0,31   8  l
    Rastatt                    1,6  0,7   1,4%    50,6 Tage     522    226                0,25 -0,47   8  l
    Ravensburg                 1,2  0,4   1,5%    47,8 Tage     558    196                0,59  1,62   8  l
    Rems-Murr-Kreis            2,5  0,6   0,5%   136,7 Tage    1596    375     [377, 379] 0,08 -0,07  14  l
    Reutlingen                0,92  0,3   0,6%   112,8 Tage    1543    538                0,75 -0,56   8  l
    Rhein-Neckar-Kreis         1,2  0,2   0,8%    82,9 Tage     957    175     [176, 177] 0,10 -0,14   7  l
    Rottweil                   1,5  1,1   1,4%    50,6 Tage     676    485                0,47 -2,33   9  l
    Schwäbisch Hall           0,00  0,0   0,0%     inf Tage     866    442                0,18 -0,07  14  l
    Schwarzwald-Baar-Kreis     2,0  0,9   1,5%    47,0 Tage     567    267     [272, 276] 0,33 -0,14   7  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     776    593                1,00  0,00   7  l
    Stuttgart                  4,0  0,6   0,8%    84,0 Tage    1496    236     [239, 240] 0,25 -0,08  13  l
    Tübingen                  0,65  0,3   0,4%   178,8 Tage    1291    568     [569, 570] 0,34 -0,08  12  l
    Tuttlingen                0,00  0,0   0,0%     inf Tage     504    360                1,00  0,00   7  l
    Ulm (Stadtkreis)           1,8  1,4   2,2%    31,7 Tage     291    230     [239, 246] 0,38 -0,14   7  l
    Waldshut                  0,46  0,3   1,0%    72,0 Tage     311    182     [184, 185] 0,38 -0,14   7  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1208    639                0,32  0,65  10  l
    
    Baden-Württemberg           45  0,4   2,5%    28,3 Tage   35094    317     [319, 321] 0,73 -0,11   7  e

Stand 05.06.2020

    Alb-Donau-Kreis           0,00  0,0   0,0%     inf Tage     642    327                0,28  0,67  10  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     184    334                1,00  0,00   7  l
    Biberach                  0,00  0,0   0,0%     inf Tage     599    300                0,48  0,98  10  l
    Böblingen                  4,7  1,2   1,2%    59,2 Tage    1363    348     [354, 358] 0,25 -0,12   8  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     290    134                1,00  0,00   7  l
    Breisgau-Hochschwarzwal   0,00  0,0   0,0%     inf Tage    1130    430                0,36  0,82  11  l
    Calw                      0,00  0,0   0,0%     inf Tage     749    473                0,39  0,53  10  l
    Emmendingen               0,67  0,4   0,8%    87,8 Tage     517    313     [315, 316] 0,17 -0,13   8  l
    Enzkreis                  0,24  0,1   0,0%     inf Tage     656    330     [330, 330] 0,44  0,24  10  l
    Esslingen                  4,4  0,8   1,1%    62,7 Tage    1820    341     [345, 348] 0,35 -0,14   7  l
    Freiburg im Breisgau (S    1,3  0,6   0,7%    96,0 Tage     968    420     [423, 425] 0,16 -0,11   9  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     569    482                1,00  0,00   7  l
    Göppingen                 0,00  0,0   0,0%     inf Tage     778    302                1,00  0,00   7  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     299    186                0,34  2,11   9  l
    Heidenheim                0,00  0,0   0,0%     inf Tage     512    386                0,05  0,82  11  l
    Heilbronn                 0,83  0,2   0,6%   113,9 Tage     944    275     [276, 277] 0,19 -0,12   8  l
    Heilbronn (Stadtkreis)     1,6  1,3   1,5%    45,1 Tage     438    348     [355, 361] 0,62 -0,14   7  l
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage     770    687                0,41  0,20  10  l
    Karlsruhe                  1,7  0,4   1,0%    72,9 Tage     976    220     [222, 223] 0,53 -0,14   7  l
    Karlsruhe (Stadtkreis)    0,96  0,3   1,1%    60,8 Tage     389    124     [126, 127] 0,24 -0,14   7  l
    Konstanz                  0,00  0,0   0,0%     inf Tage     467    164                1,00  0,00   7  l
    Lörrach                   0,00  0,0   0,0%     inf Tage     665    291                1,00  0,00   7  l
    Ludwigsburg                7,7  1,4   1,6%    44,1 Tage    1766    325     [332, 338] 0,27 -0,01   7  l
    Main-Tauber-Kreis         0,00  0,0   0,0%     inf Tage     398    301                0,17 -0,14   7  l
    Mannheim (Stadtkreis)      1,5  0,5   1,4%    50,5 Tage     487    157     [160, 162] 0,38 -0,14   7  l
    Neckar-Odenwald-Kreis     0,18  0,1   0,0%     inf Tage     440    307                0,11  0,59  11  l
    Ortenaukreis              0,00  0,0   0,0%     inf Tage    1211    282                0,64 -0,47   8  l
    Ostalbkreis                2,9  0,9   1,0%    68,2 Tage    1364    434     [439, 443] 0,25 -0,14   7  l
    Pforzheim (Stadtkreis)    0,00  0,0   0,0%     inf Tage     400    319                0,26  0,69   9  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     517    224                0,34 -1,00   9  l
    Ravensburg                0,00  0,0   0,0%     inf Tage     559    197                0,60 -0,57   7  l
    Rems-Murr-Kreis            2,9  0,7   1,0%    71,6 Tage    1582    371     [375, 378] 0,85 -0,14   7  l
    Reutlingen                0,51  0,2   0,0%     inf Tage    1541    537                0,05  0,78  13  l
    Rhein-Neckar-Kreis         1,8  0,3   1,1%    64,7 Tage     954    174                0,26 -0,75   9  l
    Rottweil                  0,00  0,0   0,0%     inf Tage     674    483                0,43 -1,00   8  l
    Schwäbisch Hall           0,00  0,0   0,0%     inf Tage     866    442                0,32  0,46   8  l
    Schwarzwald-Baar-Kreis     2,2  1,1   1,1%    65,7 Tage     562    265     [270, 273] 0,15 -0,08  13  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     776    593                0,17 -0,13   8  l
    Stuttgart                 0,26  0,0   0,0%     inf Tage    1475    232     [232, 232] 0,37  0,11  14  l
    Tübingen                  0,00  0,0   0,0%     inf Tage    1288    567                0,62  1,57   7  l
    Tuttlingen                0,93  0,7   1,1%    64,4 Tage     504    360     [363, 366] 0,38 -0,14   7  l
    Ulm (Stadtkreis)          0,89  0,7   1,1%    65,5 Tage     288    228     [231, 234] 0,04  0,14   7  l
    Waldshut                  0,00  0,0   0,0%     inf Tage     310    182                1,00  0,00   7  l
    Zollernalbkreis            2,9  1,5   1,0%    67,6 Tage    1205    638     [646, 651] 0,31 -0,20   8  l
    
    Baden-Württemberg           18  0,2   0,1%     inf Tage   34892    315     [316, 316] 0,38  0,05  11  l

Stand 30.05.2020

    Alb-Donau-Kreis            3,1  1,6   1,3%    55,1 Tage     639    326     [334, 338] 0,21 -0,10  10  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     184    334                1,00  0,00   7  l
    Biberach                   6,9  3,5   2,7%    26,2 Tage     598    299     [318, 331] 0,27 -0,10   7  l
    Böblingen                  3,0  0,8   0,8%    82,9 Tage    1343    343     [347, 349] 0,08 -0,08  13  l
    Bodenseekreis             0,38  0,2   0,9%    78,3 Tage     290    134                0,30 -1,00  10  l
    Breisgau-Hochschwarzwal    3,1  1,2   1,2%    56,7 Tage    1130    430                0,39 -0,30   8  l
    Calw                       2,1  1,3   0,9%    75,5 Tage     742    468     [475, 479] 0,19 -0,07  14  l
    Emmendingen               0,42  0,3   0,5%   138,6 Tage     515    311     [313, 313] 0,06 -0,12   8  l
    Enzkreis                   4,3  2,2   1,9%    37,8 Tage     647    325     [337, 344] 0,34 -0,14   7  l
    Esslingen                 0,00  0,0   0,0%     inf Tage    1806    338                0,30  0,91   9  l
    Freiburg im Breisgau (S   0,18  0,1   0,0%     inf Tage     963    418                0,18  0,36  11  l
    Freudenstadt              0,25  0,2   0,0%     inf Tage     569    482                0,09  0,71   7  l
    Göppingen                  3,5  1,4   2,3%    30,6 Tage     778    302                0,26 -2,75   8  l
    Heidelberg (Stadtkreis)    1,7  1,0   1,8%    39,4 Tage     297    185     [191, 195] 0,17 -0,12   8  l
    Heidenheim                0,61  0,5   0,8%    92,3 Tage     512    386     [389, 391] 0,22 -0,14   7  l
    Heilbronn                 0,00  0,0   0,0%     inf Tage     941    274                0,23  0,68  12  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     434    345                0,46  0,27   9  l
    Hohenlohekreis             1,1  1,0   0,9%    79,9 Tage     769    687     [692, 696] 0,75 -0,14   7  l
    Karlsruhe                  2,1  0,5   0,2%     inf Tage     971    219     [220, 220] 0,19  0,08   9  l
    Karlsruhe (Stadtkreis)     1,5  0,5   1,6%    42,5 Tage     386    123     [126, 128] 0,46 -0,14   7  l
    Konstanz                  0,00  0,0   0,0%     inf Tage     467    164                0,39  0,60   9  l
    Lörrach                   0,03  0,0   0,0%     inf Tage     665    291                0,08  0,39  14  l
    Ludwigsburg               0,42  0,1   0,0%     inf Tage    1743    320                0,18  0,62   8  l
    Main-Tauber-Kreis         0,00  0,0   0,0%     inf Tage     397    300                0,27  0,33   9  l
    Mannheim (Stadtkreis)      1,5  0,5   1,2%    60,5 Tage     483    156     [159, 160] 0,10 -0,14   7  l
    Neckar-Odenwald-Kreis     0,27  0,2   0,1%     inf Tage     437    304                0,14  0,33   9  l
    Ortenaukreis              1,00  0,2   0,1%     inf Tage    1216    283     [283, 283] 0,25  0,07  11  l
    Ostalbkreis                6,8  2,2   1,1%    61,4 Tage    1354    431     [441, 447] 0,15 -0,07  14  l
    Pforzheim (Stadtkreis)     6,4  5,1   3,0%    23,8 Tage     395    315     [341, 358] 0,22 -0,11   7  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     518    224                0,29  0,65  10  l
    Ravensburg                0,00  0,0   0,0%     inf Tage     560    197                0,23  1,70  10  l
    Rems-Murr-Kreis           0,00  0,0   0,0%     inf Tage    1573    369                0,25  1,35   8  l
    Reutlingen                0,00  0,0   0,0%     inf Tage    1529    533                0,13 -0,14   7  l
    Rhein-Neckar-Kreis        0,00  0,0   0,0%     inf Tage     949    173                0,20  0,53   8  l
    Rottweil                   2,0  1,4   1,2%    59,2 Tage     679    487     [494, 499] 0,13  0,20   7  l
    Schwäbisch Hall           0,00  0,0   0,0%     inf Tage     860    439                0,18  1,57   7  l
    Schwarzwald-Baar-Kreis    0,00  0,0   0,0%     inf Tage     549    258                0,23  0,83  12  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     777    594                1,00  0,00   7  l
    Stuttgart                  2,0  0,3   0,1%     inf Tage    1469    231     [232, 232] 0,34  0,12  10  l
    Tübingen                  0,26  0,1   0,0%     inf Tage    1285    565     [565, 565] 0,20  0,19  14  l
    Tuttlingen                 1,2  0,9   1,1%    63,0 Tage     502    358     [363, 366] 0,23 -0,14   7  l
    Ulm (Stadtkreis)           1,5  1,2   1,7%    42,2 Tage     284    225     [231, 235] 0,32 -0,14   7  l
    Waldshut                   1,7  1,0   2,0%    35,7 Tage     310    182                0,30 -1,45  10  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1193    631                0,33  0,38   9  l
    
    Baden-Württemberg           72  0,7   0,7%   104,0 Tage   34708    314     [317, 318] 0,40  0,00   7  l


Stand 24.05.2020

    Alb-Donau-Kreis           0,00  0,0   0,0%     inf Tage     627    320                0,24  0,42  13  l
    Baden-Baden (Stadtkreis   0,05  0,1   0,0%     inf Tage     184    334                0,05  0,82  11  l
    Biberach                  0,50  0,3   0,1%     inf Tage     576    288                0,18  0,71   7  l
    Böblingen                 0,68  0,2   0,6%   118,3 Tage    1330    340     [341, 341] 0,31 -0,14   7  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     289    134                0,19 -1,00   8  l
    Breisgau-Hochschwarzwal   0,00  0,0   0,0%     inf Tage    1120    426                0,60  0,44  14  l
    Calw                      0,00  0,0   0,0%     inf Tage     732    462                0,46  0,65  12  l
    Emmendingen               0,59  0,4   0,8%    86,9 Tage     513    310                0,24 -1,92  12  l
    Enzkreis                  0,00  0,0   0,0%     inf Tage     631    317                0,19  1,00  11  l
    Esslingen                  4,2  0,8   0,2%     inf Tage    1799    337     [340, 341] 0,06  0,02  13  l
    Freiburg im Breisgau (S    2,4  1,0   1,0%    66,6 Tage     958    416                0,38 -0,35  12  l
    Freudenstadt              0,73  0,6   0,7%    99,4 Tage     567    481     [484, 486] 0,15 -0,11   9  l
    Göppingen                 0,00  0,0   0,0%     inf Tage     776    302                0,13 -1,46  14  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     292    182                1,00  0,00   7  l
    Heidenheim                0,67  0,5   0,7%   102,9 Tage     510    385     [388, 389] 0,16 -0,12   8  l
    Heilbronn                  1,0  0,3   0,1%     inf Tage     937    273     [273, 273] 0,15  0,06  11  l
    Heilbronn (Stadtkreis)     1,9  1,5   1,4%    50,8 Tage     431    342     [350, 355] 0,28 -0,10  10  l
    Hohenlohekreis            0,62  0,6   0,1%     inf Tage     766    684                0,10  0,42  10  l
    Karlsruhe                  4,7  1,0   1,1%    62,3 Tage     955    215     [220, 223] 0,25 -0,07  14  l
    Karlsruhe (Stadtkreis)    0,00  0,0   0,0%     inf Tage     383    122                0,37  4,33   9  l
    Konstanz                   1,4  0,5   1,2%    59,7 Tage     463    162     [165, 166] 0,10 -0,14   7  l
    Lörrach                   0,00  0,0   0,0%     inf Tage     664    290                0,37  1,29  12  l
    Ludwigsburg               0,05  0,0   0,0%     inf Tage    1737    319     [319, 319] 0,45  0,25  11  l
    Main-Tauber-Kreis         0,32  0,2   0,1%     inf Tage     397    300                0,24  0,31  11  l
    Mannheim (Stadtkreis)      1,1  0,4   1,0%    69,3 Tage     477    154     [156, 157] 0,27 -0,29   9  l
    Neckar-Odenwald-Kreis     0,41  0,3   0,1%     inf Tage     433    302     [302, 302] 0,41  0,18  11  l
    Ortenaukreis               9,0  2,1   1,2%    58,9 Tage    1198    279     [288, 293] 0,06 -0,03  14  l
    Ostalbkreis                5,0  1,6   1,3%    54,3 Tage    1324    422     [430, 435] 0,38 -0,12   8  l
    Pforzheim (Stadtkreis)     5,2  4,1   2,6%    26,6 Tage     369    294     [315, 328] 0,21 -0,12   8  l
    Rastatt                    2,3  1,0   1,3%    53,3 Tage     516    223     [228, 231] 0,21 -0,18  10  l
    Ravensburg                0,00  0,0   0,0%     inf Tage     557    196                0,22  0,21  12  l
    Rems-Murr-Kreis             16  3,7   2,3%    30,5 Tage    1544    362     [381, 394] 0,15 -0,11   9  l
    Reutlingen                 3,6  1,2   1,6%    43,8 Tage    1516    529     [538, 545] 0,14 -0,16  10  l
    Rhein-Neckar-Kreis        0,00  0,0   0,0%     inf Tage     947    173                0,36  0,16  12  l
    Rottweil                   1,8  1,3   1,2%    59,3 Tage     674    483     [490, 495] 0,60 -0,14   7  l
    Schwäbisch Hall            5,5  2,8   1,9%    36,8 Tage     854    436     [451, 462] 0,33 -0,12   8  l
    Schwarzwald-Baar-Kreis    0,25  0,1   0,0%     inf Tage     548    258     [258, 258] 0,22  0,09  13  l
    Sigmaringen               0,04  0,0   0,0%     inf Tage     777    594     [594, 594] 0,00 -0,08  13  l
    Stuttgart                  3,4  0,5   0,2%     inf Tage    1450    228     [230, 230] 0,23  0,03  12  l
    Tübingen                  0,00  0,0   0,0%     inf Tage    1280    563                0,47  0,34  11  l
    Tuttlingen                0,46  0,3   0,8%    92,2 Tage     498    355     [357, 359] 0,11 -0,14   7  l
    Ulm (Stadtkreis)          0,49  0,4   0,2%     inf Tage     279    221     [221, 221] 0,20  0,16  10  l
    Waldshut                  0,00  0,0   0,0%     inf Tage     304    178                0,50 -0,55  11  l
    Zollernalbkreis           0,96  0,5   0,1%     inf Tage    1185    627     [628, 628] 0,23  0,22  10  l
    
    Baden-Württemberg           80  0,7   1,6%    44,8 Tage   34367    310     [314, 316] 0,38 -0,06   7  e

Stand 20.05.2020

    Alb-Donau-Kreis           0,00  0,0   0,0%     inf Tage     622    317                0,26  0,42  11  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     183    332                0,17 -0,12   8  l
    Biberach                  0,00  0,0   0,0%     inf Tage     570    285                0,23  0,23  13  l
    Böblingen                 0,00  0,0   0,0%     inf Tage    1328    339                0,37  0,29  13  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     290    134                0,23  0,71   7  l
    Breisgau-Hochschwarzwal   0,00  0,0   0,0%     inf Tage    1122    427                0,55  0,10  11  l
    Calw                      0,00  0,0   0,0%     inf Tage     731    461                0,72  0,75   8  l
    Emmendingen               0,38  0,2   0,9%    80,1 Tage     512    310     [311, 313] 0,18 -0,11   9  l
    Enzkreis                  0,00  0,0   0,0%     inf Tage     622    313                0,39  2,43   7  l
    Esslingen                  2,5  0,5   0,1%     inf Tage    1778    333     [334, 335] 0,53 -0,08   7  e
    Freiburg im Breisgau (S    2,6  1,1   1,5%    47,4 Tage     953    414                0,60 -1,00   8  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     565    479                0,34  0,29  13  l
    Göppingen                  2,2  0,8   1,2%    58,1 Tage     790    307     [312, 315] 0,20  0,00   7  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     292    182                0,17 -0,12   8  l
    Heidenheim                0,00  0,0   0,0%     inf Tage     508    383                0,38  0,34  12  l
    Heilbronn                  2,1  0,6   0,2%     inf Tage     929    271     [272, 272] 0,08  0,05   7  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     424    337                0,51  0,46   8  l
    Hohenlohekreis             3,1  2,8   1,8%    38,6 Tage     761    679                0,12 -0,76   7  l
    Karlsruhe                  2,5  0,6   0,8%    85,3 Tage     937    211     [213, 215] 0,11 -0,09  11  l
    Karlsruhe (Stadtkreis)    0,00  0,0   0,0%     inf Tage     383    122                0,12  1,29  12  l
    Konstanz                  0,00  0,0   0,0%     inf Tage     458    161                0,46  0,75   8  l
    Lörrach                   0,00  0,0   0,0%     inf Tage     664    290                0,39  1,19   8  l
    Ludwigsburg               0,00  0,0   0,0%     inf Tage    1728    318                0,80  0,30   7  l
    Main-Tauber-Kreis         0,14  0,1   0,0%     inf Tage     394    298                0,53  0,43   7  l
    Mannheim (Stadtkreis)     0,11  0,0   0,0%     inf Tage     473    153     [153, 153] 0,07  0,08  13  l
    Neckar-Odenwald-Kreis      1,3  0,9   0,3%     inf Tage     428    298     [301, 301] 0,46  0,06   7  e
    Ortenaukreis               7,2  1,7   1,2%    57,7 Tage    1160    270     [278, 282] 0,08 -0,06  11  l
    Ostalbkreis               0,00  0,0   0,0%     inf Tage    1311    418                0,41  0,63   7  l
    Pforzheim (Stadtkreis)    0,00  0,0   0,0%     inf Tage     351    280                0,78  0,40   7  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     507    219                0,19  0,28  14  l
    Ravensburg                0,00  0,0   0,0%     inf Tage     551    194                0,39  0,28   8  l
    Rems-Murr-Kreis           0,00  0,0   0,0%     inf Tage    1495    351                0,34  0,46   9  l
    Reutlingen                0,00  0,0   0,0%     inf Tage    1514    528                0,13 -1,11  12  l
    Rhein-Neckar-Kreis        0,00  0,0   0,0%     inf Tage     940    172                0,48  0,15   8  l
    Rottweil                  0,00  0,0   0,0%     inf Tage     669    480                0,40  1,06   7  l
    Schwäbisch Hall           0,00  0,0   0,0%     inf Tage     839    428                0,28  0,52  10  l
    Schwarzwald-Baar-Kreis     1,2  0,6   0,2%     inf Tage     546    257     [259, 259] 0,08  0,07   9  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     777    594                1,00  0,00   7  l
    Stuttgart                  1,8  0,3   0,1%     inf Tage    1428    225     [225, 225] 0,52  0,27   7  l
    Tübingen                  0,54  0,2   0,0%     inf Tage    1276    561                0,48  0,37   7  l
    Tuttlingen                0,00  0,0   0,0%     inf Tage     497    355                0,40  0,50  13  l
    Ulm (Stadtkreis)           3,2  2,5   2,2%    32,4 Tage     277    219     [232, 239] 0,41 -0,13  13  l
    Waldshut                  0,00  0,0   0,0%     inf Tage     311    182                0,46  2,43   7  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1177    623                0,57  0,21  14  l
    
    Baden-Württemberg           25  0,2   0,1%     inf Tage   34071    308     [308, 308] 0,60  0,24   7  l

Stand 16.05.2020

    Alb-Donau-Kreis            1,4  0,7   0,2%     inf Tage     612    312                0,25  0,49   7  l
    Baden-Baden (Stadtkreis   0,21  0,4   0,6%   119,9 Tage     183    332     [334, 335] 0,10 -0,08  13  l
    Biberach                  0,00  0,0   0,0%     inf Tage     562    281                0,59  0,33   9  l
    Böblingen                 0,00  0,0   0,0%     inf Tage    1327    339                0,42  0,27   9  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     289    134                0,30  1,67   9  l
    Breisgau-Hochschwarzwal    1,9  0,7   0,2%     inf Tage    1121    427     [428, 428] 0,25  0,05   7  l
    Calw                      0,00  0,0   0,0%     inf Tage     731    461                0,36  0,16   8  l
    Emmendingen               0,07  0,0   0,7%   100,5 Tage     512    310                0,06  1,67   9  l
    Enzkreis                   2,5  1,3   0,4%     inf Tage     619    311     [313, 313] 0,12  0,24   8  l
    Esslingen                  8,4  1,6   1,2%    60,5 Tage    1760    330     [337, 341] 0,29 -0,09   9  l
    Freiburg im Breisgau (S   0,00  0,0   0,0%     inf Tage     947    411                0,59  0,38  12  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     564    478                0,47  0,33   9  l
    Göppingen                 0,36  0,1   0,0%     inf Tage     784    305     [305, 305] 0,37 -0,05   7  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     292    182                0,17  0,44  12  l
    Heidenheim                0,00  0,0   0,0%     inf Tage     507    383                0,35  0,31   8  l
    Heilbronn                  5,1  1,5   1,6%    44,4 Tage     919    268     [275, 280] 0,30 -0,08   8  l
    Heilbronn (Stadtkreis)     1,1  0,9   1,0%    72,6 Tage     424    337     [341, 344] 0,07 -0,12   8  l
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage     756    675                0,04  0,33   9  l
    Karlsruhe                  3,1  0,7   1,4%    50,5 Tage     930    209     [213, 216] 0,44 -0,14   7  l
    Karlsruhe (Stadtkreis)     2,3  0,7   2,1%    33,7 Tage     382    122     [126, 130] 0,38 -0,14   7  l
    Konstanz                  0,53  0,2   0,1%     inf Tage     457    160     [160, 160] 0,13  0,26  10  l
    Lörrach                   1,00  0,4   0,2%     inf Tage     662    290     [291, 291] 0,04  0,14   8  l
    Ludwigsburg                3,6  0,7   0,2%     inf Tage    1717    316     [317, 317] 0,16  0,09   9  l
    Main-Tauber-Kreis         0,05  0,0   0,0%     inf Tage     391    295                0,15  0,64  13  l
    Mannheim (Stadtkreis)     0,00  0,0   0,0%     inf Tage     472    153                0,31  0,60  14  l
    Neckar-Odenwald-Kreis      4,4  3,1   2,1%    32,8 Tage     421    293     [308, 318] 0,22 -0,12   8  l
    Ortenaukreis               6,5  1,5   1,4%    49,1 Tage    1136    265     [272, 276] 0,12 -0,08   7  l
    Ostalbkreis                 11  3,4   2,1%    33,6 Tage    1304    415     [433, 445] 0,28 -0,14   7  l
    Pforzheim (Stadtkreis)     8,9  7,1   3,7%    18,9 Tage     346    276     [310, 332] 0,17  0,03   7  l
    Rastatt                   0,00  0,0   0,0%     inf Tage     505    219                0,31  1,14   7  l
    Ravensburg                 4,2  1,5   1,6%    42,4 Tage     550    193     [201, 205] 0,34 -0,08  13  l
    Rems-Murr-Kreis             16  3,8   1,9%    35,9 Tage    1485    348     [366, 377] 0,04 -0,14   7  l
    Reutlingen                0,00  0,0   0,0%     inf Tage    1511    527                0,55 -0,69   7  l
    Rhein-Neckar-Kreis         9,4  1,7   2,0%    34,5 Tage     935    171     [179, 184] 0,29 -0,08  12  l
    Rottweil                   1,1  0,8   0,2%     inf Tage     667    478                0,13  0,37  13  l
    Schwäbisch Hall            3,7  1,9   1,0%    72,8 Tage     837    427     [436, 441] 0,13 -0,07  14  l
    Schwarzwald-Baar-Kreis    0,80  0,4   0,1%     inf Tage     539    254     [254, 254] 0,20  0,17  14  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     777    594                0,48  0,75   8  l
    Stuttgart                  8,9  1,4   1,2%    57,2 Tage    1411    222     [229, 232] 0,21 -0,08  12  l
    Tübingen                   5,2  2,3   1,1%    64,4 Tage    1267    557     [568, 575] 0,17 -0,10  10  l
    Tuttlingen                0,00  0,0   0,0%     inf Tage     497    355                0,34  0,44   9  l
    Ulm (Stadtkreis)           2,1  1,7   2,1%    32,8 Tage     267    211     [220, 227] 0,45 -0,24   9  l
    Waldshut                   1,4  0,8   1,5%    47,4 Tage     311    182     [187, 190] 0,23 -0,11   9  l
    Zollernalbkreis           0,53  0,3   0,0%     inf Tage    1170    619     [619, 619] 0,57  0,22  10  l
    
    Baden-Württemberg           90  0,8   0,3%     inf Tage   33856    306     [308, 309] 0,23  0,05  10  l


Stand 12.05.2020

    Alb-Donau-Kreis             14  6,9   3,7%    19,0 Tage     597    305     [340, 363] 0,39 -0,11   9  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     182    330                1,00  0,00   7  l
    Biberach                   2,3  1,1   0,4%     inf Tage     562    281     [284, 284] 0,12  0,05  13  l
    Böblingen                  2,7  0,7   0,7%   100,9 Tage    1323    338     [341, 343] 0,04 -0,10  10  l
    Bodenseekreis             0,33  0,2   0,1%     inf Tage     288    133                0,03  0,31   8  l
    Breisgau-Hochschwarzwal    4,6  1,7   1,4%    51,3 Tage    1112    423     [432, 438] 0,50 -0,13   8  l
    Calw                       3,7  2,3   0,5%     inf Tage     723    456     [462, 463] 0,07  0,03   7  l
    Emmendingen               0,00  0,0   0,0%     inf Tage     514    311                0,11  0,85  13  l
    Enzkreis                   5,8  2,9   1,6%    42,8 Tage     598    301     [314, 321] 0,04 -0,09   9  l
    Esslingen                  2,9  0,5   0,2%     inf Tage    1731    324     [326, 326] 0,12  0,11  12  l
    Freiburg im Breisgau (S   0,58  0,3   0,1%     inf Tage     953    414     [414, 414] 0,20  0,25  13  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     563    477                0,23  1,40  10  l
    Göppingen                 0,58  0,2   0,1%     inf Tage     780    303                0,25  0,39   8  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     289    180                0,48  0,75   8  l
    Heidenheim                0,00  0,0   0,0%     inf Tage     504    380                0,34  0,77  12  l
    Heilbronn                 0,00  0,0   0,0%     inf Tage     902    263                0,28  0,19  14  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     419    333                0,46  2,43   7  l
    Hohenlohekreis             2,1  1,9   0,9%    76,4 Tage     757    676     [685, 691] 0,23 -0,15  13  l
    Karlsruhe                 0,00  0,0   0,0%     inf Tage     922    208                0,23  1,16  10  l
    Karlsruhe (Stadtkreis)    0,36  0,1   0,1%     inf Tage     377    120                0,12  0,49  12  l
    Konstanz                  0,27  0,1   0,1%     inf Tage     452    158     [158, 158] 0,22  0,21  11  l
    Lörrach                   0,00  0,0   0,0%     inf Tage     654    286                0,28  1,62  14  l
    Ludwigsburg                8,5  1,6   1,2%    58,8 Tage    1693    311     [318, 323] 0,07 -0,10  10  l
    Main-Tauber-Kreis         0,00  0,0   0,0%     inf Tage     384    290                0,29  1,02   9  l
    Mannheim (Stadtkreis)     0,00  0,0   0,0%     inf Tage     470    152                0,63  0,16  12  l
    Neckar-Odenwald-Kreis      1,4  0,9   0,3%     inf Tage     407    284     [284, 284] 0,26  0,01   7  l
    Ortenaukreis               1,6  0,4   0,1%     inf Tage    1111    259     [259, 259] 0,42  0,13  13  l
    Ostalbkreis               0,00  0,0   0,0%     inf Tage    1265    403                0,69  0,13   7  l
    Pforzheim (Stadtkreis)     4,6  3,7   1,8%    39,9 Tage     315    251     [267, 275] 0,01 -0,03  10  l
    Rastatt                    1,9  0,8   1,4%    49,6 Tage     504    218                0,25 -0,44   9  l
    Ravensburg                0,96  0,3   0,7%    94,0 Tage     532    187     [189, 190] 0,10 -0,11   9  l
    Rems-Murr-Kreis             18  4,3   2,1%    33,2 Tage    1437    337     [357, 369] 0,17 -0,09  11  l
    Reutlingen                0,79  0,3   0,1%     inf Tage    1539    537     [537, 537] 0,24 -0,06   7  l
    Rhein-Neckar-Kreis        0,00  0,0   0,0%     inf Tage     894    163                0,27  0,88  10  l
    Rottweil                  0,00  0,0   0,0%     inf Tage     656    470                0,30  0,15  14  l
    Schwäbisch Hall            4,1  2,1   1,3%    54,2 Tage     826    422     [432, 438] 0,20 -0,10  10  l
    Schwarzwald-Baar-Kreis    0,77  0,4   0,1%     inf Tage     531    250     [250, 250] 0,36  0,16  13  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     776    593                0,13  0,21  14  l
    Stuttgart                  6,6  1,0   1,2%    59,4 Tage    1377    217     [222, 225] 0,11 -0,12   8  l
    Tübingen                   4,5  2,0   1,3%    55,8 Tage    1250    550     [560, 567] 0,22  0,03   7  l
    Tuttlingen                0,63  0,4   0,1%     inf Tage     495    353     [354, 354] 0,17  0,11  12  l
    Ulm (Stadtkreis)          0,00  0,0   0,0%     inf Tage     261    207                0,33  0,65  14  l
    Waldshut                  0,71  0,4   1,1%    60,7 Tage     307    180     [182, 184] 0,11 -0,14   7  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1161    614                0,44  0,33  12  l
    
    Baden-Württemberg           95  0,9   0,3%     inf Tage   33393    302     [304, 305] 0,31  0,04  14  l

Stand 08.05.2020

    Alb-Donau-Kreis            4,8  2,4   3,1%    22,8 Tage     551    281     [298, 311] 0,70 -0,16   4  l
    Baden-Baden (Stadtkreis   0,00  0,0   0,0%     inf Tage     182    330                1,00  0,00   4  l
    Biberach                   6,0  3,0   3,1%    22,6 Tage     546    273     [292, 306] 0,60 -0,20   5  l
    Böblingen                  4,6  1,2   2,0%    34,8 Tage    1313    335     [344, 351] 0,73 -0,25   4  l
    Bodenseekreis              1,9  0,9   2,1%    33,7 Tage     287    133     [138, 141] 0,25 -0,14   7  l
    Breisgau-Hochschwarzwal    3,2  1,2   1,8%    38,7 Tage    1099    418     [427, 434] 0,79 -0,25   4  l
    Calw                       2,1  1,3   0,3%     inf Tage     698    441     [443, 443] 0,23  0,20  14  l
    Emmendingen               0,00  0,0   0,0%     inf Tage     513    310                0,28  1,67   9  l
    Enzkreis                  0,00  0,0   0,0%     inf Tage     571    287                0,51  0,21  13  l
    Esslingen                 1,00  0,2   0,1%     inf Tage    1710    320     [320, 320] 0,32  0,16   8  l
    Freiburg im Breisgau (S    2,2  0,9   0,9%    78,9 Tage     949    412     [417, 420] 0,23 -0,14   7  l
    Freudenstadt               1,4  1,2   1,4%    49,5 Tage     560    475     [482, 488] 0,50 -0,20   5  l
    Göppingen                  1,8  0,7   0,2%     inf Tage     776    302                0,57  0,41   4  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     289    180                0,54  0,50   4  l
    Heidenheim                0,00  0,0   0,0%     inf Tage     489    369                0,57  1,12   8  l
    Heilbronn                  5,9  1,7   2,6%    26,6 Tage     898    262     [274, 283] 0,82 -0,25   4  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     419    333                0,37  0,27  14  l
    Hohenlohekreis             2,0  1,8   1,2%    58,7 Tage     750    670     [679, 686] 0,50 -0,26   9  l
    Karlsruhe                 0,00  0,0   0,0%     inf Tage     917    206                0,33  2,17   6  l
    Karlsruhe (Stadtkreis)    0,20  0,1   0,1%     inf Tage     368    118     [118, 118] 0,80  0,33   5  l
    Konstanz                  0,00  0,0   0,0%     inf Tage     447    157                0,36  0,22  14  l
    Lörrach                   0,00  0,0   0,0%     inf Tage     649    284                0,37  1,90  10  l
    Ludwigsburg                9,1  1,7   2,6%    26,9 Tage    1659    305     [317, 328] 0,60 -0,25   4  l
    Main-Tauber-Kreis         0,00  0,0   0,0%     inf Tage     379    286                0,37  1,67   5  l
    Mannheim (Stadtkreis)     0,00  0,0   0,0%     inf Tage     467    151                0,73  0,14   8  l
    Neckar-Odenwald-Kreis      9,1  6,3   5,2%    13,8 Tage     400    279     [320, 353] 0,98 -0,25   4  l
    Ortenaukreis               1,9  0,4   0,2%     inf Tage    1090    254     [254, 254] 0,63  0,16   9  l
    Ostalbkreis                 18  5,7   3,0%    23,6 Tage    1245    396     [427, 447] 0,41 -0,17   6  l
    Pforzheim (Stadtkreis)    0,67  0,5   0,2%     inf Tage     291    232     [232, 232] 0,55  0,13  13  l
    Rastatt                    1,8  0,8   2,2%    31,4 Tage     499    216                0,45 -1,00   5  l
    Ravensburg                 1,4  0,5   1,8%    39,7 Tage     529    186     [190, 193] 0,60 -0,25   4  l
    Rems-Murr-Kreis             20  4,8   3,1%    23,1 Tage    1389    326     [351, 369] 0,59 -0,14   7  l
    Reutlingen                  12  4,3   8,9%     8,2 Tage    1513    528                0,46 -0,58   6  e
    Rhein-Neckar-Kreis        0,00  0,0   0,0%     inf Tage     888    162                0,61  1,83   6  l
    Rottweil                   5,6  4,0   3,0%    23,4 Tage     649    465     [492, 514] 0,96 -0,25   4  l
    Schwäbisch Hall            4,4  2,2   7,7%     9,3 Tage     814    416     [443, 495] 0,89 -0,23   4  e
    Schwarzwald-Baar-Kreis    0,00  0,0   0,0%     inf Tage     521    245                0,60  0,35   6  l
    Sigmaringen               0,00  0,0   0,0%     inf Tage     773    591                0,35  0,13  14  l
    Stuttgart                  8,6  1,4   2,7%    25,8 Tage    1354    213     [223, 231] 0,86 -0,25   4  l
    Tübingen                  0,00  0,0   0,0%     inf Tage    1235    543                0,90  0,47   5  l
    Tuttlingen                 3,9  2,8   3,1%    22,4 Tage     489    349     [369, 386] 0,75 -0,25   4  l
    Ulm (Stadtkreis)          0,00  0,0   0,0%     inf Tage     260    206                0,38  0,17   8  l
    Waldshut                  0,07  0,0   0,0%     inf Tage     306    179                0,37  0,43   7  l
    Zollernalbkreis           0,00  0,0   0,0%     inf Tage    1137    602                0,52  0,41   8  l
    
    Baden-Württemberg          171  1,5   5,1%    14,1 Tage   32868    297     [308, 322] 0,68 -0,16   4  e

Stand 04.05.2020

    Alb-Donau-Kreis           0,00  0,0   0,0%     inf Tage     542    276                0,99  0,61   4  l
    Baden-Baden (Stadtkreis    2,1  3,7   2,1%    32,9 Tage     182    330     [348, 359] 0,11 -0,10  10  l
    Biberach                   1,8  0,9   0,3%     inf Tage     532    266                0,29  0,69   4  l
    Böblingen                 0,00  0,0   0,0%     inf Tage    1306    333                0,70  1,00   4  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     282    130                1,00  0,00   4  l
    Breisgau-Hochschwarzwal    3,4  1,3   0,3%     inf Tage    1094    416     [418, 418] 0,40  0,30   5  l
    Calw                      0,77  0,5   0,1%     inf Tage     682    431     [431, 431] 0,48  0,20  14  l
    Emmendingen               0,00  0,0   0,0%     inf Tage     513    310                0,50  1,40   5  l
    Enzkreis                  0,00  0,0   0,0%     inf Tage     561    282                0,64  0,22   9  l
    Esslingen                  3,3  0,6   0,2%     inf Tage    1697    318     [318, 318] 0,42  0,12   4  l
    Freiburg im Breisgau (S   0,00  0,0   0,0%     inf Tage     941    409                0,68  0,76   5  l
    Freudenstadt              0,00  0,0   0,0%     inf Tage     557    472                0,19  0,71  14  l
    Göppingen                 0,00  0,0   0,0%     inf Tage     761    296                0,46  0,28  12  l
    Heidelberg (Stadtkreis)    1,1  0,7   2,0%    34,8 Tage     281    175     [180, 184] 0,80 -0,25   4  l
    Heidenheim                 2,4  1,8   0,5%     inf Tage     485    366                0,95  0,60   4  e
    Heilbronn                 0,00  0,0   0,0%     inf Tage     887    259                0,64  2,15   4  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     415    329                0,89  1,25   4  l
    Hohenlohekreis            0,00  0,0   0,0%     inf Tage     744    664                1,00  0,00   4  l
    Karlsruhe                  6,3  1,4   1,9%    37,4 Tage     912    205     [213, 218] 0,18 -0,11   7  l
    Karlsruhe (Stadtkreis)    0,00  0,0   0,0%     inf Tage     365    117                0,51  1,62   4  l
    Konstanz                  0,80  0,3   0,2%     inf Tage     442    155     [155, 155] 0,34  0,23  10  l
    Lörrach                   0,00  0,0   0,0%     inf Tage     644    282                0,53  2,19   6  l
    Ludwigsburg               0,00  0,0   0,0%     inf Tage    1646    303                0,40  0,15  11  l
    Main-Tauber-Kreis          9,7  7,3   5,8%    12,4 Tage     373    282     [331, 371] 0,46 -0,16   4  l
    Mannheim (Stadtkreis)      6,5  2,1   2,7%    25,8 Tage     464    150     [161, 168] 0,49 -0,12   8  l
    Neckar-Odenwald-Kreis      1,1  0,7   0,3%     inf Tage     381    265                0,23  0,57  10  l
    Ortenaukreis               8,0  1,9   0,7%     inf Tage    1075    250     [254, 254] 0,79  0,13   5  l
    Ostalbkreis                2,6  0,8   0,2%     inf Tage    1195    381                0,52  0,48   5  l
    Pforzheim (Stadtkreis)     1,4  1,1   0,5%     inf Tage     280    223     [225, 226] 0,72  0,21   5  e
    Rastatt                   0,00  0,0   0,0%     inf Tage     496    215                0,64  0,25   4  l
    Ravensburg                0,00  0,0   0,0%     inf Tage     527    185                0,45  0,19  13  l
    Rems-Murr-Kreis           0,00  0,0   0,0%     inf Tage    1320    310                0,73  0,37   6  l
    Reutlingen                0,00  0,0   0,0%     inf Tage    1461    510                0,82  0,20  11  l
    Rhein-Neckar-Kreis         9,0  1,6   2,9%    24,2 Tage     890    163     [172, 180] 0,50 -0,20   5  l
    Rottweil                   6,1  4,4   1,0%     inf Tage     638    457     [469, 469] 0,07  0,12   6  l
    Schwäbisch Hall           0,00  0,0   0,0%     inf Tage     804    410                0,90  1,00   4  l
    Schwarzwald-Baar-Kreis     7,8  3,7   6,0%    11,9 Tage     515    242     [267, 291] 0,70 -0,12   4  e
    Sigmaringen               0,00  0,0   0,0%     inf Tage     772    590                0,38  0,09  14  l
    Stuttgart                  4,1  0,6   0,3%     inf Tage    1340    211     [212, 212] 0,32  0,23   4  l
    Tübingen                   4,6  2,0   1,8%    38,7 Tage    1229    541     [554, 564] 0,75 -0,25   4  l
    Tuttlingen                 2,0  1,4   0,4%     inf Tage     483    345     [346, 346] 0,26  0,06   4  l
    Ulm (Stadtkreis)          0,00  0,0   0,0%     inf Tage     258    204     [204, 204] 0,45  0,12   4  l
    Waldshut                  0,00  0,0   0,0%     inf Tage     304    178                0,38  1,03   9  l
    Zollernalbkreis            5,7  3,0   0,5%     inf Tage    1113    589     [590, 590] 0,81  0,45   4  l
    
    Baden-Württemberg          113  1,0   0,3%     inf Tage   32389    293     [295, 295] 0,99  0,19   4  e


Stand 23.04.2020

    Alb-Donau-Kreis             15  7,6   4,2%    16,7 Tage     501    256     [293, 318] 0,29 -0,11   9  l
    Baden-Baden (Stadtkreis   0,81  1,5   0,5%     inf Tage     164    298     [300, 300] 0,89  0,34   4  e
    Biberach                   8,6  4,3   3,4%    20,5 Tage     472    236     [259, 275] 0,21 -0,11   5  l
    Böblingen                  6,0  1,5   0,5%     inf Tage    1272    325     [327, 327] 0,29  0,18  10  l
    Bodenseekreis             0,00  0,0   0,0%     inf Tage     276    128                0,37  0,11   7  l
    Breisgau-Hochschwarzwal     26  9,9   4,7%    15,2 Tage    1019    388     [444, 484] 0,18  0,06   4  l
    Calw                       7,4  4,7   1,2%     inf Tage     610    385     [398, 401] 0,25 -0,05   5  e
    Emmendingen               0,00  0,0   0,0%     inf Tage     507    307                0,68  1,40   5  l
    Enzkreis                    27   14  11,0%     6,6 Tage     473    238     [333, 432] 0,66 -0,17   5  e
    Esslingen                  6,9  1,3   0,4%     inf Tage    1563    293     [294, 294] 0,52  0,17  11  l
    Freiburg im Breisgau (S    7,2  3,1   0,8%     inf Tage     921    400     [407, 408] 0,52  0,11   6  l
    Freudenstadt               6,9  5,9   1,3%     inf Tage     522    443     [458, 461] 0,11  0,11  14  l
    Göppingen                   18  6,9   5,5%    12,9 Tage     700    272     [318, 354] 0,51 -0,07   4  l
    Heidelberg (Stadtkreis)   0,00  0,0   0,0%     inf Tage     267    167                0,14 -0,60   8  l
    Heidenheim                 2,7  2,0   0,7%     inf Tage     409    309     [311, 311] 0,55  0,23   4  l
    Heilbronn                  8,1  2,4   1,0%     inf Tage     800    233     [236, 236] 0,43  0,20   6  l
    Heilbronn (Stadtkreis)    0,00  0,0   0,0%     inf Tage     386    306                0,80  2,45   4  l
    Hohenlohekreis              11  9,6   4,4%    15,9 Tage     717    640     [709, 767] 0,72 -0,25   4  l
    Karlsruhe                  5,8  1,3   0,7%     inf Tage     838    189     [190, 190] 0,33  0,23   5  l
    Karlsruhe (Stadtkreis)    0,00  0,0   0,0%     inf Tage     322    103                0,32  0,11  14  l
    Konstanz                  0,96  0,3   0,2%     inf Tage     397    139     [139, 139] 0,42  0,15   7  l
    Lörrach                     13  5,8   3,3%    21,1 Tage     526    230     [257, 273] 0,32 -0,05  11  l
    Ludwigsburg                9,2  1,7   0,6%     inf Tage    1461    269     [272, 272] 0,16  0,12  14  l
    Main-Tauber-Kreis          5,6  4,2   3,9%    18,0 Tage     329    249     [274, 293] 0,20  0,05   4  l
    Mannheim (Stadtkreis)      1,1  0,4   0,3%     inf Tage     424    137     [137, 137] 0,60  0,19   7  l
    Neckar-Odenwald-Kreis      2,3  1,6   0,8%     inf Tage     300    209     [212, 212] 0,80  0,32   7  e
    Ortenaukreis                18  4,2   4,4%    16,0 Tage     936    218     [244, 264] 0,30 -0,25   4  l
    Ostalbkreis                 17  5,3   1,6%     inf Tage    1031    328     [339, 341] 0,95  0,20   4  e
    Pforzheim (Stadtkreis)      14   11   9,3%     7,8 Tage     209    166     [232, 281] 0,33 -0,16   4  l
    Rastatt                   0,93  0,4   0,2%     inf Tage     473    205     [205, 205] 0,57  0,26   7  l
    Ravensburg                 6,3  2,2  12,2%     6,0 Tage     511    180     [224, 355] 0,75 -0,31   4  e
    Rems-Murr-Kreis             37  8,8   5,7%    12,4 Tage    1106    260     [310, 347] 0,29 -0,20   5  l
    Reutlingen                0,00  0,0   0,0%     inf Tage    1314    458                0,52  0,43  10  l
    Rhein-Neckar-Kreis         8,4  1,5   1,0%     inf Tage     856    156                0,08  0,51   8  l
    Rottweil                   2,8  2,0   0,5%     inf Tage     542    389     [390, 390] 0,30  0,18   7  l
    Schwäbisch Hall            6,8  3,5   0,9%     inf Tage     726    371     [380, 383] 0,29  0,10   6  e
    Schwarzwald-Baar-Kreis     9,6  4,5   4,5%    15,7 Tage     445    210     [237, 257] 0,19 -0,10   4  l
    Sigmaringen                 15   12   4,4%    16,2 Tage     734    561     [630, 682] 0,79 -0,19   4  l
    Stuttgart                  4,3  0,7   0,3%     inf Tage    1262    199     [199, 199] 0,40  0,21  13  l
    Tübingen                    16  7,0   4,1%    17,3 Tage    1180    519     [568, 609] 0,93 -0,25   4  l
    Tuttlingen                1,00  0,7   0,2%     inf Tage     402    287     [287, 287] 0,47  0,09   8  l
    Ulm (Stadtkreis)           3,6  2,8   4,5%    15,9 Tage     233    184     [205, 221] 0,58 -0,25   4  l
    Waldshut                  0,00  0,0   0,0%     inf Tage     284    166                0,55  0,83   6  l
    Zollernalbkreis             28   15   4,5%    15,9 Tage     930    492     [568, 618] 0,14 -0,09   5  l
    
    Baden-Württemberg          350  3,2   1,2%     inf Tage   29350    265     [275, 277] 0,41  0,08   8  l

In den nachfolgenden Tabellen wurden die kumulativen Fallzahlen und nicht die täglichen Zuwächse für die Annäherungen verwendet.

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

---

<a name="todesfaelle"></a>
#### Todesfälle


    Landkreis               Zuwachs Zuwachs Wachst.- Verdoppl.  Gesamte   pro     R^2  Diff. Fenster Exp/Lin
                                      pro    rate      zeit      Fälle  100.000              größe
                                    100.000

Stand 22.10.2021

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     183     93    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,04   0,06   0,1%     inf Tage      71    129    0,04 -0,14   7  l
    Biberach                   0,50   0,25   1,0%    66,5 Tage     191     96    0,10 -0,14   7  l
    Böblingen                  0,33   0,09   0,7%    93,3 Tage     290     74    0,17 -0,13   8  l
    Bodenseekreis              0,67   0,31   1,5%    47,8 Tage     168     78    0,17 -0,13   8  l
    Breisgau-Hochschwarzwald   0,46   0,18   1,2%    56,3 Tage     196     75    0,38 -0,14   7  l
    Calw                       0,00   0,00   0,0%     inf Tage     188    119    1,00  0,00   7  l
    Emmendingen                0,58   0,35   0,3%     inf Tage     177    107    0,10  0,23   8  l
    Enzkreis                   0,04   0,02   0,0%     inf Tage     268    135    0,04 -0,14   7  l
    Esslingen                  0,36   0,07   0,6%   121,1 Tage     567    106    0,17 -0,14   7  l
    Freiburg im Breisgau (St   0,57   0,25   1,0%    69,9 Tage     174     76    0,16 -0,07  14  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage     163    138    0,17 -0,12   8  l
    Göppingen                  0,00   0,00   0,0%     inf Tage     255     99    0,14  0,75   8  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      65     41    1,00  0,00   7  l
    Heidenheim                 0,49   0,37   1,1%    64,9 Tage     172    130    0,08 -0,11   9  l
    Heilbronn                  0,42   0,12   0,8%    85,9 Tage     215     63    0,12 -0,10  10  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage     145    115    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage     139    124    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage     494    111    1,00  0,00   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     230     73    0,40  0,75   8  l
    Konstanz                   0,00   0,00   0,0%     inf Tage     306    107    1,00  0,00   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage     311    136    1,00  0,00   7  l
    Ludwigsburg                0,17   0,03   0,0%     inf Tage     530     97    0,10  0,17   8  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      94     71    0,21  0,33   9  l
    Mannheim (Stadtkreis)      0,46   0,15   1,0%    72,5 Tage     315    102    0,38 -0,14   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     143    100    1,00  0,00   7  l
    Ortenaukreis               0,83   0,19   0,7%   103,7 Tage     599    139    0,06 -0,12   8  l
    Ostalbkreis                0,71   0,23   1,0%    72,5 Tage     427    136    0,40 -0,14   7  l
    Pforzheim (Stadtkreis)     0,08   0,07   0,0%     inf Tage     214    170    0,16  0,31   8  l
    Rastatt                     1,1   0,47   1,6%    44,7 Tage     215     93    0,29 -0,13   8  l
    Ravensburg                 0,76   0,27   1,5%    47,4 Tage     152     53    0,42 -0,10  10  l
    Rems-Murr-Kreis            0,33   0,08   0,1%     inf Tage     383     90    0,21  0,15  12  l
    Reutlingen                 0,34   0,12   0,6%   124,2 Tage     280     98    0,06 -0,07  14  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage     461     84    0,35  0,16  14  l
    Rottweil                   0,53   0,38   1,1%    61,7 Tage     171    123    0,27 -0,10  10  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage     268    137    0,06  0,75   8  l
    Schwarzwald-Baar-Kreis     0,46   0,22   1,2%    60,0 Tage     221    104    0,38 -0,14   7  l
    Sigmaringen                0,67   0,51   2,1%    33,9 Tage      91     70    0,17 -0,13   8  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage     506     80    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage     190     84    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage     164    117    0,09  0,82  11  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage      89     70    1,00  0,00   7  l
    Waldshut                   0,17   0,10   0,4%   158,7 Tage     221    130    0,06 -0,07  14  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage     180     95    1,00  0,00   7  l
    
    Baden-Württemberg            13   0,12   3,4%    20,6 Tage   10882     98    0,31 -0,28   7  e

Stand 16.07.2021

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     179     91    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,17   0,31   0,9%    81,5 Tage      65    118    0,06 -0,07  14  l
    Biberach                   0,20   0,10   0,6%   124,4 Tage     178     89    0,10 -0,07  14  l
    Böblingen                  0,00   0,00   0,0%     inf Tage     275     70    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     158     73    1,00  0,00   7  l
    Breisgau-Hochschwarzwald    1,6   0,63   2,5%    28,2 Tage     188     72    0,62 -0,14   7  l
    Calw                       0,33   0,21   1,0%    73,0 Tage     183    116    0,17 -0,13   8  l
    Emmendingen                0,00   0,00   0,0%     inf Tage     158     96    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage     262    132    1,00  0,00   7  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     554    104    1,00  0,00   7  l
    Freiburg im Breisgau (St   0,11   0,05   0,8%    91,4 Tage     159     69    0,02   nan   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage     158    134    1,00  0,00   7  l
    Göppingen                  0,32   0,12   1,1%    64,3 Tage     242     94    0,16 -1,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      64     40    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage     161    122    1,00  0,00   7  l
    Heilbronn                  0,20   0,06   0,5%   133,5 Tage     203     59    0,10 -0,07  14  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage     136    108    1,00  0,00   7  l
    Hohenlohekreis             0,40   0,36   1,0%    68,4 Tage     120    107    0,10 -0,07  14  l
    Karlsruhe                  0,33   0,08   0,6%   120,2 Tage     470    106    0,17 -0,13   8  l
    Karlsruhe (Stadtkreis)     0,20   0,06   0,5%   139,7 Tage     221     71    0,10 -0,07  14  l
    Konstanz                   0,00   0,00   0,0%     inf Tage     296    104    1,00  0,00   7  l
    Lörrach                    0,34   0,15   0,5%   129,2 Tage     301    132    0,13 -0,07  14  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage     517     95    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      90     68    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage     304     98    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     142     99    1,00  0,00   7  l
    Ortenaukreis               0,49   0,11   0,6%   123,5 Tage     569    132    0,17 -0,11   9  l
    Ostalbkreis                0,07   0,02   0,0%     inf Tage     410    131    0,04 -0,14   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     199    159    1,00  0,00   7  l
    Rastatt                    0,05   0,02   0,0%     inf Tage     196     85    0,05  0,82  11  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     141     50    1,00  0,00   7  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage     359     84    1,00  0,00   7  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage     269     94    1,00  0,00   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage     434     79    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage     162    116    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage     261    133    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,46   0,22   1,2%    58,7 Tage     212    100    0,38 -0,14   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      85     65    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage     452     71    1,00  0,00   7  l
    Tübingen                   0,33   0,15   1,0%    72,8 Tage     182     80    0,17 -0,13   8  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage     156    111    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage      84     66    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage     210    123    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage     173     92    1,00  0,00   7  l

    Baden-Württemberg           6,0   0,05   0,5%   137,9 Tage   10338     93    0,88 -0,18   7  l

Stand 04.06.2021

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     178     91    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,46   0,84   2,3%    30,5 Tage      64    116    0,38 -0,14   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage     171     86    0,12  0,80  10  l
    Böblingen                  0,00   0,00   0,0%     inf Tage     270     69    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     155     72    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,08   0,03   0,0%     inf Tage     182     69    0,06  0,75   8  l
    Calw                       0,00   0,00   0,0%     inf Tage     181    114    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage     157     95    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage     248    125    0,39  2,56   9  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     533    100    0,38 -0,14   7  l
    Freiburg im Breisgau (St   0,34   0,15   0,8%    90,2 Tage     156     68    0,13 -0,07  14  l
    Freudenstadt               0,60   0,51   1,1%    63,3 Tage     157    133    0,18 -0,07  14  l
    Göppingen                  0,00   0,00   0,0%     inf Tage     231     90    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      62     39    0,11  1,73  11  l
    Heidenheim                 0,13   0,10   0,1%     inf Tage     159    120    0,18  0,07   9  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage     201     59    0,15 -0,14   7  l
    Heilbronn (Stadtkreis)     0,20   0,16   0,7%   105,4 Tage     131    104    0,10 -0,07  14  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage     116    104    1,00  0,00   7  l
    Karlsruhe                  0,71   0,16   0,9%    75,5 Tage     461    104    0,40 -0,14   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     202     65    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage     292    102    0,39  0,78   9  l
    Lörrach                     1,1   0,46   1,0%    71,3 Tage     293    128    0,48 -0,07  14  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage     507     93    0,51  0,56  11  l
    Main-Tauber-Kreis          0,01   0,01   0,0%     inf Tage      89     67    0,07  0,83  12  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage     302     98    0,17  0,14   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     138     96    1,00  0,00   7  l
    Ortenaukreis                1,1   0,27   0,7%   101,1 Tage     565    132    0,19 -0,07  14  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage     395    126    0,56  0,36  11  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     188    150    0,36  0,44  10  l
    Rastatt                    0,00   0,00   0,0%     inf Tage     192     83    1,00  0,00   7  l
    Ravensburg                 0,07   0,03   0,1%     inf Tage     134     47    0,10 -0,14   7  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage     354     83    0,44  0,31   8  l
    Reutlingen                 0,71   0,25   1,2%    55,9 Tage     263     92    0,40 -0,14   7  l
    Rhein-Neckar-Kreis          2,3   0,42   1,3%    51,7 Tage     419     77    0,06 -0,10  10  l
    Rottweil                   0,00   0,00   0,0%     inf Tage     158    113    1,00  0,00   7  l
    Schwäbisch Hall            0,89   0,45   1,0%    68,6 Tage     252    129    0,13 -0,07  14  l
    Schwarzwald-Baar-Kreis     0,34   0,16   0,7%   104,3 Tage     203     96    0,13 -0,07  14  l
    Sigmaringen                0,61   0,46   2,0%    34,3 Tage      84     64    0,22 -0,14   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage     390     61    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage     175     77    1,00  0,00   7  l
    Tuttlingen                 0,92   0,65   1,6%    42,6 Tage     147    105    0,07 -0,12   8  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage      80     63    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage     210    123    0,27  1,67   9  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage     169     89    0,41  0,33   9  l

    Baden-Württemberg           7,3   0,07   0,1%     inf Tage   10014     90    0,43 -0,01  11  e

Stand 25.04.2021

    Alb-Donau-Kreis            0,49   0,25   0,9%    78,6 Tage     167     85    0,17 -0,07  14  l
    Baden-Baden (Stadtkreis)   0,46   0,84   2,5%    28,3 Tage      56    102    0,38 -0,14   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage     155     78    0,22  0,20  10  l
    Böblingen                  0,00   0,00   0,0%     inf Tage     260     66    0,27  0,80  10  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     144     67    0,17 -0,14   7  l
    Breisgau-Hochschwarzwald   0,06   0,02   0,0%     inf Tage     175     67    0,13  0,22  12  l
    Calw                       0,36   0,23   0,8%    85,4 Tage     158    100    0,10 -0,08  12  l
    Emmendingen                0,00   0,00   0,0%     inf Tage     156     94    0,23 -0,14   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage     231    116    0,24  0,39  14  l
    Esslingen                   1,0   0,19   0,8%    86,3 Tage     488     91    0,23 -0,14   7  l
    Freiburg im Breisgau (St   0,06   0,03   0,0%     inf Tage     146     63    0,07  0,83  12  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage     146    124    0,23  0,71   7  l
    Göppingen                   1,6   0,62   1,7%    42,0 Tage     191     74    0,20 -0,08  12  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      57     36    0,45 -1,00  11  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage     140    106    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage     189     55    0,27  0,80  10  l
    Heilbronn (Stadtkreis)     0,17   0,14   0,6%   116,3 Tage     124     98    0,06 -0,07  14  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage     103     92    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage     436     98    0,47  0,71   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     184     59    1,00  0,00   7  l
    Konstanz                    1,2   0,43   1,6%    44,5 Tage     266     93    0,17 -0,14   7  l
    Lörrach                     1,3   0,58   1,6%    42,6 Tage     283    124    0,23 -0,14   7  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage     463     85    0,75  0,35   7  l
    Main-Tauber-Kreis          0,31   0,24   1,0%    68,3 Tage      83     63    0,09 -0,07  14  l
    Mannheim (Stadtkreis)       1,1   0,37   0,4%     inf Tage     284     92    0,29 -0,02   7  e
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     128     89    0,22 -0,14   7  l
    Ortenaukreis               0,34   0,08   0,1%     inf Tage     528    123    0,14  0,09  14  l
    Ostalbkreis                 2,2   0,69   1,3%    53,8 Tage     330    105    0,11 -0,07  14  l
    Pforzheim (Stadtkreis)     0,11   0,09   0,1%     inf Tage     168    134    0,04 -0,14   7  l
    Rastatt                     2,7    1,2   3,3%    21,5 Tage     158     68    0,26 -0,14   7  l
    Ravensburg                  1,1   0,40   1,6%    43,2 Tage     121     43    0,19 -0,07  14  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage     328     77    0,30  2,43   7  l
    Reutlingen                 0,21   0,07   0,1%     inf Tage     247     86    0,04 -0,14   7  l
    Rhein-Neckar-Kreis          1,4   0,25   1,6%    44,2 Tage     376     69    0,38 -0,14   7  l
    Rottweil                   0,02   0,02   0,0%     inf Tage     152    109    0,05  0,85  13  l
    Schwäbisch Hall             1,3   0,64   0,5%     inf Tage     229    117    0,06  0,11  13  l
    Schwarzwald-Baar-Kreis     0,75   0,35   1,3%    53,4 Tage     193     91    0,26 -0,12   8  l
    Sigmaringen                0,46   0,35   1,3%    52,3 Tage      75     57    0,07 -0,07  14  l
    Stuttgart                   1,9   0,30   1,3%    53,0 Tage     382     60    0,12 -0,17  11  l
    Tübingen                   0,00   0,00   0,0%     inf Tage     170     75    0,27  0,80  10  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage     132     94    0,75  0,29   7  l
    Ulm (Stadtkreis)           0,08   0,07   1,5%    47,1 Tage      70     55    0,17 -0,12   8  l
    Waldshut                   0,60   0,35   1,0%    68,4 Tage     197    115    0,07 -0,11   9  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage     157     83    0,17 -0,14   7  l

    Baden-Württemberg            15   0,14   0,2%     inf Tage    9226     83    0,20 -0,09   7  e

Stand 16.04.2021

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     164     84    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,18   0,32   0,3%     inf Tage      54     98    0,12 -0,14   7  l
    Biberach                   0,49   0,25   0,3%     inf Tage     152     76    0,08  0,16  10  l
    Böblingen                   1,1   0,28   1,1%    63,2 Tage     259     66    0,09 -0,07  14  l
    Bodenseekreis              0,50   0,23   1,0%    68,8 Tage     142     66    0,07 -0,08  12  l
    Breisgau-Hochschwarzwald   0,71   0,27   1,6%    44,5 Tage     173     66    0,40 -0,14   7  l
    Calw                       0,17   0,11   0,5%   131,7 Tage     156     98    0,06 -0,07  14  l
    Emmendingen                0,00   0,00   0,0%     inf Tage     152     92    0,50  0,33   9  l
    Enzkreis                    1,1   0,55   1,0%    67,8 Tage     230    116    0,08 -0,07  14  l
    Esslingen                  0,35   0,06   0,1%     inf Tage     480     90    0,22  0,12  10  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage     144     63    0,19  1,62   8  l
    Freudenstadt               0,67   0,57   1,4%    51,3 Tage     144    122    0,08 -0,12   8  l
    Göppingen                  0,05   0,02   0,0%     inf Tage     182     71    0,22  0,11  11  l
    Heidelberg (Stadtkreis)    0,71   0,45   2,9%    24,2 Tage      59     37    0,17 -0,14   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage     140    106    1,00  0,00   7  l
    Heilbronn                  0,93   0,27   1,9%    37,7 Tage     187     55    0,38 -0,14   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage     123     98    1,00  0,00   7  l
    Hohenlohekreis             0,24   0,22   0,9%    74,6 Tage     111     99    0,08 -0,11   9  l
    Karlsruhe                   2,1   0,47   1,3%    55,8 Tage     431     97    0,07 -0,12   8  l
    Karlsruhe (Stadtkreis)     0,11   0,03   0,1%     inf Tage     184     59    0,23  0,16  10  l
    Konstanz                   0,20   0,07   0,1%     inf Tage     260     91    0,08  0,33   9  l
    Lörrach                    0,18   0,08   0,1%     inf Tage     278    122    0,27  0,05  10  l
    Ludwigsburg                0,67   0,12   0,1%     inf Tage     453     83    0,23  0,11   8  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      81     61    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,21   0,07   0,1%     inf Tage     270     87    0,19  0,03   7  l
    Neckar-Odenwald-Kreis      0,08   0,06   0,1%     inf Tage     126     88    0,06  0,75   8  l
    Ortenaukreis                2,2   0,52   1,1%    61,8 Tage     520    121    0,07 -0,04   9  l
    Ostalbkreis                0,83   0,27   1,1%    63,4 Tage     316    101    0,38 -0,12   8  l
    Pforzheim (Stadtkreis)     0,75   0,60   2,1%    33,5 Tage     165    131    0,54 -1,88   8  l
    Rastatt                    0,29   0,12   0,2%     inf Tage     144     62    0,33 -0,02   7  l
    Ravensburg                 0,73   0,26   1,7%    41,0 Tage     114     40    0,30 -0,11   9  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage     324     76    0,38  0,56  11  l
    Reutlingen                 0,20   0,07   0,5%   147,3 Tage     244     85    0,10 -0,07  14  l
    Rhein-Neckar-Kreis         0,76   0,14   0,9%    78,0 Tage     373     68    0,42 -0,10  10  l
    Rottweil                   0,00   0,00   0,0%     inf Tage     151    108    0,29  0,21  11  l
    Schwäbisch Hall             2,8    1,4   4,6%    15,5 Tage     216    110    0,32 -0,21   7  e
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage     184     87    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      72     55    1,00  0,00   7  l
    Stuttgart                  0,42   0,07   0,6%   115,4 Tage     371     58    0,02 -0,10  10  l
    Tübingen                   0,46   0,20   1,3%    52,0 Tage     169     74    0,38 -0,14   7  l
    Tuttlingen                  1,4   0,99   2,9%    24,3 Tage     129     92    0,38 -0,14   7  l
    Ulm (Stadtkreis)           0,46   0,37   2,2%    32,3 Tage      71     56    0,38 -0,14   7  l
    Waldshut                   0,45   0,27   0,2%     inf Tage     194    114    0,12  0,05  10  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage     155     82    1,00  0,00   7  l

    Baden-Württemberg            26   0,23   1,8%    38,7 Tage    9047     82    0,26 -0,11   7  e

Stand 03.04.2021

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     161     82    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      49     89    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage     143     72    0,31  0,10  12  l
    Böblingen                  0,83   0,21   1,2%    56,0 Tage     252     64    0,19 -0,12   8  l
    Bodenseekreis              0,20   0,09   0,6%   108,4 Tage     138     64    0,10 -0,07  14  l
    Breisgau-Hochschwarzwald   0,32   0,12   0,7%    98,3 Tage     164     62    0,08 -0,08  13  l
    Calw                       0,54   0,34   1,0%    68,3 Tage     155     98    0,13 -0,07  14  l
    Emmendingen                0,00   0,00   0,0%     inf Tage     143     86    1,00  0,00   7  l
    Enzkreis                   0,37   0,19   0,7%   102,0 Tage     221    111    0,16 -0,07  14  l
    Esslingen                  0,12   0,02   0,0%     inf Tage     466     87    0,10  0,10  12  l
    Freiburg im Breisgau (St   0,33   0,14   1,1%    62,5 Tage     137     60    0,17 -0,13   8  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage     139    118    0,31  1,25  10  l
    Göppingen                  0,32   0,12   0,2%     inf Tage     169     66    0,12  0,04  11  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      56     35    0,17 -0,12   8  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage     139    105    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage     185     54    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,60   0,48   1,3%    55,1 Tage     123     98    0,10 -0,07  14  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage     109     97    1,00  0,00   7  l
    Karlsruhe                  0,92   0,21   0,9%    76,0 Tage     413     93    0,15 -0,12   8  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     174     56    0,45  0,50  10  l
    Konstanz                   0,14   0,05   0,1%     inf Tage     253     89    0,14  0,33  14  l
    Lörrach                    0,18   0,08   0,1%     inf Tage     269    118    0,31 -0,06   7  l
    Ludwigsburg                 1,5   0,27   0,8%    89,0 Tage     435     80    0,13 -0,08  13  l
    Main-Tauber-Kreis          0,95   0,72   2,4%    29,8 Tage      81     61    0,34 -0,09  11  l
    Mannheim (Stadtkreis)       1,8   0,58   2,1%    33,7 Tage     263     85    0,66 -0,14   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     124     86    1,00  0,00   7  l
    Ortenaukreis               0,38   0,09   0,1%     inf Tage     497    116    0,04  0,04   9  l
    Ostalbkreis                 1,5   0,49   1,2%    60,3 Tage     305     97    0,19 -0,07  14  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     166    132    1,00  0,00   7  l
    Rastatt                    0,91   0,40   1,4%    50,9 Tage     129     56    0,12 -0,07  14  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     109     38    0,17 -0,14   7  l
    Rems-Murr-Kreis            0,46   0,11   0,6%   117,6 Tage     312     73    0,13 -0,07  14  l
    Reutlingen                 0,45   0,16   0,2%     inf Tage     243     85    0,08  0,50  10  l
    Rhein-Neckar-Kreis         0,82   0,15   1,0%    73,2 Tage     368     67    0,27 -0,10  10  l
    Rottweil                   0,20   0,14   0,6%   111,8 Tage     146    105    0,10 -0,07  14  l
    Schwäbisch Hall            0,95   0,49   0,5%     inf Tage     183     93    0,05  0,12  11  l
    Schwarzwald-Baar-Kreis     0,33   0,16   1,0%    73,2 Tage     184     87    0,17 -0,13   8  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      68     52    1,00  0,00   7  l
    Stuttgart                  0,67   0,11   0,8%    86,3 Tage     368     58    0,21 -0,11   9  l
    Tübingen                   0,00   0,00   0,0%     inf Tage     167     73    0,17 -0,12   8  l
    Tuttlingen                  1,6    1,1   2,9%    24,5 Tage     121     86    0,40 -0,12   8  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage      70     55    0,43  2,50   8  l
    Waldshut                   0,82   0,48   1,7%    41,3 Tage     186    109    0,62 -0,14   7  l
    Zollernalbkreis            0,17   0,09   0,5%   130,8 Tage     154     82    0,06 -0,07  14  l

    Baden-Württemberg            19   0,17   1,0%    70,5 Tage    8737     79    0,12 -0,13  14  e

Stand 09.03.2021

    Alb-Donau-Kreis             1,1   0,58   1,7%    40,2 Tage     156     80    0,43 -0,09  11  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      47     85    1,00  0,00   7  l
    Biberach                   0,58   0,29   1,2%    58,3 Tage     135     68    0,08 -0,12   8  l
    Böblingen                  0,37   0,09   0,2%     inf Tage     228     58    0,14  0,18  14  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     137     63    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,49   0,18   0,9%    75,9 Tage     157     60    0,17 -0,07  14  l
    Calw                       0,00   0,00   0,0%     inf Tage     151     95    1,00  0,00   7  l
    Emmendingen                0,36   0,22   1,2%    57,1 Tage     137     83    0,17 -0,14   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage     214    108    0,47  0,29   7  l
    Esslingen                  0,36   0,07   0,1%     inf Tage     455     85    0,08  0,66  13  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage     131     57    0,25  0,75   8  l
    Freudenstadt               0,36   0,30   0,3%     inf Tage     131    111    0,62  0,07   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage     155     60    0,40  0,75   8  l
    Heidelberg (Stadtkreis)    0,46   0,29   2,6%    27,4 Tage      53     33    0,38 -0,14   7  l
    Heidenheim                 0,36   0,27   1,2%    56,9 Tage     136    103    0,17 -0,14   7  l
    Heilbronn                  0,36   0,10   1,0%    66,8 Tage     183     53    0,17 -0,14   7  l
    Heilbronn (Stadtkreis)     0,33   0,26   1,2%    57,6 Tage     118     94    0,17 -0,13   8  l
    Hohenlohekreis             0,33   0,30   1,3%    54,3 Tage     106     95    0,17 -0,13   8  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage     399     90    0,36  0,31   8  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     163     52    0,17 -0,12   8  l
    Konstanz                    2,8   0,99   2,0%    34,8 Tage     235     82    0,23 -0,07  14  l
    Lörrach                    0,00   0,00   0,0%     inf Tage     244    107    0,34  1,04   8  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage     419     77    0,83  0,26   9  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      70     53    0,62  0,14   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage     256     83    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,37   0,26   0,9%    74,1 Tage     124     86    0,16 -0,07  14  l
    Ortenaukreis               0,69   0,16   0,1%     inf Tage     480    112    0,12  0,08   9  l
    Ostalbkreis                0,25   0,08   0,1%     inf Tage     278     89    0,46  0,31   8  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     158    126    0,63  1,29   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage     114     49    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage      97     34    0,45  0,31   8  l
    Rems-Murr-Kreis            0,13   0,03   0,0%     inf Tage     304     71    0,08  0,33   9  l
    Reutlingen                 0,07   0,02   0,0%     inf Tage     226     79    0,10 -0,14   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage     356     65    0,75  0,14   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage     140    100    0,17 -0,12   8  l
    Schwäbisch Hall             1,6   0,84   2,7%    25,7 Tage     160     82    0,62 -0,14   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage     178     84    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      66     50    0,24 -0,14   7  l
    Stuttgart                  0,36   0,06   0,1%     inf Tage     353     56    0,35  0,24   9  l
    Tübingen                   0,36   0,16   1,1%    62,7 Tage     163     72    0,17 -0,14   7  l
    Tuttlingen                 0,94   0,67   1,7%    40,7 Tage     113     81    0,16 -0,07  14  l
    Ulm (Stadtkreis)           0,35   0,28   1,4%    50,6 Tage      60     47    0,12 -0,08  13  l
    Waldshut                   0,50   0,29   0,3%     inf Tage     177    104    0,06  0,05   8  l
    Zollernalbkreis            0,93   0,49   2,1%    33,5 Tage     151     80    0,38 -0,14   7  l

    Baden-Württemberg            12   0,11   0,1%     inf Tage    8314     75    0,57  0,14   8  l

Stand 16.02.2021

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     140     71    0,43  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      46     83    1,00  0,00   7  l
    Biberach                   0,36   0,18   0,3%     inf Tage     124     62    0,14 -0,05   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage     198     51    0,29  1,11  13  l
    Bodenseekreis              0,05   0,02   0,0%     inf Tage     134     62    0,13  0,83  12  l
    Breisgau-Hochschwarzwald    1,3   0,51   2,0%    35,5 Tage     152     58    0,21 -0,11   9  l
    Calw                        1,7    1,1   2,7%    25,9 Tage     143     90    0,17 -0,12   8  l
    Emmendingen                0,53   0,32   1,1%    62,9 Tage     131     79    0,19 -0,08  13  l
    Enzkreis                    4,0    2,0   4,6%    15,5 Tage     204    103    0,23 -0,80   7  l
    Esslingen                   1,7   0,31   1,0%    71,9 Tage     428     80    0,06 -0,12   8  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage     128     56    1,00  0,00   7  l
    Freudenstadt               0,13   0,11   0,1%     inf Tage     119    101    0,13  0,33   9  l
    Göppingen                  0,71   0,28   1,7%    41,4 Tage     152     59    0,40 -0,14   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      52     32    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage     128     97    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage     178     52    0,45  0,05   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage     104     83    0,62  0,71   7  l
    Hohenlohekreis             0,33   0,30   1,3%    53,2 Tage     102     91    0,17 -0,13   8  l
    Karlsruhe                  0,11   0,02   0,0%     inf Tage     383     86    0,54  0,16  10  l
    Karlsruhe (Stadtkreis)      1,2   0,38   1,6%    43,7 Tage     155     50    0,24 -0,20  12  l
    Konstanz                   0,18   0,06   0,1%     inf Tage     212     74    0,26  0,43   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage     227     99    0,36  0,16  10  l
    Ludwigsburg                 1,2   0,22   0,3%     inf Tage     385     71    0,14  0,07   7  l
    Main-Tauber-Kreis          0,89   0,67   2,2%    31,2 Tage      62     47    0,21 -0,07  14  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage     250     81    0,33  0,32  13  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage     122     85    0,40  0,71   7  l
    Ortenaukreis                3,2   0,76   0,7%     inf Tage     454    106    0,24  0,13   8  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage     253     81    0,45  0,62   7  l
    Pforzheim (Stadtkreis)     0,73   0,58   0,5%     inf Tage     147    117    0,09  0,33   9  l
    Rastatt                    0,00   0,00   0,0%     inf Tage     110     48    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage      94     33    0,43  0,47  12  l
    Rems-Murr-Kreis            0,06   0,01   0,0%     inf Tage     297     70    0,40  0,08  14  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage     221     77    0,26  0,08  14  l
    Rhein-Neckar-Kreis         0,14   0,03   0,0%     inf Tage     341     62    0,26  0,39  14  l
    Rottweil                   0,93   0,67   2,2%    31,3 Tage     134     96    0,38 -0,14   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage     151     77    0,40  1,00   9  l
    Schwarzwald-Baar-Kreis      2,5    1,2   2,3%    30,6 Tage     174     82    0,21 -0,09  11  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      60     46    1,00  0,00   7  l
    Stuttgart                   4,5   0,72   2,6%    27,0 Tage     295     46    0,09 -0,09  11  l
    Tübingen                   0,00   0,00   0,0%     inf Tage     159     70    0,25  0,33  14  l
    Tuttlingen                 0,04   0,03   0,0%     inf Tage     108     77    0,24  0,71   7  l
    Ulm (Stadtkreis)           0,92   0,73   2,9%    23,9 Tage      56     44    0,15 -0,12   8  l
    Waldshut                   0,86   0,50   0,5%     inf Tage     158     93    0,20  0,14   7  l
    Zollernalbkreis             1,7   0,89   2,0%    34,9 Tage     143     76    0,17 -0,07  14  l

    Baden-Württemberg            28   0,25   0,4%     inf Tage    7814     71    0,26  0,10   9  l

Stand 29.01.2021

    Alb-Donau-Kreis             2,5    1,3   2,6%    27,5 Tage     124     63    0,11 -0,03  14  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      45     82    0,17 -0,14   7  l
    Biberach                    2,6    1,3   4,1%    17,2 Tage     101     51    0,53 -0,12   8  l
    Böblingen                   3,2   0,82   2,8%    24,9 Tage     178     45    0,08 -0,05  10  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     108     50    0,32  0,10  12  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage     136     52    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage     136     86    0,35  1,89   9  l
    Emmendingen                0,00   0,00   0,0%     inf Tage     123     74    0,20  1,67   9  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage     170     85    0,24  2,03  11  l
    Esslingen                    11    2,0   4,3%    16,3 Tage     393     74    0,62 -0,10   8  l
    Freiburg im Breisgau (St   0,82   0,36   2,1%    33,1 Tage     125     54    0,62 -0,14   7  l
    Freudenstadt               0,92   0,78   0,9%     inf Tage     109     92    0,14  0,03  12  l
    Göppingen                  0,75   0,29   1,7%    40,3 Tage     146     57    0,24 -0,42   8  l
    Heidelberg (Stadtkreis)    0,92   0,57   3,5%    19,9 Tage      49     31    0,26 -0,12   8  l
    Heidenheim                 0,31   0,23   0,2%     inf Tage     125     94    0,09  0,56   9  l
    Heilbronn                   2,3   0,66   2,4%    29,4 Tage     159     46    0,24 -0,12   8  l
    Heilbronn (Stadtkreis)     0,11   0,09   0,1%     inf Tage      96     76    0,12  0,78   9  l
    Hohenlohekreis              1,6    1,5   3,7%    18,9 Tage      95     85    0,46 -0,14   7  l
    Karlsruhe                   2,7   0,61   0,8%     inf Tage     356     80    0,32  0,10  12  l
    Karlsruhe (Stadtkreis)      1,8   0,56   2,5%    28,2 Tage     136     43    0,26 -0,11   9  l
    Konstanz                    1,1   0,39   1,7%    41,5 Tage     200     70    0,52 -0,14   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage     206     90    0,33  0,78   9  l
    Ludwigsburg                 3,1   0,58   0,9%     inf Tage     348     64    0,05  0,11  11  l
    Main-Tauber-Kreis           2,3    1,8   5,4%    13,2 Tage      52     39    0,51 -0,09  11  l
    Mannheim (Stadtkreis)       1,7   0,57   0,8%     inf Tage     223     72    0,40  0,15   8  l
    Neckar-Odenwald-Kreis       1,8    1,3   2,5%    27,6 Tage     118     82    0,06 -0,14   7  l
    Ortenaukreis                1,4   0,32   0,4%     inf Tage     367     85    0,22  0,05  12  l
    Ostalbkreis                 2,0   0,65   1,0%     inf Tage     209     67    0,09  0,05   7  l
    Pforzheim (Stadtkreis)      1,4    1,1   2,3%    30,7 Tage      98     78    0,03 -0,10  10  l
    Rastatt                    0,03   0,01   0,0%     inf Tage     107     46    0,23  0,31  12  l
    Ravensburg                  4,0    1,4   6,9%    10,4 Tage      82     29    0,90 -0,14   7  l
    Rems-Murr-Kreis            0,92   0,22   0,3%     inf Tage     277     65    0,23  0,18  12  l
    Reutlingen                  3,6    1,2   2,8%    25,2 Tage     200     70    0,28 -0,12   8  l
    Rhein-Neckar-Kreis          4,6   0,84   5,3%    13,5 Tage     302     55    0,33 -0,23   7  e
    Rottweil                   0,69   0,50   1,4%    48,7 Tage     129     93    0,22 -0,08  12  l
    Schwäbisch Hall            0,36   0,19   0,3%     inf Tage     135     69    0,31  0,07  11  l
    Schwarzwald-Baar-Kreis     0,09   0,04   0,1%     inf Tage     154     73    0,35  0,19   9  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      54     41    1,00  0,00   7  l
    Stuttgart                   4,2   0,67   3,8%    18,7 Tage     260     41    0,48 -0,24   7  l
    Tübingen                    1,5   0,64   2,4%    29,2 Tage     149     66    0,24  0,07   7  l
    Tuttlingen                  1,2   0,89   2,5%    27,7 Tage     103     73    0,16 -0,14   7  l
    Ulm (Stadtkreis)           0,57   0,45   2,1%    33,1 Tage      49     39    0,29 -0,07  14  l
    Waldshut                    2,4    1,4   3,0%    23,7 Tage     141     83    0,63 -0,12   8  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage     131     69    0,38  0,44  12  l

    Baden-Württemberg            87   0,79   4,5%    15,6 Tage    7004     63    0,33 -0,16   7  e

Stand 23.01.2021

    Alb-Donau-Kreis             1,6   0,83   2,6%    26,9 Tage     110     56    0,41 -0,11   9  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      44     80    0,20  0,86  14  l
    Biberach                   0,05   0,02   0,0%     inf Tage      91     46    0,25  0,45  11  l
    Böblingen                  0,00   0,00   0,0%     inf Tage     161     41    0,36  0,56   8  l
    Bodenseekreis               1,6   0,74   1,7%     inf Tage      97     45    0,18 -0,24   7  e
    Breisgau-Hochschwarzwald   0,89   0,34   1,6%    42,7 Tage     136     52    0,19 -0,14   7  l
    Calw                        3,5    2,2   4,2%    16,7 Tage     133     84    0,15 -0,12   8  l
    Emmendingen                0,00   0,00   0,0%     inf Tage     122     74    0,24  1,02  10  l
    Enzkreis                    1,6   0,82   2,0%    34,9 Tage     168     84    0,05 -0,11   9  l
    Esslingen                  0,92   0,17   0,3%     inf Tage     353     66    0,84  0,08   8  l
    Freiburg im Breisgau (St   0,89   0,39   1,7%    40,3 Tage     123     53    0,04 -0,14   7  l
    Freudenstadt                2,5    2,1   4,0%    17,8 Tage     101     86    0,63 -0,14   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage     143     56    0,45  0,33   9  l
    Heidelberg (Stadtkreis)    0,57   0,36   1,8%    38,3 Tage      46     29    0,08 -0,07  14  l
    Heidenheim                  1,3   1,00   2,7%    26,3 Tage     121     91    0,23 -0,14   7  l
    Heilbronn                   3,2   0,94   3,8%    18,7 Tage     147     43    0,20 -0,14   7  l
    Heilbronn (Stadtkreis)      2,2    1,8   4,5%    15,6 Tage      92     73    0,29 -0,14   7  l
    Hohenlohekreis             0,21   0,18   0,2%     inf Tage      91     81    0,10  0,26  12  l
    Karlsruhe                   6,8    1,5   3,1%    22,9 Tage     332     75    0,33 -0,12   8  l
    Karlsruhe (Stadtkreis)     0,43   0,14   0,3%     inf Tage     128     41    0,24  0,14   7  l
    Konstanz                    5,1    1,8   3,4%    20,8 Tage     196     69    0,06 -0,06   8  l
    Lörrach                     3,9    1,7   3,4%    20,9 Tage     201     88    0,37 -0,12   8  l
    Ludwigsburg                 5,6    1,0   2,5%    28,6 Tage     321     59    0,23 -0,08  13  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      41     31    0,35  0,53  12  l
    Mannheim (Stadtkreis)       4,8    1,6   3,7%    19,0 Tage     201     65    0,47 -0,05   7  l
    Neckar-Odenwald-Kreis      0,86   0,60   0,8%     inf Tage     109     76    0,13  0,15  12  l
    Ortenaukreis                7,3    1,7   3,5%    20,2 Tage     350     81    0,35 -0,13   8  l
    Ostalbkreis                 5,1    1,6   3,9%    18,3 Tage     182     58    0,51 -0,10  10  l
    Pforzheim (Stadtkreis)     0,11   0,09   0,1%     inf Tage      89     71    0,12  0,29  14  l
    Rastatt                     1,9   0,82   2,8%    25,4 Tage     105     45    0,20 -0,10  10  l
    Ravensburg                  2,8   0,98   5,9%    12,1 Tage      70     25    0,74 -0,14   7  l
    Rems-Murr-Kreis             1,6   0,38   0,6%     inf Tage     264     62    0,09  0,18  12  l
    Reutlingen                  1,6   0,57   0,9%     inf Tage     181     63    0,16  0,05  12  l
    Rhein-Neckar-Kreis          6,4    1,2   7,7%     9,3 Tage     280     51    0,55 -0,21   7  e
    Rottweil                   0,00   0,00   0,0%     inf Tage     126     90    0,60  0,17   8  l
    Schwäbisch Hall             3,6    1,8   4,3%    16,6 Tage     128     65    0,50 -0,11   9  l
    Schwarzwald-Baar-Kreis      1,9   0,90   2,7%    26,0 Tage     150     71    0,76 -0,12   8  l
    Sigmaringen                0,56   0,43   2,0%    35,3 Tage      54     41    0,13 -0,08  13  l
    Stuttgart                    10    1,6   5,5%    12,9 Tage     252     40    0,28 -0,14   7  l
    Tübingen                   0,15   0,07   0,1%     inf Tage     144     63    0,22  0,22  12  l
    Tuttlingen                  1,4    1,0   3,0%    23,8 Tage      98     70    0,37 -0,12   8  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage      46     36    1,00  0,00   7  l
    Waldshut                    2,5    1,5   2,9%    24,4 Tage     130     76    0,12 -0,11   9  l
    Zollernalbkreis             1,0   0,53   0,8%     inf Tage     128     68    0,06  0,07   7  l
    
    Baden-Württemberg           111    1,0   4,9%    14,4 Tage    6585     59    0,35 -0,15   7  e

Stand 16.01.2021

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage     102     52    0,41  0,15  12  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      43     78    0,72  0,75   8  l
    Biberach                   0,14   0,07   0,2%     inf Tage      88     44    0,24  0,71   7  l
    Böblingen                   3,9   0,99   4,4%    16,2 Tage     152     39    0,29 -0,14   7  l
    Bodenseekreis              0,32   0,15   0,5%     inf Tage      64     30    0,45  0,10  11  l
    Breisgau-Hochschwarzwald    1,9   0,73   2,6%    27,2 Tage     132     50    0,14 -0,04   7  l
    Calw                        1,2   0,74   1,0%     inf Tage     120     76    0,10  0,22   9  l
    Emmendingen                 2,2    1,3   3,2%    21,9 Tage     120     73    0,27 -0,11   9  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage     160     80    0,59  0,21  11  l
    Esslingen                   5,2   0,98   5,3%    13,4 Tage     336     63    0,25 -0,29   7  e
    Freiburg im Breisgau (St   0,55   0,24   0,5%     inf Tage     119     52    0,15  0,11  11  l
    Freudenstadt                2,1    1,8   3,5%    20,3 Tage      91     77    0,25 -0,09  11  l
    Göppingen                   1,3   0,52   1,6%    44,2 Tage     140     54    0,22 -0,08  13  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      43     27    0,25  0,82  11  l
    Heidenheim                  1,3   0,97   1,6%    43,2 Tage     117     88    0,17 -0,07  14  l
    Heilbronn                   2,3   0,67   3,5%    20,3 Tage     135     39    0,64 -0,14   7  l
    Heilbronn (Stadtkreis)      3,1    2,5   5,7%    12,5 Tage      86     68    0,44 -0,14   7  l
    Hohenlohekreis             0,69   0,62   0,8%     inf Tage      87     78    0,04  0,40   9  l
    Karlsruhe                   2,8   0,64   1,0%     inf Tage     296     67    0,16  0,21   8  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     116     37    0,31  0,75   8  l
    Konstanz                    3,4    1,2   2,0%     inf Tage     169     59    0,06  0,18  10  l
    Lörrach                     1,5   0,66   0,8%     inf Tage     185     81    0,10  0,15   8  l
    Ludwigsburg                 4,3   0,79   2,5%    28,3 Tage     293     54    0,12  0,20   7  l
    Main-Tauber-Kreis          0,67   0,50   1,8%     inf Tage      38     29    0,16  0,11  12  l
    Mannheim (Stadtkreis)       5,8    1,9   4,6%    15,3 Tage     180     58    0,62 -0,02   7  l
    Neckar-Odenwald-Kreis       2,5    1,7   3,5%    20,2 Tage     101     70    0,10 -0,14   7  l
    Ortenaukreis                 11    2,7   4,2%    16,7 Tage     319     74    0,19 -0,07  14  l
    Ostalbkreis                0,21   0,07   0,1%     inf Tage     156     50    0,19  0,40  12  l
    Pforzheim (Stadtkreis)     0,46   0,37   0,6%     inf Tage      84     67    0,17  0,39   7  l
    Rastatt                    0,36   0,16   0,4%     inf Tage      96     42    0,42  0,19  11  l
    Ravensburg                  2,5   0,88   5,2%    13,7 Tage      61     21    0,57 -0,12   8  l
    Rems-Murr-Kreis             3,7   0,86   2,1%    34,0 Tage     250     59    0,13 -0,07  14  l
    Reutlingen                  1,8   0,64   1,1%     inf Tage     165     58    0,09  0,18  12  l
    Rhein-Neckar-Kreis          5,5    1,0   5,3%    13,3 Tage     255     47    0,27 -0,21   7  e
    Rottweil                   0,67   0,48   0,5%     inf Tage     123     88    0,13  0,31   8  l
    Schwäbisch Hall            0,37   0,19   0,3%     inf Tage     114     58    0,24  0,16  12  l
    Schwarzwald-Baar-Kreis      2,8    1,3   2,3%    31,0 Tage     143     67    0,06 -0,07  14  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      51     39    0,17 -0,12   8  l
    Stuttgart                    12    1,9   8,1%     8,9 Tage     209     33    0,55 -0,14   7  l
    Tübingen                    3,3    1,5   3,2%    22,2 Tage     137     60    0,08 -0,06  10  l
    Tuttlingen                 1,00   0,71   2,4%    29,8 Tage      93     66    0,07 -0,14   7  l
    Ulm (Stadtkreis)           0,18   0,14   0,4%     inf Tage      46     36    0,16  0,07   7  l
    Waldshut                   0,84   0,49   0,7%     inf Tage     116     68    0,19  0,21   9  l
    Zollernalbkreis            0,14   0,07   0,1%     inf Tage     118     62    0,16  0,70  11  l
    
    Baden-Württemberg           102   0,92   3,2%    22,2 Tage    6049     55    0,28 -0,06   7  e

Stand 04.01.2021

    Alb-Donau-Kreis            0,86   0,44   2,3%    30,8 Tage      94     48    0,15 -0,14   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      35     63    0,37  0,46   8  l
    Biberach                    1,0   0,50   2,4%    29,5 Tage      76     38    0,26 -0,13   8  l
    Böblingen                  0,14   0,04   0,1%     inf Tage     130     33    0,22  0,71   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage      41     19    0,58  0,22   7  l
    Breisgau-Hochschwarzwald   0,21   0,08   0,2%     inf Tage     116     44    0,26  0,29   7  l
    Calw                       0,29   0,18   0,3%     inf Tage      96     61    0,25  0,71   7  l
    Emmendingen                0,25   0,15   0,2%     inf Tage     107     65    0,38  0,31   8  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage     128     64    0,51  0,16   7  l
    Esslingen                   2,7   0,50   0,9%     inf Tage     293     55    0,45  0,16   7  l
    Freiburg im Breisgau (St   0,21   0,09   0,8%    90,1 Tage     108     47    0,10 -0,08  13  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      81     69    0,48  0,93   8  l
    Göppingen                  0,00   0,00   0,0%     inf Tage     129     50    0,54  0,20  10  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      33     21    0,22  0,12  10  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage     106     80    0,21  0,83  12  l
    Heilbronn                   3,0   0,86   3,8%    18,4 Tage     114     33    0,23 -0,09  11  l
    Heilbronn (Stadtkreis)     0,33   0,26   0,5%     inf Tage      67     53    0,47  0,17   8  l
    Hohenlohekreis              1,4    1,2   4,0%    17,7 Tage      75     67    0,38 -0,14   7  l
    Karlsruhe                   4,8    1,1   2,8%    25,2 Tage     242     54    0,09 -0,05  12  l
    Karlsruhe (Stadtkreis)      1,6   0,52   3,0%    23,7 Tage      85     27    0,13 -0,10  10  l
    Konstanz                    4,0    1,4   4,1%    17,4 Tage     117     41    0,09 -0,07  14  l
    Lörrach                    0,61   0,27   0,4%     inf Tage     157     69    0,39  0,41   7  l
    Ludwigsburg                 4,7   0,86   2,3%    29,9 Tage     261     48    0,11 -0,03  13  l
    Main-Tauber-Kreis           1,5    1,2   8,7%     8,3 Tage      24     18    0,38 -0,14   7  l
    Mannheim (Stadtkreis)      0,20   0,06   0,1%     inf Tage     146     47    0,50  0,20  10  l
    Neckar-Odenwald-Kreis       1,9    1,3   3,8%    18,7 Tage      79     55    0,08  0,14   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     242     56    0,25  1,50   8  l
    Ostalbkreis                 3,5    1,1   3,7%    19,1 Tage     139     44    0,22 -0,09  11  l
    Pforzheim (Stadtkreis)     0,11   0,09   0,2%     inf Tage      61     49    0,36  0,29   7  l
    Rastatt                    0,33   0,14   0,4%     inf Tage      79     34    0,31  0,07   8  l
    Ravensburg                 0,67   0,23   1,5%     inf Tage      46     16    0,17  0,38   8  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage     221     52    0,44  0,56   8  l
    Reutlingen                  3,2    1,1   3,2%    21,8 Tage     137     48    0,22 -0,08  13  l
    Rhein-Neckar-Kreis         0,34   0,06   0,2%     inf Tage     208     38    0,32  0,13  14  l
    Rottweil                    3,9    2,8   4,3%    16,5 Tage     110     79    0,10 -0,11   9  l
    Schwäbisch Hall             1,8   0,90   2,5%    27,7 Tage      99     51    0,14 -0,07  14  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage     118     56    0,48  0,25   8  l
    Sigmaringen                0,06   0,04   0,1%     inf Tage      49     37    0,28  0,13  14  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage     176     28    0,34  1,57   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage     108     48    0,26  0,17   8  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      84     60    0,82  0,43   7  l
    Ulm (Stadtkreis)            1,1   0,83   4,1%    17,3 Tage      40     32    0,40 -0,10  10  l
    Waldshut                    2,2    1,3   3,2%    21,8 Tage      91     53    0,16 -0,04   9  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage     103     55    0,72  0,75   8  l
    
    Baden-Württemberg            39   0,35   0,8%     inf Tage    5051     46    0,27 -0,04   8  e

Stand 19.12.2020

    Alb-Donau-Kreis             1,3   0,68   3,1%    22,6 Tage      82     42    0,44 -0,12   8  l
    Baden-Baden (Stadtkreis)   0,73    1,3   3,6%    19,5 Tage      28     51    0,23 -0,09  11  l
    Biberach                    1,5   0,75   3,2%    22,2 Tage      63     32    0,22 -0,08  13  l
    Böblingen                   2,4   0,61   3,5%    20,1 Tage     113     29    0,25 -0,14   7  l
    Bodenseekreis               1,4   0,66   8,8%     8,2 Tage      19    8,8    0,45 -0,11   9  l
    Breisgau-Hochschwarzwald    2,5   0,94   4,2%    16,9 Tage      98     37    0,28 -0,04   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      70     44    0,52  0,32  12  l
    Emmendingen                 2,3    1,4   3,0%    23,3 Tage      85     51    0,06 -0,07  14  l
    Enzkreis                    4,7    2,4   6,3%    11,3 Tage      77     39    0,14 -0,07  14  l
    Esslingen                   6,1    1,1   5,3%    13,5 Tage     230     43    0,28 -0,19   7  e
    Freiburg im Breisgau (St    1,3   0,58   2,1%    33,2 Tage      98     43    0,17 -0,07  14  l
    Freudenstadt                1,3    1,1   3,4%    20,9 Tage      58     49    0,12 -0,10  10  l
    Göppingen                   2,4   0,94   2,6%    27,5 Tage     104     40    0,05 -0,03  14  l
    Heidelberg (Stadtkreis)    0,09   0,05   0,4%     inf Tage      25     16    0,09  0,15  13  l
    Heidenheim                  1,9    1,4   2,0%     inf Tage      95     72    0,13  0,23   7  l
    Heilbronn                   4,2    1,2   7,1%    10,1 Tage      84     24    0,30 -0,06   7  l
    Heilbronn (Stadtkreis)     0,33   0,26   0,6%     inf Tage      51     40    0,09  0,16  10  l
    Hohenlohekreis              1,7    1,6   5,2%    13,6 Tage      60     54    0,56 -0,14   7  l
    Karlsruhe                   4,7    1,1   4,0%    17,6 Tage     178     40    0,41 -0,11   9  l
    Karlsruhe (Stadtkreis)      3,5    1,1   6,7%    10,7 Tage      63     20    0,51 -0,11   9  l
    Konstanz                    2,7   0,95   5,3%    13,5 Tage      76     27    0,53 -0,14   7  l
    Lörrach                     3,7    1,6   4,1%    17,1 Tage     115     50    0,14 -0,11   9  l
    Ludwigsburg                 8,4    1,5   5,7%    12,5 Tage     200     37    0,58 -0,09   7  l
    Main-Tauber-Kreis          0,07   0,05   0,4%     inf Tage      20     15    0,10 -0,14   7  l
    Mannheim (Stadtkreis)       6,5    2,1   7,3%     9,8 Tage      98     32    0,55 -0,13  10  l
    Neckar-Odenwald-Kreis       1,4    1,0   3,5%    19,9 Tage      51     36    0,11 -0,08  12  l
    Ortenaukreis                4,1   0,95   3,2%    22,3 Tage     204     47    0,19 -0,13   8  l
    Ostalbkreis                 5,2    1,7   5,0%    14,2 Tage     117     37    0,65 -0,08  13  l
    Pforzheim (Stadtkreis)      3,5    2,8  10,0%     7,3 Tage      37     29    0,72 -0,10  10  l
    Rastatt                     2,3    1,0   5,0%    14,2 Tage      58     25    0,31  0,05   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage      31     11    0,38  0,75   8  l
    Rems-Murr-Kreis             4,9    1,1   3,3%    21,5 Tage     170     40    0,07 -0,07  14  l
    Reutlingen                  2,8   0,97   3,8%    18,7 Tage     115     40    0,38 -0,14   7  l
    Rhein-Neckar-Kreis          1,9   0,35   1,2%     inf Tage     160     29    0,34 -0,08   9  e
    Rottweil                    2,7    1,9   4,3%    16,5 Tage      70     50    0,02 -0,13   8  l
    Schwäbisch Hall             1,4   0,69   2,6%    27,5 Tage      85     43    0,26 -0,08  12  l
    Schwarzwald-Baar-Kreis      1,5   0,71   3,3%    21,4 Tage      73     34    0,15 -0,12   8  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      38     29    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage     144     23    0,28  2,71   7  l
    Tübingen                    1,6   0,69   2,5%    27,7 Tage      90     40    0,20 -0,07  14  l
    Tuttlingen                 0,49   0,35   0,8%     inf Tage      63     45    0,10  0,16  14  l
    Ulm (Stadtkreis)            1,3    1,1   5,8%    12,4 Tage      31     25    0,34 -0,10  10  l
    Waldshut                   0,36   0,21   0,5%     inf Tage      68     40    0,16  0,50   7  l
    Zollernalbkreis             1,1   0,57   1,8%    39,5 Tage      96     51    0,20 -0,07  14  l
    
    Baden-Württemberg            94   0,85   2,7%    25,8 Tage    3891     35    0,42 -0,04  14  l

Stand 24.11.2020

    Alb-Donau-Kreis            0,19   0,10   0,3%     inf Tage      67     34    0,11  0,74  13  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      21     38    0,17 -0,12   8  l
    Biberach                   0,71   0,36   3,4%    20,6 Tage      45     23    0,11 -0,43   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      78     20    0,34  1,29   7  l
    Bodenseekreis              0,07   0,03   0,6%     inf Tage      11    5,1    0,04 -0,14   7  l
    Breisgau-Hochschwarzwald   0,53   0,20   1,5%    47,6 Tage      81     31    0,19 -0,08  13  l
    Calw                       0,00   0,00   0,0%     inf Tage      31     20    1,00  0,00   7  l
    Emmendingen                 1,8    1,1   4,3%    16,5 Tage      56     34    0,33 -0,08  12  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      39     20    0,40  0,75   8  l
    Esslingen                   1,6   0,30   1,7%    41,4 Tage     153     29    0,08 -0,02   9  l
    Freiburg im Breisgau (St    1,6   0,71   4,0%    17,8 Tage      86     37    0,62 -0,14   7  l
    Freudenstadt                1,0   0,85   4,1%    17,0 Tage      43     36    0,17 -0,12   8  l
    Göppingen                   1,4   0,56   3,5%    20,2 Tage      58     23    0,14 -0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage      15    9,4    0,27  1,19   8  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      45     34    1,00  0,00   7  l
    Heilbronn                   1,0   0,29   2,5%    28,1 Tage      54     16    0,09 -0,07  14  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      28     22    0,53  0,07   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      48     43    1,00  0,00   7  l
    Karlsruhe                  0,96   0,22   0,7%     inf Tage     136     31    0,17  0,07   7  l
    Karlsruhe (Stadtkreis)      1,4   0,46   4,8%    14,9 Tage      31    9,9    0,13 -0,07  14  l
    Konstanz                   0,60   0,21   1,9%     inf Tage      32     11    0,09  0,07   9  l
    Lörrach                    0,69   0,30   2,1%    33,4 Tage      68     30    0,22 -0,08  12  l
    Ludwigsburg                0,83   0,15   0,7%     inf Tage     120     22    0,21  0,11   8  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      13    9,8    1,00  0,00   7  l
    Mannheim (Stadtkreis)       2,9   0,93   7,4%     9,7 Tage      39     13    0,18 -0,08  12  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      30     21    0,17 -0,14   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     154     36    0,28  0,52   9  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      54     17    0,26  0,62  13  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage      15     12    1,00  0,00   7  l
    Rastatt                    0,46   0,20   3,7%    18,9 Tage      28     12    0,38 -0,14   7  l
    Ravensburg                 0,86   0,30   6,5%    11,0 Tage      14    4,9    0,15 -0,07  14  l
    Rems-Murr-Kreis            0,21   0,05   0,2%     inf Tage     119     28    0,19  0,29   7  l
    Reutlingen                  1,2   0,41   3,1%    22,8 Tage      92     32    0,47 -0,14   7  l
    Rhein-Neckar-Kreis          1,1   0,20   1,3%     inf Tage      83     15    0,24  0,03   7  l
    Rottweil                    1,7    1,2   6,7%    10,8 Tage      35     25    0,33 -0,14   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      70     36    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis      1,5   0,72   5,7%    12,4 Tage      44     21    0,38 -0,14   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      38     29    1,00  0,00   7  l
    Stuttgart                   1,2   0,18   2,1%    34,0 Tage      99     16    0,09 -0,10  10  l
    Tübingen                    1,0   0,44   2,6%    27,0 Tage      79     35    0,11 -0,13   8  l
    Tuttlingen                 0,37   0,27   1,9%    36,8 Tage      30     21    0,06 -0,07  14  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage      19     15    0,35  0,71   7  l
    Waldshut                    1,2   0,70   3,3%    21,6 Tage      46     27    0,18 -0,07  14  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      83     44    0,57  0,75   8  l
    
    Baden-Württemberg            32   0,29   1,6%    44,0 Tage    2530     23    0,09 -0,03  12  l

Stand 13.11.2020

    Alb-Donau-Kreis             3,0    1,5   6,6%    10,9 Tage      58     30    0,14 -0,12   8  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      20     36    1,00  0,00   7  l
    Biberach                   0,36   0,18   1,8%    38,5 Tage      41     21    0,09 -0,09  11  l
    Böblingen                   3,2   0,82   6,0%    11,9 Tage      66     17    0,49 -0,15  11  l
    Bodenseekreis              0,20   0,09   3,2%    21,7 Tage       9    4,2    0,10 -0,07  14  l
    Breisgau-Hochschwarzwald   0,59   0,22   1,7%    41,1 Tage      78     30    0,11 -0,09  11  l
    Calw                       0,00   0,00   0,0%     inf Tage      31     20    1,00  0,00   7  l
    Emmendingen                0,43   0,26   1,7%    42,0 Tage      47     28    0,10 -0,07  14  l
    Enzkreis                   0,71   0,36   3,1%    22,6 Tage      33     17    0,20 -0,07  14  l
    Esslingen                   1,5   0,28   2,4%    28,8 Tage     140     26    0,32 -0,11   9  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      82     36    0,17 -0,12   8  l
    Freudenstadt               0,17   0,15   1,1%    61,8 Tage      40     34    0,06 -0,07  14  l
    Göppingen                  0,17   0,07   0,4%     inf Tage      46     18    0,06  0,16  14  l
    Heidelberg (Stadtkreis)    0,01   0,01   0,1%     inf Tage       9    5,6    0,07  0,83  12  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      42     32    0,17 -0,14   7  l
    Heilbronn                  0,46   0,14   2,7%    25,6 Tage      47     14    0,38 -0,14   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      23     18    0,25  0,78   9  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      48     43    1,00  0,00   7  l
    Karlsruhe                   2,7   0,61   3,2%    22,3 Tage     115     26    0,19 -0,07  14  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      19    6,1    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      20    7,0    0,15  1,75  12  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      65     28    1,00  0,00   7  l
    Ludwigsburg                 1,9   0,35   3,6%    19,6 Tage     106     19    0,28 -0,14   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      12    9,1    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,82   0,26   5,5%    12,8 Tage      20    6,5    0,27 -0,10  10  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      28     20    1,00  0,00   7  l
    Ortenaukreis                3,3   0,76   3,8%    18,4 Tage     142     33    0,64 -0,11   9  l
    Ostalbkreis                 1,6   0,50   4,9%    14,4 Tage      51     16    0,40 -0,12   8  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage      12    9,6    0,08  0,78   9  l
    Rastatt                    0,16   0,07   0,7%     inf Tage      22    9,5    0,04  0,35  10  l
    Ravensburg                 0,49   0,17   6,9%    10,4 Tage       9    3,2    0,16 -0,54  12  l
    Rems-Murr-Kreis             1,4   0,32   2,7%    26,2 Tage     109     26    0,38 -0,14   7  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      89     31    0,33  0,29   7  l
    Rhein-Neckar-Kreis         0,81   0,15   1,3%     inf Tage      65     12    0,10  0,12  13  l
    Rottweil                   0,33   0,24   2,8%    25,0 Tage      27     19    0,17 -0,13   8  l
    Schwäbisch Hall            0,27   0,14   0,4%     inf Tage      70     36    0,10  0,07   9  l
    Schwarzwald-Baar-Kreis     0,33   0,16   2,3%    30,6 Tage      38     18    0,17 -0,13   8  l
    Sigmaringen                0,37   0,28   1,9%    37,1 Tage      38     29    0,16 -0,07  14  l
    Stuttgart                  0,86   0,14   2,3%    30,2 Tage      91     14    0,33 -0,14   7  l
    Tübingen                    1,6   0,70   3,7%    19,2 Tage      74     33    0,18 -0,13   8  l
    Tuttlingen                 0,31   0,22   2,0%    34,9 Tage      27     19    0,09 -0,07  14  l
    Ulm (Stadtkreis)           0,71   0,57   7,3%     9,9 Tage      14     11    0,40 -0,14   7  l
    Waldshut                   0,07   0,04   0,2%     inf Tage      37     22    0,10 -0,14   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      81     43    0,15  1,67   9  l
    
    Baden-Württemberg            35   0,32   6,7%    10,7 Tage    2241     20    0,58 -0,21   7  e

Stand 06.11.2020

    Alb-Donau-Kreis             2,5    1,3   6,8%    10,5 Tage      46     23    0,10 -0,12   8  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      20     36    1,00  0,00   7  l
    Biberach                   0,04   0,02   0,1%     inf Tage      39     20    0,04 -0,14   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      51     13    0,06 -0,07  14  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      75     29    0,09  0,82  11  l
    Calw                       0,21   0,13   1,6%    44,5 Tage      31     20    0,10 -0,08  13  l
    Emmendingen                0,46   0,28   2,8%    25,0 Tage      45     27    0,38 -0,14   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      29     15    1,00  0,00   7  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     135     25    0,31  1,19   8  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      81     35    0,17 -0,12   8  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      39     33    1,00  0,00   7  l
    Göppingen                  0,11   0,04   0,2%     inf Tage      44     17    0,19  0,29   7  l
    Heidelberg (Stadtkreis)    0,04   0,02   0,4%     inf Tage       8    5,0    0,04 -0,14   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      46     13    1,00  0,00   7  l
    Heilbronn (Stadtkreis)      1,3    1,0   8,0%     9,0 Tage      22     17    0,47 -0,14   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      48     43    1,00  0,00   7  l
    Karlsruhe                   2,2   0,50   4,4%    16,3 Tage     102     23    0,52 -0,14   7  l
    Karlsruhe (Stadtkreis)     0,25   0,08   1,3%     inf Tage      19    6,1    0,04 -0,14   7  l
    Konstanz                   0,07   0,03   0,4%     inf Tage      19    6,7    0,04 -0,14   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      65     28    1,00  0,00   7  l
    Ludwigsburg                 1,6   0,30   3,1%    22,6 Tage     100     18    0,36 -0,14   7  l
    Main-Tauber-Kreis          0,46   0,35   6,4%    11,2 Tage      12    9,1    0,38 -0,14   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      17    5,5    0,25  0,75   8  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      28     20    0,21  2,60  10  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     130     30    1,00  0,00   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      46     15    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,33   0,27   4,9%    14,4 Tage      11    8,8    0,17 -0,13   8  l
    Rastatt                    0,20   0,09   1,9%    36,0 Tage      20    8,7    0,10 -0,07  14  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage       7    2,5    0,07 -1,00   7  l
    Rems-Murr-Kreis             1,2   0,28   2,9%    24,5 Tage     104     24    0,47 -0,14   7  l
    Reutlingen                 0,80   0,28   2,2%    32,1 Tage      86     30    0,20 -0,11   9  l
    Rhein-Neckar-Kreis          1,6   0,30   3,1%    22,5 Tage      58     11    0,11 -0,08  13  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall             1,3   0,64   3,6%    19,8 Tage      67     34    0,48 -0,12   8  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      37     17    0,27  0,80  10  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      36     28    1,00  0,00   7  l
    Stuttgart                   1,8   0,28   3,0%    23,8 Tage      88     14    0,26 -0,08  13  l
    Tübingen                    1,8   0,79   4,7%    15,1 Tage      68     30    0,17 -0,14   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      25     18    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,33   0,26   4,7%    15,2 Tage      12    9,5    0,17 -0,13   8  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,67   0,35   2,2%    31,5 Tage      80     42    0,17 -0,13   8  l
    
    Baden-Württemberg            19   0,17   1,9%    35,9 Tage    2106     19    0,63 -0,07   7  l


Stand 08.10.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      26     13    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      36     18    1,00  0,00   7  l
    Böblingen                  0,17   0,04   1,0%    69,4 Tage      49     13    0,06 -0,07  14  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      72     27    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      27     17    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      44     27    1,00  0,00   7  l
    Enzkreis                   0,84   0,42   4,2%    17,0 Tage      27     14    0,21 -0,08  13  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     121     23    1,00  0,00   7  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      80     35    1,00  0,00   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      39     33    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      40     16    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage       7    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      44     13    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      17     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      81     18    1,00  0,00   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      14    4,5    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      17    6,0    1,00  0,00   7  l
    Lörrach                    0,32   0,14   1,2%    57,7 Tage      65     28    0,07 -0,08  12  l
    Ludwigsburg                0,04   0,01   0,0%     inf Tage      74     14    0,04 -0,14   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      11    8,3    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      23     16    1,00  0,00   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     126     29    1,00  0,00   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      44     14    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,33   0,27   5,6%    12,7 Tage       9    7,2    0,17 -0,13   8  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      19    8,2    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage       7    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,17   0,04   0,7%   102,8 Tage      99     23    0,06 -0,07  14  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      82     29    1,00  0,00   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      40    7,3    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      60     31    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      35     16    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      36     28    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      65     10    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      60     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      25     18    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,04   0,03   0,4%     inf Tage      10    7,9    0,04 -0,14   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      78     41    1,00  0,00   7  l
    
    Baden-Württemberg           1,9   0,02   0,4%   164,7 Tage    1898     17    0,04 -0,04   9  l


Stand 09.09.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      26     13    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      36     18    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      48     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      71     27    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      27     17    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      43     26    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      22     11    1,00  0,00   7  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     120     22    1,00  0,00   7  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      80     35    1,00  0,00   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      39     33    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage       7    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      42     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      17     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,20   0,05   0,9%    81,0 Tage      81     18    0,10 -0,07  14  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      14    4,5    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      17    6,0    1,00  0,00   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      62     27    1,00  0,00   7  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      11    8,3    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,46   0,32   4,2%    16,8 Tage      23     16    0,38 -0,14   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     125     29    1,00  0,00   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      43     14    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage       8    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage       7    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      97     23    1,00  0,00   7  l
    Reutlingen                 0,25   0,09   2,4%    28,9 Tage      82     29    0,17 -0,12   8  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      39    7,1    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      59     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      33     16    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      36     28    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      65     10    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      60     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      24     17    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage       8    6,3    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,20   0,11   0,9%    79,3 Tage      78     41    0,10 -0,07  14  l
    
    Baden-Württemberg           1,5   0,01   0,8%    83,5 Tage    1867     17    0,50 -1,00   7  l

Stand 26.08.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      27     14    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      36     18    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      71     27    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      27     17    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      43     26    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      22     11    1,00  0,00   7  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     120     22    1,00  0,00   7  l
    Freiburg im Breisgau (St   0,46   0,20   2,0%    34,6 Tage      80     35    0,38 -0,14   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      39     33    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage       7    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      42     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      17     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      80     18    1,00  0,00   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      14    4,5    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      17    6,0    1,00  0,00   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      62     27    1,00  0,00   7  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      11    8,3    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      22     15    1,00  0,00   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     125     29    1,00  0,00   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      43     14    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage       8    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage       7    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      97     23    0,17 -0,12   8  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      84     29    0,29 -1,00   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      39    7,1    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      59     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      33     16    1,00  0,00   7  l
    Sigmaringen                0,33   0,25   2,4%    29,6 Tage      36     28    0,17 -0,13   8  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      65     10    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      60     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      24     17    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage       5    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      77     41    1,00  0,00   7  l
    
    Baden-Württemberg          0,00   0,00   0,0%     inf Tage    1863     17    0,09  0,19   9  l

Stand 04.08.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      27     14    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      34     17    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      71     27    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      27     17    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      43     26    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      22     11    1,00  0,00   7  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     119     22    1,00  0,00   7  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      79     34    1,00  0,00   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      38     32    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage       7    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      42     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      17     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      80     18    1,00  0,00   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      14    4,5    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      16    5,6    0,15  0,04   8  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      62     27    1,00  0,00   7  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      11    8,3    0,15  0,12   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      22     15    1,00  0,00   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     125     29    1,00  0,00   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      38     12    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage       8    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage       7    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      96     23    0,42  3,49  12  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      82     29    1,00  0,00   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      39    7,1    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      59     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      33     16    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      35     27    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      64     10    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      60     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      24     17    0,15  0,12   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage       5    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      77     41    1,00  0,00   7  l
    
    Baden-Württemberg          0,00   0,00   0,0%     inf Tage    1847     17    0,73  0,55   8  l

Stand 29.07.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      27     14    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      34     17    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      71     27    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      27     17    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      43     26    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      22     11    1,00  0,00   7  l
    Esslingen                  0,33   0,06   1,0%    68,0 Tage     119     22    0,20  0,25  11  l
    Freiburg im Breisgau (St   0,33   0,14   1,3%    54,1 Tage      79     34    0,20  0,25  11  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      38     32    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage       7    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      42     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      17     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      80     18    1,00  0,00   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      14    4,5    1,00  0,00   7  l
    Konstanz                   0,49   0,17   5,3%    13,4 Tage      16    5,6    0,37  0,07   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      62     27    1,00  0,00   7  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      22     15    1,00  0,00   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     125     29    1,00  0,00   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      38     12    0,18  0,17   8  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage       8    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage       7    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,62   0,15   1,4%    50,6 Tage      96     23    0,11  0,26  14  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      82     29    1,00  0,00   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      39    7,1    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      59     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      33     16    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      35     27    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      64     10    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      60     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      23     16    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage       5    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      77     41    1,00  0,00   7  l
    
    Baden-Württemberg           1,9   0,02   0,6%   122,2 Tage    1845     17    0,59 -0,02  13  l


Stand 23.07.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      27     14    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      34     17    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      71     27    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      27     17    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      43     26    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      22     11    1,00  0,00   7  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     118     22    1,00  0,00   7  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      78     34    1,00  0,00   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      38     32    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage       7    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      42     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      17     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      80     18    1,00  0,00   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      14    4,5    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      15    5,3    1,00  0,00   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      62     27    1,00  0,00   7  l
    Ludwigsburg                0,06   0,01   1,6%    43,6 Tage      72     13    0,25  0,34   8  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      22     15    1,00  0,00   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     125     29    1,00  0,00   7  l
    Ostalbkreis                0,47   0,15   3,2%    22,1 Tage      38     12    0,34 -0,21   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage       8    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage       7    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      93     22    1,00  0,00   7  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      82     29    1,00  0,00   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      39    7,1    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      59     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      33     16    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      35     27    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      64     10    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      60     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      23     16    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage       5    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      77     41    1,00  0,00   7  l
    
    Baden-Württemberg          0,68   0,01   0,6%   111,6 Tage    1839     17    0,85 -2,02   7  l

Stand 04.07.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      27     14    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      34     17    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage       8    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,21   0,08   1,7%    41,7 Tage      71     27    0,07   nan   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      27     17    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      43     26    0,06 -0,07  14  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      21     11    1,00  0,00   7  l
    Esslingen                  0,53   0,10   1,2%    59,1 Tage     119     22    0,02 -0,11   9  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      78     34    1,00  0,00   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      38     32    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage       7    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      41     31    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      42     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      17     13    0,17 -0,12   8  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,17   0,04   0,8%    91,4 Tage      80     18    0,06 -0,07  14  l
    Karlsruhe (Stadtkreis)     0,04   0,01   0,3%     inf Tage      14    4,5    0,04 -0,14   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      15    5,3    0,38 -0,14   7  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      61     27    1,00  0,00   7  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      22     15    0,17 -0,12   8  l
    Ortenaukreis               0,07   0,02   1,2%    58,2 Tage     125     29    0,17 -0,14   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      37     12    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage       8    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,08   0,03   5,1%    14,0 Tage       7    2,5    0,17 -0,12   8  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      93     22    0,16  2,67  12  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      82     29    1,00  0,00   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      39    7,1    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      26     19    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      59     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,11   0,05   0,3%     inf Tage      33     16    0,09  0,29   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      35     27    0,17 -0,12   8  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      64     10    0,17 -0,14   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      60     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      23     16    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage       5    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      77     41    1,00  0,00   7  l

    Baden-Württemberg          0,15   0,00   0,0%     inf Tage    1837     17    0,19  0,14  13  l

Stand 20.06.2020

    Alb-Donau-Kreis            0,33   0,17   2,8%    25,0 Tage      27     14    0,17 -0,13   8  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      34     17    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      71     27    1,00  0,00   7  l
    Calw                       0,34   0,22   2,2%    32,2 Tage      27     17    0,06 -0,07  14  l
    Emmendingen                0,32   0,19   1,5%    45,7 Tage      43     26    0,05 -0,09  11  l
    Enzkreis                   0,02   0,01   0,1%     inf Tage      21     11    0,10  0,78   9  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     115     22    0,13  1,77  13  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      78     34    1,00  0,00   7  l
    Freudenstadt               0,04   0,03   0,1%     inf Tage      38     32    0,04 -0,14   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    1,00  0,00   7  l
    Heidenheim                 0,17   0,13   1,1%    62,7 Tage      41     31    0,06 -0,07  14  l
    Heilbronn                  0,46   0,14   2,9%    24,0 Tage      42     12    0,38 -0,14   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      16     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      79     18    0,23  0,24  14  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      16    5,6    0,17 -0,12   8  l
    Lörrach                    0,46   0,20   2,4%    29,7 Tage      61     27    0,11 -0,14   7  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      21     15    1,00  0,00   7  l
    Ortenaukreis               0,46   0,11   1,6%    44,4 Tage     126     29    0,38 -0,14   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      37     12    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     8,0    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     8,0    2,8    1,00  0,00   7  l
    Rems-Murr-Kreis             1,0   0,23   2,6%    27,0 Tage      92     22    0,17 -0,12   8  l
    Reutlingen                 0,25   0,09   1,1%    61,1 Tage      82     29    0,06 -0,12   8  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      38    6,9    1,00  0,00   7  l
    Rottweil                   0,20   0,14   1,7%    42,1 Tage      26     19    0,10 -0,07  14  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      58     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      30     14    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      34     26    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      63    9,9    1,00  0,00   7  l
    Tübingen                   0,46   0,20   2,4%    29,4 Tage      60     26    0,38 -0,14   7  l
    Tuttlingen                 0,07   0,05   0,3%     inf Tage      23     16    0,04 -0,14   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      77     41    1,00  0,00   7  l
    
    Baden-Württemberg           4,8   0,04   1,0%    72,6 Tage    1824     16    0,63 -0,12   8  l

Stand 13.06.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      26     13    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,04   0,02   0,1%     inf Tage      34     17    0,04 -0,14   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      71     27    1,00  0,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      25     16    1,00  0,00   7  l
    Emmendingen                0,34   0,21   1,7%    42,3 Tage      42     25    0,13 -0,07  14  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      20     10    0,14  0,75   8  l
    Esslingen                  0,46   0,09   1,7%    42,0 Tage     114     21    0,38 -0,14   7  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      78     34    1,00  0,00   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      37     31    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      40     30    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      41     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      16     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      47     42    1,00  0,00   7  l
    Karlsruhe                  0,46   0,10   2,0%    34,3 Tage      79     18    0,38 -0,14   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      13    4,2    1,00  0,00   7  l
    Konstanz                   0,33   0,12   3,9%    18,3 Tage      16    5,6    0,17 -0,13   8  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      60     26    0,17  1,70  10  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,40   0,13   3,7%    19,3 Tage      13    4,2    0,04 -0,07  14  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      21     15    1,00  0,00   7  l
    Ortenaukreis               0,00   0,00   0,0%     inf Tage     125     29    1,00  0,00   7  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      37     12    0,27  1,70  10  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     8,0    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     8,0    2,8    1,00  0,00   7  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      89     21    0,25  0,75   8  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      81     28    0,17  1,70  10  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      38    6,9    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      25     18    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      58     30    0,07   nan   7  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      30     14    1,00  0,00   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      34     26    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      63    9,9    0,12  0,80  10  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      59     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      21     15    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,17   0,09   0,8%    89,5 Tage      77     41    0,06 -0,07  14  l
    
    Baden-Württemberg          0,22   0,00   0,0%     inf Tage    1805     16    0,40  0,23  10  l

Stand 05.06.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      26     13    1,00  0,00   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      33     17    1,00  0,00   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      47     12    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,17   0,06   0,2%     inf Tage      71     27    0,05  0,09   8  l
    Calw                       0,00   0,00   0,0%     inf Tage      25     16    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      40     24    1,00  0,00   7  l
    Enzkreis                   0,46   0,23   4,7%    15,0 Tage      19    9,6    0,38 -0,14   7  l
    Esslingen                   2,4   0,45   4,1%    17,3 Tage     113     21    0,50 -0,49   9  l
    Freiburg im Breisgau (St   0,46   0,20   2,1%    34,1 Tage      78     34    0,38 -0,14   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      37     31    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    1,00  0,00   7  l
    Heidenheim                 0,20   0,15   1,3%    54,3 Tage      40     30    0,10 -0,07  14  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      41     12    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      16     13    1,00  0,00   7  l
    Hohenlohekreis             0,33   0,30   2,0%    34,5 Tage      47     42    0,17 -0,13   8  l
    Karlsruhe                   1,3   0,29   3,7%    19,3 Tage      78     18    0,62 -0,14   7  l
    Karlsruhe (Stadtkreis)     0,02   0,01   0,2%     inf Tage      13    4,2    0,10  0,78   9  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      15    5,3    1,00  0,00   7  l
    Lörrach                    0,40   0,17   1,5%    45,4 Tage      59     26    0,10 -0,07  14  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      72     13    1,00  0,00   7  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,46   0,15   6,7%    10,6 Tage      11    3,6    0,38 -0,14   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      21     15    0,21 -0,56   8  l
    Ortenaukreis                1,2   0,28   2,0%    35,2 Tage     125     29    0,18 -0,11   9  l
    Ostalbkreis                 1,2   0,39   4,7%    15,1 Tage      36     11    0,18 -0,09  11  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     8,0    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      17    7,4    1,00  0,00   7  l
    Ravensburg                 0,20   0,07   3,5%    20,1 Tage     8,0    2,8    0,10 -0,07  14  l
    Rems-Murr-Kreis            0,61   0,14   2,0%    35,3 Tage      88     21    0,22 -0,14   7  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      80     28    0,27  0,53  12  l
    Rhein-Neckar-Kreis         0,33   0,06   2,3%    30,6 Tage      38    6,9    0,17 -0,13   8  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      25     18    1,00  0,00   7  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      58     30    1,00  0,00   7  l
    Schwarzwald-Baar-Kreis     0,56   0,26   3,4%    21,0 Tage      30     14    0,27 -0,11   9  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      34     26    0,17 -0,14   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      62    9,8    0,12  0,38  13  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      59     26    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      21     15    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      76     40    1,00  0,00   7  l
    
    Baden-Württemberg            12   0,11   6,2%    11,6 Tage    1790     16    0,59 -0,24   7  e

Stand 30.05.2020

    Alb-Donau-Kreis             1,0   0,52   5,0%    14,2 Tage      26     13    0,07 -0,10  10  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      33     17    1,00  0,00   7  l
    Böblingen                  0,54   0,14   2,1%    33,7 Tage      47     12    0,06 -0,07  14  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,53   0,20   1,9%    36,3 Tage      67     25    0,27 -0,10  10  l
    Calw                       0,20   0,13   1,7%    41,2 Tage      25     16    0,10 -0,07  14  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      40     24    1,00  0,00   7  l
    Enzkreis                   0,05   0,02   0,3%     inf Tage      18    9,0    0,05  0,82  11  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     107     20    0,02  0,82  11  l
    Freiburg im Breisgau (St   0,17   0,07   0,8%    89,5 Tage      77     33    0,06 -0,07  14  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      37     31    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    0,16 -1,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      39     29    1,00  0,00   7  l
    Heilbronn                   1,0   0,29   4,3%    16,5 Tage      41     12    0,17 -0,12   8  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      16     13    1,00  0,00   7  l
    Hohenlohekreis             0,07   0,06   0,2%     inf Tage      46     41    0,04 -0,14   7  l
    Karlsruhe                  0,04   0,01   0,0%     inf Tage      75     17    0,04 -0,14   7  l
    Karlsruhe (Stadtkreis)     0,33   0,11   4,7%    15,2 Tage      12    3,8    0,17 -0,13   8  l
    Konstanz                   0,05   0,02   0,3%     inf Tage      15    5,3    0,05  0,82  11  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      57     25    1,00  0,00   7  l
    Ludwigsburg                0,24   0,04   1,2%    58,8 Tage      72     13    0,08 -0,11   9  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      10    3,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,46   0,32   4,2%    16,8 Tage      23     16    0,38 -0,14   7  l
    Ortenaukreis               0,33   0,08   0,3%     inf Tage     119     28    0,10  0,60   9  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      31    9,9    1,00  0,00   7  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     8,0    6,4    1,00  0,00   7  l
    Rastatt                    0,33   0,14   3,7%    18,9 Tage      17    7,4    0,17 -0,13   8  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     7,0    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,12   0,03   0,1%     inf Tage      86     20    0,12  0,75  12  l
    Reutlingen                  1,2   0,42   2,4%    29,1 Tage      77     27    0,10 -0,08  13  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      37    6,8    1,00  0,00   7  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      25     18    1,00  0,00   7  l
    Schwäbisch Hall            0,34   0,18   1,4%    51,3 Tage      58     30    0,13 -0,07  14  l
    Schwarzwald-Baar-Kreis     0,07   0,03   0,2%     inf Tage      28     13    0,13  0,33   9  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      33     25    1,00  0,00   7  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      61    9,6    0,48  0,75   8  l
    Tübingen                   0,74   0,33   2,2%    31,7 Tage      59     26    0,39 -0,07  14  l
    Tuttlingen                 0,17   0,12   1,7%    42,3 Tage      21     15    0,06 -0,07  14  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,68   0,36   1,8%    39,3 Tage      76     40    0,05 -0,09  11  l
    
    Baden-Württemberg           9,8   0,09   3,4%    20,7 Tage    1749     16    0,14 -0,30   7  e


Stand 24.05.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      21     11    0,14  0,82  11  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      33     17    0,23  0,71   7  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      44     11    1,00  0,00   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      65     25    0,22  0,39  14  l
    Calw                       0,00   0,00   0,0%     inf Tage      24     15    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      40     24    1,00  0,00   7  l
    Enzkreis                   0,04   0,02   0,2%     inf Tage      17    8,5    0,04 -0,14   7  l
    Esslingen                  0,00   0,00   0,0%     inf Tage     107     20    0,23  0,48  13  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      76     33    1,00  0,00   7  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      37     31    1,00  0,00   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      40     16    0,03 -0,08  13  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    1,00  0,00   7  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      39     29    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      38     11    1,00  0,00   7  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      16     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      44     39    1,00  0,00   7  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      74     17    1,00  0,00   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      11    3,5    1,00  0,00   7  l
    Konstanz                   0,01   0,00   0,1%     inf Tage      14    4,9    0,07  0,83  12  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      57     25    0,17  0,78   9  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      71     13    0,26  0,53  12  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    1,00  0,00   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      10    3,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      22     15    0,24  0,21  11  l
    Ortenaukreis                1,2   0,28   1,7%    40,1 Tage     114     27    0,08 -0,08  13  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      31    9,9    0,36  0,38  12  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     8,0    6,4    1,00  0,00   7  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      16    6,9    0,22 -0,14   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     7,0    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis             1,1   0,25   1,3%     inf Tage      80     19    0,04 -0,14   7  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      70     24    0,26  0,15  13  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      37    6,8    0,44  0,15  12  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      25     18    1,00  0,00   7  l
    Schwäbisch Hall            0,46   0,24   2,5%    28,6 Tage      57     29    0,38 -0,14   7  l
    Schwarzwald-Baar-Kreis     0,71   0,34   4,7%    15,1 Tage      27     13    0,40 -0,14   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      33     25    0,17 -0,12   8  l
    Stuttgart                  0,73   0,11   2,4%    28,9 Tage      59    9,3    0,22 -0,09  11  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      55     24    1,00  0,00   7  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      20     14    1,00  0,00   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,11   0,06   0,2%     inf Tage      73     39    0,23  0,08  14  l
    
    Baden-Württemberg           2,3   0,02   0,1%     inf Tage    1696     15    0,66  0,07  13  l

Stand 20.05.2020

    Alb-Donau-Kreis            0,25   0,13   1,2%     inf Tage      21     11    0,09  0,71   7  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,00   0,00   0,0%     inf Tage      32     16    0,27  0,48   9  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      44     11    0,63  0,71   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,46   0,18   2,3%    30,8 Tage      65     25    0,38 -0,14   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      24     15    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      40     24    1,00  0,00   7  l
    Enzkreis                   0,46   0,23   5,1%    14,0 Tage      17    8,5    0,38 -0,14   7  l
    Esslingen                  0,46   0,09   1,7%    40,4 Tage     106     20    0,38 -0,14   7  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      76     33    0,44  0,31   8  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      37     31    0,22 -0,14   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      40     16    1,00  0,00   7  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    0,17 -0,12   8  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      39     29    1,00  0,00   7  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      38     11    0,27  0,78   9  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      16     13    1,00  0,00   7  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      44     39    0,29  0,17   8  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      74     17    0,15  1,75  12  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      11    3,5    1,00  0,00   7  l
    Konstanz                   0,46   0,16   5,7%    12,4 Tage      14    4,9    0,38 -0,14   7  l
    Lörrach                    0,50   0,22   2,1%    33,6 Tage      57     25    0,14 -0,12   8  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      70     13    0,38  0,75   8  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage      10    7,6    0,39  0,78   9  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      10    3,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      21     15    0,47  0,29   7  l
    Ortenaukreis               0,24   0,06   0,2%     inf Tage     109     25    0,17  0,15  13  l
    Ostalbkreis                0,17   0,05   0,5%     inf Tage      31    9,9    0,21  0,31   8  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     8,0    6,4    0,19  0,80  10  l
    Rastatt                    0,82   0,36   7,5%     9,6 Tage      16    6,9    0,62 -0,14   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     7,0    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis             3,3   0,78   6,1%    11,6 Tage      75     18    0,10 -0,06   7  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      69     24    0,48  0,19   9  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      36    6,6    0,76  0,17   8  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      25     18    0,57  0,75   8  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      56     29    0,15 -0,14   7  l
    Schwarzwald-Baar-Kreis     0,08   0,04   0,3%     inf Tage      25     12    0,26  0,09   8  l
    Sigmaringen                0,20   0,15   1,4%    48,5 Tage      33     25    0,10 -0,07  14  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      56    8,8    1,00  0,00   7  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      55     24    0,41  3,38   8  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      20     14    0,17  0,14   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,22   0,12   0,3%     inf Tage      72     38    0,25  0,08  10  l
    
    Baden-Württemberg           5,2   0,05   0,3%     inf Tage    1673     15    0,63  0,06   9  l

Stand 16.05.2020

    Alb-Donau-Kreis            0,57   0,29   3,4%    20,8 Tage      19    9,7    0,05 -0,07  14  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                   0,40   0,20   1,3%     inf Tage      31     16    0,05  0,26  10  l
    Böblingen                  0,62   0,16   2,5%    28,3 Tage      44     11    0,28 -0,08  12  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,09   0,03   0,1%     inf Tage      64     24    0,14  0,52  11  l
    Calw                       0,00   0,00   0,0%     inf Tage      24     15    1,00  0,00   7  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      40     24    1,00  0,00   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      16    8,0    1,00  0,00   7  l
    Esslingen                  0,33   0,06   0,3%     inf Tage     105     20    0,17  0,12   8  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      76     33    0,15  1,06  12  l
    Freudenstadt               0,82   0,70   4,4%    16,3 Tage      37     31    0,62 -0,14   7  l
    Göppingen                  0,33   0,13   2,7%    25,7 Tage      40     16    0,19 -1,00   8  l
    Heidelberg (Stadtkreis)    0,36   0,23   7,4%     9,7 Tage     7,0    4,4    0,29 -1,00  11  l
    Heidenheim                 0,00   0,00   0,0%     inf Tage      39     29    0,19  0,78   9  l
    Heilbronn                  0,42   0,12   1,1%     inf Tage      38     11    0,08  0,20  10  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      16     13    0,17 -0,12   8  l
    Hohenlohekreis              1,0   0,92   3,1%    22,6 Tage      44     39    0,27 -0,07  14  l
    Karlsruhe                  0,46   0,10   2,1%    33,1 Tage      74     17    0,38 -0,14   7  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage      11    3,5    0,25  0,75   8  l
    Konstanz                   0,03   0,01   0,2%     inf Tage      13    4,6    0,08  0,39  14  l
    Lörrach                    0,18   0,08   0,3%     inf Tage      56     24    0,11  0,28  12  l
    Ludwigsburg                0,66   0,12   1,5%    46,7 Tage      69     13    0,05 -0,07  14  l
    Main-Tauber-Kreis          0,34   0,26   4,2%    16,7 Tage      10    7,6    0,13 -0,07  14  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      10    3,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis       1,0   0,70   6,1%    11,8 Tage      21     15    0,61 -0,10  10  l
    Ortenaukreis               0,13   0,03   0,1%     inf Tage     107     25    0,30  0,26  13  l
    Ostalbkreis                 1,4   0,45   6,4%    11,2 Tage      30    9,6    0,37 -0,12   8  l
    Pforzheim (Stadtkreis)     0,35   0,28   5,1%    13,8 Tage     8,0    6,4    0,12 -0,08  13  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      14    6,1    1,00  0,00   7  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     7,0    2,5    1,00  0,00   7  l
    Rems-Murr-Kreis            0,58   0,14   0,9%     inf Tage      65     15    0,12  0,11   9  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      68     24    0,41  0,43  11  l
    Rhein-Neckar-Kreis          1,2   0,21   5,0%    14,3 Tage      36    6,6    0,76 -0,12   8  l
    Rottweil                   0,14   0,10   0,5%     inf Tage      25     18    0,27  0,09  11  l
    Schwäbisch Hall            0,95   0,49   2,4%    29,6 Tage      56     29    0,04 -0,09  11  l
    Schwarzwald-Baar-Kreis      1,3   0,62   7,5%     9,5 Tage      24     11    0,47 -0,14   7  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      32     24    1,00  0,00   7  l
    Stuttgart                  0,02   0,00   0,0%     inf Tage      56    8,8    0,25  0,20  10  l
    Tübingen                    1,0   0,46   2,9%    24,6 Tage      55     24    0,05 -0,10  10  l
    Tuttlingen                  1,6    1,2  10,5%     6,9 Tage      20     14    0,46 -0,14   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,93   0,49   2,0%    34,2 Tage      71     38    0,13 -0,11   9  l
    
    Baden-Württemberg            21   0,19   3,9%    18,3 Tage    1645     15    0,36 -0,14   7  e

Stand 12.05.2020

    Alb-Donau-Kreis            0,55   0,28   4,2%    16,9 Tage      17    8,7    0,12 -0,10  10  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   7  l
    Biberach                    1,0   0,51   4,7%    15,2 Tage      29     15    0,13 -0,11   9  l
    Böblingen                  0,46   0,12   2,9%    24,0 Tage      42     11    0,38 -0,14   7  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   7  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      61     23    0,26  1,00   7  l
    Calw                       0,00   0,00   0,0%     inf Tage      24     15    0,18  0,06  14  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      40     24    0,40  0,71   7  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      16    8,0    1,00  0,00   7  l
    Esslingen                   1,8   0,33   2,6%    26,6 Tage     102     19    0,26 -0,09  11  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      73     32    0,44  4,25   8  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      35     30    0,40  0,71   7  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    0,02   nan   7  l
    Heidelberg (Stadtkreis)    0,08   0,05   5,5%    12,9 Tage     6,0    3,7    0,17 -0,12   8  l
    Heidenheim                 0,65   0,49   2,4%    29,4 Tage      38     29    0,07 -0,08  13  l
    Heilbronn                   1,2   0,34   4,1%    17,0 Tage      36     10    0,20 -0,09  11  l
    Heilbronn (Stadtkreis)     0,04   0,03   0,2%     inf Tage      16     13    0,09  0,38  12  l
    Hohenlohekreis             0,50   0,45   2,2%    32,4 Tage      40     36    0,13 -0,08  12  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      73     16    0,38  2,79   8  l
    Karlsruhe (Stadtkreis)     0,61   0,19   7,4%     9,7 Tage      11    3,5    0,22 -0,14   7  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      12    4,2    0,27  0,80  10  l
    Lörrach                    0,29   0,12   0,5%     inf Tage      55     24    0,10  0,34  14  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      66     12    0,47  0,16  14  l
    Main-Tauber-Kreis          0,46   0,35   7,7%     9,3 Tage     9,0    6,8    0,38 -0,14   7  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      10    3,2    1,00  0,00   7  l
    Neckar-Odenwald-Kreis      0,36   0,25   3,1%    23,0 Tage      18     13    0,09 -0,09  11  l
    Ortenaukreis               0,45   0,10   0,4%     inf Tage     105     24    0,33  0,12  13  l
    Ostalbkreis                0,11   0,03   0,4%     inf Tage      25    8,0    0,04 -0,14   7  l
    Pforzheim (Stadtkreis)     0,33   0,27   6,7%    10,7 Tage     7,0    5,6    0,17 -0,13   8  l
    Rastatt                    0,17   0,07   2,1%    32,9 Tage      14    6,1    0,06 -0,07  14  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     7,0    2,5    0,17 -0,12   8  l
    Rems-Murr-Kreis             1,6   0,38   3,8%    18,6 Tage      62     15    0,30 -0,09  11  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      66     23    0,45  0,54   7  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      32    5,8    0,57  0,75   8  l
    Rottweil                   0,00   0,00   0,0%     inf Tage      23     16    0,75  0,14   7  l
    Schwäbisch Hall            0,25   0,13   0,5%     inf Tage      53     27    0,10  0,53   8  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      20    9,4    0,32  0,78   9  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      32     24    0,17 -0,12   8  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      55    8,7    0,19  0,66  13  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      50     22    0,42  0,31   8  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      16     11    0,35  1,57   7  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   7  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   7  l
    Zollernalbkreis            0,89   0,47   2,5%    28,3 Tage      68     36    0,19 -0,14   7  l
    
    Baden-Württemberg           9,8   0,09   0,6%     inf Tage    1570     14    0,49  0,11   8  l

Stand 08.05.2020

    Alb-Donau-Kreis             1,1   0,56  11,1%     6,6 Tage      16    8,2    0,80 -0,25   4  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    1,00  0,00   4  l
    Biberach                   0,20   0,10   0,8%     inf Tage      26     13    0,15  0,44  10  l
    Böblingen                  0,00   0,00   0,0%     inf Tage      41     10    1,00  0,00   4  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   4  l
    Breisgau-Hochschwarzwald   0,60   0,23   1,0%     inf Tage      59     22    0,20 -0,10   4  l
    Calw                       0,70   0,44   6,8%    10,5 Tage      24     15    0,60 -0,25   4  l
    Emmendingen                0,80   0,48   4,3%    16,4 Tage      40     24    0,33 -0,20   5  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      16    8,0    1,00  0,00   4  l
    Esslingen                  0,04   0,01   0,0%     inf Tage      96     18    0,40  0,27  10  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      73     32    0,75  3,50   4  l
    Freudenstadt               0,71   0,61   4,0%    17,7 Tage      35     30    0,40 -0,14   7  l
    Göppingen                  0,70   0,27   5,0%    14,2 Tage      40     16    0,60 -0,25   4  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     6,0    3,7    0,30 -1,00   8  l
    Heidenheim                  1,5    1,1   7,5%     9,5 Tage      37     28    0,45 -0,25   4  l
    Heilbronn                   1,5   0,44   7,1%    10,1 Tage      33    9,6    0,62 -0,17   6  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      15     12    1,00  0,00   4  l
    Hohenlohekreis             0,33   0,30   2,3%    30,6 Tage      38     34    0,17 -0,13   8  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      71     16    0,68  7,25   4  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     9,0    2,9    0,13 -0,20   5  l
    Konstanz                   0,05   0,02   0,4%     inf Tage      12    4,2    0,17  0,67   6  l
    Lörrach                    0,10   0,04   0,2%     inf Tage      53     23    0,90  0,50   4  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      65     12    0,54  0,15  10  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage     8,0    6,0    1,00  0,00   4  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      10    3,2    1,00  0,00   4  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      17     12    0,23  0,21  11  l
    Ortenaukreis               0,91   0,21   0,9%     inf Tage     101     24    0,29  0,13   9  l
    Ostalbkreis                 2,1   0,67  13,5%     5,5 Tage      25    8,0    0,60 -0,25   4  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     6,0    4,8    1,00  0,00   4  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      13    5,6    1,00  0,00   4  l
    Ravensburg                 0,20   0,07   3,8%    18,3 Tage     7,0    2,5    0,10 -0,07  14  l
    Rems-Murr-Kreis             1,4   0,33   5,2%    13,7 Tage      57     13    0,50 -0,20   5  l
    Reutlingen                 0,45   0,16   0,7%     inf Tage      63     22    0,28  0,22  10  l
    Rhein-Neckar-Kreis         0,00   0,00   0,0%     inf Tage      32    5,8    0,80  0,50   4  l
    Rottweil                    1,2   0,86   8,2%     8,8 Tage      22     16    0,60 -0,25   4  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      50     26    0,53  2,00   4  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      19    8,9    0,50  1,40   5  l
    Sigmaringen                0,10   0,08   0,3%     inf Tage      32     24    0,07 -0,25   4  l
    Stuttgart                   1,1   0,17   5,1%    13,9 Tage      54    8,5    0,80 -0,25   4  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      49     22    0,60  0,25   4  l
    Tuttlingen                 0,20   0,14   1,3%     inf Tage      15     11    0,07 -0,25   4  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     5,0    4,0    1,00  0,00   4  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   4  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      65     34    0,45  1,25   4  l
    
    Baden-Württemberg            17   0,15   1,1%     inf Tage    1517     14    0,65  0,11   4  l

Stand 04.05.2020

    Alb-Donau-Kreis            0,00   0,00   0,0%     inf Tage      14    7,1    0,89  1,25   4  l
    Baden-Baden (Stadtkreis)   0,00   0,00   0,0%     inf Tage      19     34    0,30  0,50  10  l
    Biberach                   0,30   0,15   1,3%     inf Tage      24     12    0,60  0,12   4  l
    Böblingen                  0,70   0,18   4,9%    14,4 Tage      41     10    0,60 -0,25   4  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     8,0    3,7    1,00  0,00   4  l
    Breisgau-Hochschwarzwald   0,00   0,00   0,0%     inf Tage      53     20    0,72  2,20   5  l
    Calw                       0,00   0,00   0,0%     inf Tage      23     15    1,00  0,00   4  l
    Emmendingen                0,00   0,00   0,0%     inf Tage      38     23    0,17  0,11  14  l
    Enzkreis                   0,00   0,00   0,0%     inf Tage      16    8,0    0,13 -0,20   5  l
    Esslingen                  0,00   0,00   0,0%     inf Tage      92     17    0,77  0,35   6  l
    Freiburg im Breisgau (St   0,00   0,00   0,0%     inf Tage      67     29    0,75  0,60   5  l
    Freudenstadt               0,00   0,00   0,0%     inf Tage      33     28    0,68  3,00   5  l
    Göppingen                  0,00   0,00   0,0%     inf Tage      39     15    1,00  0,00   4  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     7,0    4,4    0,13 -0,20   5  l
    Heidenheim                 0,70   0,53   5,5%    12,9 Tage      34     26    0,60 -0,25   4  l
    Heilbronn                  0,00   0,00   0,0%     inf Tage      29    8,5    0,49  1,50   6  l
    Heilbronn (Stadtkreis)     0,20   0,16   1,3%     inf Tage      15     12    0,20  0,50   4  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      37     33    1,00  0,00   4  l
    Karlsruhe                  0,00   0,00   0,0%     inf Tage      60     14    0,29  2,41  11  l
    Karlsruhe (Stadtkreis)     0,00   0,00   0,0%     inf Tage     7,0    2,2    0,33  0,60   5  l
    Konstanz                   0,00   0,00   0,0%     inf Tage      11    3,9    0,20  1,50   6  l
    Lörrach                    0,00   0,00   0,0%     inf Tage      49     21    0,25  0,94   6  l
    Ludwigsburg                0,00   0,00   0,0%     inf Tage      63     12    0,86  0,80   5  l
    Main-Tauber-Kreis          0,20   0,15   3,5%    20,1 Tage     8,0    6,0    0,10 -0,07  14  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage      10    3,2    1,00  0,00   4  l
    Neckar-Odenwald-Kreis      0,00   0,00   0,0%     inf Tage      16     11    0,52  0,29   7  l
    Ortenaukreis                3,3   0,76   4,6%    15,3 Tage      96     22    0,28 -0,12   8  l
    Ostalbkreis                0,00   0,00   0,0%     inf Tage      22    7,0    0,36  0,21  11  l
    Pforzheim (Stadtkreis)     0,42   0,33   7,5%     9,6 Tage     6,0    4,8    0,21 -0,08  13  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      13    5,6    1,00  0,00   4  l
    Ravensburg                 0,00   0,00   0,0%     inf Tage     6,0    2,1    1,00  0,00   4  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      54     13    0,75  1,80   5  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      57     20    0,94  0,35   6  l
    Rhein-Neckar-Kreis         0,67   0,12   4,0%    17,5 Tage      30    5,5    0,17 -0,13   8  l
    Rottweil                   0,70   0,50   7,9%     9,2 Tage      19     14    0,60 -0,25   4  l
    Schwäbisch Hall            0,00   0,00   0,0%     inf Tage      46     23    1,00  0,00   4  l
    Schwarzwald-Baar-Kreis      1,4   0,66  12,8%     5,8 Tage      18    8,5    0,60 -0,25   4  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      31     24    0,13  0,86  14  l
    Stuttgart                  0,00   0,00   0,0%     inf Tage      52    8,2    0,50  1,40   5  l
    Tübingen                   0,00   0,00   0,0%     inf Tage      44     19    1,00  0,00   4  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      13    9,3    1,00  0,00   4  l
    Ulm (Stadtkreis)           0,24   0,19   6,2%    11,5 Tage     5,0    4,0    0,08 -0,11   9  l
    Waldshut                   0,00   0,00   0,0%     inf Tage      35     21    1,00  0,00   4  l
    Zollernalbkreis            0,00   0,00   0,0%     inf Tage      62     33    0,45  1,25   4  l
    
    Baden-Württemberg           7,6   0,07   0,5%     inf Tage    1422     13    0,95  0,25   5  e

Stand 23.04.2020

    Alb-Donau-Kreis            0,71   0,36  10,0%     7,3 Tage     9,0    4,6    0,40 -0,14   7  l
    Baden-Baden (Stadtkreis)   0,80    1,5   8,5%     8,5 Tage      14     25    0,20 -0,25   4  l
    Biberach                   0,00   0,00   0,0%     inf Tage      16    8,0    0,27  1,08   6  l
    Böblingen                   1,9   0,49   8,8%     8,2 Tage      36    9,2    0,90 -0,25   4  l
    Bodenseekreis              0,00   0,00   0,0%     inf Tage     7,0    3,2    0,13 -0,20   5  l
    Breisgau-Hochschwarzwald    5,3    2,0  15,8%     4,7 Tage      44     17    0,37 -0,08   4  l
    Calw                       0,10   0,06   0,8%     inf Tage      13    8,2    0,30  0,00   4  l
    Emmendingen                0,92   0,55   4,0%    17,7 Tage      35     21    0,15 -0,12   8  l
    Enzkreis                   0,19   0,10   1,6%     inf Tage      12    6,0    0,41  0,39   6  l
    Esslingen                   3,6   0,67   8,2%     8,8 Tage      67     13    0,48 -0,20   5  l
    Freiburg im Breisgau (St    4,8    2,1  12,2%     6,0 Tage      60     26    0,70 -0,16   4  l
    Freudenstadt               0,40   0,34   1,7%     inf Tage      24     20    0,60  0,31   4  l
    Göppingen                   2,2   0,86  12,1%     6,1 Tage      28     11    0,80 -0,25   4  l
    Heidelberg (Stadtkreis)    0,00   0,00   0,0%     inf Tage     6,0    3,7    1,00  0,00   4  l
    Heidenheim                 0,10   0,08   0,3%     inf Tage      30     23    0,90  0,50   4  l
    Heilbronn                   1,8   0,52  11,7%     6,3 Tage      25    7,3    0,89 -0,25   4  l
    Heilbronn (Stadtkreis)     0,00   0,00   0,0%     inf Tage      10    7,9    1,00  0,00   4  l
    Hohenlohekreis             0,00   0,00   0,0%     inf Tage      34     30    0,50  0,19   9  l
    Karlsruhe                   1,8   0,41   7,0%    10,3 Tage      45     10    0,37 -0,20   5  l
    Karlsruhe (Stadtkreis)     0,70   0,22  19,5%     3,9 Tage     5,0    1,6    0,60 -0,25   4  l
    Konstanz                   0,00   0,00   0,0%     inf Tage     8,0    2,8    1,00  0,00   4  l
    Lörrach                     2,0   0,87   7,3%     9,8 Tage      34     15    0,17 -0,07   5  l
    Ludwigsburg                 2,8   0,51   7,8%     9,2 Tage      47    8,6    0,13 -0,20   5  l
    Main-Tauber-Kreis          0,00   0,00   0,0%     inf Tage     7,0    5,3    1,00  0,00   4  l
    Mannheim (Stadtkreis)      0,00   0,00   0,0%     inf Tage     6,0    1,9    1,00  0,00   4  l
    Neckar-Odenwald-Kreis       1,8    1,2  16,3%     4,6 Tage      12    8,4    0,50 -0,17   6  l
    Ortenaukreis                1,7   0,39   2,2%     inf Tage      77     18    0,13  0,12   9  l
    Ostalbkreis                 1,5   0,49  10,9%     6,7 Tage      18    5,7    0,15 -0,17   6  l
    Pforzheim (Stadtkreis)     0,00   0,00   0,0%     inf Tage     4,0    3,2    1,00  0,00   4  l
    Rastatt                    0,00   0,00   0,0%     inf Tage      11    4,8    1,00  0,00   4  l
    Ravensburg                 0,38   0,13   8,8%     8,2 Tage     6,0    2,1    0,15 -0,17   6  l
    Rems-Murr-Kreis            0,00   0,00   0,0%     inf Tage      40    9,4    0,25  0,70   9  l
    Reutlingen                 0,00   0,00   0,0%     inf Tage      16    5,6    1,00  0,00   4  l
    Rhein-Neckar-Kreis          1,6   0,29   9,0%     8,1 Tage      26    4,7    0,57 -0,20   5  l
    Rottweil                   0,20   0,14   1,8%     inf Tage      11    7,9    0,20  0,50   4  l
    Schwäbisch Hall            0,30   0,15   0,8%     inf Tage      39     20    0,60  0,12   4  l
    Schwarzwald-Baar-Kreis     0,00   0,00   0,0%     inf Tage      13    6,1    0,45  1,25   4  l
    Sigmaringen                0,00   0,00   0,0%     inf Tage      29     22    0,25  0,16  14  l
    Stuttgart                   2,8   0,44   5,6%    12,8 Tage      45    7,1    0,11 -0,07  14  l
    Tübingen                   0,20   0,09   0,6%     inf Tage      36     16    0,34  0,80   5  l
    Tuttlingen                 0,00   0,00   0,0%     inf Tage      10    7,1    1,00  0,00   4  l
    Ulm (Stadtkreis)           0,00   0,00   0,0%     inf Tage     3,0    2,4    1,00  0,00   4  l
    Waldshut                    3,4    2,0  14,4%     5,1 Tage      32     19    0,90 -0,25   4  l
    Zollernalbkreis            0,50   0,26   1,0%     inf Tage      53     28    0,25  0,62   7  l
    
    Baden-Württemberg            56   0,51  12,3%     6,0 Tage    1103   10,0    0,48 -0,24   4  e

In den nachfolgenden Tabellen wurden die kumulativen Fallzahlen und nicht die täglichen Zuwächse für die Annäherungen verwendet.

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

Wenn Sie meine Arbeit unterstützen können, dann bitte ich Sie um eine Spende. Danke!

* Adresse für PayPal-Zahlungen: [https://PayPal.me/BenceM](https://PayPal.me/BenceM)
* Adresse für Bitcoin (BTC): `13veK2ecjhtNenTxhGKJjP83QiMmNd1M7p`
* Adresse für Ether (ETH) und Tokens: `0x49fC2a73e1eC76248324E411e699f92adD6565Ff`

Finden Sie mich auf [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), auf meiner Webseite/Blog: [Melykuti.me](https://melykuti.me), oder folgen Sie mir auf [Facebook](https://www.facebook.com/bence.melykuti) für meine öffentlichen Posts.

Ich arbeite als selbständiger Data Scientist. Sie können mich mit Ihrem Projekt beauftragen.
