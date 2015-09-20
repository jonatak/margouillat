from flask import Flask
app = Flask(__name__)

@app.route("/playbook/upload")
def upload():
    pass

@app.route("/playbook/list")
def list():
    pass

@app.route("/playbook/run")
def run():
    pass

if __name__ = "__main__":
    app.run()
