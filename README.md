# homework
## Description:
Education - this is a project to hide information about cards and accounts, and there is also a function that takes a list of dictionaries and the value for the key as input and creates a new one based on the state or date
## Installation:

1. Clone the repository:
```
git clone https://github.com/heerooin/education.git
```
2. Install dependencies:
```
pip install -r requirements.txt
```
## Testing:
1. To test the desired function, go to the file that starts with "test". Then substitute the data you need to verify the correct execution of the function
2. Run the pytest command to check the tests.
3. Check that the tests are running correctly.

## About masks

The masks function is used to mask the card or account number, you can test these functions by going to tests/test_masks

## About widget

The widget function also works with masking and date, it can mask a card or account and translate the date into an understandable format

## About processing

The processing function already works with operations, it can sort data by the key 'state' or 'date'. You can also test by going to the tests file by selecting test_processing

## About generators

This module can take information about currency in operation and filter it. Also can give description in operation.
And last function generate card nubmer, you just need to give 2 digit, start and stop. It can company help in bank sector.

## About utils

This module is used to send a file with operations in the form of JSON to it.

## About utils

This module is used to send a file with operations in the form of JSON to it.

## About external_api

This module is used to read the transaction by IP and outputs the transaction amount. The API is also used to convert to rubles.

