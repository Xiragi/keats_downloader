import sqlite3
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path
import requests
import ffmpeg
from time import sleep

class Database():
    def __init__(self):
        self.newDatabaseStatement = "CREATE TABLE \"Videos\" ( `course` TEXT NOT NULL, `courseID` TEXT NOT NULL, `week` TEXT NOT NULL, `name` TEXT NOT NULL, `pageUrl` TEXT NOT NULL UNIQUE, `videoUrl` TEXT, `srtUrl` TEXT, `file_exists` INTEGER DEFAULT 0, PRIMARY KEY(`pageUrl`) )"
        self.database = None

    def loadDatabase(self):
        self.database = sqlite3.connect("main.db")
        return self.database
    def getDatabase(self):
        return self.database
    
    def createNewDatabase(self):
        try:
            os.remove("main.db")
        except:
            print("Could not delete database (not exist or in use)")
        self.database = sqlite3.connect("main.db")
        self.database.execute(self.newDatabaseStatement)
        self.database.commit()
        

class Selenium():
    def __init__(self):
        self.webDriverOptions = "--user-data-dir=" + os.getcwd() + "/selenium/chrome_driver"
        self.webDriverPath = os.getcwd() + "/selenium/chromedriver.exe"

    def loadKeatsPage(self,webSecurity):
        options = webdriver.ChromeOptions()
        options.add_argument(self.webDriverOptions)
        if not webSecurity:
            options.add_argument("disable-web-security")
        driver = webdriver.Chrome(executable_path=self.webDriverPath, chrome_options=options)
        driver.get("https://keats.kcl.ac.uk/")
        input("Press Enter once you are logged in\n")
        driver.quit()
    def getVideoList(self,database,courses):
        options = webdriver.ChromeOptions()
        options.add_argument(self.webDriverOptions)
        options.add_argument("disable-web-security")
        driver = webdriver.Chrome(executable_path=self.webDriverPath, chrome_options=options)
        driver.get("https://keats.kcl.ac.uk/")
        wait_element = EC.presence_of_element_located((By.ID, 'page-footer'))
        WebDriverWait(driver, 10).until(wait_element)
        for course in courses:
            driver.get(course)
            WebDriverWait(driver, 10).until(wait_element)
            videoDicts = driver.execute_script(open("list_videos.js").read())
            videos = []
            for video in videoDicts:
                videos.append((video['course'], video['courseID'], video['week'], video['name'], video['pageUrl']))
            database.executemany("INSERT INTO Videos (course, courseID, week, name, pageUrl) VALUES (?, ?, ?, ?, ?) ON CONFLICT(pageUrl) DO UPDATE SET courseID=courseID",videos)
        database.commit()
        driver.quit()
    def getVideoURLs(self,database,delay):
        options = webdriver.ChromeOptions()
        options.add_argument(self.webDriverOptions)
        options.add_argument("disable-web-security")
        driver = webdriver.Chrome(executable_path=self.webDriverPath, chrome_options=options)
        driver.get("https://keats.kcl.ac.uk/")
        wait_element = EC.presence_of_element_located((By.ID, 'page-footer'))
        WebDriverWait(driver, 10).until(wait_element)
        for video in database.execute("SELECT * FROM Videos WHERE (file_exists = 0 OR file_exists IS NULL)"):
            notComplete = True
            while notComplete:
                try:
                    try:
                        print(video[1],video[2],video[3])
                        driver.get(video[4])
                        #Wait and open contentFrame
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'contentframe')))
                        driver.switch_to.frame(driver.find_element(By.ID,'contentframe'))

                        #Make sure that the player is loaded
                        driver.execute_script(open("create_player.js").read())
                        #Process player
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kplayer')))
                        driver.switch_to.frame(driver.find_element(By.ID,'kplayer_ifp'))
                        sleep(delay)
                    except Exception as e:
                        print(e)
                        print("Failed to find frame")
                        continue
                    #still using JS for some reason. Could quite easily change this to be pure selenium, but me lazy.
                    urls = driver.execute_script(open("video_url.js").read())
                    #print(urls)
                    if(urls[1] is not None):
                        print("Fount srt")
                    database.execute("UPDATE Videos SET videoUrl=?, srtUrl=? WHERE pageUrl=?",(urls[0],urls[1],video[4]))
                    database.commit()
                    notComplete= False
                except:
                    print("Error. Retrying")
                    sleep(3)
        database.commit() #I don't think this is needed here but i'll see.
        driver.quit()

class VideoSaver():
    def __init__(self,online):
        self.online = online
        self.MAX_NAME_LENGTH = 240
        if online:
            self.base_folder="online_library"
            self.extension="m3u8"
        else:
            self.base_folder="library"
            self.extension="mp4"
    def downloadVideo(self,database):
        for video in database.execute("SELECT * FROM Videos WHERE videoUrl IS NOT NULL"):
            dirs = []
            for i in range(4):
                dirs.append((video[i][0:self.MAX_NAME_LENGTH]).strip())

            directory = "{}/{}/{}".format(self.base_folder,dirs[0],dirs[2])
            path = "{}/{}.{}".format(directory,dirs[3],self.extension)
            srt_path = "{}/{}.srt".format(directory,dirs[3])

            #skip if exists
            if os.path.isfile(path):
                continue
            print("Currently Downloading and converting: ",video[1],video[2],video[3])
            #download
            Path(directory).mkdir(parents=True, exist_ok=True)
            #print(video[5])
            #print(video[6])
            if self.online:
                r = requests.get(video[5])
                open(path, "wb").write(r.content)
            else:
                try:
                    ffmpeg.input(video[5]).output(path,codec="copy").run()
                    print("Finished downloading: ",video[1],video[2],video[3])
                except Exception as e:
                    print("Error")
                    print(e)
            if (video[6] is not None):
                r = requests.get(video[6])
                open(srt_path, "wb").write(r.content)
        
class Courses():
    def __init__(self):
        self.courses = []
        with open ("courses.txt", "r") as f:
            self.courses = [line.strip() for line in f.readlines()]
    def getCourses(self):
        return self.courses
