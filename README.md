# Biuro Rachunkowe Joanna Bil

Statyczna strona dla GitHub Pages. Pliki HTML w głównym katalogu są gotowe do publikacji i zawierają pełną treść bez JavaScriptu.

## Edycja

- `site-src/pages/`: treść każdej strony, tytuły i opisy SEO.
- `site-src/partials/`: wspólne menu, stopka, kontakt i karta oferty.
- `site-src/settings.json`: aktualne ceny miesięcznej obsługi. Zmiana jest przenoszona do treści, tytułów, tabel oraz danych strukturalnych podczas generowania.
- `assets/css/style.css`: wygląd strony.
- `assets/js/menu.js`: zamykanie menu mobilnego po wybraniu odnośnika. Brak analityki i nowych cookies.

Po edycji uruchom:

```sh
python3 scripts/build.py
python3 scripts/build.py --check
python3 scripts/check.py
```

Zapisz w commicie źródła oraz wygenerowane pliki HTML. Hosting nie potrzebuje Pythona ani procesu budowania. Nie edytuj samych wygenerowanych HTML, bo następne generowanie nadpisze te zmiany.

Nową stronę dodaj do `site-src/pages/`, mapy `sitemap.xml` oraz odpowiednich odnośników. `lastmod` zmieniaj przy faktycznej, istotnej zmianie treści, nie przy każdym uruchomieniu skryptu.

## Cel poszczególnych stron

| Adres | Rola |
| --- | --- |
| `/` | Przedstawienie Joanny i wybór ścieżki współpracy |
| `/ksiegowosc-online-jdg` | Oferta obsługi online z całej Polski i podział obowiązków |
| `/cennik` | Pełne ceny i formularz zapytania |
| `/ile-kosztuje-ksiegowosc-jdg` | Poradnik porównywania kosztów i przykłady liczby dokumentów |
| `/zalozenie-firmy-jdg` | Przygotowanie do rejestracji i rozpoczęcia obsługi |
| `/zmiana-biura-rachunkowego` | Przejęcie dokumentacji i ustalenia między biurami |
| `/ksiegowosc-jdg-krakow` | Oferta lokalna dla Krakowa |
| `/ksiegowosc-nowa-huta` | Spotkania po umówieniu w Nowej Hucie |
| `/ryczalt-czy-kpir` | Wyjaśnienie form rozliczeń |
| `/ksef-faktury` | KSeF, współpraca z biurem i oficjalne materiały MF |

## Wersja do sprawdzenia przed publikacją

Zmiany przygotowane 17 października 2026 r. Adres domowy pozostaje niepubliczny. Zachowane są ceny, formularz Web3Forms oraz dotychczasowe adresy podstron. Nie dodano kalkulatora, śledzenia kliknięć ani nowych obietnic terminów realizacji.

Przed publikacją Joanna powinna przeczytać rozszerzone opisy obsługi, w szczególności zawarcie umowy, przekazywanie dokumentów, przejęcie rozliczeń rocznych i pomoc przy rejestracji firmy. Cena jednorazowej pomocy pozostaje do indywidualnego uzgodnienia, ponieważ nie została podana.

Dotychczasowe szczegółowe treści podatkowe nie są pełnym audytem prawnym. Ich aktualność i zastosowanie do klientów należy sprawdzić przed publikacją. Nie dodano podpisu sugerującego, że Joanna już zweryfikowała nowe teksty.

Do materiałów KSeF dodano odnośniki do instrukcji Ministerstwa Finansów. Nie wstawiono fikcyjnych screenów programu ani nie wskazano niepotwierdzonego dostawcy aplikacji. Zrzuty podglądu dotyczą rzeczywistego wyglądu tej wersji witryny.

FAQ pozostaje widoczne dla użytkowników. Usunięto powielone znaczniki FAQPage (Google wycofało ten rodzaj wyniku rozszerzonego w maju 2026). Zachowano dane firmy, usług i okruszków. Materiały źródłowe: https://developers.google.com/search/updates oraz https://ksef.podatki.gov.pl/aplikacja-podatnika-ksef-20/.

Publikacja wymaga osobnej decyzji i scalenia zmian z gałęzią obsługiwaną przez GitHub Pages. Samo utworzenie propozycji zmian nie publikuje strony.
