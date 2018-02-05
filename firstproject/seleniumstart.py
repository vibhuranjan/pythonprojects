from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Firefox()
driver.get("http://upresults.nic.in/")
highSchoolResult = driver.find_element_by_partial_link_text('High School')
highSchoolResult.click()
rollNumber = driver.find_element_by_name('regno')
rollNumber.send_keys('0513554')
submitButton = driver.find_element_by_name('B1')
submitButton.click()
result_file = open('C:\\fuNke\\code\\python\\pythonprojects\\result.txt','w')
result_file.write((' ' * 20))
result_file.write('High School Result')
result_file.write('\n' * 4)
# this will write roll number name and other info
for row in range(2):
    for td_count in range(4):
        first_table = driver.find_element_by_xpath("//table[2]//tbody//tr[%d]//td[%d]" % (row+1, td_count+1))
        print(first_table.text)
        result_file.write(first_table.text)
        result_file.write(' ' * 4)
    result_file.write('\n')
result_file.write('\n' * 2)
for row in range(4,9):
    for td_count in range(6):
        second_table_first_row = driver.find_element_by_xpath("//table[3]//tbody//tr[%d]//td[%d]" % (row, td_count+1))
        print(second_table_first_row.text)
        result_file.write(second_table_first_row.text)
        result_file.write(' ' * 2)
    result_file.write('\n')
result_file.close()
print("Success")
driver.close()