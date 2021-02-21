from flask import Flask, render_template
import spotifye

app = Flask(__name__)

@app.route('/')
def homepage():
    json = spotifye.analyze_user()
    return render_template('index.html', stats=json)

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)