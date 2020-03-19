## Analyse und Projektionen für die exponentielle Verbreitung der SARS-CoV-2 Coronavirus-Pandemie in Deutschland und in den deutschen Bundesländern

16 März 2020 (aktualisiert am 19 März 2020), Freiburg i. Br. -- In der Anfangsphase der Verbreitung der Epidemie ist fast die ganze Bevölkerung empfindlich und jeder Erkrankte kann eine erhebliche Anzahl von gesunden Menschen anstecken. So kann die Anzahl der Infizierter Schritt für Schritt immer ein Faktor größer werden. Dieser Verlauf ist exponentielles Wachstum.

Bisher stimmen die beobachteten Fallzahlen mit diesem Verlauf überein, sowohl in vielen europäischen Ländern als auch in Deutschland und in jedem einzigen Bundesland. In dieser Analyse versuche ich es in begreifbarer Form zu beantworten, wie schnell die Pandemie sich zur Zeit ausbreitet. Konkret, mich interessiert wieviele _aktiv ansteckende Kranke_ es gibt, dass heißt, wieviele Leute die Krankheit bekommen haben, die sich noch nicht erholt haben und noch nicht gestorben sind.

_Wie hoch ist die Wahrscheinlichkeit, dass ich mit einem Infizierten in Kontakt komme, wenn ich meine Wohnung verlasse?_ Diese Wahrscheinlichkeit kann ich nicht ausrechnen, sie wächst jedoch ungefähr proportional zur Gesamtanzahl der Ansteckenden.

### Analyse

Meine Methodologie habe ich [auf Englischem in Detail beschrieben.](https://github.com/Melykuti/COVID-19/blob/master/README.md) Für Deutschland und für die Bundesländer rechne ich für jeden Tag das Folgende aus:

`Nr. der Ansteckenden = Nr. der Fälle - Nr. der Tode.`

Ich möchte die `Nr. der Erholten` auch subtrahieren, aber diese Zahl ist bisher nicht veröffentlicht worden. In der Anfangsphase ist diese Zahl sowieso niedrig und sie verursacht keine große Ungenauigkeit.

Ich nehme den Logarithmus auf Basis 2 der Anzahl der Ansteckenden. Dass diese Zahl tatsächlich exponentiell wächst, ist daran erkennbar, dass der Logarithmus nicht unter einer geraden Linie mit einer positiven Steigung fällt.

Mit linearer Regression bestimme ich eine annährende Linie, und von deren Steigung kann ich vieles ausrechnen. Ich kann sagen, mit welchem Faktor die Anzahl von einem Tag bis zum nächsten wächst. Eng verbunden damit ist die Rate, wie lange es dauert, bis die Anzahl der Ansteckenden sich verdoppelt.

### Schaubilder

Die Anzahl der derzeit Infizierten (Ansteckenden) wird durch die gesamte Anzahl der Fälle minus die Anzahl der Tode gerechnet.

Auf der linken Seite ist die Grafik auf normaler linearer Skala, auf der rechten Seite auf logarithmischer Skala auf Basis 10. Die blaue Kurve zeigt die Beobachtungen. Die orangenfarbige Linie ist die exponentielle Annäherung.

Ich wähle immer die letzten 5-14 Tage aus, um die lineare Regression durchzuführen. Mit der Wahl der Länge des Zeitintervals versuche ich die beste Anpassung zu erreichen, gemessen an R^2 und an der Differenz zwischen dem letzten Tag in der geraden Strecke und dem letzten Datenpunkt. Seit 18.03.2020 ist diese Optimierung automatisiert.

#### Die gesamte Bundesrepublik

![Deutschland, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Deutschland_2020-03-19.png)

#### Die einzelnen Bundesländer

![Baden-Württemberg, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Baden-Württemberg_2020-03-19.png)

![Bayern, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Bayern_2020-03-19.png)

![Berlin, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Berlin_2020-03-19.png)

![Brandenburg, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Brandenburg_2020-03-19.png)

![Bremen, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Bremen_2020-03-19.png)

![Hamburg, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Hamburg_2020-03-19.png)

![Hessen, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Hessen_2020-03-19.png)

![Mecklenburg-Vorpommern, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Mecklenburg-Vorpommern_2020-03-19.png)

![Niedersachsen, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Niedersachsen_2020-03-19.png)

![Nordrhein-Westfalen, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Nordrhein-Westfalen_2020-03-19.png)

![Rheinland-Pfalz, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Rheinland-Pfalz_2020-03-19.png)

![Saarland, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Saarland_2020-03-19.png)

![Sachsen, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Sachsen_2020-03-19.png)

![Sachsen-Anhalt, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Sachsen-Anhalt_2020-03-19.png)

![Schleswig-Holstein, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Schleswig-Holstein_2020-03-19.png)

![Thüringen, Stand 19.03.2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Thüringen_2020-03-19.png)


### Resultate

Diese Resultate sind die direkte numerische Folge der linearen Anpassungen im vorherigen Abschnitt.

**Ich mache eine grobe Schätzung, wieviele Personen zur Zeit infiziert sein können.** Meine Annahme ist es, dass die gemeldeten Zahlen nur diejenigen zeigen, die schon getestet worden sind. Aber die Inkubationszeit der COVID-19 Krankheit beträgt im Schnitt fünf Tage (von 1 Tag bis 14 Tage), deshalb werden sich die heute infizierten erst in ungefähr fünf Tagen melden und testen lassen, sogar später. Aber sie sind bereits unumkehrbar infiziert und wahrscheinlich ansteckend, und ich will diese Ansteckungsgefahr schätzen.

Die Spalten haben die folgende Bedeutung:

* Die Anzahl der derzeit Infizierten (und Ansteckenden) wächst täglich um diesen Faktor (prozentual ausgedrückt)

* Die Zeitdauer bis die Anzahl der derzeit Infizierten sich verdoppelt

* Die letzte gemeldete Anzahl der derzeit Infizierten.

* Meine Schätzung der derzeit Infizierten. Konkret, die Extrapolation der angepassten exponentiellen Kurve auf 4, beziehungsweise, 6 Tage voraus. (Bis 16.03.2020, wenn R^2 kleiner als 0,945 oder die letzte Spalte größer als 0,5 ist, dann lasse ich diese Schätzung wegfallen, denn mein Vertrauen in ihr ist schwächer. Ab 18.03.2020 zeige ich die Schätzung wenn R^2 nicht kleiner als 0,95 und die vorletzte Spalte nicht größer als 0,5 ist, oder wenn die vorletzte Spalte in [-0,2;&nbsp; 0,1] ist.)

* R^2 oder Bestimmtheitsmaß oder Determinationskoeffizient der Anpassungsgüte der linearen Regression. Je näher es an 1 ist, desto besser ist die Anpassung.

* Differenz zwischen der linearen Annäherung und der wahren Beobachtung in logarithmischem Raum für den letzten Datenpunkt (für den letzten Tag). Man kann es als Exponent einer Potenz auf Basis 2 interpretieren für die Quote zwischen Schätzung und der letzten Beobachtung. Wenn diese Nummer groß ist, dann ist die Annäherung wenig gut. Wenn sie sogar negativ ist, dann ist die Annäherung viel zu niedrig und die Anzahl der Ansteckenden wird unterschätzt.

* (Ab 18.03.2020) Die Anzahl der Tage im Zeitfenster, in dem die lineare Regression stattfindet. Sie wird automatisch optimiert, so dass der Vektor (10 * (1-R^2), Differenz) in l_2 kleinstmöglich ist.)


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


