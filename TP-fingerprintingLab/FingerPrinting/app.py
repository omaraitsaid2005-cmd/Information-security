from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    print("\n========== NEW VISIT ==========")

    # Information about the request and network connection
    print("IP address                :", request.remote_addr)
    print("HTTP method               :", request.method)
    print("HTTP version              :", request.environ.get("SERVER_PROTOCOL"))
    print("Host                      :", request.headers.get("Host"))

    # --- Browser and operating-system information ---
    print("User-Agent                :", request.headers.get("User-Agent"))
    print("Sec-CH-UA                 :", request.headers.get("Sec-CH-UA"))
    print("Sec-CH-UA-Mobile          :", request.headers.get("Sec-CH-UA-Mobile"))
    print("Sec-CH-UA-Platform        :", request.headers.get("Sec-CH-UA-Platform"))

    # --- Preferred content formats and languages ---
    print("Accept                    :", request.headers.get("Accept"))
    print("Accept-Language           :", request.headers.get("Accept-Language"))
    print("Accept-Encoding           :", request.headers.get("Accept-Encoding"))

    # --- Navigation context ---
    print("Referer                   :", request.headers.get("Referer"))
    print("Sec-Fetch-Site            :", request.headers.get("Sec-Fetch-Site"))
    print("Sec-Fetch-Mode            :", request.headers.get("Sec-Fetch-Mode"))
    print("Sec-Fetch-User            :", request.headers.get("Sec-Fetch-User"))
    print("Sec-Fetch-Dest            :", request.headers.get("Sec-Fetch-Dest"))
    print("Connection                :", request.headers.get("Connection"))
    print("Cache-Control             :", request.headers.get("Cache-Control"))

    # --- Security / privacy related headers ---
    print("Upgrade-Insecure-Requests :", request.headers.get("Upgrade-Insecure-Requests"))
    print("DNT (Do Not Track)        :", request.headers.get("DNT"))
    print("Sec-GPC (Global Privacy)  :", request.headers.get("Sec-GPC"))
    print("Cookie                    :", request.headers.get("Cookie"))

    print("================================\n")
    return render_template("index.html")

@app.route("/collect", methods=["GET", "POST"])
def collect():
    print("\n========== DATA RECEIVED ON /collect ==========")
    print("IP address :", request.remote_addr)

    data = request.get_json(silent=True)
    if data:
        print("Data type  :", data.get("type"))
        for key, value in data.get("features", {}).items():
            print(f"  {key:<22}: {value}")

    print("================================================\n")
    return jsonify({"status": "received"})
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)