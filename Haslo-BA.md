# BA

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Role](Role.md)

## Definicja

BA (Business Analyst) to osoba, która pomaga zrozumieć problem biznesowy i przełożyć go na wymagania możliwe do zaprojektowania, zbudowania, przetestowania i zaakceptowania. BA łączy język biznesu, użytkowników i zespołu technicznego. Nie jest tylko „osobą od notatek”, ale właścicielem jakości analizy.

**Kategoria:** [Role](Role.md)

## Po co to istnieje

BA istnieje po to, żeby zespół nie budował rozwiązania na podstawie niejasnych oczekiwań. Interesariusze często mówią o potrzebach, wyjątkach i procesach skrótowo, a developerzy potrzebują konkretu: reguł, scenariuszy, danych, zależności i kryteriów akceptacji.

Dla PM-a BA zmniejsza ryzyko scope creep, błędnych założeń i kosztownych poprawek. Dla zespołu BA jest źródłem doprecyzowanych wymagań i kontekstu biznesowego.

## Jak to działa w praktyce

BA pracuje z interesariuszami, SME, PO, PM-em, architektem, developerami i QA. Zbiera informacje, prowadzi warsztaty, analizuje procesy, zadaje pytania o wyjątki i dokumentuje uzgodnienia.

Typowe zadania BA:

* zbieranie i doprecyzowanie wymagań,
* mapowanie procesów AS-IS i TO-BE,
* opisywanie use case'ów i user stories,
* definiowanie acceptance criteria,
* analiza wpływu zmian,
* wyjaśnianie wymagań zespołowi technicznemu,
* wsparcie testów UAT i odbioru rozwiązania.

Dobry BA nie przepisuje wypowiedzi biznesu jeden do jednego. Sprawdza spójność, szuka luk i pomaga ustalić, co naprawdę ma zostać zbudowane.

## Przykład z projektu

Biznes mówi: „Potrzebujemy raportu sprzedaży dla managerów”. Bez BA zespół może zbudować tabelę z kilkoma kolumnami i dopiero po wdrożeniu usłyszeć, że brakuje filtrów, walut, poziomów dostępu i danych historycznych.

BA prowadzi warsztat i doprecyzowuje: kto używa raportu, jakie decyzje podejmuje, jakie dane są potrzebne, jak często raport ma się odświeżać, skąd pochodzą dane i jakie są wyjątki. Dopiero wtedy powstaje wymaganie, które da się estymować i testować.

## Gdzie to się pojawia

BA pojawia się w:

* discovery i analizie wymagań,
* warsztatach z klientem lub biznesem,
* refinement backlogu,
* projektach integracyjnych i procesowych,
* UAT,
* analizie change requestów,
* dokumentacji funkcjonalnej.

W codziennej pracy BA jest szczególnie ważny tam, gdzie problem biznesowy jest bardziej złożony niż pojedyncza funkcja w systemie.

## Powiązania

* [Requirements](Haslo-Requirements.md) - główny obszar pracy BA.
* [Business Requirements](Haslo-Business-Requirements.md) - potrzeby biznesowe, które BA pomaga doprecyzować.
* [Functional Requirements](Haslo-Functional-Requirements.md) - opis zachowań systemu wynikający z analizy.
* [Use Case](Haslo-Use-Case.md) - jeden ze sposobów opisu scenariuszy.
* [Acceptance Criteria](Haslo-Acceptance-Criteria.md) - warunki odbioru wymagań.
* [SME](Haslo-SME.md) - ekspert dziedzinowy, z którym BA często pracuje.

## Typowe błędy / nieporozumienia

* Traktowanie BA jako stenotypisty. BA powinien analizować sens, spójność i konsekwencje wymagań.
* Pomijanie wyjątków procesu. To one często generują najwięcej defektów i sporów przy odbiorze.
* Dokumentacja bez decyzji. Ładny dokument nie pomaga, jeśli nie rozstrzyga, jak system ma działać.
* BA odłączony od zespołu technicznego. Wymagania muszą być zrozumiałe dla developerów i QA.
* Zbyt późne włączenie BA. Jeśli analiza zaczyna się po estymacji, projekt często ma błędny budżet i harmonogram.

## Różnica między BA a PO

BA skupia się na analizie problemu, wymaganiach, procesach i doprecyzowaniu rozwiązania. PO odpowiada za wartość produktu, priorytety backlogu i decyzje produktowe.

W praktyce BA może przygotować opcje i konsekwencje, ale PO decyduje, co ma najwyższy priorytet w produkcie.
