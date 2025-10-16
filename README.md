# textmake

音声ファイルをアップロードするとテキストファイルに変換してダウンロードできるシンプルな Web アプリです。OpenAI Whisper モデルを使用して音声を自動的に文字起こしします。

## セットアップ

1. 依存関係をインストールします。

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   > Whisper の利用には FFmpeg が必要です。未インストールの場合は各 OS の方法に従ってインストールしてください。

2. アプリケーションを起動します。

   ```bash
   flask --app app run --host 0.0.0.0 --port 5000 --debug
   ```

   初回実行時は Whisper モデルのダウンロードに時間がかかる場合があります。

3. ブラウザで `http://localhost:5000` にアクセスし、音声ファイルをアップロードしてください。変換が完了するとテキストファイルがダウンロードされます。

## 参考ドキュメント

- ローカルでの文字起こしテスト手順: [docs/local-testing.md](docs/local-testing.md)

## 環境変数

| 変数名 | 説明 | 既定値 |
| ------ | ---- | ------ |
| `TEXTMAKE_SECRET_KEY` | Flask のセッション管理に使用するシークレットキー | `change-this-secret` |
| `TEXTMAKE_WHISPER_MODEL` | 使用する Whisper モデル名 (`tiny`, `base`, `small`, `medium`, `large` など) | `base` |

## ライセンス

MIT License
