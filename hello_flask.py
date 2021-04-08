from flask import Flask  , render_template, redirect

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  


@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say')
def say():
    return "Hi Flask"

@app.route('/<name>')
def name(name):
    print("*"*80)
    print("in Hello Function")
    return f"Hello {name}"



if __name__=="__main__":      
    app.run(debug = True) 