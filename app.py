import os
import random
from flask import Flask, render_template

app = Flask(__name__)


def get_sides():
    """Return how many sides the die should have based on the DICE_SIDES env var."""
    sides_env = os.getenv("DICE_SIDES", "6")
    try:
        sides = int(sides_env)
        if sides < 2:
            raise ValueError
    except ValueError:
        sides = 6
    return sides


@app.route("/")
def index():
    sides = get_sides()
    result = random.randint(1, sides)
    return render_template("index.html", result=result, sides=sides)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
