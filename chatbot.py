import sys
import os
from gtts import gTTS 
import webbrowser
import time
from weather import Weather, Unit
import requests 
from bs4 import BeautifulSoup
from googlesearch import search
language='en'
class Test:
    def __init__(self,s):
        os.startfile(r'C:\Users\Jayanthi\Desktop\python programs\%s'%s)
        #del self
def menu():
    print(" 1.Search \n 2.Go to youtube \n 3.Calculate \n 4.Weather \n 5.Exit")
    print("Please enter your choice:")
    ch=int(input())
    if(ch==1):
        webbrowser.open('http://google.com')  # Go to example.com
    elif(ch==2):
        webbrowser.open('http://youtube.com')
    elif(ch==3):
        calc()
    elif(ch==4):
        str10="please enter your city:"
        myobj10 = gTTS(text=str10, lang=language, slow=False) 
        myobj10.save("welcome10.mp3")
        t10=Test("welcome10.mp3")
        city=input("please enter your city:")
        weather(city)
    elif(ch==5):
        print("Bye!")
        print("EXIT")
        exit()
def calc():
    str176="Here you are!!!"
    myobj23 = gTTS(text=str176, lang=language, slow=False) 
    myobj23.save("welcome23.mp3")
    t19=Test("welcome23.mp3")
    print("Here you are!!!")
    adv()
def adv():
    os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Calculator')
            
def weather(str):
    """weather = Weather(unit=Unit.CELSIUS)

    lookup = weather.lookup(600083)
    condition = lookup.condition
    print(condition.text)"""
    #language='en'
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(str)
    condition = location.condition
    myobj11 = gTTS(text=condition.text, lang=language, slow=False)
    filename="welcome11.mp3"
    myobj11.save(filename)
    t11=Test(filename)
    print(condition.text)
    print("weather forecasts for the upcoming days:")
    forecasts = location.forecast
    for forecast in forecasts:
        print("weather:",end=" ")
        print(forecast.text)
        print("Date:",end=" ")
        print(forecast.date)
        print("Max.temp",end=" ")
        print(forecast.high)
        print("Min.temp",end=" ")
        print(forecast.low)
        print()
def get_video_links(): 
        archive_url = "https://www.youtube.com/watch?v=xsbLtHql4g8"
        # create response object 
        r = requests.get(archive_url) 
        
        # create beautiful-soup object 
        soup = BeautifulSoup(r.content,'html5lib') 
        
        # find all links on web-page 
        links = soup.findAll('a') 

        # filter the link sending with .mp4 
        video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')] 
        print(video_links)
        #return video_links
        return archive_url


def download_video_series(videolinks): 

    for link in videolinks: 
                archive_url = "https://www.youtube.com/watch?v=xsbLtHql4g8"
                '''iterate through all links in video_links 
                and download them one by one'''
                
                # obtain filename by splitting url and getting 
                # last string 
                file_name = link.split('/')[-1] 

                print("Downloading file:%s"%file_name)
                
                # create response object 
                r = requests.get(link, stream = True) 
                
                # download started 
                with open(file_name, 'wb') as f: 
                        for chunk in r.iter_content(chunk_size = 1024*1024): 
                                if chunk: 
                                        f.write(chunk) 
                
                print("%s downloaded!\n"%file_name)

    print("All videos downloaded!")
    return
