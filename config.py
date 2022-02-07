from selenium.webdriver.chrome.options import Options

class driver_config:
    driver_path = '/usr/bin/chromedriver' # add chrome driver path here
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless')
    options.add_argument('--incognito')

class js_code:
    js_script_path = 'load.js'
    js_script = open(js_script_path).read()
