# Plan uzupełniania haseł

Ta strona służy do śledzenia postępu prac nad pełną dokumentacją każdego hasła w wiki. Checkbox przy haśle należy zaznaczyć dopiero wtedy, gdy strona hasła spełnia kryteria kompletności opisane niżej.

[Strona główna](Home.md) | [Pełny słownik](Slownik.md)

## Jak pracować z checklistą

1. Wybierz hasło z checklisty.
2. Otwórz podlinkowaną stronę hasła.
3. Uzupełnij dokumentację zgodnie z kryteriami kompletności.
4. Po przeglądzie merytorycznym zmień checkbox z `[ ]` na `[x]`.
5. Jeśli hasło wymaga decyzji terminologicznej, zostaw checkbox niezaznaczony i dopisz notatkę na stronie hasła.

# Standard uzupełniania haseł w wiki

## 1. Cel wiki

Ta wiki to **praktyczna baza wiedzy dla osób pracujących w delivery / PM / product / engineering**, której celem jest:

* skrócenie czasu wejścia juniora do realnej pracy,
* ujednolicenie języka między zespołami,
* eliminacja niejednoznaczności w pojęciach projektowych,
* budowa wspólnego modelu pracy (a nie encyklopedii definicji).

Nie jest to słownik ani dokumentacja akademicka.
To **system operacyjny wiedzy projektowej**.

---

## 2. Odbiorcy

Treści są pisane dla:

* junior / mid w PM, BA, delivery, engineering,
* osób zmieniających rolę (np. dev → PM),
* osób pracujących w środowisku projektowym enterprise.

Zakłada się:

* brak pełnej wiedzy kontekstowej,
* potrzebę przykładów „z życia”, nie definicji encyklopedycznych,
* konieczność zrozumienia wpływu pojęcia na pracę.

---

## 3. Filozofia treści

Każde hasło musi odpowiadać na pytanie:

> „Co to zmienia w mojej pracy jutro rano?”

Zasady:

* zero korpo-bełkotu,
* zero definicji „dla definicji”,
* maksymalna praktyczność,
* preferowanie przykładów nad teorią,
* pokazuj konsekwencje, nie tylko znaczenie.

Jeśli pojęcie nie ma zastosowania → nie istnieje.

---

## 4. Standard języka

* język: prosty polski techniczno-operacyjny,
* bez marketingu i buzzwordów,
* bez „strategicznego”, „synergii”, „optymalizacji” bez kontekstu,
* krótkie zdania, konkretne konstrukcje,
* angielskie terminy dopuszczalne tylko gdy są standardem branżowym.

---

## 5. Struktura obowiązkowa hasła

Każde hasło MUSI zawierać:

1. **Definicja (1–3 zdania)**
2. **Po co to istnieje**
3. **Jak to działa w praktyce**
4. **Przykład z projektu**
5. **Gdzie to się pojawia (konkretny kontekst pracy)**
6. **Powiązania (linki do innych haseł)**
7. **Typowe błędy / nieporozumienia**

---

## 6. Sekcje opcjonalne (tylko jeśli mają sens)

* antywzorce (jak to psuje projekt),
* checklisty użycia,
* różnice vs podobne pojęcia,
* warianty w Agile vs Waterfall,
* wpływ na budżet / scope / delivery,
* mini-case study.

---

## 7. Zasady przykładów

Przykłady muszą:

* pochodzić z realnych sytuacji projektowych,
* być jednoznaczne,
* pokazywać decyzję lub konsekwencję,
* unikać abstrakcji.

Zły przykład:

> „Projekt X używa backlogu”

Dobry przykład:

> „PO wrzuca wszystkie CR-y do backlogu → sprint się rozpada → brak priorytetyzacji → zespół traci 30% capacity”

---

## 8. Linkowanie między hasłami

Każde hasło musi:

* wskazywać pojęcia nadrzędne,
* wskazywać pojęcia zależne,
* linkować tylko wtedy, gdy relacja jest realna (nie sztuczna).

Zasada:

> linkujesz tylko to, co wpływa na decyzję.

