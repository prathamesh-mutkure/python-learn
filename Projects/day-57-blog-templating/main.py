from flask import Flask, render_template
from post import Post


app = Flask(__name__)
all_post = Post.get_all_post()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=all_post)


@app.route("/post/<int:_id>")
def get_blog_by_id(_id):
    return render_template("post.html", post=Post.get_post_by_id(all_post, _id))


if __name__ == "__main__":
    app.run(debug=True)
