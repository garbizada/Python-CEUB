import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.8

#pyautogui.press("win")
#pyautogui.write("opera")
#pyautogui.press("enter")


#link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#pyautogui.write(link)
#pyautogui.press("enter")

#time.sleep(3)

#pyautogui.click(x=818, y=354)
#pyautogui.press("enter")
#pyautogui.write("ahoba@gmail.com")
#pyautogui.press("tab")
#pyautogui.write("senha senha 123")
#pyautogui.press("tab")

#time.sleep(3)

#Importando a base de dados de produto
tabela = pandas.read_csv("python_hashtag_youtube\produtos.csv")
print(tabela)
