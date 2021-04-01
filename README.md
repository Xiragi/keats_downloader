
> This project is very WIP and some things might not work correctly. If you encounter any problems, issue a bug report or create a pull request.

# Keats Downloader
This is a project intended to automatically download all videos in a course and store them locally. Benefits include:
- Being able to playback videos at non-turtle speed (more than 2x)
- Being able to use subtitles as a semi-accurate transcript
- Being able to watch high-resolution video streams with no buffering
- Not having your lectures interrupted because the website is down

## Requirements
1. To install the python modules used by the project run the following in the directory.
	```
	pip3 install -r requirements.txt
	```

2. Download the chrome selenium driver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract and place it in the main directory such that the directory looks like this
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
1. Create a `courses.txt` file with the urls to all courses you want to download separated by newlines. Its contents should look something like this:
	```
	https://keats.kcl.ac.uk/course/view.php?id=AAAAA
	https://keats.kcl.ac.uk/course/view.php?id=BBBBB
	https://keats.kcl.ac.uk/course/view.php?id=CCCCC
	https://keats.kcl.ac.uk/course/view.php?id=DDDDD
	```
2. Run `main.py` through terminal:
	```
	python main.py
	```

You still need to have logged in to your account to use this.


## Reviews

> actual life saver
> -_Chirag_