import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
pages = FlatPages(app)
freezer = Freezer(app)

@app.route("/")
def index():
    return render_template('index.html')

if '__main__' == __name__:
    """Allow building of frozen app through the command line."""
    if 1 < len(sys.argv) and "build" == sys.argv[1]:
        freezer.freeze()
    else:
        app.run(port=5000)
