from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'), # type: ignore
            race_ethnicity=request.form.get('ethnicity'), # type: ignore
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'), # type: ignore
            test_preparation_course=request.form.get('test_preparation_course'), # type: ignore
            reading_score=float(request.form.get('writing_score')), # type: ignore
            writing_score=float(request.form.get('reading_score')) # type: ignore

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        

