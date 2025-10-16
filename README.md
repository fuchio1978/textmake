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
| `TEXTMAKE_SECRET_KEY` | Flask のセッション暗号化に利用するシークレットキー。開発用途では既定値のままでも動作しますが、本番運用では十分に長く予測困難な値に変更してください。 | いいえ | `change-this-secret` |
| `TEXTMAKE_WHISPER_MODEL` | 使用する Whisper モデル名。`tiny`, `base`, `small`, `medium`, `large` などから選択でき、モデルが大きいほど精度が高くなりますが推論時間と必要リソースも増加します。 | いいえ | `base` |

設定例や追加のカスタマイズ項目は [設定リファレンス](docs/configuration.md) を参照してください。

## 関連ドキュメント

- [ローカル動作確認ガイド](docs/local-testing.md)
