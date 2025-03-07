from framework import NewsScraper
from userinput import sitesList

for i in sitesList:
    tempSite = NewsScraper(i)
    tempSite.initializeSite()
    tempSite.headlinesScraper()
    tempSite.headlineSeparator()
    print(tempSite)