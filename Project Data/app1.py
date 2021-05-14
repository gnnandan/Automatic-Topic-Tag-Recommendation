from flask import Flask, request, render_template
import numpy as np
import re
import requests
import json
import csv
import pandas as pd

app = Flask(__name__)

def check(output):
    url = "https://twinword-topic-tagging.p.rapidapi.com/generate/"
    payload = {"text": output}
    #print(payload)
    headers = {
    'x-rapidapi-key': "ed25ca2a01msh7fd3778b4c2a35dp11cf36jsn28ceb03ff572",
    'x-rapidapi-host': "twinword-topic-tagging.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=payload)
    print(response.text)
    return response.json()["topic"]
    #return var

#home page
@app.route('/')
def home():
    return render_template('home.html')

#home page
@app.route('/summarizer')
def summarizer():
    return render_template('summarizer.html')

#summarizer page
@app.route('/summarizer',  methods=['POST'])
def summarize():
    output = request.form['output']
    output=re.sub("[^a-zA-Z.,]"," ",output)
    print(output)
    essay = check(output)

    data_file = open('data_file.csv', 'w') 
    csv_writer = csv.writer(data_file) 
    count = 0
    for emp in essay: 
        print(essay[emp])
        essay[emp] = round(essay[emp],4)
        if count == 0: 
            # Writing headers of CSV file   
            header = ['Type','Probability']
            csv_writer.writerow(header) 
            count += 1
    # Writing data of CSV file 
        d = [emp,essay[emp]]
        print(d)
        csv_writer.writerow(d) 
    data_file.close() 
    df = pd.read_csv("data_file.csv")
    temp = df.to_dict('records')
    columnNames = df.columns.values
    return render_template('summary.html',records=temp, colnames=columnNames)

    
if __name__ == "__main__":
    app.run(debug=False)
