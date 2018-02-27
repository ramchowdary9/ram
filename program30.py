import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "hijMTmSvfz4cydIyglVVSk6ZL",
    "consumer_secret"     : "pvlZzBDw0y6vIe5okG6Zu9AF2xdFTljj0gCWCPSIW3QThzrhBv",
    "access_token"        : "891242686321090561-oK8T3TygtYmtOebowEeg5czVAZXX0QZ",
    "access_token_secret" : "Zk0VBNiYCtlftzt6vmBvze4jihMkOVBALaEr2xPgAM3ma" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
