# Oxido

Niniejszy program napisany został w języku Python. Aplikacja pobiera plik tekstowy z adresu URL
, następnie łączy się z API OpenAI z modelem ChatGPT 4o mini i przekazuje 
mu wytyczne w celu przeformatowania
tekstu źródłowego na strukturę HTML. Skrypt dodaje nagłówki, wydziela paragrafy i sekcje,
ustala miejsce wstawienia obrazu wraz z promptem do ewentualnego wytworzenia grafiki
i inne. 

Po wygenerowaniu kodu, jest on zapisywany do pliku w formie gotowej do wstawienia
w element `<body>`. Szablon i podgląd skonstruowanej strony również dodano
do repozytorium.

## artykul.py
### Wymagania
- Python 3.6
- Biblioteki requests, os, openai
- Klucz API OpenAI do interakcji z modelem OpenAI

### Konfiguracja
- Sklonuj lub pobierz repozytorium
````bash
git clone https://github.com/your-repository/openai-text-formatter.git
cd openai-text-formatter
````
- Zainstaluj zależności
````bash
pip install -r requirements.txt
````
- Ustaw klucz API OpenAI

    Do skorzystania z aplikacji niezbędne jest posiadanie własnego klucza OpenAI,
który można uzyskać na stronie OpenAI: <a href="https://openai.com/index/openai-api/">OpenAI API</a>.

Artykul.py umożliwia użytkownikowi przekazanie uzyskanego klucza bezpośrednio
do klasy OpenAIAPI, lecz ze względów bezpieczeństwa zaleca się wgrać go
jako zmienną środowiskową:

Dla Linux/macOS:
````bash
export OPENAI_API_KEY="uzyskany klucz api"
````
Dla Windows(Powershell):
````bash
$env:OPENAI_API_KEY="uzyskany klucz api"
````

### Użytkowanie
Klasa OpenAIAPI: Główna klasa, która komunikuje się z API OpenAI, pobiera 
tekst, formatuje go i zapisuje wynik. Na klasę składają się:
- .text - atrybut, który pobiera tekst z URL i zapisuje go do lokalnego pliku.
- .prompt(): metoda wysyłająca zapytanie do API OpenAI z wprowadzonym przez 
użytkownika promptem, lub - w przypadku jego nie dostarczenia - promptem określonym wcześniej przez autora. 
Zapytanie używane jest z wejściem self.text, które pobiera tekst z adresu URL. Użytkownik może zmienić adres URL przypisany zmiennej self.text
na własny lub usunąć adres i swój własny tekst wprowadzić jako argument do .prompt().

- .save(): zapisuje sformatowany tekst do pliku. Daje użytkownikowi możliwość wprowadzenia do metody argumentu w celu własnego nazwania pliku.

Całość uruchamiana jest z poziomu funkcji main(). W przypadku zdecydowania się na manualne
wprowadzenie klucza API OpenAI, należy pamiętać o wprowadzeniu go do klasy OpenAIAPI("Twój_klucz")

Skrypt uruchamia się poleceniem:

````bash
python artykul.py
````
Po kilkunastu sekundach stworzy on dwa pliki:
- artykul_przykladowy.txt - będący tekstem źródłowym
- artykul.html - czyli wygenerowany przez AI tekst źródłowy w gotowy do wklejenia w ```<body>``` pliku przeglad.html.
## szablon.html
Plik szablon.html zawiera globalne style i strukturę, w której osadzone będą wygenerowane przez skrypt treści HTML.

Plik zawiera:
- ustawienia CSS dla nagłówków, akapitów, obrazów i animacji,
- ustawienia dla mediów, które umożliwiają dostosowanie wyglądu do urządzeń mobilnych (responsywność).

## podgląd.html
Łączy w sobie kod przygotowany w szablon.html oraz kod wygenerowany przez połączenie się
artykul.py z API OpenAI.



