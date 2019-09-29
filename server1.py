from flask import Flask,  jsonify, request
import math
app= Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    
    r= int (request.args.get('r'))
    circumference = str (2* math.pi *r)
    volume = str ((4*math.pi*r**3)/3) 
    area=str (math.pi * r**2)
    res = "area : "+area+"\n "
    return "area="+ area +"\nvolume ="+volume+"\ncircumference ="+circumference

app.run(host='0.0.0.0', port=7074)