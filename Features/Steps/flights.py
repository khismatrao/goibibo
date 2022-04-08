import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'user display home page')
def homePage(context):
    context.driver.get(r"https://www.goibibo.com/")
    context.driver.maximize_window()
    time.sleep(4)


@then(u'select trip')
def selectTrip(context):
    #context.driver.findElement(By.CSS_SELECTOR("sc-GEbAx kenSRj")).click()
    context.driver.find_element_by_css_selector(".sc-GEbAx.kenSRj").click()
    time.sleep(4)


@then(u'Enter the source and destination')
def enterSourceDestination(context):
    context.driver.find_element_by_css_selector(".sc-iJKOTD.iipKRx.fswWidgetPlaceholder").click()
    #context.driver.findElement(By.CSS_SELECTOR(".sc-iJKOTD.iipKRx.fswWidgetPlaceholder")).click()
    time.sleep(3)

    context.driver.find_element_by_xpath("//input[@type='text']").send_keys("Mumbai")
    time.sleep(2)

    context.driver.find_element_by_xpath("//div[@class='sc-iAKWXU iyyKqe'][1]").click()
    time.sleep(2)
    context.driver.find_element_by_xpath("//input[@type='text']").send_keys("pune")

    time.sleep(2)


@then(u'select dates')
def selectDates(context):
    context.driver.find_element_by_xpath("//div[@class='sc-iAKWXU iyyKqe'][1]").click()
    time.sleep(3)
    allDates = context.driver.find_elements_by_xpath("//div[@class='DayPicker-Month']//p")

    for element in allDates:

        date = element.text
        print(date)
        if date == "11":
            element.click()
            break

    time.sleep(4)


@then(u'click on search flights button')
def clickFlightsButton(context):
    #context.driver.find_element_by_xpath("//span[@class='sc-fHeRUh jHgPBA']").click()
    context.driver.find_element_by_css_selector(".sc-fHeRUh.jHgPBA").click()
    time.sleep(4)

@then(u'user close browser')
def closeBrowser(context):
    context.driver.close()
