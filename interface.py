from flask import Flask,request,jsonify,render_template
from utils import Pumpkin_Seed
import config

app=Flask(__name__)

@app.route('/pumpkin_model')
def home():
    #return jsonify({'Result':'Succesful'})
    return render_template('pumpkin_seed.html')

@app.route('/predict_seed',methods=['GET','POST'])
def seed_predict():
    if request.method=='GET':
        data=request.args.get
        Area=float(data('Area'))
        Perimeter=float(data('Perimeter'))
        Major_Axis_Length=float(data('Major_Axis_Length'))
        Minor_Axis_Length=float(data('Minor_Axis_Length'))
        Convex_Area=float(data('Convex_Area'))
        Equiv_Diameter=float(data('Equiv_Diameter'))
        Eccentricity=float(data('Eccentricity'))
        Solidity=float(data('Solidity'))
        Extent=float(data('Extent'))
        Roundness=float(data('Roundness'))
        Aspect_Ration=float(data('Aspect_Ration'))
        Compactness=float(data('Compactness'))

        obj=Pumpkin_Seed(Area,Perimeter,Major_Axis_Length,Minor_Axis_Length,Convex_Area,Equiv_Diameter,
                 Eccentricity,Solidity,Extent,Roundness,Aspect_Ration,Compactness)
        pred_class=obj.predict_seed()
        #return jsonify({'Result':f'Pumpkin seed class is {pred_class}'})
        return render_template('pumpkin_seed.html',prediction=pred_class)
    
    elif request.method=='POST':
        data=request.form
        Area=float(data['Area'])
        Perimeter=float(data['Perimeter'])
        Major_Axis_Length=float(data['Major_Axis_Length'])
        Minor_Axis_Length=float(data['Minor_Axis_Length'])
        Convex_Area=float(data['Convex_Area'])
        Equiv_Diameter=float(data['Equiv_Diameter'])
        Eccentricity=float(data['Eccentricity'])
        Solidity=float(data['Solidity'])
        Extent=float(data['Extent'])
        Roundness=float(data['Roundness'])
        Aspect_Ration=float(data['Aspect_Ration'])
        Compactness=float(data['Compactness'])

        obj=Pumpkin_Seed(Area,Perimeter,Major_Axis_Length,Minor_Axis_Length,Convex_Area,Equiv_Diameter,
                 Eccentricity,Solidity,Extent,Roundness,Aspect_Ration,Compactness)
        pred_class=obj.predict_seed()
        #return jsonify({'Result':f'Pumpkin seed class is {pred_class}'})
        return render_template('pumpkin_seed.html',prediction=pred_class)
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)
