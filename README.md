# Automation Web: Despegar.com.ar

**Automation script with Python and Selenium Webdriver, that runs through the main flow of the Despegar.com.ar page, interacting with all the main features of the site.**


## Starting:

This repository can be cloned on a regular basis, to run on any local machine.


## Prerequisites:

***Software required to run the script***

- Python V3.10 - https://www.python.org/downloads/

- VSCode (Optional) - https://code.visualstudio.com/

- Selenium Webdriver (ChromeDriver V110.0.5481.77) - https://chromedriver.chromium.org/downloads

- Google Chrome V110.0.5481.100 - https://www.google.com/intl/es_es/chrome/?brand=YTUH&gclsrc=ds&gclsrc=ds


## Files:

***The project is composed of 3 main files:***

###### Despegar_main.py

This file will load the automation environment, as well as the unit test library, in order to create the test case criteria (Asserts).

In this file, the 12 test cases that the script will run are loaded, which are:

**Test_Home:**

This is the opening test case, which will verify that the Webdriver opens the page, and shows the main page through the "Home" button.

