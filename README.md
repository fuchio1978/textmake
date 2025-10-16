# textmake

Whisper を利用した音声文字起こし Web アプリです。音声ファイルをアップロードするとテキストに変換し、結果をダウンロードできます。

## セットアップ

1. 依存関係をインストールします。
   ```bash
   pip install -r requirements.txt
   ```
2. 環境変数を設定します（必要に応じて `.env` を利用してください）。
3. アプリを起動します。
   ```bash
   flask --app app run --host 0.0.0.0 --port 5000 --debug
   ```

詳しい手順は [docs/setup.md](docs/setup.md) を参照してください。

## 環境変数

| 変数名 | 説明 | 既定値 |
| ------ | ---- | ------ |
| `TEXTMAKE_SECRET_KEY` | Flask セッションに利用するシークレットキー。開発環境では任意の文字列、本番では十分に長く予測困難な値を設定してください。 | `change-this-secret` |
| `TEXTMAKE_WHISPER_MODEL` | Whisper モデル ID。`tiny`, `base`, `small`, `medium`, `large-v2` などから選択できます。モデルが大きいほど精度が向上しますが処理時間は長くなります。 | `base` |

より詳しい説明は [docs/configuration.md](docs/configuration.md) を参照してください。

## ローカル動作確認

サンプル音声を使った確認手順やトラブルシューティングは [docs/local-testing.md](docs/local-testing.md) にまとめています。

## 関連ドキュメント

- [アプリ概要](docs/overview.md)
- [セットアップガイド](docs/setup.md)
- [ローカル動作確認ガイド](docs/local-testing.md)
- [設定リファレンス](docs/configuration.md)
- [音声文字起こし Web アプリ構築ガイド](docs/create-web-app-for-audio-file-transcription-Bulab.md)
