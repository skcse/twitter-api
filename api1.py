import tweepy
import pandas as pd
import json

#write all the keys 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# trends_tweets=api.trends_available()
# for tweet in trends_tweets:
#   if tweet['country']=='Japan':
#       print(tweet['url'])


# for status in tweepy.Cursor(api.user_timeline).items():
#     print(status.text)

# rtweets=api.search(q='#modi', result_type='recent', lang='en', count=1)
# for tweet in rtweets:
#   pd.read_json(tweet._json)
print("Number of tweets you want to store?")
k=int(input())
cnt=0
df=pd.DataFrame()
def process(self, status):
    arr={}
    arr['loc'] = status.user.location
    arr['text'] = status.text
    # arr['coords'] = status.coordinates
    arr['screen_name'] = status.user.screen_name
    arr['name']=status.user.name
    arr['user_created'] = status.user.created_at
    arr['followers_count'] = status.user.followers_count
    arr['id_str'] = status.id_str
    arr['created'] = status.created_at#arr['created']
    arr['retweet_count'] = status.retweet_count
    arr['favorite_count']=status.favorite_count
    arr['friends_count']=status.user.friends_count
    arr['description'] = status.user.description
    arr['language']=status.lang
    # arr['urls']=status.entities
    # for ar in arr:
    #     print(ar,'-->',arr[ar])
    # print("****************New user tweet********************")
    df2=pd.DataFrame(arr,index=[self.counter])
    df2.set_index(['id_str'],inplace=True)
    global df
    df=df.append(df2)
    df.to_csv('out.csv')
    # print(df)
print("List of top 10 trending in India")
def find_topic():
    count=0;
    topics=[]
    traffic= api.trends_available()
    for country in traffic:
        if country['name']=="India":
            wid=country['woeid']
    query=api.trends_place(wid)
    for q in query[0]['trends']:
        print('  ',q['name'])
        count+=1
        topics.append(q['name'])
        if count>=10:
            break
    return topics

class StreamListener(tweepy.StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 1
        self.limit = k+1

    def on_status(self, status):
        if status.retweeted:
            return
        if status.lang !='en':
            return
        process(self, status)
        print(' Number of tweets stored in csv file related to trending-->',self.counter,end="\r")
        # print(status._json)
        self.counter += 1
        if self.counter < self.limit:
            return True
        else:
            stream.disconnect()
    
        # print(status)
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
temp_list=find_topic()
stream.filter(track=temp_list)
print(" ")







# store=['id','text','place','retweet_count','favorite_count','lang','entities']    
    # stops = pd.DataFrame(file,columns=arr)
    # print(stops.head())


# for status in tweepy.Cursor(api.search,q='modi',result_type='recent').items(1):
#     #df=pd.DataFrame(data=status._json)
#     #print(df)
#     print("************************************************************************************************")
#     process(status._json)
