# Automation Web: Despegar.com.ar

**Automation script with Python and Selenium Webdriver, that runs through the main flow of the Despegar.com.ar page, interacting with all the main features of the site.**


## Starting:

This repository can be cloned on a regular basis, to run on any local machine.


## Prerequisites:

***Software required to run the script:***

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

```- test_home:```

This test case is the opening one, and it will verify that the home page is displayed when the "Home" button is pressed.

```- test_accomodations:```

This test case will select the "Accomodations" functionality, and verify that an option can be selected, showing the final price of the purchase.

It will select an entry date and a departure date, then select the destination city, which in this case will be "Cordoba". It will do this by entering the input "Cordoba", and selecting the first index in the list, and will search for the products corresponding to the parameters entered.

Once the search results are returned, it will use the filter to organize the results by price from lowest to highest.

Once you have seen the detail, look for the "Reserve" button, and verify that the total value of the reservation package is shown.

```- test_flights:```

In this case, webdriver will select the "Flights" functionality, and select an outbound and a return date, select tickets for two adults and three children, and select first class.

Select the destination, which in this case will be "Cordoba", and verify that there are available flights according to the parameters entered.

```- test_packages:```

The test case will select the "Packages" functionality, and select the destination "New York", then, select room for one person, and check the no date option, then press the search button.

It is expected that the search of the entered parameters will find the availability of the package, or in case there is no availability, it will show the corresponding message.

```- test_offers:```

