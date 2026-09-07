from flask import Flask, request, Response
import requests

app = Flask(__name__)

BACKEND = "https://usd-price-widget-eu.onrender.com"


@app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def proxy(path):
    url = f"{BACKEND}/{path}"
    resp = requests.request(
        method=request.method,
        url=url,
        headers={k: v for k, v in request.headers if k.lower() != "host"},
        data=request.get_data(),
        params=request.args,
        timeout=25,
    )
    excluded = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in excluded]
    return Response(resp.content, resp.status_code, headers)
