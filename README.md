# Driver Drowsiness Detection
A simple python script which utlises dlib for facial landmark recognition and a heuristic to determine drowsiness in a driver. 


## How to run this code??
1. clone this repo by running the following command: git clone https://github.com/iakash2604/drowsiness_detection
2. a default alarm sound is kept in the directory /files. replace with any audio file (.wav) format of your choice. do not remove the .dat file present there. 
3. open terminal and navigate to /src
4. run the following command: python3 main.py 

## Requirements
1. python 3.6
2. opencv 3.1
3. dlib 19.17.0

A bash script is present in the /src directory which will install all the required libraries. 

## Misc
1. The code assumes that the index of the video peripheral being used is 0 (generally true for webcams on ubuntu). but make sure it is changed to the index of whatever device will be used to stream the video. 
