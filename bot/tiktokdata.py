import requests
import pyshorteners
def get_trending_data():
	url = "https://tiktok_solutions.p.rapidapi.com/trending/US"

	querystring = {"custom_cursor":""}

	headers = {
		"X-RapidAPI-Key": "66686e774dmsh02ecbf6f05cc5d7p1ea5bcjsn31fdccd6cac2",
		"X-RapidAPI-Host": "tiktok_solutions.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring).json()

	data = []
	for video in response['data']['list']:
		try:
			if video['author']['custom_verify']:
				if video['author']['custom_verify'] == 'Verified account':
					verified = '✅'
				else:
					verified = ''
		except:
			verified = ''
		# Shorten numbers
		likes = shorten_number(int(video['statistics']['digg_count']))
		plays = shorten_number(int(video['statistics']['play_count']))
		shares = shorten_number(int(video['statistics']['share_count']))
		comments = shorten_number(int(video['statistics']['comment_count']))
		# Shorten video url
		video_link = pyshorteners.Shortener().tinyurl.short(video['share_url'])
		# Append data to list
		data.append({
			'username': video['author']['nickname'],
			'video_url': video_link,
			'sound_used': video['music']['title'],
			'play_count': plays,
			'like_count': likes,
			'is_verified': verified,
			'share_count': shares,
			'comment_count': comments,
		})
	return data

#function that will shorten a large number
def shorten_number(number):
	if number >= 1000000:
		return str(round(number/1000000, 1)) + 'M'
	elif number >= 1000:
		return str(round(number/1000, 1)) + 'K'
	else:
		return str(number)