from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import xlwt,xlsxwriter

driver = webdriver.Firefox()
driver.get("http://upresults.nic.in/")
highSchoolResult = driver.find_element_by_partial_link_text('High School')
highSchoolResult.click()
rollNumber = driver.find_element_by_name('regno')
rollNumber.send_keys('0513554')
submitButton = driver.find_element_by_name('B1')
submitButton.click()

result_excel_file = xlwt.Workbook(encoding="utf-8")
sheet = result_excel_file.add_sheet('Sheet 1')
row_number = 0
col_number = 0
# this will write roll number name and other info
for row in range(2):
    for td_count in range(1,5):
        first_table = driver.find_element_by_xpath("//table[2]//tbody//tr[%d]//td[%d]" % (row+1, td_count))
        sheet.write(row_number, col_number, first_table.text)
        if td_count %2 == 1:
            col_number += 1
        else:
            row_number += 1
        
for row in range(4,9):
    for td_count in range(6):
        second_table_first_row = driver.find_element_by_xpath("//table[3]//tbody//tr[%d]//td[%d]" % (row, td_count+1))
        print(second_table_first_row.text)

result_excel_file.save('Result_Excel.xls')
print("Success")
driver.close()