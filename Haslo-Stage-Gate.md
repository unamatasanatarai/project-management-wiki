# Stage Gate

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Fundamenty projektu](Fundamenty-projektu.md)

## Definicja

Stage Gate to formalny punkt decyzyjny między etapami projektu. W tym punkcie sprawdza się, czy projekt spełnia kryteria przejścia dalej: ma wymagane deliverables, akceptacje, kontrolę ryzyk, aktualny budżet i nadal ma sens biznesowy. Stage gate nie jest spotkaniem statusowym, tylko decyzją: go, no-go, hold albo rework.

**Kategoria:** [Fundamenty projektu](Fundamenty-projektu.md)

## Po co to istnieje

Stage Gate istnieje po to, żeby organizacja nie przechodziła automatycznie do kolejnego etapu tylko dlatego, że minęła data w harmonogramie. Pozwala zatrzymać projekt, poprawić braki albo zmienić kierunek zanim koszt błędu wzrośnie.

Dla PM-a stage gate jest mechanizmem kontroli i ochroną przed „płynięciem dalej” mimo nierozwiązanych ryzyk, braku akceptacji lub niejasnego zakresu.

## Jak to działa w praktyce

Przed stage gate PM przygotowuje materiał decyzyjny: status, deliverables, ryzyka, problemy, budżet, zależności, decyzje otwarte i rekomendację. Osoby decyzyjne oceniają, czy projekt może przejść do kolejnej fazy.

Możliwe decyzje:

* go - projekt przechodzi dalej,
* no-go - projekt nie przechodzi dalej,
* hold - projekt zostaje wstrzymany,
* rework - trzeba poprawić określone elementy i wrócić do decyzji,
* conditional go - projekt przechodzi dalej pod warunkiem spełnienia konkretnych działań.

Kryteria stage gate powinny być znane wcześniej. Jeśli pojawiają się dopiero na spotkaniu, zespół nie miał realnej szansy przygotować się do decyzji.

## Przykład z projektu

Po fazie analizy zespół chce przejść do developmentu. Stage gate wymaga zatwierdzonych wymagań, architektury rozwiązania, estymacji, planu testów i potwierdzenia dostępności zespołu klienta do UAT.

Na przeglądzie okazuje się, że architektura integracji nie została zaakceptowana przez security. Decyzja brzmi: rework, nie go. Development nie startuje, bo rozpoczęcie prac bez akceptacji mogłoby oznaczać kosztowne przeróbki po kilku sprintach.

## Gdzie to się pojawia

Stage Gate pojawia się w:

* projektach waterfall i hybrydowych,
* wdrożeniach enterprise,
* programach transformacyjnych,
* projektach compliance lub regulacyjnych,
* governance model,
* decyzjach inwestycyjnych i portfolio,
* przejściach między fazami: discovery, analiza, build, testy, wdrożenie.

W codziennej pracy PM używa stage gate do zebrania decyzji, których nie da się rozwiązać samym raportem statusowym.

## Powiązania

* [Phase](Haslo-Phase.md) - stage gate zwykle znajduje się między fazami.
* [Lifecycle](Haslo-Lifecycle.md) - model cyklu życia określa, gdzie są punkty decyzyjne.
* [Approval / Sign-off](Haslo-Approval-Sign-off.md) - akceptacje mogą być warunkiem przejścia przez gate.
* [Steering Committee](Haslo-Steering-Committee.md) - często podejmuje decyzje stage gate.
* [Health Check / Audit](Haslo-Health-Check-Audit.md) - może dostarczać danych do decyzji o kontynuacji.
* [Business Case](Haslo-Business-Case.md) - stage gate może sprawdzać, czy projekt nadal ma sens biznesowy.

## Typowe błędy / nieporozumienia

* Traktowanie stage gate jak formalności. Jeśli decyzja zawsze brzmi „go”, gate nie pełni funkcji kontrolnej.
* Brak kryteriów przejścia. Zespół powinien wiedzieć wcześniej, co musi być gotowe.
* Decyzje bez właścicieli. Jeśli gate kończy się listą problemów bez ownerów, projekt dalej stoi.
* Przepuszczanie projektu mimo braku kluczowych akceptacji. To zwykle przenosi ryzyko na droższy etap.
* Zbyt ciężki proces dla małych inicjatyw. Stage gate powinien być proporcjonalny do ryzyka i skali projektu.

## Różnica między stage gate a milestone

Milestone oznacza osiągnięcie ważnego punktu. Stage gate oznacza formalną decyzję, czy można przejść dalej.

Przykład: „Analiza zakończona” może być milestone'em. „Decyzja o rozpoczęciu developmentu po analizie” jest stage gate.
