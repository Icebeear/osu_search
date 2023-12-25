import psycopg2

import asyncio
from aiohttp import ClientSession

from datetime import datetime
import os 

conn = psycopg2.connect(
    host="postgres",
    database="osu_maps",
    user="osu_user",
    password="12345",
    port=5432
)

cur = conn.cursor()

API_KEY = os.environ.get('API_KEY')

genres = {
    "0": "any",
    "1": "unspecified",
    "2": "video game",
    "3": "anime",
    "4": "rock",
    "5": "pop",
    "6": "other",
    "7": "novelty",
    "9": "hip hop",
    "10": "electronic",
    "11": "metal",
    "12": "classical",
    "13": "folk",
    "14": "jazz"
}

languages = {
    "0": "any",
    "1": "unspecified",
    "2": "english",
    "3": "japanese",
    "4": "chinese",
    "5": "instrumental",
    "6": "korean",
    "7": "french",
    "8": "german",
    "9": "swedish",
    "10": "spanish",
    "11": "italian",
    "12": "russian",
    "13": "polish",
    "14": "other"
}

map_types = {
    "4": "loved",
    "3": "qualified",
    "2": "approved",
    "1": "ranked",
    "0": "pending",
    "-1": "WIP",
    "-2": "graveyard"
}

maps = 0

async def get_maps(year, month, day):
    global maps 
    beatmapset_link = "https://osu.ppy.sh/beatmapsets/"
    asset_link = "https://assets.ppy.sh/beatmaps/"

    async with ClientSession() as session:

        params = {
            "k": API_KEY,
            "m": 0,
            "since": f"{year}-{month}-{day} 00:00:01",
        }

        url = "https://osu.ppy.sh/api/get_beatmaps"

        async with session.get(url=url, params=params) as response:
            try:
                data = await response.json()
            except:
                print(f"Status code {response.status}, too many requests")
            else:
                for beatmap in data:
                    mapset_id = beatmap['beatmapset_id']
                    title = beatmap["title"]
                    artist = beatmap["artist"]
                    mapper = beatmap["creator"]
                    source = beatmap["source"]

                    link = f"{beatmapset_link}{mapset_id}#osu/{beatmap['beatmap_id']}"
                    image = f"{asset_link}{mapset_id}/covers/cover.jpg"

                    genre = genres[beatmap["genre_id"]]
                    language = languages[beatmap["language_id"]]
                    map_type = map_types[beatmap["approved"]]
                    
                    total_length = int(beatmap["total_length"])
                    play_count = int(beatmap["playcount"])
                    favourite_count = int(beatmap["favourite_count"])

                    star_difficulty = float(beatmap["difficultyrating"])
                    bpm = float(beatmap["bpm"])
                    ar = float(beatmap["diff_approach"])
                    od = float(beatmap["diff_overall"])
                    hp = float(beatmap["diff_drain"])
                    cs = float(beatmap["diff_size"])

                    submit_date = beatmap["approved_date"]
                    song_id = mapset_id

                    if beatmap["approved"] not in ("3", "0", "-1"):

                        cur.execute("INSERT INTO beatmaps (title, artist, mapper,\
                                    source, link, image, genre, language, \
                                    map_type, total_length, \
                                    play_count, favourite_count, star_difficulty, \
                                    bpm, ar, od, hp, cs, submit_date, song_id) \
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, \
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                                    (title, artist, mapper, source, link, image, 
                                        genre, language, map_type, total_length, 
                                        play_count, favourite_count, 
                                        star_difficulty, bpm, ar, 
                                        od, hp, cs, submit_date, song_id)
                        )

                        maps += 1 
                        conn.commit() 
        

async def main():
    tasks = []
    with open("leetcode/data.txt", "r") as file:
        for line in file.readlines():
            year, month, day = line.strip().split()
            tasks.append(asyncio.create_task(get_maps(year, month, day)))
    
    for task in tasks:
        await task 


start_time = datetime.now()
print("Adding maps..")
print(f"Start time: {start_time}")

asyncio.run(main())

end_time = datetime.now()
print("Complete")
print(f"End time: {end_time}")
print(f"Total time: {end_time - start_time}")
print(f"total maps: {maps}")