import pandas as pd
import numpy as np

def inter_quantile_range(data,column, upper,lower):
    q1 = data[column].quantile(upper)
    q3 = data[column].quantile(lower)
    iqr = q3-q1
    return q1,q3,iqr

def perform(data,i,instruction):
    if i == 110:
        if(instruction in data.columns):
            data[instruction] = data[instruction].dropna()
    elif i == 121:
        for i in data.columns:
            if type(data[i]) in ['int16','int32','int64','float16','float32','float64']:
                data[i] = data[i].fillna(np.mean(data[i]))
    elif i == 122:
        for i in data.columns:
            if type(data[i]) in ['int16','int32','int64','float16','float32','float64']:
                data[i] = data[i].fillna(np.median(data[i]))
    elif i == 123:
        for i in data.columns:
            if type(data[i]) in ['int16','int32','int64','float16','float32','float64']:
                data[i] = data[i].fillna(float(instruction))
    elif i == 130:
        for i in data.columns:
            if type(data[i]) in ['int16','int32','int64','float16','float32','float64']:
                q1,q3,iqr = inter_quantile_range(data,i,u,l)
                l = q1 - 1.5*iqr
                u = q3 + 1.5*iqr
                data[i] = data[(data[i] < u) | (data[i] > l)]
    elif i == 211:
        data = pd.read_csv(instruction)
    elif i == 212:
        data = pd.read_excel(instruction)
    elif i == 221:
        df = pd.read_csv(instruction)
        if len(df) == len(data):
            data = pd.concat([df,data], axis = 1)
    elif i == 222:
        df = pd.read_excel(instruction)
        if len(df) == len(data):
            data = pd.concat([df,data],axis = 1)
    elif i == 310:
        if len(data) < int(instruction):
            data.drop(int(instruction),inplace = True)
    elif i == 320:
        if instruction in tuple(data.columns):
            data.drop(instruction, axis=1,inplace = True)
    elif i == 411:
        for i in data.columns:
            if type(data[i]) not in ['int16','int32','int64','float16','float32','float64']:
                data[i] = pd.get_dummies(data[i], drop_first = True)
    elif i == 412:
        for i in data.columns:
            if type(data[i]) not in ['int16','int32','int64','float16','float32','float64']:
                data[i].astype('category')
                data[i] = data[i].cat.codes
    elif i == 421:
        for i in data.columns:
            if type(data[i]) not in ['int16','int32','int64','float16','float32','float64']:
                data[i] = (data[i]-min(data[i])/(max(data[i])) - min(data[i]))
    elif i == 422:
        for i in data.columns:
            if type(data[i]) not in ['int16','int32','int64','float16','float32','float64']:
                data[i] = data[i] - data[i].mean()/data[i].std()
    elif i == 431:
        for i in data.columns:
            if type(data[i]) not in ['int16','int32','int64','float16','float32','float64']:
                data[i] = data[i].transform(lambda x: np.log(x))
    elif i == 432:
        for i in data.columns:
            if type(data[i]) not in ['int16','int32','int64','float16','float32','float64']:
                data[i] = data[i].transform(lambda x: x*x)
    return data

def make(FILE,ATTFILE,data):
    d2  = data
    f1 = open(FILE,"r")
    f2 = open(ATTFILE,"r")
    l1 = f1.readlines()
    l2 = f2.readlines()
    if l1 != []:
        l1  = l1[0]
    else: 
        return data,data
    if l2 != []:
        l2 = l2[0]
    else:
        return data,data
    l1 = l1.split(",")
    l2 = l2.split(",")
    for i in range(len(l2) - 1):
        data = perform(data,int(l1[i]),l2[i])
        d2 = perform(d2,int((l1[i])),l2[i])
        try:
            l1.remove('')
        except:
            pass
    d2 = perform(d2,int(float(l1[-1])),l2)
    return data,d2

    