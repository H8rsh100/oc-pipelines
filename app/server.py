"""Sample application entry point - runs the oc-pipelines news service."""

from flask import Flask, jsonify

from app.news import summarise

app = Flask(__name__)

ARTICLES = [
    {"source": "Reuters", "headline": "Markets rally"},
    {"source": "reuters", "headline": "Oil slips"},
    {"source": "BBC", "headline": "Election called"},
    {"source": "ap", "headline": "Rate decision"},
]


@app.route("/")
def index():
    """Return a json summary of the sample articles grouped by source."""
    return jsonify({"articles": summarise(ARTICLES)})


def main():
    """Start the service on port 8000."""
    print("oc-pipelines news service starting", flush=True)
    print("loading article feed ...", flush=True)
    print("SERVICERUNNING", flush=True)
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
