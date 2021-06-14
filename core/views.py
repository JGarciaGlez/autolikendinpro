

from django.contrib.auth.forms import AuthenticationForm
from core.forms import Loginlikendin
import re
from core.scripts.iraconectar import  conectar
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import time
from numpy import load
import pyautogui
# Create your views here.
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions as exceptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
from bs4 import BeautifulSoup
import csv
import _strptime
import pandas as pd
from .forms import Loginlikendin, Passwordform, Scrappingform, VisitedForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages  # import messages
    
def register(request):
    if request.method == "POST":
        form = Loginlikendin(request.POST)       
        if form.is_valid():
            user=form.save()            
            raw_password = form.cleaned_data.get('password1')
            user.save()
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, "Registro completado.")
            return redirect("core:login")
        messages.error(request, "Fallo en el registro.Información inválida.")
    form = Loginlikendin()
    return render(request, 'layouts/register.html', context={"user_form": form})


def conectli(request):
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.linkedin.com/home')   

    sleep(3)   
    buscalogin = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
    sleep(1)
    email = 
    
    password = 
    

    emaillotele = driver.find_element_by_xpath("//*[@id='session_key']")
    contraseña = driver.find_element_by_xpath("//*[@id='session_password']")
    emaillotele.send_keys(email)
    contraseña.send_keys(password)
    sleep(10)
    login = driver.find_element_by_class_name("sign-in-form__submit-button")
    login.click() 
    time.sleep(60)
    print(driver.get_cookies())    
    """


def home(request):
    return render(request, 'layouts/home.html')

def scrapping(request):
    if request.method == "POST":
        form = Scrappingform(request.POST)
        if form.is_valid():                   
            localization = request.POST.get('localization','')
            name = request.POST.get('name','')
            pages = request.POST.get('pages','')
            print(localization)
            print(name)
            print(pages)                    
            driver = webdriver.Chrome(ChromeDriverManager().install())
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-popup-blocking")        
            sleep(3)
            query = 'site:linkedin.com/in/' +'+"'+name+'"+"'+localization+'"'
            print(query)
            sleep(5)
            links = []
            n_pages = pages
            for page in range(1, int(n_pages)):
                url = "http://www.google.com/search?q=" + \
                    query + "&start=" + str((page - 1) * 10)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                search = soup.find_all('div', class_="yuRUbf")
                for h in search:
                    links.append(h.a.get('href'))
            driver.close()
            wtr = csv.writer(open('out.csv', 'w'), delimiter=',', lineterminator='\n')
            for x in links:
                wtr.writerow([x])
        else:
            messages.error(request, "datos inválidos.")
    form = Scrappingform()

    return render(request, 'layouts/scrapping.html', context={"scraping": form})

    """
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    query = "recursos humanos"
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-popup-blocking")

    query = 'site:linkedin.com/in/ + "recursos humanos" + "barcelona"'
    links = []
    n_pages = 2
    for page in range(1, n_pages):
        url = "http://www.google.com/search?q=" + \
            query + "&start=" + str((page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            links.append(h.a.get('href'))

    driver.close()
    wtr = csv.writer(open('out.csv', 'w'), delimiter=',', lineterminator='\n')
    for x in links:
        wtr.writerow([x])
"""
    return render(request, 'layouts/scrapping.html')
    
from django.contrib.auth.models import User
def busqueda(request):
    username = request.user.username   
    emailu = request.user.email
    if request.method == "POST":
        form = Passwordform(request.POST)
        if form.is_valid(): 
            likendinContraseña = request.POST.get('LikendinContraseña','')           
            driver = webdriver.Chrome(ChromeDriverManager().install())
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-popup-blocking")
            driver.get('https://www.linkedin.com/home')
            sleep(3)
            buscalogin = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
            sleep(1)
            #emails = User.objects.filter(is_active=True).values_list('email', flat=True)
            email = emailu
            #
            # passwords=User.objects.filter(is_active=True).values_list('passwordlikendin',flat=True)
  
            emaillotele = driver.find_element_by_xpath("//*[@id='session_key']")
            contraseña = driver.find_element_by_xpath("//*[@id='session_password']")
            emaillotele.send_keys(email)
            contraseña.send_keys(likendinContraseña)
            sleep(10)
            login = driver.find_element_by_class_name("sign-in-form__submit-button")
            login.click()
            sleep(3)
            from .scripts import iraconectar
     
            with open("out.csv", 'r') as f:
                for line in f:
                    print(line)
                    while line:                       
                        driver.get(line)                       
                        sleep(2)
                        conectar()   
                        sleep(2)                  
                        break
        else:
            messages.error(request, "Datos inválidos.")          
    form = Passwordform()
    return render(request, 'layouts/conectar.html',{'conect':form})
    # localizacion='españa'
    # irlocalizacion.send_keys(localizacion+keys.ENTER)
    # sleep(10)
    #mensajepersonalizado=['Hola, me gustaría conectar con usted , para recirbir ofertas de trabajo, soy junior en python(django),js,php,html,css3']
    maxconesiones = 100
    conesiones = 0

    #WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//*[@id='artdeco-hoverable-artdeco-gen-53']/div[1]/div/form/fieldset/div[1]/ul/li[1]/label").is_displayed())
    # driver.execute_script("document.getElementsByClassName('#artdeco-hoverable-artdeco-gen-61 > div.artdeco-hoverable-content__shell > div > form > fieldset > div.pl4.pr6 > div.click();")
    i = 0  # for scrolling the window
    # count of connection
    # while conesiones!=maxconesiones:
    # try:
    # nextk=driver.find_element_by_class_name('artdeco-pagination__button--next')
    # print(nextk)
    #print('hola javi')

    # if nextk:
    # nextk.click()
    # except:
    # pass
    # for i in range(0,13):
    # i=i+1
    # sc=i*100#scroll

    # try:
    # time.sleep(random.randint(5,7))
    # cn=driver.find_element_by_xpath('//button[text()="Connect"]')

    # if cn:
    # cn.click()
    # time.sleep(random.randint(2,4))
    # driver.find_element_by_class_name('ml1').click()
    # conesiones=conesiones+1
    # print(conesiones)
    # driver.execute_script("window.scrollTo(0,"+str(sc)+")")
    # except:
    # try again till connection count is not completd
    #print("try again")
    # driver.execute_script("window.scrollTo(0,"+str(sc)+")")




def visitar(request):
    username = request.user.username   
    emailu = request.user.email
    if request.method == "POST":
        form = VisitedForm(request.POST)
        if form.is_valid():             
            likendinContraseña = request.POST.get('LikendinContraseña','')           
            driver = webdriver.Chrome(ChromeDriverManager().install())
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-popup-blocking")
            driver.get('https://www.linkedin.com/home')
            sleep(3)
            buscalogin = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
            sleep(1)
            email = emailu          
            emaillotele = driver.find_element_by_xpath("//*[@id='session_key']")
            contraseña = driver.find_element_by_xpath("//*[@id='session_password']")
            emaillotele.send_keys(email)
            contraseña.send_keys(likendinContraseña)
            sleep(10)
            login = driver.find_element_by_class_name("sign-in-form__submit-button")
            login.click()
            sleep(5)
            visited=0
            with open("out.csv", 'r') as f:
                for line in f:
                    visited+=1
                    print(line)
                    while line:
                        screenWidth, screenHeight = pyautogui.size()
                        print(screenHeight, screenWidth)
                        sleep(5)
                        driver.get(line)
                        sleep(2)
                        
                        break
                   
            sleep(6)
            driver.quit() 
            messages.success(request,"Has visitado a"+ str(visited)+"muy bien hecho.")    
        else:
            messages.error(request, "Datos inválidos.")    
    form = VisitedForm
    return render(request, 'layouts/visitar.html',{'visited':form})


def mensajes(request):
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())    
    chrome_options = webdriver.ChromeOptions()

    driver.get('https://www.linkedin.com/home')

    sleep(3)   
    buscalogin = driver.find_element_by_xpath("/html/body/nav/div/a[2]")
    sleep(1)
    email = ""
    password = ""
    emaillotele = driver.find_element_by_xpath("//*[@id='session_key']")
    contraseña = driver.find_element_by_xpath("//*[@id='session_password']")
    emaillotele.send_keys(email)  
    contraseña.send_keys(password)
    sleep(10)
    login = driver.find_element_by_class_name("sign-in-form__submit-button")
    login.click() 
    sleep(3)



    names = [']
    ctr = 0

    for name in names:

        # search for the name
        driver.find_element_by_xpath("//input[@type = 'text']").send_keys(name)

        driver.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.RETURN)

        sleep(3)


        driver.find_element_by_xpath("//button[text() = 'Message']").click()


        message = 'Hola estoy buscando trabajo como junior en python,js.'

        sleep(1)


        if ctr == 0:
            driver.find_element_by_xpath("//div[@role = 'textbox']").send_keys(message)
        else:
            driver.find_elements_by_xpath("//div[@role = 'textbox']")[ctr].send_keys(message)

        sleep(1)    

        if ctr == 0:
            driver.find_element_by_xpath("//button[@type = 'submit']").click()
        else:
            driver.find_elements_by_xpath("//button[@type = 'submit']")[ctr].click()

        ctr = ctr + 1

        sleep(1)   

        driver.find_element_by_xpath("//input[@type = 'text']").clear()"""
    return render(request, 'layouts/mensajes.html')
