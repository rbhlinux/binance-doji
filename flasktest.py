import os
import pandas as pd
from os import listdir
import glob
import datetime
from flask import Flask,render_template, request
import numpy as np
from datetime import timedelta

app = Flask(__name__,template_folder='/home/code/templates')

path4h="/home/code/4hour"
filenames4h = [f for f in glob.glob(path4h + "**/*.csv", recursive=True)]
combined_csv_4h = pd.concat( [ pd.read_csv(f) for f in filenames4h ] )

path30m="/home/code/30min"
filenames30m = [f for f in glob.glob(path30m + "**/*.csv", recursive=True)]
combined_csv_30m = pd.concat( [ pd.read_csv(f) for f in filenames30m ] )


time2 = datetime.datetime.now()
print(time2)

@app.route("/4hour")
def fourhour():
        return render_template("temp1.html",data=combined_csv_4h.to_html())

@app.route("/30min")
def thirtymin():
        return render_template("temp2.html",data=combined_csv_30m.to_html())

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8012)

