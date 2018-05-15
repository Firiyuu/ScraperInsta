from urllib.parse import quote
from urllib.request import urlopen
import urllib.request
from io import StringIO
import json
import os
from pandas.io.common import EmptyDataError
import datetime
import sched, time
import csv


from csvhandler import writeToCsv, writeToCsv1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options, DesiredCapabilities
import re
import schedule
from os import listdir
from os.path import isfile, join
from feedhandler import writeToCsv, analyzeCsvFeed



# def monitor():


def getfollowers(browser):
        today = date.today()
        today.strftime('%m%d%y')
        running = True
        while running:
           try:
             
              url = 'https://www.instagram.com/heromotorsports/followers/'
              browser.get(url)

              # delay = 3 seconds you can edit delay here just in case your internet speed is down.
              # time.sleep(delay)
              
              #GETTING FOLLOWERS

              if browser.find_elements_by_xpath("//div[@class='_9mmn5']"):

                   followers = browser.find_elements_by_xpath("//div[@id='_9mmn5']")
                   followers_username = browser.find_elements_by_xpath("//div[@class='_2nunc']/a")
                   print(followers)

                   file_name ='followers' + str(today) + '.csv'

                   for follower, user in zip(followers, followers_username):
                        fields = (str(follower.get_attribute("innerText")) + ',' + str(user.get_attribute("innerText")))
                        writeToCsv(fields, file_name)
             



           except NoSuchElementException as e:
           	      print(e)
                  # new = ALL_PROXIES.pop()
                  # pd = proxy_driver(ALL_PROXIES)
                  # print("--- Switched proxy to: %s" % new)
                  # time.sleep(1)

           except TimeoutException:
                  print("Loading took too much time!")

           except Exception as e:
                  print(e)

           # except:
           #     new = ALL_PROXIES.pop()
           #     pd = proxy_driver(ALL_PROXIES)
           #     print("--- Switched proxy to: %s" % new)
           #     time.sleep(1)  

def scraper(browser):
        today = date.today()
        today.strftime('%m%d%y')

        running = True
        while running:
           try:
             
              url = 'https://www.instagram.com/heromotorsports/followers/'
              browser.get(url)

              # delay = 3 seconds you can edit delay here just in case your internet speed is down.
              # time.sleep(delay)
              
              #GETTING FOLLOWERS

              if browser.find_elements_by_xpath("//div[@class='_9mmn5']"):

                   followers = browser.find_elements_by_xpath("//div[@id='_9mmn5']")
                   followers_username = browser.find_elements_by_xpath("//div[@class='_2nunc']/a")
                   print(followers)

                   file_name ='followers' + str(today) + '.csv'

                   for follower, user in zip(followers, followers_username):
                       fields = (str(follower.get_attribute("innerText")) + ',' + str(user.get_attribute("innerText")))
                       writeToCsv(fields, file_name)
              analyzeCsvFeed()



           except NoSuchElementException as e:
               print(e)
               # new = ALL_PROXIES.pop()
               # pd = proxy_driver(ALL_PROXIES)
               # print("--- Switched proxy to: %s" % new)
               # time.sleep(1)

           except TimeoutException:
               print("Loading took too much time!")

           except Exception as e:
               print(e)

           # except:
           #     new = ALL_PROXIES.pop()
           #     pd = proxy_driver(ALL_PROXIES)
           #     print("--- Switched proxy to: %s" % new)
           #     time.sleep(1)                        


#UNFINISHED--------------------------------------------------------------------------------------------------------

