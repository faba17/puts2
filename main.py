from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/div')
def divide():
    flag = False;
    result = 0
    for arg in request.args:
        try:
            if not flag:
                result = eval(request.args.get(arg, default="0"))
                flag = True
                continue
            result = result / eval(request.args.get(arg, default="0"))
        except:
            pass
    return '%f \n' % result

if __name__ == "__main__":
    app.run()
