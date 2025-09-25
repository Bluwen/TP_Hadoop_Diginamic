#!/usr/bin/env python3
# -*-coding:utf-8 -*
import pandas as pd
import sys
import logging
 
logging.basicConfig(filename='debug.log',level=logging.DEBUG)
logging.debug("Entering mapper.py")


name_column = ["track_name","artist(s)_name","artist_count","released_year","released_month","released_day","in_spotify_playlists","in_spotify_charts","streams","in_apple_playlists","in_apple_charts","in_deezer_playlists","in_deezer_charts","in_shazam_charts","bpm","key","mode","danceability_%","valence_%","energy_%","acousticness_%","instrumentalness_%","liveness_%","speechiness_%","cover_url"]
df = pd.read_csv(sys.stdin, engine = "python", header = None, names = name_column)

for index, row in df.iterrows():
   print("%s\t%s\t\%i" %(row["danceability_%"], row["energy_%"], row["streams"]))