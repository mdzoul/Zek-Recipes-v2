from flask import Flask, render_template, request
import requests
import smtplib
import os

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


@app.route('/contact', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        data = request.form

        EMAIL = "zoulaimi@hotmail.com"
        PASSWORD = os.environ.get("PASSWORD")
        SMTP_SERVER = {
            "gmail": "smtp.gmail.com",
            "yahoo": "smtp.mail.yahoo.com",
            "hotmail": "smtp-mail.outlook.com",
        }
        with smtplib.SMTP(f"{SMTP_SERVER['hotmail']}") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f'Subject:New Message\n\n'
                    f'Name: {data["name"]}\nEmail: {data["email"]}\nPhone: {data["phone"]}\nMessage: {data["message"]}'
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
