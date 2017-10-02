from flask import Flask, render_template
#Create server
app = Flask(__name__)\
#app.config("debug") = True
#app.config("SECURITY) = True

#Configure
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/about"):
    def about():

#Run
if __name__ == '__main__':
    app.run(debug=True)
