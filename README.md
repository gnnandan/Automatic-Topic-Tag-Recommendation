# Automatic Topic Tag Recommendation 
 Automatic Topic Tag Recommendation using flask and rapid API
 
#solution to analyze huge amounts of text data 

Topic analysis is a Natural Language Processing (NLP) technique that allows us to 
automatically extract meaning from texts by identifying recurrent themes or topics. Topic 
analysis models enable you to sift through large sets of data and identify the most common 
and most important topics in an easy, fast, and completely scalable way.

**Requirements**
1. python idle 3.x
2. anaconda navigator {spyder}
3. libraries:- {numpy, pandas ,flask}
4. Rapid API account required to import API 

**imports in code**
from flask import Flask, request, render_template
import numpy as np
import re
import requests
import json
import csv
import pandas as pd

**Rapid API Code Snippet**
import requests

url = "https://twinword-topic-tagging.p.rapidapi.com/generate/"

payload = "text=Computer%20science%20is%20the%20scientific%20and%20practical%20approach%20to%20computation%20and%20its%20applications.%20It%20is%20the%20systematic%20study%20of%20the%20feasibility%2C%20structure%2C%20expression%2C%20and%20mechanization%20of%20the%20methodical%20procedures%20(or%20algorithms)%20that%20underlie%20the%20acquisition%2C%20representation%2C%20processing%2C%20storage%2C%20communication%20of%2C%20and%20access%20to%20information%2C%20whether%20such%20information%20is%20encoded%20as%20bits%20in%20a%20computer%20memory%20or%20transcribed%20in%20genes%20and%20protein%20structures%20in%20a%20biological%20cell.%20An%20alternate%2C%20more%20succinct%20definition%20of%20computer%20science%20is%20the%20study%20of%20automating%20algorithmic%20processes%20that%20scale.%20A%20computer%20scientist%20specializes%20in%20the%20theory%20of%20computation%20and%20the%20design%20of%20computational%20systems."
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "ed25ca2a01msh7fd3778b4c2a35dp11cf36jsn28ceb03ff572",
    'x-rapidapi-host': "twinword-topic-tagging.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
