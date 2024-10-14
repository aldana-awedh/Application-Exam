
import requests
import json
import pandas as pd

# Task 1
def espresso(num):
    if num % 18 == 0:
        print('ESPRESSO!')
    else:
        print(f'{num} is not espresso')


# Task 2
def preferred_coffee():
    # Get request 
    response = requests.get('https://randomuser.me/api/')
    data = response.json()['results']

    # Extract gender, first name, and last name 
    gender = data[0]['gender'] 
    first_name = data[0]['name']['first']
    last_name = data[0]['name']['last']

    # Find a user's preferred drink based on the first letter of their name 
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    if first_name[0].upper() in vowels:
        preferred_drink = 'latte'
    else:
        preferred_drink = 'macchiato'

    print(f'{gender}, {first_name} {last_name}, {preferred_drink}')

# Helper function to retrieve the names of 3 random users 
for i in range(3):
    preferred_coffee()


# Task 3 
# Create DataFrame with desired column names 
df = pd.DataFrame(columns = ['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Postal Code/Zip Code', 'Preferred Coffee Drink'])

def document_preferred_coffee():
    # Get 7 random users 
    for i in range(7):
        # Get request 
        response = requests.get('https://randomuser.me/api/')
        data = response.json()['results']

        # Extract data from JSON object 
        first_name = data[0]['name']['first']
        last_name = data[0]['name']['last']
        street_address = str(data[0]['location']['street']['number']) + ' ' + data[0]['location']['street']['name']
        city = data[0]['location']['city']
        state = data[0]['location']['state']
        postcode = data[0]['location']['postcode']

        # Find a user's preferred drink based on the first letter of their name 
        vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
        if first_name[0].upper() in vowels:
            preferred_drink = 'latte'
        else:
            preferred_drink = 'macchiato'


        # Create DataFrame with random user data 
        df.loc[i] = [first_name, last_name, street_address, city, state, postcode, preferred_drink]
    
    # Create CSV with random user data
    df.to_csv('document_preferred_coffee_results.csv', index=False)
  