---

## 9. Rozróżnianie pojęć

Jeśli dwa pojęcia są podobne:

* MUSI pojawić się sekcja „Różnica między X a Y”
* musi być jasno powiedziane:

  * kiedy używać jednego,
  * kiedy drugiego,
  * co się psuje przy pomyłce.

---

## 10. Standard skrótów

Jeśli hasło jest skrótem:

* rozwiń pełną nazwę,
* wyjaśnij różnicę między skrótem a potocznym użyciem,
* podaj kontekst branżowy (nie akademicki).

---

## 11. Jakość hasła (minimum)

Hasło jest NIEKOMPLETNE jeśli:

* brak przykładu,
* brak kontekstu użycia,
* brak relacji do innych pojęć,
* definicja jest ogólna („zarządzanie czymś”),
* nie da się podjąć decyzji na jego podstawie.

---

## 12. Checklist review

Przed oznaczeniem `[x]` sprawdź:

* [ ] Czy definicja jest jednoznaczna?
* [ ] Czy przykład jest realny?
* [ ] Czy wiadomo gdzie to się używa?
* [ ] Czy nie ma pustych, ogólnych zdań?
* [ ] Czy ktoś junior po tym rozumie temat?
* [ ] Czy da się to pomylić z innym hasłem? (jeśli tak → popraw)

---

## 13. Kryterium oznaczenia `[x]`

Checkbox można zaznaczyć tylko jeśli:

* wszystkie sekcje obowiązkowe są uzupełnione,
* reviewer nie ma pytań,
* nie ma otwartych decyzji terminologicznych,
* hasło nie zawiera „placeholder thinking”.

---

## 14. Zasady dla AI

AI może:

* proponować strukturę,
* uzupełniać drafty,
* sugerować linki.

AI nie może:

* domyślać się kontekstu projektu,
* generować „ładnych definicji bez sensu”,
* usuwać niejednoznaczności bez oznaczenia tego.

Zasada:

> jeśli coś jest niepewne → oznacz to, nie ukrywaj.

---

## 15. Zasady dla reviewerów

Reviewer:

* nie poprawia stylu, tylko sens,
* usuwa ogólne zdania,
* wymusza przykład lub kontekst,
* blokuje oznaczenie `[x]` jeśli hasło nie jest operacyjne.

Reviewer ma prawo:

* cofnąć status kompletności,
* dodać notatkę decyzyjną,
* wymusić rozbicie hasła na 2.

---

## 16. Unikanie korpo-bełkotu

Zakazane są:

* „effective”, „robust”, „optimized” bez kontekstu,
* definicje typu „proces zarządzania czymś”,
* zdania, które nie niosą decyzji.

Zasada:

> jeśli zdanie nie zmienia działania → usuń je.

---

## 17. Praktyczność

Każde hasło musi odpowiadać:

* co robi PM / dev / BA,
* kiedy to się pojawia w projekcie,
* co się psuje jeśli to źle rozumiesz.

---

## 18. Tłumaczenia enterprise

Jeśli pojęcie pochodzi z korpo/enterprise:

* tłumacz na „co to realnie robi w projekcie”,
* nie kopiuj definicji vendorów,
* redukuj abstrakcję do decyzji operacyjnych.

---

## 19. Standard jakości całej wiki

Wiki jest kompletna jeśli:

* można nią prowadzić projekt end-to-end,
* junior rozumie zależności między pojęciami,
* nie trzeba Google do podstawowych decyzji,
* każdy termin ma konsekwencję operacyjną.

---

## 20. Reguły publikacji (HTML / ebook)

* jedna struktura sekcji dla wszystkich haseł,
* brak wolnej narracji,
* każdy wpis renderowalny jako niezależna jednostka,
* linki zawsze względne,
* brak zależności od kontekstu strony głównej.

---

## 21. Ostateczna zasada

> Jeśli hasło nie pomaga podejmować decyzji w projekcie — nie spełnia standardu.

---

Do uzupełnienia: **171 haseł**.

## Fundamenty projektu

