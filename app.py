from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from flask import Flask, render_template, request

app = Flask(__name__)

# irisデータセットの読み込み
iris = load_iris()
X = iris.data
y = iris.target

# 学習データとテストデータの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ロジスティック回帰モデルの学習
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracyの確認
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy:.2f}')

# 花の名前の定義
flower_names = ['setosa', 'versicolor', 'virginica']

# Webページのルーティング
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 予測結果の計算と表示
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        flower_name = flower_names[prediction[0]]
        return render_template('result.html', flower_name=flower_name)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)