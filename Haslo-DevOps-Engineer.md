# DevOps Engineer

[Strona główna](Home.md) | [Pełny słownik](Slownik.md) | [Role](Role.md)

## Definicja

DevOps Engineer to osoba wspierająca szybkie, powtarzalne i bezpieczne dostarczanie oprogramowania przez automatyzację infrastruktury, CI/CD, deploymentu, monitoringu i operacji. Łączy perspektywę developmentu i utrzymania. W praktyce pilnuje, żeby zespół mógł wdrażać bez ręcznego chaosu i bez zaskoczeń na produkcji.

**Kategoria:** [Role](Role.md)

## Po co to istnieje

DevOps Engineer istnieje po to, żeby delivery nie kończyło się na „kod działa lokalnie”. Projekt potrzebuje środowisk, pipeline'ów, konfiguracji, sekretów, logów, alertów, rollbacku i stabilnego procesu wdrożenia.

Dla PM-a ta rola jest krytyczna przy planowaniu realnego go-live. Bez DevOps łatwo pominąć prace infrastrukturalne, które nie są widoczne w UI, ale blokują wdrożenie.

## Jak to działa w praktyce

DevOps Engineer pracuje z developerami, QA, architektami, security i operations. Automatyzuje procesy, utrzymuje środowiska i dba o obserwowalność systemu.

Typowe zadania:

* konfiguracja CI/CD,
* automatyzacja deploymentu,
* infrastruktura jako kod,
* zarządzanie środowiskami dev, test, staging i prod,
* monitoring, logowanie i alerting,
* wsparcie release i rollback,
* zarządzanie sekretami i konfiguracją,
* wsparcie wymagań security i compliance.

DevOps nie powinien być ostatnią osobą wołaną przed wdrożeniem. Jego praca powinna być częścią planu od początku, szczególnie przy projektach z integracjami, chmurą i wymaganiami bezpieczeństwa.

## Przykład z projektu

Zespół buduje nowy moduł płatności. Funkcjonalnie wszystko działa na środowisku developerskim, ale przed UAT okazuje się, że nie ma stabilnego środowiska testowego, pipeline wymaga ręcznych kroków, a logi nie pozwalają diagnozować błędów transakcji.

DevOps Engineer przygotowuje automatyczny deployment, oddzielne konfiguracje środowisk, monitoring błędów płatności i procedurę rollbacku. Dzięki temu UAT i go-live przestają zależeć od ręcznych działań jednej osoby.

## Gdzie to się pojawia

DevOps Engineer pojawia się w:

* konfiguracji środowisk,
* development i release planning,
* deploymentach,
* projektach cloud i infrastrukturalnych,
* monitoringu produkcji,
* incident response,
* wymaganiach security, compliance i SLA.

W codziennej pracy PM powinien uwzględniać DevOps tasks w planie, bo pipeline, środowiska i monitoring są częścią dostarczenia, nie dodatkiem po development.

## Powiązania

* [Developer](Haslo-Developer.md) - DevOps wspiera przepływ kodu od developmentu do produkcji.
* [Technical Requirements](Haslo-Technical-Requirements.md) - wymagania techniczne często obejmują infrastrukturę i deployment.
* [Release Plan](Haslo-Release-Plan.md) - wdrożenia wymagają przygotowania pipeline'ów i środowisk.
* [SLA](Haslo-SLA.md) - monitoring i stabilność pomagają spełniać poziomy usług.
* [Compliance](Haslo-Compliance.md) - proces deploymentu i infrastruktura muszą spełniać wymagania organizacji.
* [Risk](Haslo-Risk.md) - brak automatyzacji i monitoringu zwiększa ryzyko go-live.

## Typowe błędy / nieporozumienia

* Traktowanie DevOps jako osoby „od kliknięcia deploya”. Rola powinna automatyzować i stabilizować proces, a nie ręcznie ratować wdrożenia.
* Pomijanie prac DevOps w estymacji. Środowiska, pipeline'y i monitoring zużywają realne capacity.
* Brak środowisk podobnych do produkcji. Testy na nierealnym środowisku dają fałszywe poczucie bezpieczeństwa.
* Monitoring dopiero po incydencie. Obserwowalność powinna być gotowa przed go-live.
* Oddzielenie DevOps od zespołu. Jeśli DevOps nie zna zmian aplikacyjnych, deployment staje się ryzykowny.

## Różnica między DevOps Engineer a System Administrator

System Administrator zwykle skupia się na utrzymaniu systemów i infrastruktury. DevOps Engineer koncentruje się na automatyzacji procesu dostarczania, integracji developmentu z operacjami i powtarzalnym wdrażaniu zmian.

W wielu organizacjach obowiązki mogą się nakładać, ale DevOps powinien zmniejszać ręczną pracę operacyjną przez automatyzację.
