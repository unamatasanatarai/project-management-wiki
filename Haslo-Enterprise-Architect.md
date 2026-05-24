# Enterprise Architect

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Role](Role.md)

## Definicja

Enterprise Architect to rola odpowiedzialna za spójność architektury na poziomie całej organizacji. Patrzy nie tylko na jeden projekt, ale na krajobraz systemów, integracji, danych, standardów technologicznych i zgodność rozwiązań ze strategią firmy. Pomaga uniknąć sytuacji, w której każdy projekt buduje własny, niekompatybilny fragment technologii.

**Kategoria:** [Role](Role.md)

## Po co to istnieje

Enterprise Architect istnieje po to, żeby decyzje techniczne w pojedynczych projektach nie psuły całej organizacji. Projekt może wybrać rozwiązanie szybkie lokalnie, ale kosztowne globalnie: kolejny system, duplikację danych, niestandardową integrację albo technologię trudną do utrzymania.

Dla PM-a Enterprise Architect jest ważnym interesariuszem przy decyzjach, które wpływają na wiele systemów, bezpieczeństwo, dane, integracje albo standardy organizacji.

## Jak to działa w praktyce

Enterprise Architect definiuje kierunek i zasady architektoniczne na poziomie enterprise. Może uczestniczyć w architecture review, opiniować rozwiązania, zatwierdzać wyjątki od standardów i wskazywać zależności między projektami.

Typowe zadania:

* utrzymanie mapy systemów i integracji,
* definiowanie standardów technologicznych,
* ocena zgodności projektów z architekturą docelową,
* wskazywanie ryzyk architektonicznych,
* wsparcie decyzji build vs buy,
* ograniczanie duplikacji systemów i danych,
* współpraca z security, compliance i governance.

Enterprise Architect nie projektuje każdego ekranu ani każdej klasy w kodzie. Jego poziom decyzji jest szerszy: spójność, kierunek i konsekwencje dla organizacji.

## Przykład z projektu

Zespół chce wdrożyć osobne narzędzie do zarządzania klientami w jednym dziale, bo jest szybkie i tanie. Enterprise Architect sprawdza, że organizacja ma już centralny CRM, master data model i standard integracji z systemem billingowym.

Decyzja o nowym narzędziu mogłaby stworzyć duplikację danych klienta, kolejne integracje i problem z raportowaniem. Enterprise Architect rekomenduje rozszerzenie istniejącej platformy albo formalny wyjątek z planem migracji.

## Gdzie to się pojawia

Enterprise Architect pojawia się w:

* dużych organizacjach enterprise,
* projektach integracyjnych,
* wyborze platform i technologii,
* programach transformacyjnych,
* architecture review board,
* projektach z wymaganiami security i compliance,
* decyzjach o danych, systemach core i standardach.

W codziennej pracy PM powinien angażować Enterprise Architecta wcześnie, jeśli projekt dotyka systemów krytycznych, wielu integracji albo wyjątków od standardów.

## Powiązania

* [Solution Architect](Haslo-Solution-Architect.md) - projektuje rozwiązanie dla konkretnego projektu lub obszaru.
* [Technical Lead / Architect](Haslo-Technical-Lead-Architect.md) - wspiera decyzje techniczne w zespole.
* [Technical Requirements](Haslo-Technical-Requirements.md) - standardy enterprise wpływają na wymagania techniczne.
* [Compliance](Haslo-Compliance.md) - architektura musi wspierać zgodność z regulacjami i politykami.
* [Governance Model](Haslo-Governance-Model.md) - decyzje architektoniczne często wymagają formalnego governance.
* [Dependency](Haslo-Dependency.md) - architektura enterprise ujawnia zależności między systemami i projektami.

## Typowe błędy / nieporozumienia

* Włączanie Enterprise Architecta dopiero przed go-live. Wtedy zmiana architektury jest już kosztowna.
* Traktowanie standardów jako biurokracji. Standardy często chronią przed kosztami utrzymania i integracji.
* Optymalizacja tylko dla jednego projektu. Lokalnie szybka decyzja może zwiększyć koszt całego portfolio.
* Brak mechanizmu wyjątków. Czasem odstępstwo ma sens, ale powinno być świadome i udokumentowane.
* Mylenie Enterprise Architecta z Solution Architectem. Jeden patrzy na całą organizację, drugi na konkretne rozwiązanie.

## Różnica między Enterprise Architect a Solution Architect

Enterprise Architect odpowiada za spójność architektury organizacji. Solution Architect odpowiada za projekt konkretnego rozwiązania w ramach projektu lub produktu.

Przykład: Enterprise Architect ustala, że dane klienta muszą pochodzić z centralnego master data system. Solution Architect projektuje, jak konkretny portal klienta zintegruje się z tym systemem.
