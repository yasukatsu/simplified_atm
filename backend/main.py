from flask import Flask, render_template, request, jsonify
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

@app.route('/init')
def init():
    # データベースに接続（無ければ作成）
    dbname = ('/usr/src/app/backend/models/atm.db')
    conn = sqlite3.connect(dbname)

    # テーブル作成
    table = "atm"
    cursor = conn.cursor()
    sql = f"""CREATE TABLE IF NOT EXISTS {table}(
        id integer primary key autoincrement,
        amount integer default 0
    )"""
    cursor.execute(sql)
    conn.commit()

    # レコードを格納
    sql = f"INSERT INTO {table}(amount) VALUES (0)"
    cursor.execute(sql)
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
    

@app.route('/receive', methods=['POST'])
def receive():
    if not request.is_json:
        print("hoge")
        return jsonify({"errorMsg": "Missing JSON in request"}), 400

    data = request.json
    print(data)
    accountId = data["accountId"]
    print(accountId)
    amount = data["amount"]
    print(amount)

    # db接続
    dbname = ('/usr/src/app/backend/models/atm.db')
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    # 現在の預金額を取得
    table = "atm"
    sql = f"SELECT amount FROM {table} WHERE id={accountId}"
    cursor.execute(sql)
    db_amount = cursor.fetchone()
    print(db_amount[0])
    if db_amount[0] is None:
        return jsonify({"errorMsg": "Not exist accountId"}), 400

    total_amount = db_amount[0] + amount

    sql = f"UPDATE {table} SET amount=(?) WHERE id={accountId}"
    data = (total_amount,)
    cursor.execute(sql, data)
    conn.commit()

    conn.close()

    response = {
        'responseMsg': 'ok',
        'totalAmount': total_amount
    }
    return jsonify(response)


@app.route('/pay', methods=['POST'])
def pay():
    if not request.is_json:
        return jsonify({"errorMsg": "Missing JSON in request"}), 400

    data = request.json
    print(data)
    accountId = data["accountId"]
    print(accountId)
    amount = data["amount"]
    print(amount)

    # db接続
    dbname = ('/usr/src/app/backend/models/atm.db')
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    # 現在の預金額を取得
    table = "atm"
    sql = f"SELECT amount FROM {table} WHERE id={accountId}"
    cursor.execute(sql)
    db_amount = cursor.fetchone()
    print(db_amount[0])
    if db_amount[0] is None:
        return jsonify({"errorMsg": "Not exist accountId"}), 400

    total_amount = db_amount[0] - amount

    sql = f"UPDATE {table} SET amount=(?) WHERE id={accountId}"
    data = (total_amount,)
    cursor.execute(sql, data)
    conn.commit()

    conn.close()

    response = {
        'responseMsg': 'ok',
        'totalAmount': total_amount
    }
    return jsonify(response)


# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
