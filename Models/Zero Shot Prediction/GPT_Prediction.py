# -*- coding: utf-8 -*-
"""Chat-gpt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_tuFx0C04t9e4xx7yzl1M2LUwtp3z8t0
"""

import requests

# Define your API key and endpoint
api_key = ""
api_endpoint = "https://api.openai.com/v1/chat/completions"

# Define the data for your chat conversation

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "in one word only say yes or no without explaination whether this is a good etiquette -"},
    ]
}

import pandas as pd
import time
df=pd.read_csv('/content/India.csv',encoding='Latin-1')

sentences=list(df['0'])



master_list=[]

gpt_pred=[]
#c=0
for j in sentences:
 # c=c+1;
  #print(c)
  # Make the API request
  response = requests.post(
      api_endpoint,
      headers={"Authorization": f"Bearer {api_key}"},
      json=data
  )

  # Process the response
  if response.status_code == 200:
      result = response.json()
      assistant_response = result["choices"][0]["message"]["content"]
      gpt_pred.append(assistant_response)

  else:
      print("Error:", response.status_code, response.text)
      gpt_pred.append('Abstention')
  if c%100==0:
      time.sleep(1)

#gpt_pred



# prompt: create a new list and append gpt pred to that
for pred in gpt_pred:
  master_list.append(pred)



# prompt: convert masterlist to df then to c

master_list_df=pd.DataFrame(master_list)
master_list_df.to_csv('gpt_pred_India_P.csv', index=False)