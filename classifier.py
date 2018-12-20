# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import support vector classifier
from sklearn.svm import SVC 
import cv2
# import warnings to remove any type of future warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# reading csv file and extracting class column to y.
dataf = pd.read_csv("Datasetinfectedhealthy.csv")

# extracting two features
X = dataf.drop(['imgid','fortnum'], axis=1)
y = X['label']
X = X.drop('label', axis=1)

#print(y)
#print("\nTraining dataset:-\n")
#print(X)


log = pd.read_csv("Datasetunlabelledlog.csv")

log = log.tail(1)
X_ul = log.drop(['imgid','fortnum'], axis=1)

#print("\nTest dataset:-\n")
#print(X_ul)


#X.plot(kind='scatter',x='feature1',y='feature2')
#plt.show()


Sum = 0
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

#for n in range(4):
x_train, Xi_test, y_train, yi_test = train_test_split(X, y, test_size=0.3, random_state=60)
svc_classifier = SVC(kernel='linear')
svc_classifier.fit(x_train,y_train)
pred = svc_classifier.predict(Xi_test)

svc_cm = confusion_matrix(yi_test,pred)
svc_correct = svc_cm.trace(offset=0,axis1=0,axis2=1,dtype=None,out=None)
svc_total = svc_cm.sum()
svc_accuracy = (svc_correct/svc_total)*100
print(svc_accuracy)


#Naive-Bayes
'''nb_classifier = GaussianNB()
nb_classifier.fit(x_train, y_train)
nb_prediction = nb_classifier.predict(Xi_test)

nb_cm = confusion_matrix(yi_test,nb_prediction)
nb_correct = nb_cm.trace(offset=0,axis1=0,axis2=1,dtype=None,out=None)
nb_total = nb_cm.sum()
nb_accuracy = (nb_correct/nb_total)*100
print(nb_accuracy)
'''

#Logistic Regression
'''lreg = LogisticRegression()
lreg.fit(x_train, y_train)
lr_prediction = lreg.predict(Xi_test)

lr_cm = confusion_matrix(yi_test,lr_prediction)
lr_correct = lr_cm.trace(offset=0,axis1=0,axis2=1,dtype=None,out=None)
lr_total = lr_cm.sum()
lr_accuracy = (lr_correct/lr_total)*100
print(lr_accuracy)
'''

	#Sum = Sum + pred
	#print("Y test:\n")
	#print(yi_test)  
#print("\nprediction:",Sum)

'''if(Sum < 2):
	print("The leaf is sufficiently healthy!")
else:
	print("The leaf is infected!")
'''
print("\nKeypress on any image window to terminate")
#print(classification_report(yi_test,y_pred))
#print "\n Average precision percentage: %.2f"  %avg_pred + "%"
cv2.waitKey(0)
