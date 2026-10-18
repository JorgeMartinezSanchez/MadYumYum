from backend.flask.app import Flask

app = Flask(__name__)
app.config.from_object("backend.flask.app.config.Config")

@app.route("/")
def hello_world():
  return "<p>¡Hola, Mundo!</p>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)