#!/usr/bin/env python
# coding: utf-8

# In[12]:

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import Stream

# In[6]:
import socket, json

# In[ ]:
consumer_key = '8x1lrPMIzL6o5zGzCoE1Knf0d'
consumer_secret = 'YnMtV5meYJVbjRmUEm5mu6jyCfOP2AKyHiqZzzkTTRPnS41nv8'
access_token = '1488708070419095552-laXXm5ywYPJKWajKEanXT2xx2TOoHC'
access_secret = 'VhIXfp6pkzgO7I4g0wfcBZSPGXURQcZkAgCxl97XyDzaQ'

# In[2]:
class TweetListener(Stream):
    def __init__(self, *args, csocket):
        super().__init__(*args)
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("ERROR ", e)
        
        return True
    
    def on_error(self, status):
        print(status)
        return True


# In[13]:


def send_data(c_socket):
    twtr_stream = TweetListener(
        consumer_key, consumer_secret,
        access_token, access_secret,
        csocket=c_socket
    )
    twtr_stream.filter(track=['$SHIB','Shiba Inu', 'Shiba', 'ShibaInu'])
    Stream()


# In[8]:


if __name__ == '__main__':
    s = socket.socket()
    host = '127.0.0.1'
    port = 9999
    s.bind((host, port))
    
    print(f'listening on port {port}')
    
    s.listen(3)
    c, addr = s.accept()
    
    send_data(c)   
