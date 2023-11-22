import time
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from time import sleep


@pytest.mark.booking_2
def test_booking_2():
    driver1 = webdriver.Chrome()
    driver1.get("https://ddasports.com/app/")

    # --------------------------------------------------------------------------------------------------------------

    # Variables
    username = "M0967"
    password = "M0967"
    waitTime = 60
    bookingDate = "26-08-2023"
    # 0 = 06:00 - 06:40
    # 1 = 06:40 - 07:20
    # 2 = 07:20 - 08:00
    # 3 = 08:00 - 08:40
    # 4 = 08:40 - 09:20
    # 5 = 09:20 - 10:00
    # 6 = 10:00 - 10:40
    # 7 = 10:40 - 11:20
    # 8 = 11:20 - 12:00
    courtTiming: str = "MainContent_grdGameSlot_ddlCourtTable_5"
    courtTimingSelect: str = "MainContent_grdGameSlot_lnkEdit_5"
    courtNumber: str = "2"
    waitTimeBetweenEvents = 2
    # Enter UserName
    email_input = driver1.find_element("name", "txtUserName")
    email_input.send_keys(username)

    # Enter Password
    pass_input = driver1.find_element("name", "txtPassword")
    pass_input.send_keys(password)

    user_type = driver1.find_element("name", "ddlUserType")
    user_type.send_keys("LM")

    complex_type = driver1.find_element("name", "ddlCompName")
    complex_type.send_keys("SBS")

    # Select Wait Time
    time.sleep(waitTime)

    driver1.find_element("name", "btnLogin").click()

    driver1.get("https://ddasports.com/app/Booking")

    booking_date1 = driver1.find_element("id", "MainContent_txtBookingDate")
    booking_date1.clear()

    # Select Booking Date
    booking_date1.send_keys(bookingDate)
    booking_date1.submit()

    time.sleep(waitTimeBetweenEvents)

    game_category1 = driver1.find_element("id", "MainContent_ddlGames")
    driver1.execute_script(
        "showDropdown = function (element) {var event; event = document.createEvent('MouseEvents'); event.initMouse"
        "Event('mousedown', true, true, window); element.dispatchEvent(event); }; showDropdown(arguments[0]);",
        game_category1)
    driver1.find_element("xpath", "//select[@id='MainContent_ddlGames']/option[text()='Badminton']").click()

    # now you dropdown will be open
    # this will click the option which text is custom and onchange event will be triggered.

    sub_game_category1 = driver1.find_element("id", "MainContent_ddlGameCategory")
    driver1.execute_script(
        "showDropdown = function (element) {var event; event = document.createEvent('MouseEvents'); event.initMouse"
        "Event('mousedown', true, true, window); element.dispatchEvent(event); }; showDropdown(arguments[0]);",
        sub_game_category1)

    driver1.find_element("xpath",
                         "//select[@id='MainContent_ddlGameCategory']/option[text()='Indoor']").click()

    time.sleep(waitTimeBetweenEvents)

    driver1.find_element("id", "MainContent_btnSearch").click()

    time.sleep(waitTimeBetweenEvents)
    A = 1
    while A == 1:
        try:
            # Select Time
            if driver1.find_element("id", courtTiming):
                driver1.find_element("id", "MainContent_btnSearch").click()
                print("Element Exist")
                time.sleep(waitTimeBetweenEvents)
                A = 2
        except NoSuchElementException:
            driver1.find_element("id", "MainContent_btnSearch").click()
            time.sleep(waitTimeBetweenEvents)
            A = 1

    # Select Time
    select_court1 = driver1.find_element("id", courtTiming)

    # Enter Court Number
    select_court1.send_keys(courtNumber)

    # Select Time
    driver1.find_element("id", courtTimingSelect).click()

    # --------------------------------------------------------------------------------------------------------------

    src1 = driver1.find_element("id", "MainContent_imgCaptchaImage").get_attribute("src")

    a = src1.split("=")
    time.sleep(waitTimeBetweenEvents)
    driver1.find_element("id", "MainContent_txtCpCode").send_keys(a[1])

    time.sleep(waitTimeBetweenEvents)

    driver1.find_element("id", "MainContent_btnSave").click()

    driver1.switch_to.alert.accept()

    time.sleep(1000)
