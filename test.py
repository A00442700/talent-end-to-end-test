from selenium import webdriver
import time
import random
from base64 import b64encode

def findCount():
    text_count = driver.find_elements_by_xpath("//*[contains(text(), 'Todo Count')]")
    for i in text_count:
        TotalCount = i.text.split(":")[1]
    return TotalCount

def actualCount():
    ToDo_count = driver.find_elements_by_css_selector('[class="table table-striped"]>tbody>tr')
    TotalCount = len(ToDo_count)
    return TotalCount

driver = webdriver.Chrome()
driver.get("http://localhost")
time.sleep(5)
EnterTask = driver.find_element_by_css_selector("input[placeholder='Enter task..']")
Add_ToDo = driver.find_element_by_xpath("//*[contains(text(), 'Add Todo')]")
EnterTask.send_keys("one")
Add_ToDo.click()
time.sleep(2)
Edit = driver.find_elements_by_css_selector('[class="btn btn-primary btn-sm"]')
Delete = driver.find_elements_by_css_selector('[class="btn btn-danger btn-sm"]')
Edit[0].click()
EnterTask.clear()
EnterTask.send_keys("Edited")
Edit_ToDo = driver.find_element_by_xpath("//*[contains(text(), 'Edit Todo')]")
Edit_ToDo.click()
time.sleep(2)

count = int(findCount())

i=0
while i < count:    
    Delete[i].click()
    time.sleep(2)
    count = int(findCount())

for i in range(5):
    EnterTask.send_keys(i)
    Add_ToDo.click()
    time.sleep(2)
    
Delete = driver.find_elements_by_css_selector('[class="btn btn-danger btn-sm"]')
Delete[0].click()
time.sleep(2)

count = int(findCount())
actual_count = int(actualCount())

if count == actual_count:
    print(" Total count  is ", count)

