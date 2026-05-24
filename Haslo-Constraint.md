# Constraint

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Fundamenty projektu](Fundamenty-projektu.md)

## Definicja

Constraint to ograniczenie, które wpływa na sposób realizacji projektu. Może dotyczyć budżetu, terminu, zasobów, technologii, regulacji, architektury, dostępności klienta albo modelu kontraktu. Constraint nie jest automatycznie problemem; jest warunkiem brzegowym, który trzeba uwzględnić w planowaniu i decyzjach.

**Kategoria:** [Fundamenty projektu](Fundamenty-projektu.md)

## Po co to istnieje

Constraints istnieją po to, żeby zespół wiedział, w jakich granicach może działać. Projekt bez nazwanych ograniczeń szybko wpada w nierealistyczne obietnice: za dużo zakresu, za mało czasu, za mało ludzi albo rozwiązanie techniczne niedopuszczalne przez organizację.

Dla PM-a constraint jest sygnałem: „tego parametru nie możemy swobodnie zmienić”. Jeśli termin jest stały, trzeba negocjować zakres lub zasoby. Jeśli budżet jest stały, trzeba kontrolować scope i model delivery.

## Jak to działa w praktyce

Constraints powinny być zidentyfikowane na początku projektu i regularnie weryfikowane. Niektóre są jawne, np. „go-live musi być przed 1 grudnia”. Inne wychodzą dopiero w rozmowach, np. „klient może testować tylko dwa dni w tygodniu” albo „system musi działać na istniejącej infrastrukturze”.

Typowe constraints:

* fixed deadline, np. wymóg prawny lub kampania marketingowa,
* fixed budget, np. zatwierdzony limit finansowania,
* ograniczona dostępność SME lub zespołu klienta,
* narzucona technologia albo standard architektury,
* compliance, security lub wymagania regulatora,
* kontrakt fixed price z ograniczoną tolerancją na zmianę zakresu.

Gdy constraint wpływa na delivery, PM powinien pokazać konsekwencję. Przykład: jeśli termin nie może się przesunąć, a klient dodaje zakres, trzeba usunąć inne elementy, zwiększyć zespół albo zaakceptować ryzyko jakości.

## Przykład z projektu

Zespół buduje integrację z systemem płatności. Klient mówi, że produkcyjny go-live musi nastąpić przed Black Friday, bo wtedy startuje kampania sprzedażowa. Termin jest constraintem.

W trakcie prac biznes prosi o dodatkowy moduł raportowy. PM nie traktuje tego jako zwykłego dopisania zadania. Pokazuje, że przy stałym terminie są trzy opcje: przesunąć moduł raportowy po go-live, zwiększyć zespół albo ograniczyć testy, co podnosi ryzyko awarii.

Constraint pomaga więc przenieść rozmowę z „czy możecie to jeszcze dorobić?” na „który parametr projektu świadomie zmieniamy?”.

## Gdzie to się pojawia

Constraints pojawiają się w:

* project charter i inicjacji projektu,
* estymacji i planowaniu harmonogramu,
* rozmowach o scope, budżecie i zasobach,
* risk register, jeśli ograniczenie zwiększa prawdopodobieństwo problemu,
* change control, gdy zmiana narusza warunki brzegowe,
* status reportach, jeśli constraint zaczyna blokować delivery.

W codziennej pracy PM używa constraints do obrony realności planu. To nie jest wymówka, tylko sposób pokazania, że każda decyzja ma koszt.

## Powiązania

* [Triple Constraint](Haslo-Triple-Constraint.md) - pokazuje zależność między zakresem, czasem i kosztem.
* [Scope](Haslo-Scope.md) - zakres często musi być dopasowany do ograniczeń czasu lub budżetu.
* [Budget / BAC](Haslo-Budget-BAC.md) - zatwierdzony budżet może być głównym ograniczeniem projektu.
* [Timeline](Haslo-Timeline.md) - deadline albo okno wdrożeniowe mogą tworzyć ograniczenia harmonogramu.
* [Risk](Haslo-Risk.md) - constraint może generować ryzyko, jeśli ogranicza opcje reakcji.
* [Dependency](Haslo-Dependency.md) - zależność od innego zespołu może działać jak ograniczenie planu.

## Typowe błędy / nieporozumienia

* Mylenie constraint z ryzykiem. Constraint już istnieje jako warunek projektu; risk to potencjalne zdarzenie.
* Ignorowanie ograniczeń miękkich. Dostępność klienta, proces akceptacji albo polityka security potrafią opóźnić projekt tak samo jak brak developerów.
* Traktowanie każdego życzenia jako constraint. „Chcielibyśmy szybciej” nie jest constraintem, dopóki nie ma realnej konsekwencji biznesowej lub formalnej.
* Brak komunikacji wpływu. Samo zapisanie ograniczenia nic nie daje, jeśli PM nie pokazuje, jak wpływa ono na scope, koszt i termin.
* Próba „obejścia” compliance lub security. Takie constraints zwykle wymagają planowania, a nie negocjowania na końcu.

## Różnica między constraint a dependency

Constraint to ograniczenie warunków realizacji, np. stały budżet, deadline albo wymóg użycia konkretnej technologii. Dependency to zależność od wykonania czegoś przez inną osobę, zespół lub system.

Przykład: „go-live przed 1 grudnia” to constraint. „Musimy dostać API od zespołu płatności przed testami” to dependency. Oba wpływają na plan, ale wymagają innego zarządzania.
