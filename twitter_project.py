from TikTokApi import TikTokApi

def get_top_videos_in_last_24_hours():
    api = TikTokApi()
    trending_videos = api.trending(count=30)

    # Beğeni sayısına göre videoları sıralayın
    sorted_videos = sorted(trending_videos, key=lambda x: x['itemInfo']['itemStruct']['diggCount'], reverse=True)

    return sorted_videos

if __name__ == "__main__":
    top_videos = get_top_videos_in_last_24_hours()
    for index, video in enumerate(top_videos, start=1):
        print(f"{index}. Video URL: {video['itemInfo']['itemStruct']['video']['downloadAddr']}")
        print(f"   Beğeni Sayısı: {video['itemInfo']['itemStruct']['diggCount']}")
        print(f"   Yorum Sayısı: {video['itemInfo']['itemStruct']['commentCount']}")
        print(f"   Paylaşım Sayısı: {video['itemInfo']['itemStruct']['shareCount']}")
        print(f"   İzlenme Sayısı: {video['itemInfo']['itemStruct']['playCount']}")
        print("------------------------------------")
