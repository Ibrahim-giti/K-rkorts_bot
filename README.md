## Körkorts bot
Detta är en simpel bot som kan användas för att hitta lediga körprovstider.
Boten använder biblioteket Playwright som styr webbläsaren automatiskt istället för att göra det manuellt.

## Hur det fungerar
1. Playwright öppnar en webbläsare och navigerar till Trafikverkets bokningssida
2. Du loggar in manuellt med BankID (en gång)
3. Inloggningen sparas som cookies i en fil kallad `session.json`
4. Nästa gång boten startar laddar den cookiesen automatiskt – inget nytt BankID-godkännande krävs
5. (Nästa steg) Boten söker igenom valda städer och meddelar när en ledig tid hittas

## Status
- [x] Boten kan öppna Trafikverkets bokningssida
- [x] Inloggning med BankID fungerar
- [ ] Session sparas och återanvänds automatiskt
- [ ] Sökning efter lediga tider
- [ ] Notifikation via e-post

## Installation
pip install playwright
playwright install chromium
