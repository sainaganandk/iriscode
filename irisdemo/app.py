from flask import *

app=Flask(__name__)

@app.route('/home',methods = ['GET'])

def home():
    sl=request.args.get('s_len')
    sw=request.args.get('s_wid')
    pl=request.args.get('p_len')
    pw=request.args.get('p_wid')
    a=int(sl)
    b=int(sw)
    c=int(pl)
    d=int(pw)
    import pandas as pd
    import numpy as np
    data=pd.read_csv(r"C:/Users/91939/OneDrive/Desktop/ML/datasets/Iris.csv")
    data.drop("Id",axis=1,inplace=True)
    x=data.drop(["Species"],axis=1)
    y=data["Species"]
    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    y=le.fit_transform(y)
    x=np.array(x)
    cat=['setosa','versi','virginica']
    from sklearn import tree
    DT=tree.DecisionTreeClassifier()
    DT.fit(x,y)
    q=np.array([[a,b,c,d]])
    pre=DT.predict(q)
    if cat[int(pre[0])]=="setosa":
        return render_template("setosa.html")
    elif cat[int(pre[0])]=="versi":
        return render_template("versicolor.html")
    elif cat[int(pre[0])]=="virginica":
        return render_template("verginica.html")
    else:
        return "wrong"
    

    
    
@app.route('/poject')

def project():
    return 'this is project'


if __name__=="__main__":
    app.run(debug=True)
