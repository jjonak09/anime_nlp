with open('animeinfo_100year.txt',mode='r',encoding='utf-8') as f:
    anime = f.read()
# print(anime)

anime = anime.split('\n')
# print(len(anime))
# print(anime[0])
with open('animetitle_100year_only_tv.txt',mode='w') as f:

    for i in range(len(anime)-1):
        anime_title = anime[i].split(',')
        if anime_title[1] == "TV":

            f.write(anime_title[4]+'\n')
        # print(anime_title[4])
