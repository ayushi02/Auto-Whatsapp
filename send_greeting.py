from selenium import webdriver
from time import sleep
import filter_contacts


wishingContacts = filter_contacts.filter_contacts("google.csv")
driver = webdriver.Chrome("C:\Users\DELL LAPI\Desktop\Personalised-Greetings-master\chromedriver")
driver.get('https://web.whatsapp.com')
sleep(15)
contacts = dict()

for key, value in wishingContacts.items():
    pre_msg = "Good Morning "
    post_msg = "!! How are you?"
    input_box = driver.find_element_by_css_selector("input[type='text']")
    input_box.click()
    input_box.send_keys(key)
    sleep(1)
    userbox = driver.find_element_by_css_selector("span[title='"+key+"']")
    userbox.click()
    inputbox = driver.find_element_by_css_selector("div[data-tab='1']")

    inputbox.click()
    inputbox.send_keys(pre_msg+value+post_msg)
    send_button = driver.find_element_by_css_selector("span[data-icon='send']")
    send_button.click()
    sleep(1)
