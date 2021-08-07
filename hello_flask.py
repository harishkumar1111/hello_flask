import flask

# Create the application.
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/hello',methods=['Get'])
def home():
    return "Hello1111"


if __name__ == '__main__':
    app.debug=True
    app.run()
