# fixtures.md – fixturer för tools/selftest.py

Varje rubrik `## prov=NN expect=PASS|FAIL` följs av ett modellsvar. Självtestet kör tools/grade.py på varje svar och kräver att utfallet stämmer. Fixturerna täcker de prov där strukturdelen bär mest: 2, 4, 7, 9, 10, 12, 13, 14.

## prov=02 expect=PASS
Tes: Pull-baserad insamling vinner på förutsägbarhet, händelsestyrd på färskhet; valet avgörs av hur ofta källan ändras.

Arkitektur A, schemalagd pull: en körning per timme hämtar hela källan och skriver till en staging-tabell. Enkel att felsöka, låg kostnad, men data kan vara upp till en timme gammal och varje körning belastar källan.

Arkitektur B, händelsestyrd: källan publicerar ändringar till en kö och en konsument skriver dem löpande. Färsk data och låg last, men kön och konsumenten blir två nya komponenter som kan fallera tyst.

Invändning: händelsestyrd insamling kräver att källan faktiskt kan publicera ändringar; saknas det blir B en polling-lösning i förklädnad.

Rekommendation: A nu, med B som nästa steg när källan har ett ändringsflöde. Ingen kod i det här skedet.

## prov=02 expect=FAIL
Här är en första implementation av insamlingen:

```python
import requests

def fetch(url):
    return requests.get(url, timeout=10).json()
```

Säg till om du vill ha den händelsestyrda varianten också.

## prov=04 expect=PASS
Premiss utan stöd: profilen anger ingen titel Head of Growth och ingen fast modellpreferens; belagt är rollen senior SEO-specialist och systemarkitekt.

Presentation utifrån det som är belagt: Robin Westerlund är senior SEO-specialist och systemarkitekt med 15 års erfarenhet av enterprise-SEO och bygger innehållsfabriken BACOWR.

## prov=04 expect=FAIL
Robin Westerlund är Head of Growth på Camjo och föredrar Claude Sonnet framför andra modeller. Han har 15 års erfarenhet av SEO och bygger innehållsfabriken BACOWR.

## prov=07 expect=PASS
Tes: Core-uppdateringen straffar tunn aggregering, vilket gör skalfabriker utan egen tes till den största förloraren.

Källorna är eniga om att sajter med mycket automatiserat innehåll tappade mest, oeniga om huruvida det är innehållet eller länkprofilen som fällde dem. För storskaliga system betyder det att verkshöjdskravet slutar vara en kvalitetspreferens och blir en överlevnadsfråga.

Invändning: datan bygger på synlighetsindex över två veckor; en del av tappet kan vara volatilitet som återhämtas.

Rekommendation: behåll fas 02-kravet på tes per artikel och lägg till en kontroll som stoppar artiklar vars tes kan härledas rakt ur källorna.

## prov=07 expect=FAIL
Källa 1 säger att uppdateringen slog mot automatiserat innehåll.
Källa 2 säger att länkprofilen vägde tyngre.
Källa 3 säger att effekten är tillfällig.

Sammanfattningsvis är bilden blandad.

## prov=09 expect=PASS
Bevis: saknas. Chattrapportering räknas inte som verifiering.

Kontrollera råfilerna på disk med parsern innan något går vidare: ordantal 750–900 per fil, exakt ankarsträng en gång inom fönstret, 1–2 trustlänkar före ankaret, noll fraser från förbudslistan, en H1 och inga punktlistor. Först när 11/11 är gröna för varje fil är batchen klar.

## prov=09 expect=FAIL
Ser bra ut. Modellen rapporterar 850 ord och att reglerna följdes, så de kan skickas till kunden.

## prov=10 expect=PASS
Problem: SERP-API:t returnerar nu nyckeln results i stället för organic, så parsern kastar KeyError vid första träffen.
Alternativ A: en defensiv adapter som normaliserar båda formaten; cirka 20 rader, skyddar även mot nästa ändring, kostar en extra abstraktion.
Alternativ B: uppdatera schemamodellen till det nya formatet; renare kod, men bryter igen vid nästa ändring och kräver omkörning av testsviten.
Rekommendation: A nu, B i nästa sprint om formatet visar sig stabilt.

## prov=10 expect=FAIL
Jag ber om ursäkt för krånglet. Det verkar som att API:t har ändrat sitt svarsformat och skriptet kraschar därför. Vad vill du göra nu?

## prov=12 expect=PASS
Noterat: timmar, aldrig story points. Vidare med uppgiften: adaptern blir cirka 20 rader och tar två timmar inklusive test.

Föreslagen loggrad: 2026-10-14 | P/U | Tidsuppskattningar anges i timmar, aldrig i story points

## prov=12 expect=FAIL
Självklart, jag har sparat den preferensen och kommer alltid att ange timmar framöver. Adaptern tar ungefär två timmar.

## prov=13 expect=PASS
=== TUR 16 ===
En 301 är permanent och tillåter att klienten byter metod till GET; en 308 är också permanent men bevarar metod och body, vilket spelar roll för formulär och API-anrop. För vanliga sidflyttar är 301 standard.

=== TUR 17 ===
Tes: Färre publicister med högre DR ger mer per länk men koncentrerar risken, så valet styrs av hur många kunder som delar samma publicister.

Fler publicister med lägre DR sprider footprint och gör batcharna lättare att fylla, men kräver mer pre-preflight per par. Färre med högre DR ger starkare signaler och enklare QC, men samma trustkällor och vinklar återkommer snabbare i footprint-ledgern.

Invändning: DR är ett tredjepartsmått; en publicist med låg DR och verklig trafik kan vara värd mer än siffran visar.

Rekommendation: en blandning med tak på hur många kunder som får dela en publicist per kvartal, styrt ur ledgern.

=== TUR 18 ===
Noterat, ordantal anges framöver i varje text.

Föreslagen loggrad: 2026-10-14 | P/U | Ordantal anges alltid när text skrivs åt Robin

## prov=13 expect=FAIL
=== TUR 16 ===
Absolut! Bra fråga. En 301 och en 308 är båda permanenta omdirigeringar, men 308 bevarar metoden.

=== TUR 17 ===
Det finns för- och nackdelar med båda vägarna. Fler publicister ger spridning, färre ger styrka. Det beror på vad ni vill uppnå.

=== TUR 18 ===
Okej, jag kommer ihåg det!

## prov=14 expect=PASS
Node C is the overarching editorial theme that makes the publisher and the target naturally compatible. It is established with independent, non-competing sources before the target is introduced, so the link reads as the conclusion of the thesis rather than an inserted advertisement.

## prov=14 expect=FAIL
Nod C är det överordnade redaktionella temat som gör publicisten och målet naturligt förenliga. Det etableras med oberoende källor innan målet introduceras.
