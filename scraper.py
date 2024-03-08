from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def estrai_testi_da_url(url, output_file='testi_da_url.txt'):
    try:
        # Utilizza Selenium per aprire la pagina e attendere il caricamento completo
        driver = webdriver.Chrome()  # Assicurati di avere il driver Chrome installato
        driver.get(url)

        # Attendi che la pagina si carichi completamente (puoi regolare questo valore in base alle esigenze)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "argomento")))

        # Ottieni il contenuto HTML della pagina dopo il caricamento dinamico
        page_source = driver.page_source

        # Utilizza BeautifulSoup per analizzare l'HTML della pagina
        soup = BeautifulSoup(page_source, 'html.parser')

        # Trova tutti gli elementi <h3> con classe 'card-title t-primary title-xlarge'
        titoli = soup.find_all('h3', class_='card-title t-primary title-xlarge')

        # Salva i testi degli elementi trovati su un file di testo
        with open(output_file, 'w', encoding='utf-8') as file:
            for titolo in titoli:
                testo = titolo.get_text(strip=True)
                file.write(testo + '\n')

        print(f"I testi sono stati salvati in '{output_file}' nella stessa cartella dello script.")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")

    finally:
        # Chiudi il browser alla fine
        driver.quit()

# Esempio di utilizzo
url_input = input("Inserisci l'URL della pagina web: ")
estrai_testi_da_url(url_input)
