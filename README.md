> :warning: This project is very WIP, the link to the video page or the video itself might not be recognised.

> This project is also a fork of the original repository so our programs may not work together in the future.

# Videos Downloader for websites using Moodle along with kaltura as a video host.
This is a project intended to automatically download all videos in a course and store them locally. Benefits include:
- Being able to playback videos at speeds the kaltura player doesn't allow you
- Being able to use subtitles as a semi-accurate transcript
- Being able to watch high-resolution video streams with no buffering
- Offline download for those with bad internet connections.

## Todo

- Convert variable names from camel case to snake case
- Add an auto-install script
- Improve setup experience
- Headless mode
- Use of other drivers
- Linux and Mac OSX support
- srt download option
- Auto-add ffmpeg to path 
- Add padding so files are in order and avoid overwriting of videos of the same file name.
- Checking of files that exist so that you don't need find and search for the same links again.

## Confirmed working on
 - Keats
 
## Requirements
1. To install the python modules used by the project run the following in the directory.
```
pip3 install -r requirements.txt
```
2. Download the chrome selenium driver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract and place it in the main directory such that the directory looks like this. 

### **Make sure the selenium driver you get is the same version as the chrome browser you are using!!**

```
./selenium/chromedriver.exe
./selenium/chromedriver/
```

3. Download FFMpeg [here](https://github.com/BtbN/FFmpeg-Builds/releases). Copy the contents of the bin folder so that there are 3 files in the main directory.

```
./ffmpeg.exe
./ffplay.exe
./ffprobe.exe
```

## Basic usage
1. Edit  `courses.txt` file with the URLs to all the courses modules you want to download separated by a new line. Its contents should look something like this(+example for keats):
```
https://[Moodle Website]/course/view.php?id=AAAAA
https://[Moodle Website]/course/view.php?id=BBBBB
https://keats.kcl.ac.uk/course/view.php?id=CCCCC
https://keats.kcl.ac.uk/course/view.php?id=DDDDD
```
2. Execute main.py and it should walk you through the steps. 
