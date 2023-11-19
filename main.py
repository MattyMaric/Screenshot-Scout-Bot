from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
from character_list import characters 
from html2image import Html2Image


hti= Html2Image()

#Asks the user hot many screnshots he wants to look through and save to his computer
NumOfSS = int(input('How many screenshots do you want to save? '))

#Initializes the webdriver and loads the main page.
class SSScout():
    def __init__(self):
        self.browser = webdriver.Chrome()

    def LoadPage(self):
        sleep(2)
        self.browser.get('http://prnt.sc/')
    

    #RSF (Random Screenshot Finder) - Has a counter (num) that is used to enumerate screenshot saves so that there can't be multiple screenshots with the same name, which can cause errors
    #There was no testing done on running the bot twice in a row without getting rid of old screenshots beforehand
    #The bot opens up a random link that is composed from the webpage url with a additional 6 characters chosen at random to find a random screenshot on the page
    #Afterwards the bot saves the image to the folder where the code was run from and adds a +1 to the num counter and the cycle repeats for the amount of times the user has chosen on the start

    def RSF(self):
        num = 0
        for x in range(NumOfSS):
            self.browser.get(str('http://prnt.sc/' + choice(characters) + choice(characters) + choice(characters) + choice(characters) + choice(characters) + choice(characters)))
            pageurl = self.browser.current_url
            print(str(pageurl))
            sleep(2)
            hti.screenshot(url=pageurl, save_as='prntsc' + str(num) + ('.png'))
            num += 1
            
            

    


#Tells the bot which actions to perform and in what order
bot = SSScout()
bot.LoadPage()
bot.RSF()
