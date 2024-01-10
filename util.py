#helper code
import json
import pickle
import numpy as np

__locTemp = None
__loc = None
__model = None

def estimator(bed,bath,acre_lot,house_size,location):
    try:
        index = __locTemp.index(location.lower())
    except:
        index = -1

    x = np.zeros(len(__locTemp))
    x[0] = bed
    x[1] = bath
    x[2] = acre_lot
    x[3] = house_size
    if index >= 0:
        x[index] = 1
    
    return round(__model.predict([x])[0],2)

def getLocs():
    return __loc

def locations():
    global __locTemp
    global __loc
    global __model

    with open("./backend/info/columns.json",'r') as f:
        __locTemp = json.load(f)['data_columns']
        __loc = __locTemp[3:]
        
    with open("./backend/info/ny_house_prediction_model.pickle","rb") as f:
        __model = pickle.load(f)
    



if __name__ == '__main__':
    locations()
    print(estimator(3,1,60,1176,'Bjjkjon'))
    

