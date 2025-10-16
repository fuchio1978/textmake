# textmake

Whisper を利用して音声ファイルをテキストに変換する Flask ベースの Web アプリです。アップロードした音声を即座に文字起こしし、テキストファイルとしてダウンロードできます。

## 1. セットアップ

ローカル開発環境の準備手順は [セットアップガイド](docs/setup.md) にまとめています。依存関係のインストールから Flask アプリの起動まで順を追って説明しているので、まずはこちらを参照してください。

## 2. アプリの起動と基本操作

セットアップが完了したら、以下のコマンドでアプリを起動できます。

```bash
flask --app app run --host 0.0.0.0 --port 5000 --debug
```

ブラウザで `http://localhost:5000` を開き、音声ファイルをアップロードすると文字起こし結果がダウンロードされます。UI の流れや注意点は [音声文字起こし Web アプリ構築ガイド](docs/create-web-app-for-audio-file-transcription-Bulab.md) で確認できます。

## 3. ローカルテスト

詳細な動作確認の手順やトラブルシューティングは [ローカル動作確認ガイド](docs/local-testing.md) に整理しています。サンプル音声を使ったテストや、エラー発生時のチェックポイントもこちらを参照してください。

## 4. 設定

環境変数や Whisper モデルの選択肢など、アプリの調整に関する情報は [設定リファレンス](docs/configuration.md) にまとめています。

## 関連ドキュメント

- [セットアップガイド](docs/setup.md)
- [ローカル動作確認ガイド](docs/local-testing.md)
- [音声文字起こし Web アプリ構築ガイド](docs/create-web-app-for-audio-file-transcription-Bulab.md)
- [設定リファレンス](docs/configuration.md)
