import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd

#load .env variables
load_dotenv()

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

def auth():
  """returns the BEARER TOKEN to access tweets based on id"""
  return os.environ.get("BEARER_TOKEN")


def create_url(ids):
    # ids = "ids=1213764224356421633,1255542774432063488"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets?ids={}".format(ids)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    
    response_json_keys = response.json().keys()
    # if status code is 200 or json returned an error
    if response.status_code != 200 or "errors" in response_json_keys:
      return None #if there url tweet id is invalid
        # raise Exception(
        #     "Request returned an error: {} {}".format(
        #         response.status_code, response.text
        #     )
        # )
    return response.json()

def main():
  bearer_token = auth()
  url = create_url()
  headers = create_headers(bearer_token)
  json_response = connect_to_endpoint(url, headers)
  print(json.dumps(json_response, indent=4, sort_keys=True))

def nullify_tweet_col(df):
    df['tweet'] = None
    # print(df)
    return df

def test_extract():
  bearer_token = auth()
  df_test = pd.read_csv('./dataset/train.csv')
  df = nullify_tweet_col(df_test)

  #loop over df
  for i in range(2):
    # print(df['tweet_id'][i])
    ids = df_test['tweet_id'][i]
    # print(ids)
    url = create_url(ids)
    
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json_response)
    # print(json.dumps(json_response, indent=4, sort_keys=True))





  # print(len(df_test))
  # for i in range(len(df_test)):
  #   print(df_test['tweet_id'][i])

  # ids = df_test['tweet_id'][0]
  # url = create_url(ids)
  # headers = create_headers(bearer_token)
  # json_response = connect_to_endpoint(url, headers)
  # print(json.dumps(json_response, indent=4, sort_keys=True))
  #loop over df test and get id
  #create url
  #extract tweet
  #append tweet for the column

  # url = create_url(id)
  # headers = create_headers(bearer_token)
  # json_response = connect_to_endpoint(url, headers)
  # print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    # main()
    test_extract()