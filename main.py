from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    all_posts = requests.get(url='https://api.npoint.io/616be3dc7b1dffd42d65').json()
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<num>')
def post(num):
    all_posts = requests.get(url='https://api.npoint.io/616be3dc7b1dffd42d65').json()
    return render_template("post.html", posts=all_posts, num=int(num))


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
