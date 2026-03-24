from flask import Flask, jsonify
import yt_dlp

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"status": "ok", "message": "yt-dlp audio service is running"})


@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200


@app.route('/get_audio/<video_id>/')
def get_audio(video_id):
    URL = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'quiet': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(URL, download=False)
            audio_url = info.get("url")
            if not audio_url:
                return jsonify({"error": "Could not extract audio URL"}), 404
            return jsonify({"url": audio_url})
    except yt_dlp.utils.DownloadError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "detail": str(e)}), 500


if __name__ == '__main__':
    app.run()