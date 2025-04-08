from flask import Flask, render_template
import requests

blog_api_endpoint = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = blog_api_endpoint.json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",blogs=blog_data)

@app.route('/<id>')
def post(id):
    return render_template("post.html", blogs=blog_data, num=int(id))

if __name__ == "__main__":
    app.run(debug=True)
