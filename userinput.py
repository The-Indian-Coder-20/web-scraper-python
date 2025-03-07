sitesList = []
key = True
while key:
    siteInput = str(input("What news site would you like to scrape (something.com)?: "))
    sitesList.append(siteInput)
    more = input("Continue? [y/n] ")
    if more.lower() == "n":
        key = False

for j in range(len(sitesList)):
    sitesList[j] = "https://" + sitesList[j]