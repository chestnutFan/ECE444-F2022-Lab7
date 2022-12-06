import requests, json
import urllib.parse
from time import time

ENDPOINT = "http://flask-env1.eba-9b9f2p8a.us-east-2.elasticbeanstalk.com/"

def api_latency_cal(text):
    """
    Call API 100 times and calculate the average response time.
    """
    params = {'text': text}
    time = 0

    for i in range(100):
        result = requests.get(f'{ENDPOINT}detector?{urllib.parse.urlencode(params)}')
        time += result.elapsed.microseconds # in ms

    average_time = time / 100

    print(text)
    print(f'Average response time is {average_time} ms')

api_latency_cal("Mark Zuckerberg is unveiled to be an alien") 
api_latency_cal("UofT has changed its full name to University of Tears") 
api_latency_cal("The Federal Reserve will continue to raise interest rates in 2023")
api_latency_cal("Salesforce Co-CEO Bret Taylor is going to step down") 

