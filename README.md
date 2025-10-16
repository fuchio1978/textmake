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

## ライセンス

MIT License

## 環境変数

利用可能な環境変数の一覧や設定例は [設定リファレンス](docs/configuration.md) にまとめています。用途ごとの詳しい説明や推奨値が必要な場合はそちらを参照してください。

## 関連ドキュメント

- [ローカル動作確認ガイド](docs/local-testing.md)
