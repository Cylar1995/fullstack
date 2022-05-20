from flask import render_template, redirect , url_for, Blueprint

my_view= Blueprint ('my_view', __name__)

@my_view.route("/")
def home():
    return render_template ("index.html")

@my_view.route("/about")
def pageone():
    return render_template ("about.html")

@my_view.route("/pagetwo")
def pagetwo():
    return render_template ("page_two.html")

@my_view.route("/pagethree")
def pagethree():
    return render_template ("page_three.html")

@my_view.route("/pagefour")
def pagefour():
    return render_template ("page_four.html")

@my_view.route("/pagefive")
def pagefive():
    return render_template ("pagefive.html")

@my_view.route("/home")
@my_view.route("/js")
@my_view.route("/javascript")
def homeredirect():
    return redirect(url_for("my_view.home"))