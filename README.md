> :warning: This project is still buggy, it doesn't support all forms of video formats on keats

# This project is for downloading videos off of keats.
This is a project intended to automatically download all videos in a course and store them locally. 
The original idea was to merge [memst's](https://github.com/memst/keats_downloader) and [dylantjb's](https://github.com/dylantjb/keats_downloader) but this has rolled off to be a maintained version of keats downloader 

Benefits include:
- Being able to play back videos at speeds the Kaltura player doesn't allow you
- Being able to use subtitles as a semi-accurate transcript
- Being able to watch high-resolution video streams with no buffering
- Offline download for those with bad internet connections.
 
## Installation
#### 1. Install python modules used by the project
Open up a terminal pointing to the folder and run the command below. 
```
pip3 install -r requirements.txt
```
#### 2. Download the chrome selenium driver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract and place it in the main directory such that the directory looks like this. 

### **Make sure the selenium driver you get is the same version as the Chrome browser you are using!!**
To check what Chrome version you have, 
 1. click the settings icon at the top right
 2. Hover help and click about chrome 
 3. The version number should be displayed 

```
./selenium/chromedriver.exe
./selenium/chromedriver/
```

#### 3. Install FFmpeg 


For windows: [Download This](https://github.com/BtbN/FFmpeg-Builds/releases). 
Copy the contents of the bin folder so that there are 3 files in the main directory.
```
...
/keats_downloader/ffmpeg.exe
/keats_downloader/ffplay.exe
/keats_downloader/ffprobe.exe
/keats_downloader/main.py
/keats_downloader/downloader.py
...
```

For ubuntu: run 
```
sudo apt install ffmpeg
```

For mac:
```
brew install ffmpeg
```

## Basic usage
1. Edit  `courses.txt` file with the URLs to all the courses modules you want to download separated by a new line. Its contents should look something like this(+example for Keats):
```
https://keats.kcl.ac.uk/course/view.php?id=CCCCC
https://keats.kcl.ac.uk/course/view.php?id=DDDDD
```
2. Execute main.py. It should walk you through the steps. 

## Todo

- [ ] Convert variable names from camel case to snake case
- [ ] Add an auto-install script
- [ ] Improve setup experience
- [ ] Headless mode
- [x] Linux and Mac OSX support
- [ ] srt download option
- [ ] Add padding so files are in order and avoid overwriting of videos of the same file name.
- [ ] Checking of files that exist so that you don't need to find and search for the same links again.
- [x] Multithread the get video list function to improve speed(currently the biggest bottleneck in the code)
## Confirmed working on
 - Keats with kaltura video hosting