from configs import Config

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import NoSuchElementException

import time

class  Scrapper:

    def __init__(self) -> None:
        pass

    def Scrap(self):
        config = Config()
        driver = config.ChromeSetUp()
        fileData = open("urls.csv")
        lines = fileData.readlines()
        finalData = []
        for line in lines:
            user = line.split(",")[0]
            link = line.split(",")[1]
            driver.get(link)
            time.sleep(5)
            try:
                userName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div/span[1]/span[1]").get_attribute("innerHTML")
            except NoSuchElementException:
                userName = "None"
            try:
                link1 = driver.find_element(By.CLASS_NAME, "css-4rbku5.css-18t94o4.css-901oao.css-16my406.r-1cvl2hr.r-1loqt21.r-4qtqp9.r-poiln3.r-1b7u577.r-bcqeeo.r-qvutc0").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
            except NoSuchElementException:
                link1 = "None"
            try:
                extraLink = driver.find_element(By.CLASS_NAME, "css-4rbku5.css-18t94o4.css-901oao.css-16my406.r-1cvl2hr.r-1loqt21.r-poiln3.r-bcqeeo.r-qvutc0").find_element(By.TAG_NAME, "span").get_attribute("innerHTML")
            except NoSuchElementException:
                extraLink = "None"
            
            finalData.append(f"{user}:{link}:{userName}:{link1 }:{extraLink}")
        print(finalData)
        
        with open("final.csv", "w") as final:
            for data in finalData:
                final.write(data)
                final.write("\n")


if __name__ == "__main__":
    scrap = Scrapper()
    scrap.Scrap()