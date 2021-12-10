from flask import Flask ,escape,request,render_template
import pickle
vector=pickle.load(open("vector1.pkl",'rb'))
model=pickle.load(open("final_model.pkl",'rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news=str(request.form['news'])
        print(news)
        predict=model.predict(vector.transform([news]))[0]
        print(predict)
        return render_template("prediction.html",prediction_text="News Headline is -> {}".format(predict))
    else:
        return render_template("prediction.html")







if __name__=='__main__':
    app.run(debug=True)