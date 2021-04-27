import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

#load .env variables
load_dotenv()

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
    print(response.json())
    response_json_keys = response.json().keys()
    # print(response_json_keys)
    # if status code is 200 or json returned an error
    if response.status_code != 200 or "errors" in response_json_keys:
      return None #if there url tweet id is invalid
    return response.json()

def nullify_tweet_col(df):
  """Adds a column named tweet will null values"""
  df['tweet'] = None
  return df

def extract(df):
  bearer_token = auth()
  df = nullify_tweet_col(df)
  #loop over df
  for i in range(len(df)):
    ids = df['tweet_id'][i]
    url = create_url(ids)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    #if json response is not None
    if json_response is not None:
      #get the text
      text = json_response['data'][0]['text']
      #append the text to the df 
      df['tweet'][i] = text
  # print(df.head())
  return df

def write_to_file(df, filename):
  df.to_csv(f'./data_preprocess/{filename}')

def main():
   #get train data
    # df_train = pd.read_csv('./dataset/train.csv')
    # df = extract(df_train)
    # filename = 'train.csv'
    # write_to_file(df, filename)

    #get test data
    df_test = pd.read_csv('./dataset/test.csv')
    df = extract(df_test)
    filename = 'test.csv'
    write_to_file(df, filename)

    #get dev data

if __name__ == "__main__":
    main()
    