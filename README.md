# Phishing_Link_Detector_Project
A machine learning-based phishing link detector that identifies and blocks malicious URLs to enhance web security.
**Description:**
# Phishing Link Detector

A machine learning-based project to detect phishing links.

## Description

This project uses a machine learning model to detect phishing links. It extracts features from web pages and uses a random forest classifier to classify the links as either safe or phishing.

## Steps for Reproducing the Project

1. Install the required packages using `pip install -r requirements.txt`.
2. Move the project folder to the correct localhost location.
3. Modify the path of your Python 2.x installation in `clientServer.php`.
4. Go to `chrome://extensions`, activate developer mode, click on load unpacked and select the 'Extension' folder from our project.
5. Now, you can go to any web page and click on the extension in the top right panel of your Chrome window. Click on the 'Safe of not?' button and wait for a second for the result.

## Research Paper

http://ieeexplore.ieee.org/document/8256834/

## Abstract

Naive users using a browser have no idea about the back-end of the page. The users might be tricked into giving away their credentials or downloading malicious data. Our aim is to create an extension for Chrome which will act as middleware between the users and the malicious websites, and mitigate the risk of users succumbing to such websites.

## Demo

https://youtu.be/0-wky0h3hmM

## Screenshots

![spit_safe](https://user-images.githubusercontent.com/18022447/35985360-7cd910f2-0cc4-11e8-9edf-d38bf83d19a1.png)
_**Fig 1.** A safe website - www.spit.ac.in (College website)_

![drive_phishing](https://user-images.githubusercontent.com/18022447/35985366-81a9c5b8-0cc4-11e8-887d-7f427ffa8a8e.png)
_**Fig 2.** A phishing website which looks just like Google Drive._

![dropbox_phishing](https://user-images.githubusercontent.com/18022447/35985373-84056c86-0cc4-11e8-8751-cf511d5b8aa0.png)
_**Fig 3.** A phishing website which looks just like Dropbox_

![moodle_safe](https://user-images.githubusercontent.com/18022447/35985384-881ea85a-0cc4-11e8-9bea-cf71b3089364.png)
_**Fig 4.** A safe website - www.google.com_
