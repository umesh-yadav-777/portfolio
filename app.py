from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print("New Message")
    print(name, email, message)

    return redirect('/')

if __name__ == '__main__':
    import os
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
