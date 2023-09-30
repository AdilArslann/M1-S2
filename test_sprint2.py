import pytest
import unittest
from sprint2 import send_email, fetch_cryptocurrency_data, validate_email, mail_body

def test_fetch_cryptocurrency_data():
    #Test 1 Valid Crypto_id and currency
    data = fetch_cryptocurrency_data("bitcoin", "usd")
    market_data = data["market_data"]
    assert 'name' in data, "Expected 'name' key not found in data"
    assert "current_price" in market_data, "Expected 'current_price' key not found in data"

    #Test 2 invalid Crypto_id
    data = fetch_cryptocurrency_data("invalid_crypto_id", "invalid_currency")
    assert 'market_data' not in data
    assert 'name' not in data

    #Test 3 invalid currency
    data = fetch_cryptocurrency_data("invalid_crypto_id", "invalid_currency")
    assert 'market_data' not in data
    assert 'name' not in data

    #Test 4 Invalid Crypto_id and currency
    data = fetch_cryptocurrency_data("invalid_crypto_id", "invalid_currency")
    assert 'market_data' not in data
    assert 'name' not in data


def test_send_email():
    # Test case 1: Valid inputs since everything has to be correct to reach this
    # in my program
    to = "1goblinchief1@gmail.com"
    subject = "Test Email"
    body = "This is a test email."
    result = send_email(to, subject, body)
    assert result == True, "Failed to send email with valid inputs"


def test_validate_email():
    assert validate_email("1goblinchief1@gmail.com") == True
    assert validate_email("1goblinchief") == False
    #hoping that no one decided to create an account this absurd D:
    assert validate_email("1goblincjkahksf3525235jh747@gmail.com") == False 
    assert validate_email("1goblinhief1.com") == False
    assert validate_email("1goblinchief1@gmail") == False

def test_mail_body():
    name = "Bitcoin"
    all_time_high = 64805.54
    current_price = 54321.98
    currency = "usd"
    expected_body = f"""Hello,
    Here is the information for {name}:

    Coin Name: {name}
    All Time High: {all_time_high}
    Current Price: {current_price}
    Currency: {currency.upper()}

    Regards,
    Cryptocurrency Bot"""
    result_body = mail_body(name, all_time_high, current_price, currency)
    assert result_body == expected_body

if __name__ == "__main__":
    test_validate_email()
    test_fetch_cryptocurrency_data()
    test_send_email()
    test_mail_body()
    print("test was successful")