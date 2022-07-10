from requests_oauthlib import OAuth1Session
import datetime
from decouple import config
import json

def create_tweet(tweet_dict):
    # Access tokens
    consumer_key = config('CONSUMER_KEY')
    consumer_secret = config('CONSUMER_SECRET')
    access_token = config('ACCESS_TOKEN')
    access_token_secret = config('ACCESS_TOKEN_SECRET')
    print(consumer_key, consumer_secret, access_token, access_token_secret)

    # Get request token
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    tweet_list = [tweet_dict['part1']]
    # Convert text into split tweets
    splice_tweet = trim(tweet_dict['part2'])
    # Add split tweets to list
    for item in splice_tweet:
        tweet_list.append(item)

    for tweet in tweet_list:
        # Convert the text to a json object
        payload = {"text": tweet}
        # Making the request
        response = oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    return(json.dumps(json_response, indent=4, sort_keys=True))

def find_punctuation(sequence):
    '''
    returns the end point closest to 280 with a punctuation in it
    returns 0 if not found (ie a string with no punctuation in it at all
    '''
    punctuation = '~'
    if len(sequence) <= 200:
        return len(sequence)
    for end in range(199, 0, -1):
        if sequence[end] in punctuation:
            return end +1
    return 0

def find_space(sequence):
    '''
    returns the end point closest to 137 with a space in it
    returns 0 if not found (ie a string with no punctuation in it at all
    '''
    if len(sequence) <= 200:
        return len(sequence)
    for end in range(199, 0, -1):
        if sequence[end] == ' ':
            return end+1
    return 0

def trim(sequence):
    '''
    simple version:  returns a list of strings split on punctuation, closest to
    270
    '''

    result = []
    while sequence:
        end = find_punctuation(sequence)
        if not end:
            # ok, no endpoint found so slice at 137, unless the len of the
            # sequence is now shorter
            end = min(260,len(sequence))
        result.append(sequence[0:end].strip())
        sequence = sequence[end:]

    # add prefix to each tweet if result is longer than 1
    if len(result) > 1:
        for i in range(1, len(result)):
            result[i] = f"{datetime.datetime.now().strftime('%d %b, %Y')} -\n" + result[i]
    for i in range(len(result)):
        result[i] = result[i] + '\n#trending'
    return result