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

![Captura Des](https://user-images.githubusercontent.com/110279710/220990775-1b599ac1-aee7-4b05-a94a-2ffaa1e11b89.JPG)


```- test_accomodations:```

This test case will select the "Accomodations" functionality, and verify that an option can be selected, showing the final price of the purchase.

It will select an entry date and a departure date, then select the destination city, which in this case will be "Cordoba". It will do this by entering the input "Cordoba", and selecting the first index in the list, and will search for the products corresponding to the parameters entered.

Once the search results are returned, it will use the filter to organize the results by price from lowest to highest.

Once you have seen the detail, look for the "Reserve" button, and verify that the total value of the reservation package is shown.

![Captura Des2](https://user-images.githubusercontent.com/110279710/220993307-25a26054-e8b7-4f06-837e-48f296a24f07.JPG)

```- test_flights:```

In this case, webdriver will select the "Flights" functionality, and select an outbound and a return date, select tickets for two adults and three children, and select first class.

Select the destination, which in this case will be "Cordoba", and verify that there are available flights according to the parameters entered.


```- test_packages:```

The test case will select the "Packages" functionality, and select the destination "New York", then, select room for one person, and check the no date option, then press the search button.

It is expected that the search of the entered parameters will find the availability of the package, or in case there is no availability, it will show the corresponding message.


```- test_offers:```

Here you will verify that the "Offers" functionality will show the current featured offers, and select the first featured item.

It will verify the corresponding steps until reaching the final result, according to the price of the selected package, showing "Total".


```- test_rents:```

In this script we will generate the rents functionality, select the destination "Cordoba", and enter an entry date, and an exit date, and then, search for the result generated by the inputs.

It will verify that the result of the first index, "Ordenar Por", is shown.


```- test_activities:```

The "Activities" case will search for available activities, entering "Buenos Aires" as the destination, select the first index in the list that returns.

Select the date, time, and add it to the cart, and then verify the final price with "Detail of your purchase".


```- test_getaways:```

This functionality will select a destination, and check the packets available to the user, choosing the first one as the visible object.

Then it will check the availability of the selected package, and if it is available, it will select it as a reservation, to return the charge detail.

```- test_cars:```

Here the script will select the feature "Cars", and will select as destination "Buenos Aires", then choose the date selected, and search the availability of the cars found.

```- test_dsny:```

In this case, you will select the "Disney" functionality, and select an entry date, along with the number of people traveling.

Then, add the package to the shopping cart, and verify the total amount to be paid.

```- test_assists:```

In the case of "Assists", once the feature is selected, the destination will be entered, which in this case will be "Argentina", and an entry date and a departure date will be selected.

Then, you will search for the availability of the assistances, and you will buy the first available package, and then verify the total price.

```- test_transfers:```

The "Transfers" case will select the entry destination, which in this case will be "Ezeiza", and then select an arrival destination, which will be "Icaro".

Afterwards, you will select the date on which you wish to request the transfer, and proceed to purchase the package, and then display the total price of the package purchase.

## Notes:

- The script was created under the page object model paradigm.

- Dates entered are temporary, and should be updated over time.

- This site usually has weekly changes, so frequent updates should be made to keep the functionality of the script up to date.

- Most of the web elements are selected by CSS_Selector, in order to guarantee the highest stability in terms of scripting. In some cases they were selected by XPATH.

- All test cases come by default with unittest.skip, so that you can isolate them in case you want to test them individually.

- The maximize_window variable was implemented in the main, so that all test cases are executed in full screen and avoid scope problems in webdriver.
