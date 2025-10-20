# app.py (faster-whisper 版)
import os
import tempfile
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from faster_whisper import WhisperModel

app = Flask(__name__)
app.secret_key = os.environ.get("TEXTMAKE_SECRET_KEY", "change-this-secret")

MODEL_NAME = os.environ.get("TEXTMAKE_WHISPER_MODEL", "base")
# CPUでも速め：int8。GPUがあれば compute_type="float16" 等に変更可
model = WhisperModel(MODEL_NAME, compute_type="int8")

ALLOWED_EXTS = {".mp3", ".wav", ".m4a", ".mp4", ".aac", ".wma", ".flac", ".webm", ".ogg"}

def allowed_file(filename: str) -> bool:
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED_EXTS

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/transcribe")
def transcribe():
    if "audio" not in request.files:
        flash("音声ファイルが見つかりません。")
        return redirect(url_for("index"))

    f = request.files["audio"]
    if f.filename == "":
        flash("ファイルが選択されていません。")
        return redirect(url_for("index"))

    if not allowed_file(f.filename):
        flash("対応していない拡張子です。mp3, wav, m4a, mp4 などをお試しください。")
        return redirect(url_for("index"))

    # 一時保存
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(f.filename)[1]) as tmp_in:
        f.save(tmp_in.name)

    # 日本語メインなら language="ja" 推奨
    segments, info = model.transcribe(tmp_in.name, language="ja", beam_size=5)
    text = "".join(seg.text for seg in segments).strip()

    # テキストを一時ファイルに書き出し、ダウンロード
    out_path = tempfile.NamedTemporaryFile(delete=False, suffix=".txt").name
    with open(out_path, "w", encoding="utf-8") as fw:
        fw.write(text)

    return send_file(out_path, as_attachment=True, download_name="transcript.txt", mimetype="text/plain")
