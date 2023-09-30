# Cryptocurrency and Cat Fact Emailer

## Overview

This Python script is a simple email utility that allows you to retrieve and send two types of email content:

1. Cryptocurrency Information: Retrieve data about a specific cryptocurrency's name, all-time high, and current price in a chosen currency using the CoinGecko API. The information is then emailed to a specified Gmail address.

2. Random Cat Fact: Fetch a random cat fact from the CatFact Ninja API and send it via email.

The script offers flexibility in terms of the recipient's email address and the type of content to be emailed (cryptocurrency or cat fact).

## Features

### 1. Cryptocurrency Information

- Retrieves cryptocurrency data (name, all-time high, current price) from the CoinGecko API.
- Validates user input for cryptocurrency name and currency.
- Sends an informative email with cryptocurrency details.

### 2. Random Cat Fact

- Fetches a random cat fact from the CatFact Ninja API.
- Formats the cat fact into an email.
- Sends a fun and random cat fact email.

## Tests

The script includes tests to ensure its functionality. You can run these tests using the `pytest` framework. Here are the available tests:

1. **test_fetch_cryptocurrency_data**: This test checks the `fetch_cryptocurrency_data` function for various scenarios, including valid and invalid cryptocurrency IDs and currencies.

2. **test_send_email**: This test checks the `send_email` function's ability to send an email with valid inputs.

3. **test_validate_email**: This test checks the `validate_email` function, which uses an additional API for email validation. It verifies email addresses for validity.

4. **test_mail_body**: This test checks the `mail_body` function's ability to format email content based on cryptocurrency data.

To run the tests, execute the following command:
