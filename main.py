from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/mul')
def multiply():
    result = 1
    for arg in request.args:
        try:
            result = result * eval(request.args.get(arg, default="0"))
        except:
            pass
    return '%f \n' % result

if __name__ == "__main__":
    app.run()
