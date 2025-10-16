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

| 変数名 | 説明 | 必須 | デフォルト |
| --- | --- | --- | --- |
| `OPENAI_API_KEY` | OpenAI API の API キー | はい | - |
| `WHISPER_MODEL` | Whisper モデル名 (`tiny`, `base`, `small`, `medium`, `large`, `tiny.en`, `base.en`, `small.en`) | いいえ | `base` |

より詳細な設定項目は [設定リファレンス](docs/configuration.md) を参照してください。

## 関連ドキュメント

- [ローカル動作確認ガイド](docs/local-testing.md)
