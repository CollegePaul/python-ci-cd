from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"
    return "This is pointless"


#ensure this is the main application
if __name__ == "__main__":
    app.run()