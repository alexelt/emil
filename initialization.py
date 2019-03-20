from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import json


class actions():

    def scroll_end(self, driver):
        driver.find_element_by_tag_name('body').send_keys(
            Keys.END)  # Scroll with end so that i wont use js after the page has loaded

    def scroll_up(self, driver):
        driver.find_element_by_tag_name('body').send_keys(
            Keys.UP)

    def scroll_down(self, driver):
        driver.find_element_by_tag_name('body').send_keys(
            Keys.PAGE_DOWN)  # Scroll with end so that i wont use js after the page has loaded


def send(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    if response['status']:
        raise Exception(response.get('value'))
    return response.get('value')


def add_script(driver, script):
    send(driver, "Page.addScriptToEvaluateOnNewDocument", {"source": script})  # adding js to the driver so that i can hide that it is a webdriver and that it is in headless mode


def initialize():

    opts = Options()
    # opts.add_argument('headless')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument("--incognito")
    opts.add_argument("--start-maximized")
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
    prefs = {'profile.default_content_setting_values.notifications': 2}
    opts.add_experimental_option('prefs', prefs)

    #xy = proxy
    #opts.add_argument(xy)

    driver = webdriver.Chrome("C:/Users/alexander/PycharmProjects/chromedriver_win32/chromedriver.exe",  chrome_options=opts)

    WebDriver.add_script = add_script
    driver.add_script("Object.defineProperty(navigator, 'webdriver', {get: () => false,});")  # initializing the driver
    driver.add_script("window.chrome = { runtime: {} };")
    driver.add_script(
        "window.navigator.permissions.query = (parameters) => ( parameters.name === 'notifications' ? Promise.resolve({ state: Notification.permission }) : originalQuery(parameters) );")
    driver.add_script("Object.defineProperty(navigator, 'plugins', {  get: () => [1, 2, 3, 4, 5], });")

    return driver
