# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:21:40 2020

@author: fmarc
"""

## 1. Todas as importações 
from selenium import webdriver 
from time import sleep

## 2. Todos os parametros 
url = 'https://www.linkedin.com/jobs/search?keywords=Cientista%20De%20Dados&location=Curitiba%2C%20Paran%C3%A1%2C%20Brasil&geoId=103501557&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0' 


## 3. Execucao do codigo 
if __name__ == '__main__':
# Criar uma instancia do Google Chrome pelo Selenium     
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
# acessar url do linkedin
    driver.get(url)

#Iniciar while loop em cima de todos os resultados
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricao = []
    
#Iniciar while loop em cima de todos os resultados 
    while True:
        # for loop para coletar descricoes de dados
        for r in resultados[len(lista_descricao):]:
            r.click() # Clicar na descricao 
            sleep(1)
            try:
                # pegar elemento com a descricao 
                descricao = driver.find_element_by_class_name('description')
                # anexar o texto na lista
                lista_descricao.append(descricao.text)
            except:
                print('Erro')
                pass
        
        resultados = driver.find_elements_by_class_name('result-card')
    
    # Critério de saída do While
        if len(lista_descricao) == len(resultados):
            break
    
    #salvar descricoes de vagas
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt', 'w') as f:
        f.write(descricao_salvar)
        
    #fechar o google
    driver.quit()
    