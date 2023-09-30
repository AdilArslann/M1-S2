import json
import requests
import smtplib
import sys



""" Function for getting cryptocurrency data using crypto name and currency you want
to see it's value in. The api is public api from coingecko  """
def fetch_cryptocurrency_data(crypto_id, currency):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}?vs_currency={currency}"
    try:
        response = requests.get(url)
        data = response.json()
    except:
        sys.exit("Try again later")
    else:
        return data



""" This function is for sending mail using Gmail, i have created an 
 account just for the sake of the project, but it can be easily changed if it was necessary
 """
def send_email(to, subject, body):
    from_email = "tturing95@gmail.com" # Can be replaced with prefered gmail (This will be used to send mails from)
    password = "vqvjmxaqioibkubg"  # App password for the prefered gmail account.
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(from_email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(from_email, to, message)
        server.close()
        return True
    except Exception as e:
        return False
    


""" This function checks if the email the user inputs is valid, i have used api because why not
so now it makes sure that email actually exists, but please do not test run this too much since
the api can be used only 100 times."""
def validate_email(email):
    url = f"https://api.apilayer.com/email_verification/check?email={email}"
    payload = {}
    headers= {
        "apikey" : 'IRPu9iWBNm7YD7XkZ2Z3trgv1d0vBUbv'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    if response.status_code == 200:
        result = json.loads(response.text)
        try:
            if result["format_valid"] and result["mx_found"] and result["smtp_check"]:
                return True
            else:
                return False
        except KeyError as e:
            return False
    else:
        print(f"Error occurred during email validation: {response.status_code}")
        return False


"""This function is for getting/harvesting/collecting data about the cryptocurrency that we got from the
coingecko api, since we do not need everything the api sent us we just take the necessary informations such as: name, ath(All Time high)
, and current_price. If the function fails to collect necessary information than most probably the crypto_id and/or currency was incorrect
so it tells the user what went from and calls the function for getting user input for crypto_id and currency, and continues the loop until
the requirements are met. If it gets all the necessart information it will create subject with the name and create a format the mail will be in
using mail_body function and then returning both subject and body (format)
"""
def get_information_from_api_data(crypto_id, currency):
    while True:
        data = fetch_cryptocurrency_data(crypto_id, currency)
        try:
            name = data["name"]
            all_time_high = data["market_data"]["ath"][currency]
            current_price = data["market_data"]["current_price"][currency]
        except KeyError as e:
            print("Incorrect crypto id or currency")
            crypto_id, currency = get_coin_name_from_user()
        else:
            subject = f"Cryptocurrency Information - {name}"
            body = mail_body(name, all_time_high, current_price, currency)
            return subject, body
    


"""Asks the user for gmail address and directly sends it to the validate_email function to make sure it is valid
if not they will be repromted until they input a valid email address"""
def get_email():
    to_email = input("Enter your Gmail address: ")
    while not validate_email(to_email):
        print("Invalid email address")
        to_email = input("Enter your Gmail address: ")
    return to_email



"""This is rather only for the looks and to make it easy to manage this is simply creating how the 
email be formatted and it's really easy to change, since it is identical to what you see in your mail."""
def mail_body(name, all_time_high, current_price, currency):
    body = f"""Hello,
    Here is the information for {name}:

    Coin Name: {name}
    All Time High: {all_time_high}
    Current Price: {current_price}
    Currency: {currency.upper()}

    Regards,
    Cryptocurrency Bot"""
    return body



"""Asks user for crypto_id and currency and returns those values, pretty straight forward"""
def get_coin_name_from_user():
    crypto_id = input("Name of the cryptocurrency: ").strip().lower()
    currency = input("Currency (example: eur/usd/aud): ").strip().lower()
    return crypto_id, currency



def get_random_cat_fact():
    url = "https://catfact.ninja/fact?"
    try:
        response = requests.get(url)
        data = response.json()
    except:
        sys.exit("Try again later")
    else:
        return data




def get_random_cat_fact_from_data(data):
    return data["fact"]



def mail_body_cat(fact):
    body = f"""Hello,
    Here is a random fact about cats:
    {fact}

    Regards,
    Your sketchy cat fact distributor"""
    return body



def main():
    if len(sys.argv) != 3:
        sys.exit("Incorrect, please run the program like: Python sprint2.py 'example@domain.com' cat/crypto")
        
    to_email = sys.argv[1]
    if not validate_email(to_email):
            to_email = get_email()

    if sys.argv[2].lower() == "crypto":

        crypto_id, currency = get_coin_name_from_user()

        subject, body = get_information_from_api_data(crypto_id, currency)   
    elif sys.argv[2].lower() == "cat":

        data = get_random_cat_fact()
        fact = get_random_cat_fact_from_data(data)
        subject = "Random cat fact"
        body = mail_body_cat(fact)
    else:
        sys.exit("Wrong api")

    if send_email(to_email, subject, body):
        sys.exit("Email sent successfully!")
    else:
        sys.exit("Error sending email:")

        

if __name__ == "__main__":
    main()    



#Ctrl + B opens/closes side bar (left)
#Ctrl + D renames everything with the same name in the file
#Alt + Shift + A makes the selected area comment block, can be extra useful while testing your code
#Ctrl + Shift + F it's a global search in the file directory
#Up arrow and Down arrow keys can be used in terminal to access previous inputs