from flask import redirect, render_template, url_for, Blueprint

main_blueprint = Blueprint(
    "main",
    __name__,
    static_url_path="/static",
    static_folder="./static",
    template_folder="templates",
)


@main_blueprint.route("/")
def index():
    return render_template("main/index.html", title="Main")
