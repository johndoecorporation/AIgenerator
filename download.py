from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

songs_dir = os.getcwd() + '/songs/'


def download(playlist_url:str="https://www.youtube.com/playlist?list=PLo2kk5luT7QG6c9ASB0Ux9i21mxMKeK7b"):
    # Download video
    playlist = Playlist(playlist_url)
    for url in playlist:
        YouTube(url).streams.filter(only_audio=True).first().download(songs_dir)

    # Convert as Mp3
    for file in os.listdir(songs_dir):
        if re.search('mp4', file):
            mp4_path = os.path.join(songs_dir,file)
            mp3_path = os.path.join(songs_dir,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    