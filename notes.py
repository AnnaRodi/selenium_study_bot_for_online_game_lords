#Back and forward
from selenium import webdriver
driver = webdriver.Firefox()
#Open apress webpage
driver.get('https://apress.com')
#Open Google page
driver.get('https://google.com')
#Go back to previous 'apress' page
driver.back()
print("Moved to first page")
#Go to current page
driver.forward()
print("Moved to second page")
#Page refresh command
driver.refresh()

#XPath with Logical Operators
form_element=driver.find_element_by_xpath("//input[@name='fname' and @type='text']")
form_elements=driver.find_elements_by_xpath("//input[@name='fname'] or [@name='newpassword']")
form_elements=driver.find_elements_by_xpath("//input[@name='fname'] or [@name='lname'] or [@type='email']")
#Types of XPath Functions
#contains()
#//xpath[contains(@attribute, 'attribute value')]
#The following is an example of contains() in complete and partial text.
#//with complete text
#element1 =driver.find_elements_by_xpath("//input[contains(@id, 'fname']")
#//with Partial Link
#element2 =driver.find_elements_by_xpath("//input[contains(@name, 'pass']")
#text()
element3 =driver.find_elements_by_xpath("//button[text() = 'Submit']")

#CSS_selectors
#<p id="apress_press"></p>
#<p id="apress_123"></p>
#<p id="123_apress_press"></p>
#The following shows a CSS selector locating with a substring.
#Using Halt '^' for suffix
press3 =driver.find_element_by_css_selector("p[id^='123']")
#Using Dollar '$' for prefix
press3 =driver.find_element_by_css_selector("p[id$='press']")
#Using Asterisk '*' for all
press3 =driver.find_element_by_css_selector("p[id* ='_apress_']")
#Using Colon ':' for contain method
press3 =driver.find_element_by_css_selector("p:contains('_apress_')")
#<p>Apress</p>
press5 =driver.find_element_by_css_selector("p:contains('Apress')")
#CSS Selector for Multiple Attributes
#<p class ="container" id="apress" style="align-self: center;"></p>
press4 =driver.find_element_by_css_selector("p[class= 'container'] [id='apress'][style='align-self:center']")
