from flask import Flask, render_template
import pandas as pd
import numpy as np
from IPython.display import HTML
import json
import sys  
import os.path

path= "C:\\Users\\19177\\Downloads\\html5up-aerial\\templates"

# Read csv file into Dataframe def fname(arg):
df = pd.read_csv('MoneyDates.csv')
df = df[df.Name != '']
rows = np.random.choice(df.index.values, 1)
sampled = df.loc[rows]
print (sampled)
result = sampled.to_html(classes='table table-striped text-center', justify='center')


df2 = pd.read_csv('FreeDates.csv')
df2 = df2[df2.Where !='']
rows1 = np.random.choice(df2.index.values, 1)
sampled1 = df2.loc[rows1]
print(sampled1)

result1 = sampled1.to_html(classes='table table-striped text-center', justify='center')


print(result)
print(result1)

file_name2="freedata.html"
file_name="data.html"
completeName = os.path.join(path, file_name)
completeName2 = os.path.join(path, file_name2)




text_file = open(completeName, "w")
text_file.write(result)
text_file.close()

text_file2 = open(completeName2, "w")
text_file2.write(result1)
text_file2.close()



app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page2.html')
def page2():
    return render_template('page2.html')

@app.route('/page3.html')
def data():
    with open("MoneyDates.csv") as file:
        return render_template("data.html")

@app.route('/page4.html')
def data1():
    with open("FreeDates.csv") as file:
        return render_template("freedata.html")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)