def getPower(tags, browser):
    for tag in tags:
       browser.get('https://www.instagram.com/explore/tags/'+ str(tag) +'/')
       try:
         
          url = 'https://www.instagram.com/heromotorsports/'
          browser.get(url)

          # delay = 3 seconds you can edit delay here just in case your internet speed is down.
          # time.sleep(delay)
          
          #GETTING FOLLOWERS

          if browser.find_element_by_xpath("//span[@class='_fd86t ']"):

               power = browser.find_element_by_xpath("//span[@class='_fd86t ']").get_attribute('innerText')

               print(power)

               file_name ='tags' + str(today) + '.csv'
               writeToCsv(power,file_name)
          else:
               print('Not Found!')


                   
        



       except NoSuchElementException as e:
           print(e)
           # new = ALL_PROXIES.pop()
           # pd = proxy_driver(ALL_PROXIES)
           # print("--- Switched proxy to: %s" % new)
           # time.sleep(1)

       except TimeoutException:
           print("Loading took too much time!")

       except Exception as e:
           print(e)
 




def gethashpower(browser):
        today = date.today()
        today.strftime('%m%d%y')
        running = True
        while running:
           try:
             
              url = 'https://www.instagram.com/heromotorsports/'
              browser.get(url)

              # delay = 3 seconds you can edit delay here just in case your internet speed is down.
              # time.sleep(delay)
              
              #GETTING FOLLOWERS

              if browser.find_elements_by_xpath("//div[@class='_2di5p']"):

                   tag_elements = browser.find_elements_by_xpath("//div[@id='_2di5p']")

                   print(tag_elements)

                  

                   for tag in tag_elements:
                       s = tag.get_attribute('alt')
                       tags = re.compile(r"#(\w+)")
                       tags = tag.findall(s)
                       getPower(tags, browser)



                       
            



           except NoSuchElementException as e:
               print(e)
               # new = ALL_PROXIES.pop()
               # pd = proxy_driver(ALL_PROXIES)
               # print("--- Switched proxy to: %s" % new)
               # time.sleep(1)

           except TimeoutException:
               print("Loading took too much time!")

           except Exception as e:
               print(e)

           # except:
           #     new = ALL_PROXIES.pop()
           #     pd = proxy_driver(ALL_PROXIES)
           #     print("--- Switched proxy to: %s" % new)
           #     time.sleep(1) 




# def get_proxies(co=co):
#     driver = webdriver.Firefox(firefox_options=co)
#     driver.get("https://free-proxy-list.net/")

#     PROXIES = []
#     proxies = driver.find_elements_by_css_selector("tr[role='row']")
#     for p in proxies:
#         result = p.text.split(" ")

#         if result[-1] == "yes":
#             PROXIES.append(result[0]+":"+result[1])

#     driver.close()
#     return PROXIES


# ALL_PROXIES = get_proxies()


# def proxy_driver(PROXIES, co=co):
#     prox = Proxy()

#     if PROXIES:
#         pxy = PROXIES[-1]
#     else:
#         print("--- Proxies used up (%s)" % len(PROXIES))
#         PROXIES = get_proxies()

#     prox.proxy_type = ProxyType.MANUAL
#     prox.http_proxy = pxy
#     prox.socks_proxy = pxy
#     prox.ssl_proxy = pxy

#     capabilities = webdriver.DesiredCapabilities.FIREFOX
#     prox.add_to_capabilities(capabilities)

#     driver = webdriver.Firefox(firefox_options=co, desired_capabilities=capabilities)

#     return driver



#RUN

browser = webdriver.Firefox(executable_path="\selenium\webdriver\geckodriver.exe") #CONFIGURE PATH TO DRIVER
print("Firefox Browser Invoked")

#LOG-IN SESSION
print("I will start scraping!")
login_url = 'https://www.instagram.com/'
browser.get(login_url)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

#INSERT CREDENTIALS HERE
username.send_keys('') 
password.send_keys('') 
#INSERT CREDENTIALS HERE----


login_attempt = browser.find_element_by_name("_qv64e")
login_attempt.click()
print("Wait 10 Secs for a successful login")
time.sleep(10)
print("Login Succesful")


while True:
    choice = input("What do you want to do?\n\n1 - Get Instagram Follower Count\n2 - Track Instagram Followers\n3 - Get Hashtags Power")
    if(choice == '1'):
        getfollowers(browser)
    elif(choice == '2'):
        scraper(browser)
    elif(choice == '3'):
        gethashpower(browser)
    else:
        print("Invalid Key!")