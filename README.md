# iTexico \<main\> 2020
This repository contains a hello world of Automation using Python, Pytest and Selenium Webdriver. This demo was presented in the iTexico \<main\> event last March 12, 2020.

Find the slides of the presentation in the following link:
- https://slides.com/alejandro-serrano/test-automation-symphony

## Getting started
1.- Ensure that the latest version of Python is installed in your system.
2.- If the [Python](https://www.python.org/downloads/) installer doesn't add the Python installation directory with its corresponding libraries and scripts to your PATH environment variable, please do it.
3.- Clone this repository or download the zip with the source code in to your local system.
```
git clone https://github.com/alejandro-serrano/itexico-main-2020.git
```
4.- Download [chrome webdriver](https://chromedriver.chromium.org/downloads), unzip the file if that is the case, move it to the drivers folder of this repository and finally add it to your PATH environment variable.

## Prepare your development environment

1.- In command shell change to the directory where the code of this repository live. Notice in my case I'm in a Windows environment, however, the commands should be similar for Mac or Linux.
```
C:\> cd itexico-main-2020
```
2.- Create a python virtual environment.
```
C:\itexico-main-2020> python -m venv e2e
```
3.- Activate the python virtual environment.
```
C:\itexico-main-2020> C:\itexico-main-2020\e2e\Scripts\activate.bat

(e2e) C:\itexico-main-2020>
```
4.- Install pytest in your virtual environment.
```
(e2e) C:\itexico-main-2020> pip install -U pytest
```
5.- Install selenium in your virtual environment.
```
(e2e) C:\itexico-main-2020> pip install -U selenium
```

## Running the tests
1.- You can run the tests suite from a command shell by calling the following command.
```
(e2e) C:\itexico-main-2020> pytest --verbose tests\
```

## Demo
