

#importing libraries 
import pandas as pd 
from sklearn.ensemble import ExtraTreesClassifier 
  
#loading the dataset 
data = pd.read_csv('dataset.csv') 
  
#separating independent and dependent variables 
X = data.iloc[:, 0:10] #independent variables 
y = data.iloc[:, -1] #dependent variable 
  
#building the model 
model = ExtraTreesClassifier() 
model.fit(X, y) 

   #plot graph of feature importances for better visualization 
feat_importances = pd.Series(model.feature_importances_, index=X.columns) 
feat_importances.nlargest(10).plot(kind='barh')