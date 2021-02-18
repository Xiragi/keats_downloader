import downloader
import threading
import time

# Setup stage

# Database
print("Would to like to create a new database?(Y/N)")
print("If this is the first time running this then type in Y")
response = input("")
databaseHandler = downloader.Database()
if response == "Y":
    databaseHandler.createNewDatabase()
    database = databaseHandler.getDatabase()
else:
    database = databaseHandler.loadDatabase()

global finalStep
finalStep = False


def aSyncVideoDownload():
    global FinalStep
    print("\nasync video download thread started\n")
    database_handler2 = downloader.Database()
    database2 = database_handler2.loadDatabase()
    video_downloader = downloader.VideoSaver(False)
    while not finalStep:
        time.sleep(2)
        video_downloader.downloadVideo(database2)
    print("\nasync video download thread ended\n")


a = threading.Thread(target=aSyncVideoDownload)
a.start()

# Login
print("Have you logged in before? (Y/N)")
response = input("")
Browser = downloader.Selenium()
if response == "N":
    print("Once you are logged in close the browser and wait")
    Browser.loadKeatsPage(False)

print("Setup stage complete")
# Video Setup

# Listing videos
print("Trying to load courses.txt file")
try:
    courses = downloader.Courses().getCourses()
except:
    print(
        "Something went wrong opening courses.txt. Make sure that text file exists with your module link on each line")

print("Getting the video list")
Browser.getVideoList(database, courses)
print("Getting video URLs")
delay = 1.0  # Increase this to 1.0 if you get a lot of "Failed to find frame"

Browser.getVideoURLs(database, delay)

# Video downloading
# Downloading videos
finalStep = True
print("Downloading videos")
videoDownloader = downloader.VideoSaver(False)
videoDownloader.downloadVideo(database)
