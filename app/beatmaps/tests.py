import psycopg2
from datetime import datetime, timedelta
from requests import get

conn = psycopg2.connect(
        host="localhost",
        database="osu_maps",
        user="postgres",
        password="12345",
        port=5432
    )

cur = conn.cursor()

KEY = "cedb7fcf648182733cfed8f3b78eb53c4ddb0663"

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

start_time = datetime.now() 

print("Adding maps..")
print(f"Start time: {start_time}")

params = {
    "k": KEY,
    "m": 0,
    "since": start_time - timedelta(days=1)
}

response = get(url="https://osu.ppy.sh/api/get_beatmaps", params=params)

data = response.json()

if data:
    for beatmap in data:

        title = beatmap["title"]
        artist = beatmap["artist"]
        mapper = beatmap["creator"]
        source = beatmap["source"]

        link = f"https://osu.ppy.sh/beatmapsets/{beatmap['beatmapset_id']}#osu/{beatmap['beatmap_id']}"
        image = f"https://assets.ppy.sh/beatmaps/{beatmap['beatmapset_id']}/covers/cover.jpg"

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
        song_id = beatmap['beatmapset_id']

        if beatmap["approved"] not in ("3", "0", "-1"):

            cur.execute("INSERT INTO beatmaps_beatmap (title, artist, mapper, source, link, image, genre, language, map_type, total_length, play_count, favourite_count, star_difficulty, bpm, ar, od, hp, cs, submit_date, song_id) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                        (title, artist, mapper, source, link, image, genre, language, map_type, total_length, play_count, favourite_count, star_difficulty, bpm, ar, od, hp, cs, submit_date, song_id))
            
            conn.commit()


end_time = datetime.now()

print("Complete")
print(f"End time: {end_time}")
print(f"Total time: {end_time - start_time}")

cur.close()
conn.close()

