from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome('Project/Project-141/chromedriver.exe')
print(browser)
browser.get(start_url)
time.sleep(10)
planet_data=[]
def scrap():
    for i in range(0,1):
        print(f'Scrapping page {i+1}...')
        soup=BeautifulSoup(browser.page_source,"html.parser")
        print(soup)
        for ul_tag in soup.find_all("ul",attrs={"class","Brightest star"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li in enumerate(li_tags):
                print(index)
                if index==0:
                    temp_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            browser.find_element(by=By.XPATH,value='//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a')
scrap()
headers=["Name","Distance","Mass","Radius"]
planet_dataframe1=pd.DataFrame(planet_data,columns=headers)
planet_dataframe1.to_csv("bightestStar.csv",index=True,index_label="id")