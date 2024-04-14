from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictor',methods=['POST'])
def predict_placement():
    Clump = float(request.form.get('Clump'))
    UnifSize = int(request.form.get('UnifSize'))
    Unifshape = int(request.form.get('Unifshape'))
    MargAdh = int(request.form.get('MargAdh'))
    SingEpiSize = int(request.form.get('SingEpiSize'))
    BareNuc = int(request.form.get('BareNuc'))
    BlandChrom = int(request.form.get('BlandChrom'))
    NormNucl = int(request.form.get('NormNucl'))
    Mit = int(request.form.get('Mit'))
    

    # prediction
    result = model.predict(np.array([Clump,UnifSize,Unifshape,MargAdh,SingEpiSize,BareNuc,BlandChrom,NormNucl,Mit]).reshape(1,9))

    if result[0] == 2:
        result = 'placed'
    else:
        result = 'not placed'

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)