### Datenquelle

Die Daten werden durch das Robert Koch Institut gesammelt und [veröffentlicht](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html). Da ich auf der Webseite nur die aktuellen Fallzahlen finde, verwende ich [Wikipedia](https://de.wikipedia.org/wiki/COVID-19-Pandemie_in_Deutschland#Infektionsf%C3%A4lle_nach_Bundesl%C3%A4ndern), wo Freiwillige die ganzen Zeitreihen gespeichert haben.

### Programmdateien

* **download_DEU.py** ist das Skript um die Daten von [Wikipedia](https://de.wikipedia.org/wiki/COVID-19-F%C3%A4lle_in_Deutschland) herunterzuladen.

* **DEU.py** ist das für Deutschland spezifische Skript, das hauptsächlich für die Vorbereitung der Daten von Wikipedia zuständig ist.

* **utils.py** hat die gemeinsame Funktionen, die die Analyse und die Visualisierung durchführen.

### Konklusion

Unsere Intuition kann mit nichtlinearen Effekten schwer umgehen. Exponentielles Wachstum ist solch ein Beispiel. **Das Risiko, dass man sich mit der Krankheit auf der Straße ansteckt, wächst um den Faktor 15-50% täglich.** Es ist zu erwarten, dass man über die Erkrankung zunächst nur aus den Nachrichten hören wird, dann plötzlich wird sie überall im Bekanntenkreis auftauchen, wenn die Eindämmung nicht erfolgt.

Wenn man die Ansteckung vermeiden will, dann ist es besser eine Besorgung noch heute und nicht morgen zu machen, und es ist besser morgen Vormittag als morgen Nachmittag das Zuhause zu verlassen. (Angenommen, dass genau so viele Leute sich auf den Straßen und in den Supermärkten befinden werden. Wenn deren Anzahl zurückgeht, dann sinkt die Kontaktwahrscheinlichkeit auch.)

Neben der Nichtlinearität ist die durch die Inkubationszeit ausgelöste Zeitverzögerung ein zweiter überraschender Aspekt der Pandemie. **Die Anzahl der heute ansteckenden Erkrankten ist schon so viel, wie die Fallanzahl erst in ungefähr fünf Tagen (die durchschnittliche Inkubationszeit) gemeldet werden wird. Das Problem ist deshalb viel größer, als die aktuellen Fallzahlen es zeigen.**

Für das medizinische Personal ist es zu erwarten, dass die Anzahl der neuen Patienten auch exponentiell mit der gleichen Rate wachsen wird. Wenn ein Tag schwierig war, dann wird der nächste 15-50% schwieriger, und der übernächste noch 15-50% schwieriger werden.

### Bitte um Spenden

Wenn Sie meine Arbeit unterstützen können, dann bitte ich Sie, mein [Ocean Plastic Detector](https://www.gofundme.com/OceanPlasticDetector) Projekt aufzusuchen und dort eine Spende durchzuführen. Danke!

Finden Sie mich auf [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), auf meiner Webseite/Blog: [Melykuti.me](https://melykuti.me), oder folgen Sie mir auf [Facebook](https://www.facebook.com/bence.melykuti) für meine öffentlichen Posts.

Ich arbeite als selbständiger Data Scientist. Sie können mich mit Ihrem Projekt beauftragen.