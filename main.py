from flask import Flask,render_template
import requests
import datetime


app = Flask(__name__)
blog_url = "https://api.npoint.io/a37c3d43105f73ed0a8b"
blog_response = requests.get(blog_url)
posts = blog_response.json()
@app.route('/')
def home():
    current_year=datetime.datetime.now().year
    return render_template("index.html", all_posts=posts,year=current_year)

@app.route('/index.html')
def get_all_posts():
    current_year=datetime.datetime.now().year
    return render_template("index.html", all_posts=posts,year=current_year)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    current_year = datetime.datetime.now().year
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post,year=current_year)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)