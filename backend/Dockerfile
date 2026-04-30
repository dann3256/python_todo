FROM python:3.12-slim
# DockerHub上にある公式のPython環境をベースに使う

WORKDIR /app
# コンテナの中での作業フォルダを /app に設定

COPY requirements.txt .
RUN pip install -r requirements.txt
# 依存ライブラリを先にインストール（キャッシュ効率のため）

COPY . .
# ソースコードをコンテナにコピー