import numpy as np
import skfuzzy as fuzz
from sklearn.linear_model import LinearRegression
 
X = np.array([[2,3],[3,4],[5,5],[6,7],[8,8],[9,10]])
y = np.array([18,22,40,50,60,70])
u = np.arange(0, 11, 1)
sets = [[0,0,5],[0,5,10],[5,10,10]]
 
features = []
for dirt, load in X:
    d = [fuzz.interp_membership(u, fuzz.trimf(u,s), dirt) for s in sets]
    l = [fuzz.interp_membership(u, fuzz.trimf(u,s), load) for s in sets]
    features.append([min(d[0],l[0]), min(d[1],l[1]), min(d[2],l[2])])
 
features = np.array(features)
model = LinearRegression()
model.fit(features, y)
print("MODEL TRAINED SUCCESSFULLY")
print("Rule Weights:", model.coef_.round(2))
print("Bias:", round(model.intercept_, 2))
 
dirt = float(input("Enter Dirtiness (0-10): "))
load = float(input("Enter Load Size (0-10): "))
d = [fuzz.interp_membership(u, fuzz.trimf(u,s), dirt) for s in sets]
l = [fuzz.interp_membership(u, fuzz.trimf(u,s), load) for s in sets]
print("Dirtiness:", [round(x,3) for x in d])
print("Load Size:", [round(x,3) for x in l])
rules = [min(d[i],l[i]) for i in range(3)]
print("Rule Strengths:", [round(x,3) for x in rules])
predicted_time = model.predict(np.array([rules]))
print("Predicted Wash Time =", round(predicted_time[0],2), "minutes")

# pip install numpy scikit-fuzzy scikit-learn