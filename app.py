from flask import request,Flask,render_template
from flask_cors import cross_origin , CORS

app=Flask(__name__)
CORS(app)

@app.route('/',methods=['GET','POST'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/Prediction',methods=['POST'])
@cross_origin()
def index():

    try:
        if request.methods=="POST":
            return render_template("results.html")
        else :
            return render_template("index.html")

    except Exception as e:
        log_writer.log(log_message="Error Occured in index page route")
        return print(e)


if __name__=="__main__":
    app.run(debug=True,host="127.0.01",port=8001)

