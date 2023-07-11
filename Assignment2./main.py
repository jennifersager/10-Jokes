from flask import Flask
import random
import json

app = Flask(__name__)
@app.route('/')
def hello_world():
    f = open('jokes.json')

    data = json.load(f)

    arr = [json.dumps(data['Joke1']), data['Joke2'], data['Joke3'], data['Joke4'], data['Joke5'],data['Joke6'], data['Joke7'], data['Joke8'], data['Joke9'], data['Joke10']] 

    #randomjoke = random.choice(arr)
    #return randomjoke
    #pretty_output = json.dumps(data, indent=4)
    #return pretty_output

    return arr
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
