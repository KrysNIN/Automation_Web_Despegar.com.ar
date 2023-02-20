# Automation Web: Despegar.com.ar

**Automation script with Python and Selenium Webdriver, that runs through the main flow of the Despegar.com.ar page, interacting with all the main features of the site.**


## Starting:

This repository can be cloned on a regular basis, to run on any local machine.


## Prerequisites:

***Software required to run the script***

- [Python V3.10](https://www.python.org/downloads/)

- [VSCode](https://code.visualstudio.com/) (Optional)

- [Selenium Webdriver (ChromeDriver V110.0.5481.77)](https://chromedriver.chromium.org/downloads)

- [Google Chrome V110.0.5481.100](https://www.google.com/intl/es_es/chrome/?brand=YTUH&gclsrc=ds&gclsrc=ds)


## Files:

***The project is composed of 3 main files:***


```Despegar_main.py:```

This file will load the automation environment, as well as the unit test library, in order to create the test case criteria (Asserts).


```Despegar_set.py:```

This file will be in charge of creating the logic of all the tests contained in Despegar_main.py. In it will be contained the arguments and the webelements that are going to interact with each other, in order to reach the corresponding end-points.


```Despegar_get.py:```

Finally, the get file will be in charge of searching for the endpoint against which the comparison of the asserts contained in the tests of the main file will be made, and thus, be able to reach the conclusion that the test passes or fails.

 
## Test Cases:

***The test cases are 12, and are composed as follows:***

**- Test_Home:**

This test case is the opening one, and it will verify that the home page is displayed when the "Home" button is pressed.

**- Test_Accomodations:**

In this case, the functionality "Accomodations" will be checked, which consists of selecting the functionality, and entering a destination, which in this case will be "Cordoba", by means of the autocomplete field, and selecting the first index in the list.

Once the destination is selected, the flow will continue by selecting the date of entry, and the date of departure, and then search the available options.
