import datetime
import random
from tiktokdata import get_trending_data
from tweeter import create_tweet
data = get_trending_data()
random_number = random.randint(0, 2)
if random_number == 0:
    tweet = {
        'part1': f"🔥The TikTok rundown for {datetime.datetime.now().strftime('%d %b, %Y')}:\n# 1️⃣ goes to... {data[0]['username']}{data[0]['is_verified']}🥳 | 🎵{data[0]['sound_used']}\n{data[0]['video_url']}\n❤️{data[0]['like_count']}\n💬{data[0]['comment_count']}\n🗣️{data[0]['share_count']}\n🎬{data[0]['play_count']}\n #trending #tiktok #tiktoktrending #allbottrending",
        'part2': ''
    }
    tweet['part2'] += f"""{datetime.datetime.now().strftime('%d %b, %Y')} -\n"""
    for i in range(1, len(data) if len(data) < 5 else 5):
        tweet['part2'] += f"""#{i+1} {data[i]['username']}{data[i]['is_verified']}\n{data[i]['video_url']}\n❤️{data[i]['like_count']}\n💬{data[i]['comment_count']}\n🗣️{data[i]['share_count']}\n🎬{data[i]['play_count']}\n~\n"""
elif random_number == 1:
    tweet = {
        'part1': f"🤖Data incoming... \n For {datetime.datetime.now().strftime('%d %b, %Y')}:\n {data[0]['username']}{data[0]['is_verified']} takes first!🙌\n🎵Sound: {data[0]['sound_used']}\n{data[0]['video_url']}\n👍Likes: {data[0]['like_count']}\n💭Comments: {data[0]['comment_count']}\n🤝Shares: {data[0]['share_count']}\n👀Views: {data[0]['play_count']}\n #trending #tiktok #tiktoktrending #allbottrending",
        'part2': ''
    }
    tweet['part2'] += f"""{datetime.datetime.now().strftime('%d %b, %Y')} -\n"""
    for i in range(1, len(data) if len(data) < 5 else 5):
        tweet['part2'] += f"""#{i+1} {data[i]['username']}{data[i]['is_verified']}\n{data[i]['video_url']}\n👍Likes: {data[i]['like_count']}\n💭Comments: {data[0]['comment_count']}\n🤝Shares: {data[i]['share_count']}\n👀Views: {data[i]['play_count']}\n~\n"""
elif random_number == 2:
    tweet = {
        'part1': f"TOP TRENDING FOR {datetime.datetime.now().strftime('%d %b, %Y')}:\n🏆{data[0]['username']}{data[0]['is_verified']}🏆 | 🎵{data[0]['sound_used']}\n{data[0]['video_url']}\n💬{data[0]['comment_count']}\n❤️{data[0]['like_count']}\n🎬{data[0]['play_count']}\n #trending #tiktok #tiktoktrending #allbottrending",
        'part2': ''
    }
    tweet['part2'] += f"""{datetime.datetime.now().strftime('%d %b, %Y')} -\n"""
    for i in range(1, len(data) if len(data) < 5 else 5):
        tweet['part2'] += f"""#{i+1} {data[i]['username']}{data[i]['is_verified']}\n{data[i]['video_url']}\n💬{data[i]['comment_count']}\n❤️{data[i]['like_count']}\n🎬{data[i]['play_count']}\n~\n"""
create_tweet(tweet)