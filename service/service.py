from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route('/start')
def start():
    return json.dumps({'data':None})

@app.route('/obstacles')
def obstacles():
    s = [0,1,2,3]
    t = {}
    t['obstacle1'] = s
    t['obstacle2'] = s
    return json.dumps(t, ensure_ascii=False)

@app.route('/points')
def points():
    points_list = [0,1,2,3,4,5,6]
    return json.dumps({'data':points_list}, ensure_ascii=False)


@app.route('/login')
def index():
    return render_template('login.html')


@app.route('/FlaskTutorial', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        return render_template('success.html', email=email)
    else:
        pass


if __name__ == "__main__":
    app.run()
