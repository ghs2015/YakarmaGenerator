import time
import praw
r=praw.Reddit('PRAW top post saver by /u/another_asian_')

def crawlinit():
	f = open("test.txt","w")
	count=2
	while count>0:
		 #opens file with name of "test.txt"
		subreddit=r.get_subreddit('showerthoughts')
		for submission in subreddit.get_top_from_all(limit=None):
			f.write(submission.title+"\n")
		time.sleep(2)
		count= count - 1
	f.close()

def crawlupdate():
	f = open("test.txt","a")
	count=2
	while count>0:
		 #opens file with name of "test.txt"
		subreddit=r.get_subreddit('showerthoughts')
		for submission in subreddit.get_hot(limit=10):
			f.write(submission.title+"\n")
		time.sleep(2)
		count= count - 1
	f.close()