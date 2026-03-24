from flask import Flask
import yt_dlp
import json
app = Flask(__name__)

@app.route('/get_audio/<video_id>/')
def returnJSON(video_id):
    URL = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
        print(info["url"])
        return info["url"]