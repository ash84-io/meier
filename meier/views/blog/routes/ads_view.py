from flask import Blueprint

ads_view = Blueprint("ads_view", __name__, url_prefix="")


@ads_view.route("/ads.txt", methods=["GET"])
def get_post_list_view():
    return "google.com, pub-8699046198561974, DIRECT, f08c47fec0942fa0"
