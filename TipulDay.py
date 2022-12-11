# This Code gets phone number, name and mail and prints it as a form in given websites/given google searchx amount of estimated websites.

# Notes:
# be sure to change all the details in the next section to answer your needs
# VERY RECOMMENDED TO USE VPN
# google might block you after some attempts so try to using vpn if you get "Error 1 message" in the console.
# Some websites might block you from entering the info, but its ok to get errors as long as the script runs and gets more websites that succesfully retrieve forms.

###############################################################################################################################################################################

# List Of Potential Errors

# Error 1: Google Blocked you from entering more requests,consider sending requests from a different IP (vpn for an example).
# Error 2: Error 2: Form posting failed.
# Error 3: Could Not Add the manually entered websites.
# Error 4: Issue Posting Request to server.
# Error 5: Issue requesting from the website.
# Error 6: Some parameters might be missing:

###############################################################################################################################################################################

# Libraries that are needed

# importing the necessary libraries
import requests
from bs4 import BeautifulSoup
import re

###############################################################################################################################################################################

# Default variables

SearchStartNum = 0
websites = []

###############################################################################################################################################################################

# Before we start, set the next parameters:

# the google search value to submit values into
# recommended 'leave details'/'leave a phone number/Contact restraunts(for restraunt forms submitting)' etc
SearchString = 'Dog Adopting leave your details'

# Enter amount of websites to try to submit forums to:
# number of websites is this value x12, note that google has a limit of this search value so from a specific number there will be no change.
AmountOfWebsitesToSendFormsTo = 3

# enter form name value
FormNameValue = 'Nice Guy'  # Target first + last name

# enter form number
FormPhoneNumberValue = '6666666666'  # Target phone number

# enter form email # you can use corob21626@gmail.com as a sample
FormEmailValue = 'Example@gmail.com'  # Target Email

# Optional, enter comment. usually not mandatory by most websites, but entering something may increase the submitted forms amount
FormCommentValue = ''  # example : Hello, please call me and send me emails!

# Optional, enter websites to search through into the websites array and remove # tags
# try:
#     websites.append = ['Site1','Site2','Site3']
# except:
#     print('Error 3: Could Not Add the manually entered websites.')

###############################################################################################################################################################################

# This code gets all the websites that will potentially have data submitted into them

print("[*] Started collecting website data")

# formatting for the google search
SearchString = SearchString.replace(" ", "+")


for lp in range(AmountOfWebsitesToSendFormsTo):
    url = f'https://www.google.com/search?q={SearchString}&start={SearchStartNum}'
    response = requests.get(url)

    # parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # get the top 1000 websites from the search results
    for link in soup.find_all('a'):
        if link.get('href').startswith('/url?q='):
            websites.append(link.get('href')[7:])

    # increases after every loop to start in +10 search value
    SearchStartNum = SearchStartNum+10

print("[*] Websites collected")

###############################################################################################################################################################################

# Code that inputs the form into all the websites

print("[*] Submitting forms")

if(len(websites) > 0):
    SuccessfullForms = 0
    FailedForms = 0
    for website in websites:
        # specifying the website url
        url = website

        # making a request to the website and getting the response
        try:
            response = requests.get(url)
        except:
            print("[!] Error 5: Issue requesting from the website")
            FailedForms += 1
            continue

        # parsing the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # finding the form elements in the page
        form_elements = soup.find_all('input')
        #form_elements.append(soup.find_all('input', {'type': 'tel'}))
        # creating a dictionary to store the form data
        form_data = {}

        # looping through the form elements and getting the data
        for element in form_elements:
            name = element.get('name')
            value = element.get('value')  # why is the value necessary?
            form_data[name] = value

        for data in form_data:
            DataName = data
            try:
                if "name" in DataName:  # Some developers like to name the fields fname or lname so this will miss
                    form_data[DataName] = FormNameValue
                # You are searching with a constant string field-names that can be Phone or phoneNumber and this line wont recognize them
                if "phone" in DataName or "num" in DataName or "tel" in DataName:
                    form_data[DataName] = FormPhoneNumberValue
                if "mail" in DataName:
                    form_data[DataName] = FormEmailValue
                if "Comment" in DataName or "message" in DataName:
                    form_data[DataName] = FormCommentValue
                # To make it simpler try to create a regex to match the names of these inputs and not strings. In addition the 'type' attribute can help you find this information faster
            except:
                print('[!] Error 6: Some parameters might be missing:', website)

            # making a post request to the website with the form data
        # Here the issue can be that some sites will use a different location to post the form. Here you should read the 'target' attribute of the post form and append it to the base URL. I think because of this issue many form posts will fail
        try:
            print('[*] Trying to post: ', form_data)
            response = requests.post(url, data=form_data)
        except:
            print('[!] Error 4: Issue Posting Request to server')
            SuccessfullForms += 1  # Why are you adding to the successfull posts on exception
            continue
            # checking the response status code
        if response.status_code == 200:  # code 200 is success
            print('[V] Form filled successfully! Website: ' + website)
            SuccessfullForms += 1
            continue
        else:
            print('[!] Error 2: Form posting failed, Web Error: ',
                  response.status_code)
            FailedForms += 1
            continue
            # except:
            #         print('Error 4: Issue Posting Request to Website.')
            #         FailedForms=FailedForms+1
        # except:
        #          print('Error 5: Issue requesting from the website.')
        #          FailedForms=FailedForms+1

else:
    print('[!] Error 1: Google Blocked you from entering more requests,consider sending requests from a different IP (vpn for an example).')


###############################################################################################################################################################################

# Final Information Print
print("[*] Finished Submitting Forms")
print('\n\tForm Filling Template: \n Name:'+FormNameValue+' \n Phone Number:' +
      FormPhoneNumberValue+' \n Email:'+FormEmailValue+' \n Meaasge(Optional):'+FormCommentValue)
print('\n\tSuccessfully Filled Forms:', str(SuccessfullForms))
print('\n\tFailed Filled Forms:', str(FailedForms))
