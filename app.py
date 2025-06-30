from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hello brevjizino ok temo test')

if __name__ == '__main__':
    # listen on all interfaces (access via localhost)
    app.run(debug=True, host='127.0.0.1', port=5000)

# To run the app, use the command: python app.py
