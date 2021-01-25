################################
#        Welcome to the        #
#       Barstool Newtech       #
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
  print("*    Welcome to the    *");
  print("*   Barstool Newtech   *");
  print("*      Tweet Bot!      *");
  print("************************");
  print("✓ Authentication Successful ✓\n\n");
except:
  print("An error occurred during authentication.\nVerify that Twitter API and Token Keys are correct.\n");


replyList = [];
def getRandomReply(replyCount):
  replyList.append("Response 1");
  replyList.append("Response 2");
  replyList.append("Response 3");
  replyList.append("Response 4");
  replyList.append("Response 5");
  replyList.append("Response 6");
  replyList.append("Response 7");
  return replyList[replyCount];


def autoReply(statusID, replyCount):
  username = api.get_status(statusID).user.screen_name;
  api.update_status( 
    status = ('@'+ username + "  " + getRandomReply(replyCount)), 
    in_reply_to_status_id = statusID
  );


def main():
  replyCount = 0;
  listID = 0; # Create a twitter list and put its ID into this number
  currentTweetID = (api.list_timeline(list_id = listID)[0].id) + 1;

  
  while (input("Type anything to terminate process:\n")):
    revTimeline = reversed(api.list_timeline(list_id = listID));
    for status in revTimeline:
      if (currentTweetID < status.id):
        currentTweetID = status.id;
        print("Status ID: " + str(status.id));
        if (replyCount <= len(replyList)):
          replyCount = (replyCount + 1);
        else:
          replyCount = 0;
        autoReply(status.id, replyCount);
      time.sleep(60); # 1 minute loop


# Final method call
main();
