from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    # name = request.args.get("name", "world")
    # print(name)
    return render_template('index.html')


@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name") #flask puts GET args in args and POST args in form
    education = request.form.get("education")
    print(name, education)

    if not name or not education:
        return 'Failure'
    else:
        return 'Success'

if __name__ == "__main__":
    app.run(debug=True)