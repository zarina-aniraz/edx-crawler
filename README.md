# edx-crawler

edx-crawler is a Python-based cross-platform tool for mining text data from the courses available on edx.org. It was developed by teaching assistants at Tokyo Tech Online Education Development Office as an extension of [edx-dl](https://github.com/coursera-dl/edx-dl).

## Prerequisites
Python packages and dependencies

* [Python](https://www.python.org/downloads/) - version 3.5+
* [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) - a Python library for pulling data out of HTML and XML files
* [webvtt-py](https://pypi.python.org/pypi/webvtt-py) -  a Python module for reading/writing WebVTT caption files
* [youtube-dl](https://github.com/rg3/youtube-dl) - command-line program to download videos from YouTube.com

## How to run

1. Run a python script edx_crawler.py passing edx course link, username -u and password -p as parameters.

	python edx_crawler.py course_url -u edx_user_name -p dx_user_password.

## OPTIONS

	-url, --course-urls		Specify target course urls
	-u, --username			Specify your edX username (email)
	-p, --password			Input your edX password
	-d, --html-dir			Specify directory to store data
	
The output is a weekly organized structure of the course in "HTMLs" folder.
The contents are the following:

* seq_contents_#.html - text data of the sequence (unit) in the .html format
* seq_contents_#.txt - text data of the sequence (unit) in the .txt format
* seq_contents_#_prob.txt - text data of the quiz sections in the .txt format
* seq_contents_#_vdo.json - video transcript information in .json format

2. JSON format

After crawling courses, you may run txtcomp2json to summarize data in json format.

	python txtcomp2json.py
	
 The program processes html data and produces .json output:
*all text components -> all_textcomp.json
*all problem components -> all_probcomp.json
*all video components -> all_videocomp.json
*all components (text, problems, videos) -> all_comp.json

## Extra files and folders

transcript_error_report.txt contains the information about videos which are not accompanied by transcripts.

