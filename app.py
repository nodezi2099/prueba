from flask import  Flask


from flask import Flask
app = Flask(__name__)    

@app.route('/')
def hello_world():
    return 'HOLA PYTHON'

if __name__ == '__main__':
       app.run()