- [x] [Baseline](Haslo-Baseline.md)
- [x] [Benefits Realization](Haslo-Benefits-Realization.md)
- [x] [Business Case](Haslo-Business-Case.md)
- [x] [Constraint](Haslo-Constraint.md)
- [x] [Deliverable](Haslo-Deliverable.md)
- [x] [Lifecycle](Haslo-Lifecycle.md)
- [x] [Milestone](Haslo-Milestone.md)
- [x] [Objective](Haslo-Objective.md)
- [x] [Outcome](Haslo-Outcome.md)
- [x] [Phase](Haslo-Phase.md)
- [x] [PMO](Haslo-PMO.md)
- [x] [Portfolio](Haslo-Portfolio.md)
- [x] [Program](Haslo-Program.md)
- [x] [Project](Haslo-Project.md)
- [x] [Project Charter](Haslo-Project-Charter.md)
- [x] [Stage Gate](Haslo-Stage-Gate.md)
- [x] [Success Criteria](Haslo-Success-Criteria.md)
- [x] [Triple Constraint](Haslo-Triple-Constraint.md)

## Role

- [x] [BA](Haslo-BA.md)
- [x] [Consultant](Haslo-Consultant.md)
- [x] [Developer](Haslo-Developer.md)
- [x] [DevOps Engineer](Haslo-DevOps-Engineer.md)
- [x] [Engineering Manager](Haslo-Engineering-Manager.md)
- [x] [Enterprise Architect](Haslo-Enterprise-Architect.md)
- [x] [PM](Haslo-PM.md)
- [x] [PO](Haslo-PO.md)
- [ ] [Portfolio Manager](Haslo-Portfolio-Manager.md)
- [ ] [Program Manager](Haslo-Program-Manager.md)
- [ ] [QA / Tester](Haslo-QA-Tester.md)
- [ ] [Resource Manager](Haslo-Resource-Manager.md)
- [ ] [Scrum Master](Haslo-Scrum-Master.md)
- [ ] [SME](Haslo-SME.md)
- [ ] [Solution Architect](Haslo-Solution-Architect.md)
- [ ] [Team](Haslo-Team.md)
- [ ] [Team Lead](Haslo-Team-Lead.md)
- [ ] [Technical Lead / Architect](Haslo-Technical-Lead-Architect.md)
- [ ] [UX/UI Designer](Haslo-UX-UI-Designer.md)
- [ ] [Vendor / Supplier](Haslo-Vendor-Supplier.md)

## Zakres i wymagania

- [ ] [Acceptance Criteria](Haslo-Acceptance-Criteria.md)
- [ ] [Backlog](Haslo-Backlog.md)
- [ ] [Business Requirements](Haslo-Business-Requirements.md)
- [ ] [Change Control](Haslo-Change-Control.md)
- [ ] [DoD](Haslo-DoD.md)
- [ ] [DoR](Haslo-DoR.md)
- [ ] [Epic](Haslo-Epic.md)
- [ ] [Feature](Haslo-Feature.md)
- [ ] [Functional Requirements](Haslo-Functional-Requirements.md)
- [ ] [In Scope / Out of Scope](Haslo-In-Scope-Out-of-Scope.md)
- [ ] [MoSCoW Prioritization](Haslo-MoSCoW-Prioritization.md)
- [ ] [MVP](Haslo-MVP.md)
- [ ] [NFR](Haslo-NFR.md)
- [ ] [Persona](Haslo-Persona.md)
- [ ] [Prioritization](Haslo-Prioritization.md)
- [ ] [Product Backlog](Haslo-Product-Backlog.md)
- [ ] [Refinement / Grooming](Haslo-Refinement-Grooming.md)
- [ ] [Requirements](Haslo-Requirements.md)
- [ ] [Scope](Haslo-Scope.md)
- [ ] [Scope Creep](Haslo-Scope-Creep.md)
- [ ] [Sprint Backlog](Haslo-Sprint-Backlog.md)
- [ ] [Technical Requirements](Haslo-Technical-Requirements.md)
- [ ] [Traceability Matrix](Haslo-Traceability-Matrix.md)
- [ ] [Use Case](Haslo-Use-Case.md)
- [ ] [User Story](Haslo-User-Story.md)

