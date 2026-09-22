from flask import Flask, render_template, request, make_response
import secrets

app = Flask(__name__)

@app.route("/")
def home():
    aid = request.cookies.get("aid")
    is_new = aid is None
    if is_new:
        aid = secrets.token_hex(8)

    response = make_response(render_template("index.html"))

    if is_new:
        response.set_cookie(key="aid", value=aid, samesite="Strict")

    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)