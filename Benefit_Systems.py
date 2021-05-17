from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.benefitsystems.pl")

driver.maximize_window()
# O nas - click (full xpath)
driver.find_element_by_xpath("//body[1]/header[1]/nav[1]/div[1]/div[2]/ul[1]/li[5]/a[1]").click()
# Kariera - click (by css selector)
driver.find_element_by_css_selector("#bs-example-navbar-collapse-1 > ul > li.dropdown.open > div > ul > li:nth-child(4) > a").click()
# Oferty Benefit Systems SA - (click by xpath-contains text)
driver.find_element_by_xpath("//a[contains(text(),'Oferty Benefit Systems SA')]").click()
# Select region Mazowieckie
region_select = Select(driver.find_element_by_id("lstAvailableRegions"))
region_select.select_by_visible_text("mazowieckie")
# Input keyword "Tester Oprogramowania" and send keys
driver.find_element_by_xpath("/html/body/section/div/section/div/div[2]/div[1]/div/div[2]/p[1]/input").send_keys("Tester Oprogramowania")
# Press "Szukaj"
driver.find_element_by_xpath("//input[@value='Szukaj']").click()
# Wait 2s and open in new window offer 'Tester Oprogramowania'
import time
time.sleep(2)
driver.find_element_by_xpath("//tr[2]/td").click()
# Verify title site
assert "Oferty pracy" in driver.title
# switch title window "Oferty pracy" to "Praca w Benefit Systems S.A.: Tester Oprogramowania | Warszawa, mazowieckie"
current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)
# Window - Full screen
driver.maximize_window()
# Verify actual title site and text present on a web page
title_second_site = "Praca w Benefit Systems S.A.: Tester Oprogramowania | Warszawa, mazowieckie"
assert title_second_site in driver.title
text = "Brzmi dobrze? Dołącz do nas!"
assert text in driver.page_source
# Wait 2s, print and quit test
time.sleep(2)
print("Koniec Testu!")
driver.quit()

