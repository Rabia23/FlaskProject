Task:

-------

Create a REST API with 2 endpoints:

1) a POST '/grab_and_save'

2) a GET '/last'

3) Wrap up everything in Docker. Use several containers: for API, DB, frontend if you have it.
Put them together using Docker compose.

4) optionally (if you have finished all the other requirements and want to show off your frontend
dev capabilities) create a page that uses an ajax request call to the /last endpoint and shows the
response in a nice way.


Requirements:

--------------------

* You will need to use Flask-RESTful extension for Flask.

* You will need to install, configure (use default config) and use a MySQL DB.

* You will need to use SQLAlchemy as your ORM to operate against a MySQL DB. Do not use plain SQL commands.

* You will need to use Requests library to make calls to external APIs. Do not use urllib directly.

* Responses should be all in JSON.

* The final API will be tested using CURL, so you will need to include a read.me file in your project's
root folder with examples of curls for testing and how to start your API.



Functional requirements.

---------------------------------

1) a POST '/grab_and_save'

the endpoint must accept a "currency" (ISO3 code, for example EUR, USD, BTC etc) and also an "amount",
for example 100.23 or 0.25567801.

a. When someone calls this endpoint, your code logic must call OpenExchangeRates API and grab the latest
forex prices. Please see the documentation at https://docs.openexchangerates.org/docs/latest-json
Use this APIKEY to access Open Exchange Rate (a.k.a. OER) API so you can complete the exercise.
OER appkey --> 841a28ce9a464522bae12e9001d22ec8

b. Using the information you get from the above call, obtain the price for the currency passed in the
POST request body.

c. Multiply the price for the amount passed in the POST request body and obtain a final amount.

d. Store in MySQL the currency, the amount requested, the price given by open exchange rate and the
final amount in USD. [Use a precision of 8 decimal digits, and always round up. Do not loose precision
in calculations!] Add whatever other fields, index, etc you feel are required, keep in mind the requirements
of the other endpoint.


2) a GET '/last'

this endpoint can be called alone, in which case it will return the last operation stored in MySQL
... or it can be passed a "currency" in which case you will need to return the last record for that
specific currency from the MySQL DB.
... or it can be called with a number (int) in which case it will return the last N operations.
... or it can be called using both a currency and a number, in which case you will need to return
the last N operations for that currency.


TIPS:

-------

* BE YOU! Use your coding style, code as you normally do.

* Don't be nervous if you find out you don't know a technology involved in this exercise enough to use it,
just do what you normally do, google it and read about it and then implement what you learnt, but please
don't copy and paste others code, without knowing what it does, as you may be asked to explain your code.

* It's better to have something working than nothing so try to stick to the requirements as much as possible,
but if you can't, do what you need to finish the exercise.

* Last but not least, this is a useless API, it is probably just a trivial example of your capabilities,
but it does not mean you need to be careless about how you code it. This exercise aims to measure your
skills and performance so "show yourself off", use your best code, experience, and knowledge. Code this
as a world-class production-level software, but do not overcomplicate the resolution. Good luck!