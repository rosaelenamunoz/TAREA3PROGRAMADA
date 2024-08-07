#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:31:16 2024

@author: rosaelenamunoz
"""
# -*- coding: utf-8 -*-

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# URL de la página para extraer los datos.
PAGINA_PRINCIPAL = "https://www.scrapethissite.com/pages/forms/"

# Configurar opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar Chrome en modo headless (sin interfaz gráfica)

# Inicializar el navegador
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
navegador.get(PAGINA_PRINCIPAL)
navegador.implicitly_wait(10)

datos = []
equipos = navegador.find_elements(By.CLASS_NAME, 'team')

for equipo in equipos:
    nombre = equipo.find_element(By.CLASS_NAME, 'name')
    year = equipo.find_element(By.CLASS_NAME, 'year')
    wins = equipo.find_element(By.CLASS_NAME, 'wins')
    losses = equipo.find_element(By.CLASS_NAME, 'losses')
    ot_losses = equipo.find_element(By.CLASS_NAME, 'ot-losses')
    pct = equipo.find_element(By.CLASS_NAME, 'pct')
    gf = equipo.find_element(By.CLASS_NAME, 'gf')
    ga = equipo.find_element(By.CLASS_NAME, 'ga')
    diff = equipo.find_element(By.CLASS_NAME, 'diff')

    datos.append({
        'Nombre': nombre.text,
        'Año': year.text,
        'Victorias': wins.text,
        'Derrotas': losses.text,
        'OT Derrotas': ot_losses.text,
        'Pct': pct.text,
        'GF': gf.text,
        'GA': ga.text,
        'Diff': diff.text
    })

navegador.quit()

# Crear un DataFrame con los datos extraídos
df = pd.DataFrame(datos)
print(df)

# Guardar los datos en un archivo Excel
ruta = "/Users/rosaelenamunoz/Desktop/TAREAPROYECTO"
df.to_excel(ruta, index=False)


