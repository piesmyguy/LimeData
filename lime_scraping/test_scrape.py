#TwitterAccounts:
#First Name: tws, DOB: 1/2/2000, Gender: F, 

#Acccount 1: tws9157899267, tws17937@gmail.com, 87z-vKH9#8jo1h0c[/Q7

import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`

    #Have a database of acccouts to add
    #await api.pool.add_account("tws9157899267", "87z-vKH9#8jo1h0c[/Q7", "tws17937@gmail.com", "87z-vKH9#8jo1h0c[/Q7")
    await api.pool.login_all()

    #Pull accountName db and corresponding account info, obtain required info
    user_logins = ["CryptoGodJohn"]
    acct = []
    for user_login in user_logins:
        acct.append(await api.user_by_login(user_login))

    #print(acct.dict()['id'])
    #acct_id = acct.dict()['id']
    
    #Work out how to filter these tweets: by time is easy using data, pulling tokens using cashtags is easy,
    #Work out api to get sentiment of tweet
    tweets = await gather(api.user_tweets(acct_id, limit=5))
    #Loop through and write each tweet to a file
    with open('tweets.txt', 'w') as f:
        for tweet in tweets:
            f.write(tweet.json())
            f.write('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
  
    # user info
    # user_id = 2244994945
    # await api.user_by_id(user_id)  # User
    # await gather(api.followers(user_id, limit=20))  # list[User]
    # await gather(api.following(user_id, limit=20))  # list[User]
    # await gather(api.user_tweets(user_id, limit=20))  # list[Tweet]
    # await gather(api.user_tweets_and_replies(user_id, limit=20))  # list[Tweet]

    # change log level, default info
    set_log_level("DEBUG")


if __name__ == "__main__":
    asyncio.run(main())
    
    
    