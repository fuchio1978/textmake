# 設定リファレンス

アプリの動作を調整するために利用できる主な環境変数や、関連する設定項目をまとめています。

## 環境変数

| 変数名 | 説明 | 既定値 |
| ------ | ---- | ------ |
| `TEXTMAKE_SECRET_KEY` | Flask のセッション管理に使用するシークレットキー。開発環境では任意の文字列でも構いませんが、本番運用する場合は十分に長く予測困難な値に変更してください。 | `change-this-secret` |
| `TEXTMAKE_WHISPER_MODEL` | 使用する Whisper モデル名。`tiny`, `base`, `small`, `medium`, `large` などから選択できます。モデルが大きくなるほど精度は向上しますが、初回ダウンロードと推論に時間がかかります。 | `base` |

## Whisper モデルを変更する場合

1. `.env` などに `TEXTMAKE_WHISPER_MODEL` を設定します。例: `export TEXTMAKE_WHISPER_MODEL=small`。
2. アプリを再起動すると新しいモデルがダウンロード・利用されます。
3. 既にダウンロードされたモデルは `~/.cache/whisper` に保存されるため、必要に応じて削除することでディスク容量を確保できます。

## シークレットキーを変更する場合

`TEXTMAKE_SECRET_KEY` は Flask のセッション暗号化に利用されます。デバッグ目的であっても、環境変数や `.env` ファイルで明示的に設定しておくと便利です。

```bash
export TEXTMAKE_SECRET_KEY="your-secure-secret"
flask --app app run --debug
```

## 関連情報

- [ローカル動作確認ガイド](local-testing.md)
- [音声文字起こし Web アプリ構築ガイド](create-web-app-for-audio-file-transcription-Bulab.md)
