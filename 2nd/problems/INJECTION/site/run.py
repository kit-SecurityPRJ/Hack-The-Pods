from flask import Flask, render_template, request
import pymysql.cursors

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    name = request.args.get("name", default="")

    conn = pymysql.connect(
            host="mysql",
            user="inject",
            password="inject",
            db="injection",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor)

    result = ""
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE name != 'HideMan' AND name LIKE '%{}%'".format(name)
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print(e)
        result = e
    finally:
        conn.close()

    return render_template("table.html", users=result)

app.run(host="0.0.0.0", port="80")
