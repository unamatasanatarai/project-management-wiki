# Triple Constraint

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Fundamenty projektu](Fundamenty-projektu.md)

## Definicja

Triple Constraint to model pokazujący zależność między zakresem, czasem i kosztem projektu. Jeśli jeden z tych parametrów się zmienia, zwykle wpływa na pozostałe. W praktyce oznacza to, że nie da się bez konsekwencji dodać zakresu, skrócić terminu albo obniżyć budżetu.

**Kategoria:** [Fundamenty projektu](Fundamenty-projektu.md)

## Po co to istnieje

Triple Constraint istnieje po to, żeby decyzje projektowe były uczciwe. Pomaga PM-owi pokazać, że projekt nie jest magicznym pudełkiem, do którego można dokładać pracę bez zmiany czasu, kosztu albo jakości.

Dla zespołu i klienta ten model jest językiem negocjacji. Jeśli termin jest stały, trzeba rozmawiać o zakresie lub zasobach. Jeśli budżet jest stały, trzeba kontrolować scope. Jeśli zakres jest stały, trzeba zabezpieczyć czas i koszt.

## Jak to działa w praktyce

PM używa Triple Constraint przy planowaniu, change control, eskalacjach i rozmowach o priorytetach. Model nie oznacza, że każdy parametr ma identyczną wagę. W niektórych projektach najważniejszy jest deadline, w innych budżet, a w innych pełny zakres.

Typowe decyzje:

* klient dodaje funkcję - rośnie czas, koszt albo trzeba usunąć inny zakres,
* sponsor skraca termin - trzeba zwiększyć zespół, zmniejszyć scope albo zaakceptować większe ryzyko,
* budżet zostaje obcięty - trzeba ograniczyć deliverables lub zmienić podejście,
* jakość jest krytyczna - nie można bezpiecznie skracać testów bez podniesienia ryzyka.

W nowoczesnym delivery często dodaje się też jakość jako czwarty wymiar. Nawet jeśli model mówi o trzech ograniczeniach, jakość jest konsekwencją decyzji w tych trzech obszarach.

## Przykład z projektu

Zespół ma wdrożyć MVP do końca września za 500 000 PLN. W lipcu klient prosi o dodanie integracji z dodatkowym systemem.

PM pokazuje trzy opcje: przesunąć go-live o 4 tygodnie, zwiększyć budżet i dodać ludzi, albo usunąć mniej ważną funkcję z MVP. Jeśli klient oczekuje dodatkowej integracji bez zmiany terminu i budżetu, realnym skutkiem będzie przeciążenie zespołu, mniej testów albo niedowiezienie innego elementu.

Triple Constraint zamienia tę rozmowę z presji na zespół w decyzję biznesową.

## Gdzie to się pojawia

Triple Constraint pojawia się w:

* estymacji i planowaniu projektu,
* definiowaniu scope,
* negocjacjach z klientem,
* change control,
* status reportach i eskalacjach,
* analizie opóźnień i przekroczeń budżetu,
* rozmowach o MVP i priorytetach.

W codziennej pracy PM wraca do tego modelu za każdym razem, gdy ktoś chce zmienić jeden parametr bez rozmowy o pozostałych.

## Powiązania

* [Scope](Haslo-Scope.md) - jeden z głównych parametrów modelu.
* [Budget / BAC](Haslo-Budget-BAC.md) - zatwierdzony budżet określa koszt projektu.
* [Timeline](Haslo-Timeline.md) - pokazuje czas i kluczowe terminy projektu.
* [Schedule Baseline](Haslo-Schedule-Baseline.md) - zatwierdzony harmonogram jest punktem odniesienia dla czasu.
* [Change Control](Haslo-Change-Control.md) - formalnie ocenia wpływ zmian na zakres, czas i koszt.
* [Constraint](Haslo-Constraint.md) - ograniczenia wskazują, który parametr ma najmniejszą elastyczność.

## Typowe błędy / nieporozumienia

* Zakładanie, że zespół „jakoś dowiezie” dodatkowy zakres. To zwykle kończy się ukrytym kosztem albo spadkiem jakości.
* Brak rozmowy o trade-offach. Jeśli zmienia się zakres, PM powinien pokazać konsekwencje dla czasu i budżetu.
* Traktowanie jakości jako darmowej zmiennej. Skrócenie czasu bez zmiany zakresu często oznacza mniej testów, więcej defektów i dług techniczny.
* Używanie modelu jako wymówki. Triple Constraint nie służy do blokowania zmian, tylko do świadomego wyboru konsekwencji.
* Brak baseline. Bez punktu odniesienia trudno pokazać, co realnie się zmieniło.

## Różnica między triple constraint a constraint

Triple Constraint to konkretny model zależności między zakresem, czasem i kosztem. Constraint to dowolne ograniczenie projektu, np. compliance, dostępność klienta, narzucona technologia albo fixed deadline.

Przykład: stały termin go-live jest constraintem. Jego wpływ na zakres i koszt można wyjaśnić przez Triple Constraint.
