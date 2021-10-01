from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import pyttsx3

driver = webdriver.Chrome('E:\\browser-assistant\\chromedriver')
driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('Hi')
engine.runAndWait()
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
        recognizer.adjust_for_ambient_noise(source)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
        print(response)
    except:
        response = "Error"
    return response

time.sleep(3)
speak("Hello zixer! I am now online..")
gender=1

    #  <-----------------------------------------Check Point--------------------------------------------------------------> 
# hello

while True:
    speak("How can I help you?")
    voice = recognize_speech().lower()
    # <-----------------------------------------Google Section----------------------------------------------------------->    
    if 'open google' == voice:
        speak('Opening google..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://google.com')
    elif 'search google' in voice:
        try:
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element_by_name('q')
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)
        except:
            speak('Please open google first')
    elif 'login google' == voice:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[2]/a').click()
            while True:
                speak('Enter ID')
                query = recognize_speech()
                if query != 'Error':
                    break
            if(query!='hello world'):
                speak('wrong ID, please try again')
                continue    
            element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
            element.clear()
            element.send_keys('zixersparrow@gmail.com') 
            element.send_keys(Keys.RETURN)
            while True:
                speak('Enter password')
                query = recognize_speech()
                if query != 'Error':
                    break
            if(query!='python'):
                speak('wrong password, please try again')
                continue   
            element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
            element.clear()
            element.send_keys('Sanu@2310')    
            element.send_keys(Keys.RETURN)
            time.sleep(30)
        except:
            speak('Google is not open. Please open google first') 


    # <-----------------------------------------Youtube Section------------------------------------------------------->
    elif 'open youtube' in voice:
        speak('Opening youtube..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://youtube.com')
    elif 'search youtube' in voice:
        try:    
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element_by_name('search_query')
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)
        except:
            speak('Youtube is not open. Please open youtube first')    
    elif 'history' in voice:
        try:
            element=driver.find_element_by_xpath('/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item/yt-formatted-string')
            element.click()
        except:
            speak('You are not in youtube home page. Please go to youtube home page')    
    elif 'youtube home' in voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item/yt-formatted-string').click()
        except:
            speak('You are not in youtube home page. Please go to youtube home page')    
    elif 'explore' in voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a/tp-yt-paper-item').click()
        except:
            speak('You are not in youtube home page. Please go to youtube home page')     
    elif 'subscriptions' in voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[3]/a/tp-yt-paper-item').click()   
        except:
            speak('You are not in youtube home page. Please go to youtube home page')        
    elif 'library' in voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[1]/ytd-guide-entry-renderer/a/tp-yt-paper-item/yt-formatted-string').click()    
        except:
            speak('You are not in youtube home page. Please go to youtube home page')     
    elif 'like the video' == voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button').click()     
        except:
            speak('No video on screen to like')
    elif 'play the first video' == voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div').click() 
        except:
            speak('Facing problem opening the video. Please search another')     
    elif ('pause the video' in voice) or ('play the video' == voice):
        try:
            driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
        except:
            speak('No video playing on screen')    
    elif ('mute' in voice) or ('unmute' in voice):
        try:
            driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > span > button').click()    
        except:
            speak('No video playing on screen')    
    elif ('full screen' in voice) or ('exit full screen' in voice):
        try:
            driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button').click()
        except:
            speak("No video playing on screen")    
    elif 'dislike the video' in voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[6]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-icon-button').click()
        except:
            speak('No video on screen to dislike')    
    elif 'turn caption' in voice:
        try:
            driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-subtitles-button.ytp-button').click()
        except:
            speak('Captions Unavailable')    
    elif 'theatre mode' in voice:
        try:
            driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-size-button.ytp-button').click()
        except:
            speak('No video playing on screen')    
    elif ('subscribe' in voice) or ('unsubscribe' in voice):
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[7]/div[2]/ytd-video-secondary-info-renderer/div/div/div/ytd-subscribe-button-renderer/tp-yt-paper-button/yt-formatted-string').click()
            if('unsubscribe' in voice):
                driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/tp-yt-paper-button').click() 
        except:
            speak('Facing Problem')    
    elif 'next video' in voice:
        try:
            driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button').click()
        except:
            speak('No videos available')    
    elif 'login youtube' in voice:
        try:
            
            driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button').click()
            while True:
                speak('Enter ID')
                query = recognize_speech()
                if query != 'Error':
                    break
            if(query!='hello world'):
                speak('wrong ID, please try again')
                continue
            element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
            element.clear()
            element.send_keys('zixersparrow@gmail.com') 
            element.send_keys(Keys.RETURN)
            while True:
                speak('Enter password')
                query = recognize_speech()
                if query != 'Error':
                    break
            if(query!='python'):
                speak('wrong password, please try again')
                continue   
            element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
            element.clear()
            element.send_keys('Sanu@2310')    
            element.send_keys(Keys.RETURN)
            time.sleep(30)
        except:
            speak('Please open Youtube first')    
    elif 'liked videos' in voice:
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-entry-renderer[3]/a/tp-yt-paper-item/yt-formatted-string').click()
        except:
            speak('Open Youtube first')    
   
    # <-----------------------------------------Facebook Section------------------------------------------------------>
    elif 'open facebook' in voice:
        speak('Opening facebook..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://facebook.com')
    elif 'login facebook' in voice:
        try:
            while True:
                speak('Enter ID')
                query = recognize_speech()
                if query != 'Error':
                    break
            if(query!='hello world'):
                speak('wrong ID, please try again')
                continue    
            element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
            element.clear()
            element.send_keys('zixersparrow@gmail.com') 
            while True:
                speak('Enter password')
                query = recognize_speech()
                if query != 'Error':
                    break
            if(query!='python'):
                speak('wrong password, please try again')
                continue   
            element = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
            element.clear()
            element.send_keys('zixer4245')    
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
            time.sleep(4)
        except:
            speak('Open Facebook first')   
    elif 'search facebook' in voice:
        try:
            while True:
                speak('Enter name of your friend..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input')
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)  
        except:
            speak('Open Facebook first')    
    elif 'add friend' in voice:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[1]/div/div/div').click()    
        except:
            speak('Open friends profile in facebook first')    
    elif 'message' in voice:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div').click()  
        except:
            speak('Open friends profile in facebook first')      
    elif 'show' in voice and 'profile' in voice:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[4]/a').click()
        except:
            speak('open facebook first')    
    elif 'open' in voice and 'messenger' in voice:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/span/a').click()
        except:
            speak('open facebook first')
    elif 'show' in voice and 'notifications' in voice:
        try:
            driver.get('https://www.facebook.com/notifications')
        except:
            speak('open facebook first')    
    elif 'dark mode' in voice:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[3]/div/div[1]/div[2]').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/label/div/div/div/div/div[1]/div').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]').click()
        except:
            speak('open facebook first')    
    elif 'logout' in voice and 'facebook' in voice:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]').click()
    elif 'light mode' in voice:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[3]/div/div[1]/div[2]').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[1]/label/div/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]').click()
        except:
            speak('open facebook first')  

    # <-----------------------------------------Wikipedia Section----------------------------------------------------->
    elif 'open wikipedia' in voice:
        speak('Opening wikipedia..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://www.wikipedia.org')
    elif 'search wikipedia' in voice:
        try:
            while True:
                speak('I am listening..')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element_by_name('search')
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)
        except:
            speak('Open Wikipedia first')    
    
    # <-----------------------------------------Google Maps Section--------------------------------------------------->
    elif 'open google map' in voice:
        speak('Opening Google Maps..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://www.google.com/maps')
    elif 'find path' in voice:
        try:
            driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div/button').click()
            while True:
                speak('Where to start from?....')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input')
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)

            while True:
                speak('Enter your destination....')
                query = recognize_speech()
                if query != 'Error':
                    break
            element = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input')
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)
        except:
            speak('Open Google maps first')    
   
    # <-----------------------------------------Other Section--------------------------------------------------------->
    elif 'open' in voice and 'form' in voice:
        speak('Opening form..')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('E:\\browser-assistant\\project-site.html')
    elif 'fill' in voice:
        try:
            while True:
                speak('What is the first name?..')
                query = recognize_speech()
                if query != 'Error':
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            element = driver.find_element_by_xpath('/html/body/div[2]/form/div/input[1]')
            element.clear()
            element.send_keys(query)
            while True:
                speak('What is the last name?..')
                query = recognize_speech()
                if query != 'Error':
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            element = driver.find_element_by_xpath('/html/body/div[2]/form/div/input[2]')
            element.clear()
            element.send_keys(query)
            while True:
                speak('Enter college name')
                query = recognize_speech()
                if query != 'Error':
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            element = driver.find_element_by_xpath('/html/body/div[2]/form/input[1]')
            element.clear()
            query.capitalize()
            element.send_keys(query)
            while True:
                speak('Enter yout email')
                query = recognize_speech()
                if query != 'Error':
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            element = driver.find_element_by_xpath('/html/body/div[2]/form/input[2]')
            element.clear()
            query.replace(" ","")
            element.send_keys(query+'@gmail.com')
            while True:
                speak('Enter Area code')
                query = recognize_speech()
                if query != 'Error':
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            element = driver.find_element_by_xpath('/html/body/div[2]/form/input[3]')
            element.clear()
            element.send_keys('+'+query)
            while True:
                speak('Enter phone number')
                query = recognize_speech()
                if query != 'Error':
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            element = driver.find_element_by_xpath('/html/body/div[2]/form/input[4]')
            element.clear()
            element.send_keys(query)
            driver.find_element_by_xpath('/html/body/div[2]/form/select').click()
            while True:
                speak('What is your subject?')
                query = recognize_speech()
                if query != 'Error' and (query=='science' or query =='math' or query=='computer'):
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            if 'science' in query:
                driver.find_element_by_xpath('/html/body/div[2]/form/select/option[2]').click()
            elif 'math' in query:
                driver.find_element_by_xpath('/html/body/div[2]/form/select/option[3]').click()    
            else:
                driver.find_element_by_xpath('/html/body/div[2]/form/select/option[4]').click() 
            driver.find_element_by_xpath('/html/body/div[2]/form/select').click()
            while True:
                speak('Are you a fresher?')
                query = recognize_speech()
                if query != 'Error':
                    break
                else:
                    speak('Cannot get that. Please repeat' )
            if 'yes' in query:
                driver.find_element_by_xpath('/html/body/div[2]/form/label[3]/input').click()
            else:
                   driver.find_element_by_xpath('/html/body/div[2]/form/label[4]/input').click() 
            speak("form filled. Thank you")
        except:
            speak('Open a form first')    
    elif 'roll' in voice and 'dice' in voice:
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://www.google.com/search?q=roll+a+dice&oq=roll+a+dice&aqs=chrome..69i57.2202j0j7&sourceid=chrome&ie=UTF-8')
        speak('Rolling a dice')
    elif 'flip' in voice and 'coin' in voice:
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://www.google.com/search?q=flip+a+coin&oq=flip+a+coin&aqs=chrome..69i57.3436j0j7&sourceid=chrome&ie=UTF-8')
        speak('Flipping a coin')
    elif 'switch tab' in voice:
        try:
            num_tabs = len(driver.window_handles)
            cur_tab = 0
            for i in range(num_tabs):
                    if driver.window_handles[i] == driver.current_window_handle:
                        if i != num_tabs - 1:
                            cur_tab = i + 1
                            break     
            driver.switch_to_window(driver.window_handles[cur_tab])
        except:
            speak('Facing problem to do that')    
    elif 'go back' in voice:
        driver.back()
    elif 'go forward' in voice:
        driver.forward()
    elif 'exit' in voice:
        speak('Goodbye Zixer!')
        driver.quit()
        break
    elif 'refresh' in voice:
        speak('Refreshing the page')
        driver.refresh()    
    elif 'change voice' in voice:
        if(gender==1):
            gender=0
            speak('changing voice')
            engine.setProperty('voice', voices[0].id)
            speak('voice changed')
        else:
            gender=1
            speak('changing voice')
            engine.setProperty('voice', voices[1].id)
            speak('voice changed')  
    elif 'take a break' in voice:
        speak('Enter your break time')
        t=float(input("Enter your value: "))
        time.sleep(t)
    else:
        speak('Not a valid command. Please try again.')
    time.sleep(2)