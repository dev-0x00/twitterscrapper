from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time, zipfile

class Config:
        
    def __init__(self):
        pass

    def ChromeSetUp(self, use_proxy=False, user_agent=None):
        chromeOptions = Options()
        if use_proxy:
            pluginFile = "proxyAuthPlugin.zip"

            with zipfile.ZipFile(pluginFile, "w") as zipFile:
                zipFile.writestr("manifest.json", self.manifest_json)
                zipFile.writestr("background.js", self.background_js)

        if user_agent:
            chromeOptions.add_argument("--user-agent=%s" % user_agent)
        option = Options()
        #option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        service = Service(ChromeDriverManager().install())
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        #option.add_argument("--headless")
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-extensions")
        option.add_argument("--disable-setuid-sandbox")
        option.add_argument("--remote-debugging-port=9222")
        option.add_argument("--disable-gpu")
        option.add_argument("--start-maximized")
        option.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=service, options=option)
        time.sleep(10)
        return driver

if __name__ == "__main__":
    gleam = Config()
    gleam.ChromeSetUp(use_proxy=False, user_agent=None)
        
