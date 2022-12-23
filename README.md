# Uebungsblatt8

Aufgabe 2:
Das Pivotelement teilt das Array (bestenfalls in gleich große Teile) in zwei Teile. Alle Elemente die kleiner als das Pivotelement sind werden links davon angeordnet
und alle die größer sind rechts davon. In unserer Implementierung ist das Pivotelement das letzte Element in einem Array.

Aufgabe 3: 
Ja bei SelectionSort ist es O(n²), da bei jedem Durchlauf das Array von vorne bis hinten komplett durchlaufen wird.
Bei QuickSort ist es ebenfalls O(n²). Der Fall trifft auf wenn man als Pivotelement das kleinste oder das größte Element in einem Array erwischt.

Aufgabe 4:
Wir haben folgende 3 Testfälle gewählt:
+ Ein normales Array um zu schauen ob der Algorithmus es richtig sortiert
+ Ein leeres Array um zu schauen ob der Algorithmus einen Fehler ausgibt der abgefangen werden muss
+ Ein Array mit nur einem Element, da dies als ein sortiertes Array gilt und wir so sehen konnte wie der Algorithmus auf ein sortiertes Array reagiert und auf ein
Array mit nur einem Element

Aufgabe 6:
Bei Selectionsort ist ab einer Eingabelänge von 3000 Elementen ein größerer Sprung in der Laufzeit bemerkbar, da braucht der Algorithmus schon deutlich länger
Bei Quicksort macht es sich erst ab 5000 Elemente bemerkbar und ist hier schneller als Selectionsort

Aufgabe 7: Die Konstanten sind jeweils aus dem Code zu entnehmen

Aufgabe 8: Da Python schon von Grund auf sehr viel für den Benutzer selbst macht, ist dementsprechend die Laufzeit höher als bei effizienteren Sprachen wie zum Beispiel Java
