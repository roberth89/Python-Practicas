import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException 
from threading import Thread, Barrier

def func(threads, usuario):

    # Inicia el push
    web = webdriver.Chrome()

    # Formulario de registro
    web.get('https://q4rgmwkiq3gupnq.us.qlikcloud.com/')      

    # para varios usuarios usar lista.
    nombre_correo = usuario.email
    passoword = usuario.password

    correo_web = WebDriverWait(web, 30).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/main/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div/div[1]/div[2]/input")))
    correo_web.send_keys(nombre_correo)

    password_web = WebDriverWait(web, 30).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/main/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div/div[3]/span/div/div/div/div/div/div/div/div/div/div[2]/div/div[2]/input")))
    password_web.send_keys(passoword)

    WebDriverWait(web, 30).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div/main/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div/form/div/div/div[4]/button/span"))).click()
    threads.wait()
 
    time.sleep(10.4)     

    WebDriverWait(web, 30).until(EC.element_to_be_clickable(
    (By.XPATH, " /html/body/div/div[1]/div[2]/div[1]/div/div/div/div/ul/nav/div[4]/a/div[2]/span"))).click()

    #https://q4rgmwkiq3gupnq.us.qlikcloud.com/item/641cdd37297dd42261408eff/details
    #/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[2]


    web.get('https://q4rgmwkiq3gupnq.us.qlikcloud.com/item/641cdd37297dd42261408eff/details')    
    WebDriverWait(web, 30).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div/button[2]"))).click()  
 
    time.sleep(10.4)   
    screenshot = web.save_screenshot(str(usuario.email)+ 'my_screenshot.png')


class usuarios: 
    def __init__(self, email, password, id): 
        self.email = email 
        self.password = password,
        self.id = id,
list = [] 
list.append( usuarios('roberto.cordero@grupomonge.com', 'ABC123xyz', 1) )
list.append( usuarios('eduardo.morales@grupomonge.com', 'Ed1234**',2) )

numero_tareas = 2
barrier = Barrier(numero_tareas)
threads = []

for _ in range(numero_tareas):
	i = Thread(target=func, args=(barrier,list[_]))
	i.start()
	threads.append(i)

for i in threads:
	i.join()
    