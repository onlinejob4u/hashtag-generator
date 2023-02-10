import random

def generate_hashtags(num_hashtags, tags_list):
    generated_tags = random.sample(tags_list, num_hashtags)
    return generated_tags

instagram_tags = ['#love', '#beautiful', '#happy', '#cute', '#like4like', '#followme', '#selfie', '#nature', '#picoftheday', '#fashion', '#photography', '#art', '#instagood', '#fun', '#summer', '#smile']
tiktok_tags = ['#fyp', '#fypシ', '#fyppage', '#fyp️', '#fyp💡', '#xyzbca', '#viral', '#tiktok', '#tiktokmemes', '#tiktokdance', '#tiktokmusic', '#tiktokgirls', '#tiktokboys', '#tiktokindia', '#tiktokusa', '#tiktokfunny']

generated_instagram_tags = generate_hashtags(25, instagram_tags)
generated_tiktok_tags = generate_hashtags(25, tiktok_tags)

print("Instagram Hashtags: ", generated_instagram_tags)
print("TikTok Hashtags: ", generated_tiktok_tags)
