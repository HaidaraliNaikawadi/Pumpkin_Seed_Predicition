import numpy as np
import pickle
import config

class Pumpkin_Seed():
    def __init__(self,Area,Perimeter,Major_Axis_Length,Minor_Axis_Length,Convex_Area,Equiv_Diameter,
                 Eccentricity,Solidity,Extent,Roundness,Aspect_Ration,Compactness):
        self.Area=Area
        self.Perimeter=Perimeter
        self.Major_Axis_Length=Major_Axis_Length
        self.Minor_Axis_Length=Minor_Axis_Length
        self.Convex_Area=Convex_Area
        self.Equiv_Diameter=Equiv_Diameter
        self.Eccentricity=Eccentricity
        self.Solidity=Solidity
        self.Extent=Extent
        self.Roundness=Roundness
        self.Aspect_Ration=Aspect_Ration
        self.Compactness=Compactness

    def load_data(self):
        with open(config.Model_Path,'rb') as f:
            self.model=pickle.load(f)

    def predict_seed(self):
        self.load_data()
        test_array=np.array([self.Area,self.Perimeter,self.Major_Axis_Length,self.Minor_Axis_Length,self.Convex_Area,
                            self.Equiv_Diameter,self.Eccentricity,self.Solidity,self.Extent,self.Roundness,
                            self.Aspect_Ration,self.Compactness],ndmin=2)
        pred_type=self.model.predict(test_array)
        return pred_type[0]
