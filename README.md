# Eget-Projekt
markdown# Case Study: Processkartläggning & Kravhantering för Molnmigrering av Affärsdata

Detta projekt är en fallstudie som visar min metodik som Business Analyst i gränslandet mellan verksamhet och IT. Projektet simulerar en övergång från ett lokalt system till en molnbaserad miljö (Azure) med fokus på datadriven analys och regulatorisk efterlevnad.

## 1. Affärsproblem & Kontext
**Sammanhang:** Organisationen upplevde flaskhalsar i den finansiella rapporteringen. Rådata hämtades manuellt från lokala servrar, vilket ledde till ledtider på 5 dagar för ledningsrapporter samt hög risk för mänskliga fel.
**Problemet:** Verksamheten behövde realtidsinsikter för beslutsfattande, medan IT behövde avveckla lokal infrastruktur för att minska underhållskostnader och möta nya lagkrav kring datalagring.

## 2. Min Analys: Strukturering av Behov, Krav & Scope
För att bryta ner initiativet genomförde jag processkartläggning (AS-IS / TO-BE) och kategoriserade kraven i tre spår:

*   **Funktionella krav (FR):** Systemet ska automatiskt uppdatera Power BI-dashboards var 6:e timme via molnet.
*   **Icke-funktionella krav (NFR):** Svarstiden för rapportgenerering får inte överstiga 3 sekunder under hög belastning.
*   **Regulatoriska krav (RR):** All datahantering och kryptering måste uppfylla gällande säkerhetsskyddsbestämmelser (Data-in-transit och Data-at-rest).

*Källkod för kraven återfinns i filen `requirements.sql` i detta arkiv.*

## 3. Stakeholders & Beslut (Hantering av Målkonflikter)
Under analysfasen uppstod en målkonflikt:
*   **Verksamheten (Finans):** Ville ha obegränsad tillgång till all historisk rådata i molnet för ad-hoc-analyser.
*   **IT-Säkerhet:** Motsatte sig detta på grund av lagringskostnader och strikta säkerhetsregler kring känslig data.

**Min åtgärd:** Jag faciliterade en workshop där vi använde en konsekvensmatris. Jag visade att 85% av besluten baserades på data från de senaste 3 åren. 
**Beslut:** Vi nådde alignment genom att införa en "Hot/Cold"-datastrategi: de senaste 3 åren migrerades till snabbt molnlagring (Azure), medan äldre data arkiverades billigt och säkert.

## 4. Prioritering & Värde (MoSCoW-metoden)
För att säkerställa att rätt saker byggdes sorterade jag kraven tillsammans med produktägaren:
*   **Must Have:** Automatiserad ETL-pipeline till molnet för kärndata samt grundläggande säkerhetsbehörigheter.
*   **Should Have:** Power BI-dashboard för ledningsgruppen.
*   **Could Have:** Prediktiv analys av framtida kassaflöden med Python.
*   **Won't Have (just now):** Realtidsströmning per minut.

## 5. Resultat & Utfall
*   **Effekt:** Ledtiden för månadsrapporteringen minskade från 5 dagar till 0 (automatiserad realtid).
*   **Kvalitet:** Manuella fel i datainmatningen eliminerades helt tack vare de automatiserade valideringsreglerna.
*   **Säkerhet:** Det nya molnlandskapet godkändes i den externa säkerhetsgranskningen utan anmärkningar.

## 6. Förbättrat Arbetssätt
Under projektets gång märkte jag att utvecklingsteamet (IT) ofta missförstod verksamhetens behov. Jag introducerade därför **Behavior-Driven Development (BDD)** i form av *"Given-When-Then"*-scenarier i Jira. Detta förbättrade kommunikationen, minskade antalet buggar i testfasen med 30% och stärkte team-samspelet avsevärt.