a=[]
str1="Type to say something..."
myobj1 = gTTS(text=str1, lang=language, slow=False) 
myobj1.save("welcome1.mp3")
t1=Test("welcome1.mp3")
print("Type to say something...")
while True:
    print("-->",end=" ")
    chat=input()
    if("hi" in chat or "hello" in chat):
        str4="Hello"
        myobj2 = gTTS(text=str4, lang=language, slow=False) 
        myobj2.save("welcome4.mp3")
        t4=Test("welcome4.mp3")
        print("Hello!")
    elif("help" in chat):
        str2="Yes!"
        str3="Here are some of the things that I can do for you!"
        #1
        myobj3 = gTTS(text=str2, lang=language, slow=False) 
        myobj3.save("welcome2.mp3") 
        t2=Test("welcome2.mp3")
        #2
        myobj4 = gTTS(text=str3, lang=language, slow=False) 
        myobj4.save("welcome3.mp3")
        t3=Test("welcome3.mp3")
        print("Yes!")
        print("Here are some of the things that I can do for you!")
        menu()
    elif('nice' in chat or 'cool' in chat or 'thanks' in chat or 'thank you' in chat):
        str5="You are welcome!"
        myobj5 = gTTS(text=str5, lang=language, slow=False) 
        myobj5.save("welcome5.mp3")
        t3=Test("welcome5.mp3")
        print("You are welcome!")
    elif('boredom' in chat or 'bored' in chat or 'facts' in chat):
        str6="Reading facts is one of the ways for kicking out boredom! Here they are! Go for it!"
        myobj6 = gTTS(text=str6, lang=language, slow=False) 
        myobj6.save("welcome90.mp3")
        t89=Test("welcome90.mp3")
        time.sleep(6)
        print("Reading facts is one of the ways for kicking out boredom!")
        print("\n Here they are! Go for it!")
        str8="LOADING..."
        myobj8 = gTTS(text=str8, lang=language, slow=False) 
        myobj8.save("welcome8.mp3")
        t91=Test("welcome8.mp3")
        print("LOADING...",end=" ")
        time.sleep(2)
        print("...")
        time.sleep(5)
        webbrowser.open('http://scoopwhoop.com/30-Amazing-Facts-From-Around-The-World-That-You-Wont-Believe-Are-True/#.m93entpyj')
    elif('bye' in chat or 'exit' in chat or 'close' in chat or 'later' in chat):
        str20="Bye! See you later!"
        myobj20 = gTTS(text=str20, lang=language, slow=False) 
        myobj20.save("welcome90.mp3")
        t100=Test("welcome90.mp3")
        print("Bye! See you later!")
        break
    elif('weather' in chat):
        str9="please enter your city:"
        myobj9 = gTTS(text=str9, lang=language, slow=False) 
        myobj9.save("welcome9.mp3")
        t3=Test("welcome9.mp3")
        city=input("please enter your city:")
        weather(city)
    elif('kill' in chat):
        str120="Do not be so Brutal!!!"
        myobj22 = gTTS(text=str120, lang=language, slow=False) 
        myobj22.save("welcome9.mp3")
        t45=Test("welcome9.mp3")
        print("Do not be so Brutal!!!")
    elif('music' in chat):
        archive_url = "https://www.youtube.com/watch?v=xsbLtHql4g8"
        video_links = get_video_links() 
        download_video_series(video_links)
    elif(chat=='speak'):
        print('type stop for stopping the speech')
        inp=input()
        myobj45= gTTS(text=inp, lang=language, slow=False)
        myobj45.save("welcome56.mp3")
        t45=Test("welcome56.mp3")
        chat = 'speak'
    elif(chat=='stop'):
        break
        
    else:
        
        query = chat
        tt=search(query, tld="co.in", num=10, stop=1, pause=2)
        for k in tt:
            a.append(k)
        if(a==[]):
            str25="I am not able to understand what you are saying!"
            myobj68= gTTS(text=str25, lang=language, slow=False)
            myobj68.save("welcome34.mp3")
            t38=Test("welcome34.mp3")
            print("I am not able to understand what you are saying!")
        else:    
            str23="Here is what I got!"
            myobj67= gTTS(text=str23, lang=language, slow=False)
            myobj67.save("welcome34.mp3")
            t34=Test("welcome34.mp3")
            print("Here is what I got!")
            tt=search(query, tld="co.in", num=10, stop=1, pause=2)
            
            for j in tt: 
                print(j)
        
sys.exit()    
        
