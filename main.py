from flask import Flask, send_from_directory
import subprocess
import os

app = Flask(__name__)

HLS_DIR = "hls"
STREAM_URL = "http://kongking.shop:80/uCJ5tSYJZ5/bZtDNkpxuN/234398"

# Crear carpeta si no existe
if not os.path.exists(HLS_DIR):
    os.makedirs(HLS_DIR)

def start_ffmpeg_stream():
    command = [
        "ffmpeg",
        "-i", STREAM_URL,
        "-c:v", "copy",
        "-c:a", "aac",
        "-f", "hls",
        "-hls_time", "5",
        "-hls_list_size", "5",
        "-hls_flags", "delete_segments",
        f"{HLS_DIR}/stream.m3u8"
    ]
    subprocess.Popen(command)

@app.route('/')
def index():
    return 'Servidor Flask funcionando con FFmpeg y HLS'

@app.route('/hls/<path:filename>')
def stream_file(filename):
    return send_from_directory(HLS_DIR, filename)

if __name__ == '__main__':
    start_ffmpeg_stream()
    app.run(host='0.0.0.0', port=10000)
