from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_posts = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965").json()


@app.route('/')
def home():
    global blog_posts
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/blog/<int:number>")
def blog_posts_url(number):
    global blog_posts
    return render_template("post.html", number=number, blog_posts=blog_posts)


if __name__ == "__main__":
    app.run(debug=True)
