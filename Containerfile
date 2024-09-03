FROM python:3.9-slim

EXPOSE 5000

# ワークディレクトリを作成
WORKDIR /app

# 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# 環境変数を設定
ENV FLASK_APP app.py
ENV FLASK_ENV production

# コマンドを実行
CMD ["flask", "run", "--host=0.0.0.0"]