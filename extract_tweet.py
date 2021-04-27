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
    response_json_keys = response.json().keys()
    # if status code is 200 or json returned an error
    if response.status_code != 200 or "errors" in response_json_keys:
      return None #if there url tweet id is invalid
    return response.json()

def main():
  bearer_token = auth()
  url = create_url()
  headers = create_headers(bearer_token)
  json_response = connect_to_endpoint(url, headers)
  print(json.dumps(json_response, indent=4, sort_keys=True))

def nullify_tweet_col(df):
    df['tweet'] = None
    return df

def test_extract():
  bearer_token = auth()
  df_test = pd.read_csv('./dataset/train.csv')
  df = nullify_tweet_col(df_test)

  #loop over df
  for i in range(6):
    ids = df['tweet_id'][i]
    url = create_url(ids)
    
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)

    #if json response is not None
    if json_response is not None:
      #get the text
      text = json_response['data'][0]['text']
      print(text)
      #append the text to the df 
      df['tweet'][i] = text

  print(df.head())

if __name__ == "__main__":
    # main()
    test_extract()