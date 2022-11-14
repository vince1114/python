from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #keep driver active
options.add_argument("--incognito") #private mode

driver = webdriver.Chrome(options=options)
driver.get('http://google.com')

assert "Google" in driver.title #ensure it is in the page

search_item = input("Please enter valid city or country: ") + " temperature"

search_Elem = driver.find_element(By.NAME,'q')
search_Elem.clear() #clear all the pre-filled, just in case
search_Elem.send_keys(search_item)
search_Elem.send_keys(Keys.RETURN) #keyboard RETURN

assert search_item + " - Google Search" in driver.title

#get the unit from google
celcius_unit = driver.find_element(By.XPATH, "//span[@aria-label='°Celsius']").text
fahrenheit_unit = driver.find_element(By.XPATH, "//span[@aria-label='°Fahrenheit']").text

unit = (str(input("Fahrenheit(F) or Celcius(C): ") or "F")).lower() #Fahrenheit by default

if(unit == "fahrenheit" or unit == "f"):
    unit_button = driver.find_element(By.XPATH, '//span[@aria-label="°Fahrenheit"]')
    output_unit = fahrenheit_unit
elif(unit == "celcius" or unit == "c"):
    unit_button = driver.find_element(By.XPATH, '//span[@aria-label="°Celsius"]')
    output_unit = celcius_unit

unit_button.click() 
degree = driver.find_element(By.XPATH, "//div[@class='vk_bk TylWce SGNhVe']").text


print(f"The current temperature in {search_item} is {degree}{output_unit}")


