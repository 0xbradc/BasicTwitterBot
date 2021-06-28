################################
#          Welcome to          #
#          Tweet Bot!          #
#    Created 01 / 16 / 2020    #
#       By Brad Campbell       #
################################

import tweepy;
import time;

# Authenticates to Twitter
consumer_key = ""
consumer_secret = ""
public_key = ""
secret_key = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
auth.set_access_token(public_key, secret_key);

# Creates API object
api = tweepy.API(
  auth, 
  wait_on_rate_limit=True, 
  wait_on_rate_limit_notify=True);
try:
  api.verify_credentials();
  print("************************");
  print("*      Welcome to      *");
  print("*      Tweet Bot!      *");
  print("************************");
  print("✓ Authentication Successful ✓\n\n");
except:
  print("An error occurred during authentication.\nVerify that Twitter API and Token Keys are correct.\n");


replyList = ["Reponse 1", "Reponse 2", "Reponse 3", "Reponse 4", "Reponse 5"];


def getRandomReply(reply_count):
  return replyList[reply_count];


def autoReply(status_id, reply_count):
  username = api.get_status(status_id).user.screen_name;
  api.update_status( 
    status = ('@'+ username + "  " + getRandomReply(reply_count)), 
    in_reply_to_status_id = status_id
  );


def main():
  reply_count = 0;
  listID = 0; # Create a twitter list and put its ID into this number
  currentTweetID = (api.list_timeline(list_id = listID)[0].id) + 1;

  
  while (input("Type anything to terminate process:\n")):
    rev_timeline = reversed(api.list_timeline(list_id = listID));
    for status in rev_timeline:
      if (currentTweetID < status.id):
        currentTweetID = status.id;
        print("Status ID: " + str(status.id));
        if (reply_count <= len(replyList)):
          reply_count = (reply_count + 1);
        else:
          reply_count = 0;
        autoReply(status.id, reply_count);
      time.sleep(60); # 1 minute loop


# Final method call
if __name__ == "__main__":
  main();
  
