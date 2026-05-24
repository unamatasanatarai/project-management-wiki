# Baseline

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Fundamenty projektu](Fundamenty-projektu.md)

## Definicja

Baseline to zatwierdzona wersja planu, wobec której mierzy się późniejszy stan projektu. Najczęściej dotyczy zakresu, harmonogramu albo budżetu. Jeśli coś zmienia się względem baseline, PM może pokazać odchylenie i uruchomić decyzję, zamiast dyskutować na podstawie pamięci lub oczekiwań.

**Kategoria:** [Fundamenty projektu](Fundamenty-projektu.md)

## Po co to istnieje

Baseline istnieje po to, żeby projekt miał jeden uzgodniony punkt odniesienia. Bez niego nie wiadomo, czy zespół jest opóźniony, czy zakres faktycznie urósł, albo czy budżet został przekroczony.

Dla PM-a baseline jest narzędziem kontroli. Pozwala powiedzieć: „planowaliśmy X, teraz mamy Y, różnica wynosi Z i wymaga decyzji”. Dzięki temu rozmowa z klientem, sponsorem albo steering committee opiera się na faktach, a nie na ogólnym poczuciu, że „projekt się rozjeżdża”.

## Jak to działa w praktyce

Na początku projektu zespół ustala plan bazowy, np. scope, daty milestone'ów i budżet. Ten plan jest zatwierdzany przez właściwe osoby: sponsora, klienta, steering committee albo właściciela budżetu.

W trakcie delivery aktualny status porównuje się z baseline:

* czy dostarczamy uzgodniony zakres,
* czy terminy nadal pasują do zatwierdzonego harmonogramu,
* czy koszty mieszczą się w zatwierdzonym budżecie,
* czy zmiany przeszły przez change control.

Baseline nie oznacza, że plan nigdy się nie zmienia. Oznacza, że zmiana musi być świadoma, zatwierdzona i widoczna. Jeśli klient dodaje nowy moduł, PM nie dopisuje go po cichu do planu. Powinien pokazać wpływ na scope, czas i koszt, a po akceptacji zaktualizować baseline.

## Przykład z projektu

Projekt wdrożenia portalu klienta ma zatwierdzony baseline:

* zakres: logowanie, profil klienta, historia zamówień,
* termin go-live: 30 września,
* budżet: 420 000 PLN.

W sierpniu klient prosi o dodanie programu lojalnościowego. Zespół szacuje, że to dodatkowe 6 tygodni pracy i 90 000 PLN kosztu.

Jeśli PM ma baseline, może przygotować Change Request i pokazać konkretny wpływ: nowy scope przesuwa go-live na listopad albo wymaga zwiększenia zespołu. Jeśli baseline nie istnieje, klient może traktować nową funkcję jako „część projektu”, a zespół zaczyna dowozić więcej pracy w tym samym czasie i budżecie.

## Gdzie to się pojawia

Baseline pojawia się w:

* planowaniu projektu po zatwierdzeniu scope'u, budżetu i harmonogramu,
* status reportach, gdy PM pokazuje odchylenia od planu,
* change control, gdy oceniany jest wpływ zmiany,
* steering committee, gdy trzeba podjąć decyzję o przesunięciu terminu, budżetu lub zakresu,
* analizie odchyleń, forecastach i kontroli finansowej.

W codziennej pracy PM używa baseline, gdy musi odpowiedzieć na pytania: „czy jesteśmy jeszcze zgodni z planem?”, „co dokładnie się zmieniło?” i „kto zatwierdził tę zmianę?”.

## Powiązania

* [Scope](Haslo-Scope.md) - baseline zakresu pokazuje, co było formalnie uzgodnione jako część projektu.
* [Schedule Baseline](Haslo-Schedule-Baseline.md) - szczególny typ baseline dotyczący harmonogramu.
* [Cost Baseline](Haslo-Cost-Baseline.md) - szczególny typ baseline dotyczący budżetu rozłożonego w czasie.
* [Change Control](Haslo-Change-Control.md) - proces zatwierdzania zmian względem baseline.
* [Variance Analysis](Haslo-Variance-Analysis.md) - analiza różnic między baseline a aktualnym wynikiem projektu.
* [Triple Constraint](Haslo-Triple-Constraint.md) - pokazuje, dlaczego zmiana zakresu wpływa na czas i koszt.

## Typowe błędy / nieporozumienia

* Mylenie baseline z aktualnym planem. Baseline to zatwierdzony punkt odniesienia, a aktualny plan może już zawierać zmiany i forecast.
* Traktowanie baseline jak blokady zmian. Zmiany są możliwe, ale powinny przejść przez decyzję i być widoczne.
* Brak właściciela akceptacji. Jeśli nikt formalnie nie zatwierdził baseline, trudno używać go w rozmowach o odpowiedzialności.
* Aktualizowanie baseline bez śladu decyzji. To kasuje historię odchyleń i utrudnia wyjaśnienie, dlaczego projekt zmienił koszt albo termin.
* Posiadanie baseline tylko dla harmonogramu. W praktyce projekt może potrzebować osobnego punktu odniesienia dla scope'u, kosztów i terminów.

## Różnica między baseline a forecast

Baseline mówi, jaki plan został zatwierdzony. Forecast mówi, gdzie projekt prawdopodobnie skończy, patrząc na aktualne dane.

Jeśli baseline budżetu wynosi 420 000 PLN, a forecast pokazuje 510 000 PLN, problemem nie jest sam forecast. Problemem jest odchylenie, które wymaga decyzji: ograniczyć scope, zwiększyć budżet, zmienić termin albo zaakceptować przekroczenie.
