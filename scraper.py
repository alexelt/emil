from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from initialization import initialize
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from initialization import actions
from bs4 import BeautifulSoup
import time


def stuff(driver):
    try:

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableau_base_widget_SearchWidget_0"]/div/textarea'))
        )
        element.click()
        txt = 'ALI'
        element.send_keys(txt)
        element.send_keys(Keys.ENTER)
        time.sleep(10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        search_results = soup.find('div', {'class': 'SearchResults'})
        names = search_results.find_all('a', {'class': 'FIText'})
        for name in names:
            nm = name.text
            print(nm)
    except:
        pass


if __name__ == '__main__':
    dr = initialize()
    action = actions()
    url = 'https://public.tableau.com/views/SamtligenavneiVollsmoseSogn/SamtligenavneiVollsmoseSogn?%3Aembed=y&%3AshowTabs=y&%3Adisplay_count=yes&%3AshowVizHome=no&fbclid=IwAR1s_2TuD0hpEczKIJhmSZKz3JI2vTA1fc5hBFZaSOT8Tc1G9kFtMzA7v88'
    dr.get(url)
    stuff(dr)
    dr.quit()

