# Let's use python to make an API call using package called requests
# dependencies are pip
import requests
import json
# take user
user_postcode = input(" please enter your postcode ")

post_api_response =  requests.get("https://api.postcodes.io/postcodes/se120nb")

user_postcode_received = user_postcode

if post_api_response.status_code == 200:
    print("Thanks you for your request your status code is " + str(post_api_response.status_code))
else:
    print("Sorry the postcode is incorrect please enter the correct postcode")




















# #response_bbc = requests.get("https://www.bbc.co.uk/")
#
# #print(response_bbc)
# #print(response_bbc.status_code)
#
# print(response_bbc.headers)
# data_headers = response_bbc.headers
#
# for date_in in data_headers.keys():
#
#     print(date_in)


#print(data_headers)

# for date in
# print(type(response_bbc.headers))
