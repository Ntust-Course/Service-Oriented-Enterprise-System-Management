from flask import Flask

from views import RegistryView

app = Flask(__name__)
app.url_map.strict_slashes = False

app.add_url_rule("/api/registry", view_func=RegistryView.as_view("registry"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
