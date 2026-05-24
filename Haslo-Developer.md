# Developer

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Role](Role.md)

## Definicja

Developer to osoba odpowiedzialna za tworzenie, zmianę i utrzymanie oprogramowania. W projekcie nie tylko pisze kod, ale też uczestniczy w projektowaniu rozwiązania, estymacji, analizie technicznej, code review, naprawie defektów i dbaniu o jakość techniczną produktu.

**Kategoria:** [Role](Role.md)

## Po co to istnieje

Developer istnieje po to, żeby zamienić wymagania i decyzje projektowe w działające rozwiązanie techniczne. Bez udziału developera projekt może wyglądać dobrze w dokumentach, ale nie być wykonalny, skalowalny albo utrzymywalny.

Dla PM-a developer jest źródłem informacji o realnej złożoności, ryzykach technicznych i wpływie zmian na harmonogram. Dla BA i PO developer pomaga sprawdzić, czy wymagania są wystarczająco jasne do implementacji.

## Jak to działa w praktyce

Developer pracuje na backlog items, taskach, bugach i zmianach technicznych. Współpracuje z PO, BA, QA, DevOps, architektem i innymi developerami.

Typowe zadania:

* implementacja funkcjonalności,
* analiza techniczna wymagań,
* estymacja prac,
* code review,
* pisanie testów automatycznych,
* naprawa defektów,
* refaktoryzacja i ograniczanie długu technicznego,
* wsparcie wdrożeń i diagnoza problemów produkcyjnych.

Dobry developer komunikuje ryzyka wcześnie. Jeśli wymaganie jest niejasne, integracja niestabilna albo deadline wymusza skróty techniczne, powinno to trafić do rozmowy projektowej.

## Przykład z projektu

BA opisuje wymaganie: „system ma wysyłać powiadomienie do klienta po zmianie statusu zamówienia”. Developer doprecyzowuje, skąd ma przyjść event, czy powiadomienia mają być retry'owane, co zrobić przy błędzie dostawcy email i jak uniknąć wysłania duplikatu.

Bez tych pytań funkcja może działać w prostym demo, ale psuć się w realnej produkcji. Udział developera zmienia wymaganie w rozwiązanie, które da się bezpiecznie wdrożyć.

## Gdzie to się pojawia

Developer pojawia się w:

* refinement i estymacji,
* development sprintach lub fazie build,
* code review,
* testowaniu i naprawie defektów,
* wdrożeniach,
* analizie incydentów,
* rozmowach o długu technicznym i architekturze.

W codziennej pracy developer powinien być włączany wcześniej niż na etapie „weź wymaganie i zakoduj”, szczególnie przy złożonych integracjach i ryzykach technicznych.

## Powiązania

* [Team](Haslo-Team.md) - developer jest częścią zespołu delivery.
* [Technical Lead / Architect](Haslo-Technical-Lead-Architect.md) - wspiera decyzje techniczne i standardy implementacji.
* [QA / Tester](Haslo-QA-Tester.md) - współpracuje z developerem przy jakości i defektach.
* [User Story](Haslo-User-Story.md) - częsta jednostka pracy developera w Agile.
* [Technical Requirements](Haslo-Technical-Requirements.md) - wpływają na sposób implementacji.
* [DoD](Haslo-DoD.md) - określa, kiedy praca developera może być uznana za ukończoną.

## Typowe błędy / nieporozumienia

* Traktowanie developera tylko jako wykonawcy kodu. Developer powinien współtworzyć rozwiązanie i wskazywać ryzyka techniczne.
* Zbyt późne włączenie w analizę. Wtedy estymacje i wymagania mogą ignorować realną złożoność.
* Pomijanie pracy technicznej w planie. Refaktoryzacja, testy, review i poprawki też zużywają capacity.
* Brak komunikacji o długu technicznym. Ukryty dług wraca jako wolniejsze delivery i więcej defektów.
* Ocenianie pracy tylko liczbą zadań. Ważna jest wartość, jakość i utrzymywalność rozwiązania.

## Różnica między developer a technical lead

Developer implementuje rozwiązanie i odpowiada za jakość swojej pracy technicznej. Technical Lead koordynuje decyzje techniczne, standardy i kierunek rozwiązania dla zespołu lub obszaru.

W małym zespole jedna osoba może pełnić obie role, ale odpowiedzialności nadal są różne.
