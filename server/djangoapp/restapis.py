# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
# def get_request(url,**kwargs):
#     print(kwargs)
#     print("GET from {} ".format(url))
#     try:
#         # Call get method of requests library with URL and parameters
#         response = requests.get(url,
# headers={'Content-Type': 'application/json'},
#                                     params=kwargs)
#     except:
#         # If any error occurs
#         print("Network exception occurred")
#     status_code = response.status_code
#     print("With status {} ".format(status_code))
#     json_data = json.loads(response.text)
#     return json_data


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")


def post_request(url, json_payload, **kwargs):
    response = requests.post(url, params=kwargs, json=json_payload)
    return response


# ---- commented as didn't find if used---
# def get_dealers_from_cf(url, **kwargs):
#     results = []
#     # Call get_request with a URL parameter
#     json_result = get_request(url)
#     if json_result:
#         # Get the row list in JSON as dealers
#         dealers = json_result["rows"]
#         # For each dealer object
#         for dealer in dealers:
#             # Get its content in `doc` object
#             dealer_doc = dealer["doc"]
#             # Create a CarDealer object with values in `doc` object
#             dealer_obj = CarDealer(address=dealer_doc["address"],
# city=dealer_doc["city"], full_name=dealer_doc["full_name"],
#                                    id=dealer_doc["id"],
# lat=dealer_doc["lat"], long=dealer_doc["long"],
#                                    short_name=dealer_doc["short_name"],
#                                    st=dealer_doc["st"],
#                                    zip=dealer_doc["zip"])
#             results.append(dealer_obj)

#     return results

# def get_dealer_reviews_from_cf(url, dealerId):
#     results = []
#     # Call get_request with a URL parameter
#     json_result = get_request(url)
#     if json_result:
#         # Get the row list in JSON as dealers
#         dealers = json_result["rows"]
#     review_obj.sentiment = analyze_review_sentiments(review_obj.review)


# def analyze_review_sentiments(dealerreview):
#     get_request(url, **kwargs)
# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# def post_review(data_dict):
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
# Add code for posting review
