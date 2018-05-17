from urllib.parse import quote
from urllib.request import urlopen
import urllib.request
from io import StringIO
import json
import os
from pandas.io.common import EmptyDataError
from datetime import date, timedelta
import sched, time
import csv



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
from feedhandler import writeToCsv, analyzeCsvFeed, GetUnfollowersNames






def getfollowers(browser):

          print('FLAG1')
          today = date.today()
          today.strftime('%m%d%y')
          url = 'https://www.instagram.com/heromotorsports/'
          browser.get(url)
          time.sleep(5)

          
          browser.find_element_by_xpath("//a[@href='/heromotorsports/followers/']").click()
          time.sleep(5)
             


          # delay = 3 seconds you can edit delay here just in case your internet speed is down.
          # time.sleep(delay)
          
          #GETTING FOLLOWERS
          print('FLAG2')
          # follower_list = []
          # follower_user_list = []
          # number_of_followers = int((browser.find_element_by_xpath("(//span[@class='_fd86t '])[2]").text).replace(",",""))
          # followers_panel = browser.find_element_by_xpath("//div[@class='_o0j5z']/div")
          # print(number_of_followers)



          dialog = browser.find_element_by_xpath("//div[@class='_o0j5z']/div")
          #find number of followers
          allfoll= int((browser.find_element_by_xpath("(//span[@class='_fd86t '])[2]").text).replace(",",""))
          #scroll down the page
          follow_list_1 = []
          follow_list_2 = []


          #scroll down the page
          for i in range(int(allfoll/2)):
              browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
              followers_elems = browser.find_elements_by_xpath("(//div[@class='_eryrc']/div)")
              print(followers_elems)
              follow_list_1.append(followers_elems)
              follower_username = browser.find_elements_by_xpath("(//div[@class='_2nunc'])")
              print(follower_username)
              follow_list_2.append(followers_elems)

           
              print("Extract friends %",round((i/(allfoll/2)*100),2),"from","%100")

          # followers_elems = browser.find_elements_by_xpath("(//div[@class='_eryrc']/div)")

          # follower_username = browser.find_elements_by_xpath("//div[@class='_2nunc']")

          follower = [e[0].text for e in follow_list_1]
          username = [e[0].text for e in follow_list_2]

          for f,i in zip(follower,username):
              fields = (str(f) + ',' + str(i))
              print('FLAG4')
              file_name ='followers' + str(today) + '.csv'

              writeToCsv(fields, file_name)


          # print('FLAG3')

          # followers = browser.find_elements_by_xpath("//div[@class='_eryrc']/div")
          # followers_username = browser.find_elements_by_xpath("//div[@class='_2nunc']/a")
          # print(followers)
          # print(followers_username)

          # file_name ='followers' + str(today) + '.csv'

          # print('FLAG3')
          # print(file_name)



          # for follower in followers:
          #     follower_list.append(str(follower.text))

          # for user in followers_username:
          #     follower_user_list.append(str(user.get_attribute("title")))



               




def scraper(browser):
           today = date.today()
           today.strftime('%m%d%y')


           try:
             
              url = 'https://www.instagram.com/heromotorsports/'
              browser.get(url)
              time.sleep(5)

              
              browser.find_element_by_xpath("//a[@href='/heromotorsports/followers/']").click()
              time.sleep(5)

              # delay = 3 seconds you can edit delay here just in case your internet speed is down.
              # time.sleep(delay)
              
              #GETTING FOLLOWERS

          

              followers = browser.find_elements_by_xpath("//div[@id='_9mmn5']")
              followers_username = browser.find_elements_by_xpath("//div[@class='_2g7d5 notranslate _o5iw8 ']/a")
              print(followers)

              file_name ='followers' + str(today) + '.csv'

              for follower, user in zip(followers, followers_username):
                       fields = (str(follower.get_attribute("innerText")) + ',' + str(user.get_attribute("innerText")))
                       writeToCsv(fields, file_name)
              analyzeCsvFeed()



           except NoSuchElementException as e:
               print(e)


           except TimeoutException:
               print("Loading took too much time!")

           except Exception as e:
               print(e)

                   


#UNFINISHED--------------------------------------------------------------------------------------------------------

def getPower(tags,browser):
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

#     prox.proxy_type = ProxyType.MANUALwaht second optionwahtwwwfs
#     prox.http_proxy = pxy
#     prox.socks_proxy = pxy
#     prox.ssl_proxy = pxy

#     capabilities = webdriver.DesiredCapabilities.FIREFOX
#     prox.add_to_capabilities(capabilities)

#     driver = webdriver.Firefox(firefox_options=co, desired_capabilities=capabilities)

#     return driver




browser = webdriver.Firefox(executable_path="C:\Python36\ASIN\ASINENV\selenium\webdriver\geckodriver.exe") #CONFIGURE PATH TO DRIVER
print("Firefox Browser Invoked")

#LOG-IN SESSION
print("I will start scraping!")
login_url = 'https://www.instagram.com/'
browser.get(login_url)
time.sleep(10)

browser.find_element_by_xpath("//a[@href='/accounts/login/']").click()
time.sleep(10)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

#INSERT CREDENTIALS HERE
username.send_keys('jedharhart@gmail.com') 
password.send_keys('Firiyuu77')
#INSERT CREDENTIALS HERE----


login_attempt = browser.find_element_by_xpath("//button[@class='_qv64e       _gexxb _4tgw8     _njrw0   ']")
login_attempt.click()
print("Wait 10 Secs for a successful login")
time.sleep(10)
print("Login Succesful")



choice = input("What do you want to do?\n\n1 - Get Instagram Follower Count\n2 - Track Instagram Followers\n3 - Get Hashtags Power")
if(choice == '1'):
    getfollowers(browser)
elif(choice == '2'):
    scraper(browser)
elif(choice == '3'):
    gethashpower(browser)
else:
    print("Invalid Key!")