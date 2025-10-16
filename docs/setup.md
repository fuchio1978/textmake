# セットアップガイド

このガイドでは、音声をテキストに変換する Flask ベースの Web アプリをローカル環境で動かすための準備手順を説明します。

## 1. 依存関係のインストール

Python の仮想環境を作成し、必要なパッケージをインストールします。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Whisper を利用するには FFmpeg が必要です。未導入の場合は各 OS に合わせてインストールしてください。

## 2. アプリケーションの起動

以下のコマンドで開発サーバーを起動します。

```bash
flask --app app run --host 0.0.0.0 --port 5000 --debug
```

初回起動時は Whisper モデルのダウンロードに時間がかかる場合があります。

## 3. ブラウザから動作確認

1. ブラウザで `http://localhost:5000` を開きます。
2. 「音声ファイルを選択」から音声ファイル (wav / mp3 / m4a など) をアップロードします。
3. 「文字起こしを開始」をクリックし、完了メッセージとテキストファイルのダウンロードを確認します。

## 4. 設定の調整

利用可能な環境変数や Whisper モデルの選択肢は [設定リファレンス](configuration.md) にまとめています。カスタマイズが必要な場合は合わせて参照してください。

## 5. 次のステップ

- 詳細なテスト手順は [ローカル動作確認ガイド](local-testing.md) を参照してください。
- アプリ全体の構成や UI の概要は [音声文字起こし Web アプリ構築ガイド](create-web-app-for-audio-file-transcription-Bulab.md) にまとめています。
