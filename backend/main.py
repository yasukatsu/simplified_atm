from flask import Flask, render_template, jsonify
# CORS：Ajax通信するためのライブラリ
from flask_cors import CORS
from random import *
import sqlite3

# static_folder：vueでビルドした静的ファイルのパスを指定
# template_folder：vueでビルドしたindex.htmlのパスを指定
app = Flask(__name__,
            static_folder="./../frontend/dist/static",
            template_folder="./../frontend/dist")

app.config.from_object(__name__)

CORS(app)



# 任意のリクエストを受け取った時、index.htmlを参照


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch(path):
    return render_template("index.html")

# '/rand'が叩かれた時、乱数を生成


@app.route('/rand')
def random():
    response = {
        'randomNum': randint(1, 100)
    }
    return jsonify(response)

@app.route('/init')
def init():
    # データベースを新規作成
    dbname = ('./backend/models/atm.db')
    conn = sqlite3.connect(dbname)

    # テーブル作成
    table = "atm"
    cursor = conn.cursor()
    sql = f"""CREATE TABLE IF NOT EXISTS {table}(
        id integer primary key autoincrement,
        amount integer
    )"""
    cursor.execute(sql)
    conn.commit()

    # レコードを格納
    sql = f"INSERT INTO {table} (amount) VALUES (?)"
    data = (0,)
    cursor.execute(sql, data)
    conn.commit()

    # レコードを取得
    sql = f"SELECT max(id) FROM {table}"
    cursor.execute(sql)
    latest_data = cursor.fetchall()
    latest_id = latest_data[0]

    conn.close()

    response = {
        'accountId': latest_id
    }
    return jsonify(response)
    

# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
