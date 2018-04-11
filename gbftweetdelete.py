import twitter
import config

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_KEY,
                  access_token_secret=config.ACCESS_SECRET)


def def_keyword_str(query_mode='0'):
    keyword_str = None
    if query_mode == '0':  # Multi player raid
        print("Searching for multi player raid tweets...")
        if config.LANG == "EN":
            keyword_str = "I need backup!"
        else:
            keyword_str = "参加者募集！"
    elif query_mode == '1':  # Daily tweet for AP/BP recovery
        print("Searching for daily stamina recover tweets...")
        #if config.LANG == "EN":
        #   keyword_str = ""
        #else:
        keyword_str = "スマホRPGは今これをやってるよ"
    return keyword_str;


# Create the actual query
screen_name = api.VerifyCredentials().screen_name
input_mode = input("Type 0 to search for raid tweets and 1 for daily stamina recovery tweets: ")
query_str = "q={}&from={}&count=100".format(def_keyword_str(input_mode), screen_name)
results = api.GetSearch(raw_query=query_str)

tweet_count = len(results)
print("Found {} tweets in 7 days".format(tweet_count))

if tweet_count > 0:
    for thisStatus in results:
        print("\"{}\" created on {}".format(thisStatus.text, thisStatus.created_at))

    answer = input("Do you wish to proceed and delete all above tweets? Type 1 for yes: ")
    if answer == '1':
        for thisStatus in results:
            api.DestroyStatus(status_id=thisStatus.id)