## Planowanie i harmonogram

- [ ] [Burndown / Burnup Chart](Haslo-Burndown-Burnup-Chart.md)
- [ ] [Capacity Planning](Haslo-Capacity-Planning.md)
- [ ] [Critical Path](Haslo-Critical-Path.md)
- [ ] [Dependency](Haslo-Dependency.md)
- [ ] [Estimate / Effort Estimation](Haslo-Estimate-Effort-Estimation.md)
- [ ] [Float / Slack](Haslo-Float-Slack.md)
- [ ] [Gantt Chart](Haslo-Gantt-Chart.md)
- [ ] [Iteration Plan](Haslo-Iteration-Plan.md)
- [ ] [Lead Time / Cycle Time](Haslo-Lead-Time-Cycle-Time.md)
- [ ] [Milestone Plan](Haslo-Milestone-Plan.md)
- [ ] [Release Plan](Haslo-Release-Plan.md)
- [ ] [Resource Planning / Allocation](Haslo-Resource-Planning-Allocation.md)
- [ ] [Roadmap](Haslo-Roadmap.md)
- [ ] [Schedule Baseline](Haslo-Schedule-Baseline.md)
- [ ] [Task / Subtask](Haslo-Task-Subtask.md)
- [ ] [Timeline](Haslo-Timeline.md)
- [ ] [Utilization](Haslo-Utilization.md)
- [ ] [WBS](Haslo-WBS.md)

## Budżet i finanse

- [ ] [Budget / BAC](Haslo-Budget-BAC.md)
- [ ] [Burn Rate](Haslo-Burn-Rate.md)
- [ ] [CAPEX / OPEX](Haslo-CAPEX-OPEX.md)
- [ ] [Contingency / Management Reserve](Haslo-Contingency-Management-Reserve.md)
- [ ] [Cost Baseline](Haslo-Cost-Baseline.md)
- [ ] [CPI](Haslo-CPI.md)
- [ ] [EAC](Haslo-EAC.md)
- [ ] [ETC](Haslo-ETC.md)
- [ ] [Financial Tracking](Haslo-Financial-Tracking.md)
- [ ] [Fixed Price](Haslo-Fixed-Price.md)
- [ ] [Invoice / PO](Haslo-Invoice-PO.md)
- [ ] [Retainer / Unit Rate](Haslo-Retainer-Unit-Rate.md)
- [ ] [ROI](Haslo-ROI.md)
- [ ] [T&M](Haslo-T-and-M.md)
- [ ] [TCO](Haslo-TCO.md)
- [ ] [VAC](Haslo-VAC.md)

## Kontrola i raportowanie

- [ ] [Action / Decision Log](Haslo-Action-Decision-Log.md)
- [ ] [Compliance](Haslo-Compliance.md)
- [ ] [Dashboard](Haslo-Dashboard.md)
- [ ] [EV / PV / AC](Haslo-EV-PV-AC.md)
- [ ] [Forecast](Haslo-Forecast.md)
- [ ] [Health Check / Audit](Haslo-Health-Check-Audit.md)
- [ ] [KPI](Haslo-KPI.md)
- [ ] [Lessons Learned Register](Haslo-Lessons-Learned-Register.md)
- [ ] [OKR](Haslo-OKR.md)
- [ ] [RAG Status](Haslo-RAG-Status.md)
- [ ] [RAID Log](Haslo-RAID-Log.md)
- [ ] [SPI / CPI](Haslo-SPI-CPI.md)
- [ ] [Status Report](Haslo-Status-Report.md)
- [ ] [Variance Analysis](Haslo-Variance-Analysis.md)

## Ryzyko i problemy

