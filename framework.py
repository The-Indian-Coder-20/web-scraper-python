from userinput import sitesList
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

class NewsScraper:
    def __init__(self, site):
        self.site = site
        self.headlineElementList = []
        self.headlineList = []
        self.finalText = ""

    def initializeSite(self):
        driver.get(self.site)

    def headlinesScraper(self):
        driver.implicitly_wait(20)
        self.headlineElementList = driver.find_elements(By.XPATH, "//*[@data-testid='card-headline']")
        for headline in self.headlineElementList:
            if headline.text != "":
                self.headlineList.append(headline.text)

    def headlineSeparator(self):
        for i in self.headlineList:
            self.finalText += f"\n- {i}"

    def __str__(self):
        return f"Here are the headlines for today: \n{self.finalText}"

