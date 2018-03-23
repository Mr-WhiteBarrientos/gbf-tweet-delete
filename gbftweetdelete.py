import twitter
import config

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_KEY,
                  access_token_secret=config.ACCESS_SECRET)

screen_name = api.VerifyCredentials().screen_name
#screen_name = 'konnpeki27'

keyword_str = '参加者募集！'
if config.lang == 'EN':
    keyword_str = 'I need backup!'

# Searching for tweets of multiplayer raids with since value hardcoded since gbf happened
query_str = "q={}&from={}&since=2014-03-10&count=100".format(keyword_str, screen_name)
results = api.GetSearch(raw_query=query_str)

print(len(results))
for thisStatus in results:
    print("\"{}\" created on {}".format(thisStatus.text, thisStatus.created_at))

answer = input("Do you wish to proceed and delete all above tweets? Type 1 for yes:")
if answer == '1':
    for thisStatus in results:
        api.DestroyStatus(status_id=thisStatus.id)

# Future implementation: スマホRPGは今これをやってるよ。
