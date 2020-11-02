import downloader

#Setup stage

###Database
print("Would to like to create a new database?(Y/N)")
print("If this is the first time running this then type in Y")
response = input("")
databaseHandler = downloader.Database()
if response == "Y":
    databaseHandler.createNewDatabase()
    database = databaseHandler.getDatabase()
else:
    database = databaseHandler.loadDatabase()

###Login
print("Have you logged in before? (Y/N)")
response = input("")
Browser = downloader.Selenium()
if response == "N":   
    Browser.loadKeatsPage(False)
    input("Press Enter once you are logged in")

print("Setup stage complete")
#Video Setup

###Listing videos
print("Trying to load courses.txt file")
try:
    courses = downloader.Courses().getCourses()
except:
    print("Something went wrong opening courses.txt. Make sure that text file exists with your module link on each line")

print("Getting the video list")
Browser.getVideoList(database,courses)
print("Getting video URLs")
delay = 1.0 #Increase this to 1.0 if you get a lot of "Failed to find frame"

Browser.getVideoURLs(database,delay)


#Video downloading
###Downloading videos
print("Downloading videos")
videoDownloader = downloader.VideoSaver(False)
videoDownloader.downloadVideo(database)
