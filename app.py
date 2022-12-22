from flask import Flask, render_template 
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service')
def show_service_detail():
    return render_template('service.html')

@app.route('/ai')
def index1():
    return render_template('ai.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