- [ ] [Blocker](Haslo-Blocker.md)
- [ ] [Impediment](Haslo-Impediment.md)
- [ ] [Issue](Haslo-Issue.md)
- [ ] [Mitigation](Haslo-Mitigation.md)
- [ ] [Mitigation: accept](Haslo-Mitigation-accept.md)
- [ ] [Mitigation: avoid](Haslo-Mitigation-avoid.md)
- [ ] [Mitigation: contingency plan](Haslo-Mitigation-contingency-plan.md)
- [ ] [Mitigation: delegate](Haslo-Mitigation-delegate.md)
- [ ] [Mitigation: ignore](Haslo-Mitigation-ignore.md)
- [ ] [Mitigation: reduce](Haslo-Mitigation-reduce.md)
- [ ] [Mitigation: transfer](Haslo-Mitigation-transfer.md)
- [ ] [Risk](Haslo-Risk.md)
- [ ] [Risk Register](Haslo-Risk-Register.md)
- [ ] [Risk Response](Haslo-Risk-Response.md)

## Klient i współpraca

- [ ] [Account Manager](Haslo-Account-Manager.md)
- [ ] [Alignment Meeting](Haslo-Alignment-Meeting.md)
- [ ] [Approval / Sign-off](Haslo-Approval-Sign-off.md)
- [ ] [Business Review / QBR](Haslo-Business-Review-QBR.md)
- [ ] [Client / Customer](Haslo-Client-Customer.md)
- [ ] [Client Communication](Haslo-Client-Communication.md)
- [ ] [CR](Haslo-CR.md)
- [ ] [CSM](Haslo-CSM.md)
- [ ] [Delivery Manager](Haslo-Delivery-Manager.md)
- [ ] [Engagement Manager](Haslo-Engagement-Manager.md)
- [ ] [Escalation](Haslo-Escalation.md)
- [ ] [Escalation Path](Haslo-Escalation-Path.md)
- [ ] [Executive Sponsor](Haslo-Executive-Sponsor.md)
- [ ] [Expectation Management](Haslo-Expectation-Management.md)
- [ ] [Follow-up](Haslo-Follow-up.md)
- [ ] [Governance Model](Haslo-Governance-Model.md)
- [ ] [Key Stakeholder](Haslo-Key-Stakeholder.md)
- [ ] [Kick-off Meeting](Haslo-Kick-off-Meeting.md)
- [ ] [MoM](Haslo-MoM.md)
- [ ] [Sponsor](Haslo-Sponsor.md)
- [ ] [Stakeholder](Haslo-Stakeholder.md)
- [ ] [Stakeholder Management](Haslo-Stakeholder-Management.md)
- [ ] [Stakeholder Mapping](Haslo-Stakeholder-Mapping.md)
- [ ] [Steering Committee](Haslo-Steering-Committee.md)
- [ ] [Touchpoint](Haslo-Touchpoint.md)
- [ ] [Workshop](Haslo-Workshop.md)

## Zakupy i kontakt z klientem

- [ ] [BAFO](Haslo-BAFO.md)
- [ ] [Call / Discovery Call](Haslo-Call-Discovery-Call.md)
- [ ] [Client Workshop](Haslo-Client-Workshop.md)
- [ ] [Commercials](Haslo-Commercials.md)
- [ ] [Contract](Haslo-Contract.md)
- [ ] [Due Diligence](Haslo-Due-Diligence.md)
- [ ] [ITT](Haslo-ITT.md)
- [ ] [MSA](Haslo-MSA.md)
- [ ] [NDA](Haslo-NDA.md)
- [ ] [Pre-sales](Haslo-Pre-sales.md)
- [ ] [Procurement Plan](Haslo-Procurement-Plan.md)
- [ ] [Proposal](Haslo-Proposal.md)
- [ ] [Rate Card](Haslo-Rate-Card.md)
- [ ] [RFI](Haslo-RFI.md)
- [ ] [RFP](Haslo-RFP.md)
- [ ] [RFQ](Haslo-RFQ.md)
- [ ] [SLA](Haslo-SLA.md)
- [ ] [SoW](Haslo-SoW.md)
- [ ] [Tender / Bid](Haslo-Tender-Bid.md)
- [ ] [Vendor Evaluation](Haslo-Vendor-Evaluation.md)
