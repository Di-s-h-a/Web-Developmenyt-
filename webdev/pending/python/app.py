from flask import Flask
app = Flask(__name__)
if __name__ == "__main__":
    app.run()
@app.route('/')
# def home():
    # return "Hello, Flask!"
def index():
    return '<h1>Hello</h1>'
app.add_url_rule('/', 'index', index())

