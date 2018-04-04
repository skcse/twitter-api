import pandas as pd
def search(target,key):
    df = pd.read_csv('out.csv')
    a = df[df[target]>=key] 
    print(a['text'])

def search_str(target,key):
    df = pd.read_csv('out.csv')
    a = df[df[target]==key] 
    print(a['text'])

arr=["name","screen_name", "retweet_count", "favorite_count","friends_count", "followers_count", "tweet_created"]
print("\n  Enter 1 for sorting by text or Enter 2 for filter")
n=int(input())
if n==1:
	df=pd.read_csv('out.csv')
	a=df.sort_values(by='text')
	print("\n  Sorted by tweets\n")
	print(df['text'])
if n==2:
	print("\n  Applying filters")
	print("\n  Press 1 for name, Press 2 screen_name,Press 5 friends_count, Press 6 followers_count")
	k=int(input())
	if k<=2:
		print("\n  Enter ", arr[k-1]," to see the tweet\n")
		st=input()
		search_str(arr[k-1],st)
	elif k==6 or k==5:
		print("\n",arr[k-1],"greater than ?")
		num=int(input())
		print("\n  tweets of users whose",arr[k-1],"is greater than",num,"\n")
		search(arr[k-1],num)
	else:
		print("\n  Invalid Input")