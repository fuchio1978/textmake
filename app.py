import io
import os
import importlib
import tempfile
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"wav", "mp3", "m4a", "flac", "ogg", "webm"}
UPLOAD_DIR = Path(tempfile.gettempdir()) / "textmake_uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.environ.get("TEXTMAKE_SECRET_KEY", "change-this-secret")


_model_cache = None


def _load_model():
    global _model_cache
    if _model_cache is None:
        try:
            whisper = importlib.import_module("whisper")
        except ModuleNotFoundError as exc:  # pragma: no cover - runtime feedback
            raise RuntimeError(
                "whisper パッケージが見つかりません。requirements.txt を使って依存関係をインストールしてください。"
            ) from exc

        model_name = os.environ.get("TEXTMAKE_WHISPER_MODEL", "base")
        _model_cache = whisper.load_model(model_name)
    return _model_cache


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        flash("音声ファイルが見つかりません。ファイルを選択してください。")
        return redirect(url_for("index"))

    uploaded_file = request.files["audio"]

    if uploaded_file.filename == "":
        flash("ファイルが選択されていません。")
        return redirect(url_for("index"))

    if not allowed_file(uploaded_file.filename):
        flash("対応していないファイル形式です。wav, mp3, m4a, flac, ogg, webm に対応しています。")
        return redirect(url_for("index"))

    filename = secure_filename(uploaded_file.filename)
    suffix = Path(filename).suffix

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix, dir=UPLOAD_DIR) as temp_audio:
        uploaded_file.save(temp_audio.name)
        temp_path = Path(temp_audio.name)

    model = _load_model()

    try:
        result = model.transcribe(str(temp_path))
    except Exception as exc:  # pragma: no cover - runtime feedback
        temp_path.unlink(missing_ok=True)
        flash(f"文字起こし中にエラーが発生しました: {exc}")
        return redirect(url_for("index"))

    temp_path.unlink(missing_ok=True)

    transcript_text = result.get("text", "").strip()

    if not transcript_text:
        flash("文字起こし結果が空でした。別の音声ファイルでお試しください。")
        return redirect(url_for("index"))

    text_stream = io.BytesIO(transcript_text.encode("utf-8"))
    text_stream.seek(0)
    download_name = Path(filename).with_suffix(".txt").name

    return send_file(
        text_stream,
        mimetype="text/plain",
        as_attachment=True,
        download_name=download_name,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
