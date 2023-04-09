from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openai

openai.api_key = "YOUR_API_KEY"
ai_model = "gpt-3.5-turbo"

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")

while True:
    mesajlar = driver.find_elements(By.CLASS_NAME, "_27K43")
    if not mesajlar:
        continue

    son_mesaj =     mesajlar[-1].text
    
    if "?" in son_mesaj and not son_mesaj.startswith("Soru:"):
        prompt = f"Q: {son_mesaj}\nA:"
        response = openai.ChatCompletion.create(
        max_tokens=1024,
        stop=None,
        temperature=0.7,
        model=ai_model, 
        messages=[{"role": "user", "content": son_mesaj}]
)

        cevap =  response["choices"][0]["message"]["content"].strip()
        
        giris_kutusu = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
        giris_kutusu.send_keys(f"Einstein: {cevap}")
        giris_kutusu.send_keys(u'\ue007')   