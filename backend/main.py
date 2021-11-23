from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3

class error:
    BAD_REQUEST = "JSON形式じゃないリクエストです。"
    NOT_EXIST_ACCOUNT = "口座が存在しません。"
    IS_INSUFFICIENT = "残高が不足しております。"

class db:
    PATH = "/usr/src/app/backend/models/atm.db"
    TABLE = "atm"

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

# 口座開設処理
@app.route('/init')
def init():
    # データベースに接続（無ければ作成）
    conn = sqlite3.connect(db.PATH)

    # テーブル作成
    cursor = conn.cursor()
    sql = f"""CREATE TABLE IF NOT EXISTS {db.TABLE}(
        id integer primary key autoincrement,
        amount integer default 0
    )"""
    cursor.execute(sql)
    conn.commit()

    # レコードを格納
    sql = f"INSERT INTO {db.TABLE}(amount) VALUES (0)"
    cursor.execute(sql)
    conn.commit()

    # レコードを取得
    sql = f"SELECT max(id) FROM {db.TABLE}"
    cursor.execute(sql)
    latest_data = cursor.fetchall()
    latest_id = latest_data[0]

    conn.close()

    response = {
        'accountId': latest_id
    }
    return jsonify(response)
    
# 入金処理
@app.route('/receive', methods=['POST'])
def receive():
    if not request.is_json:
        print(error.BAD_REQUEST)
        return jsonify(), 400

    data = request.json
    accountId = data["accountId"]
    amount = data["amount"]

    # db接続
    conn = sqlite3.connect(db.PATH)
    cursor = conn.cursor()

    # 現在の預金額を取得
    sql = f"SELECT amount FROM {db.TABLE} WHERE id={accountId}"
    cursor.execute(sql)
    db_amount = cursor.fetchone()
    if db_amount is None:
        return jsonify({"errorMsg": error.NOT_EXIST_ACCOUNT})

    total_amount = db_amount[0] + amount

    sql = f"UPDATE {db.TABLE} SET amount=(?) WHERE id={accountId}"
    data = (total_amount,)
    cursor.execute(sql, data)
    conn.commit()

    conn.close()

    response = {
        'responseMsg': 'ok',
        'totalAmount': total_amount
    }
    return jsonify(response)

# 出金処理
@app.route('/pay', methods=['POST'])
def pay():
    if not request.is_json:
        return jsonify({"errorMsg": "Missing JSON in request"}), 400

    data = request.json
    accountId = data["accountId"]
    amount = data["amount"]

    # db接続
    conn = sqlite3.connect(db.PATH)
    cursor = conn.cursor()

    # 現在の預金額を取得
    sql = f"SELECT amount FROM {db.TABLE} WHERE id={accountId}"
    cursor.execute(sql)
    db_amount = cursor.fetchone()

    if db_amount is None:
        return jsonify({"errorMsg": error.NOT_EXIST_ACCOUNT})

    if db_amount[0] < amount:
        return jsonify({"errorMsg": error.IS_INSUFFICIENT})

    total_amount = db_amount[0] - amount

    sql = f"UPDATE {db.TABLE} SET amount=(?) WHERE id={accountId}"
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
