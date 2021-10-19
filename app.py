from flask import request,Flask,render_template
from flask_cors import cross_origin , CORS
from Log_Writer.logger import App_Logger
from Raw_Data_Formatter.data_formatter import formatter

app=Flask(__name__)
CORS(app)

log_writer=App_Logger()

@app.route('/',methods=['GET','POST'])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/Prediction',methods=['POST'])
@cross_origin()
def index():

    try:
        if request.method=="POST":

            # Gathering the data and converting it to dataframe
            data = formatter().format_data()


            return render_template("results.html")
        else :
            return render_template("index.html")

    except Exception as e:
        log_writer.log(log_message="Error Occurred in index page route")
        return print(e)


if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1",port=8001)

