# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import support vector classifier
from sklearn.svm import SVC 
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from catboost import CatBoostRegressor
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import cross_val_score
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

print("\nTraining dataset:-\n")
print(X)


log = pd.read_csv("datasetlog/Datasetunlabelledlog.csv")

log = log.tail(1)
X_ul = log.drop(['imgid','fortnum'], axis=1)

print("\nTest dataset:-\n")
print(X_ul)

print("\n*To terminate press (q)*")

#X.plot(kind='scatter',x='feature1',y='feature2')
#plt.show()


Sum = 0
from sklearn.model_selection import train_test_split  
for n in range(2):
	x_train, Xi_test, y_train, yi_test = train_test_split(X, y, test_size=0.52, random_state=60)  
	if cv2.waitKey(1) == ord('q' or 'Q'): break  

	#Following are the 11 classifiers. The best model suited for the required dataset can be chosen.  

	#SVM classifier 
	classifierSVM = SVC()  
	classifierSVM.fit(x_train, y_train)  
	pred = classifierSVM.predict(X_ul)

	#Random Forest classifier
	classifierRF = RandomForestClassifier(n_estimators =20,criterion = 'entropy',n_jobs=-1)
	classifierRF.fit(x_train, y_train)
	pred = classifierRF.predict(X_ul)

	#Logistic Regression classifier
	classifierLR = LogisticRegression(C=10)
	classifierLR.fit(x_train, y_train)
	pred = classifierLR.predict(X_ul)


	#KNN classifier
	classifierKNN = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
	classifierKNN.fit(x_train, y_train)
	pred = classifierKNN.predict(X_ul)

	#Naive Bayes classifier
	classifierNB = GaussianNB()
	classifierNB.fit(x_train, y_train)
	pred = classifierNB.predict(X_ul)


	#XGBoost classifier
	classifierXGB = XGBClassifier(n_estimators=20,n_jobs=-1)
	classifierXGB.fit(x_train, y_train)
	pred = classifierXGB.predict(X_ul)


	#Bagging Classifier
	classifierBG = BaggingClassifier(tree.DecisionTreeClassifier(),n_estimators=20,n_jobs=-1)
	classifierBG.fit(x_train, y_train)
	pred = classifierBG.predict(X_ul)

	#Gradient Boosting Classifier
	classifierGB=GradientBoostingClassifier(n_estimators=20,learning_rate=1.0,max_depth=1).fit(x_train, y_train)
	pred = classifierGB.predict(X_ul)


	#Adaboost classifier
	classifierAB = AdaBoostClassifier(base_estimator=RandomForestClassifier(n_estimators = 20,criterion = 'entropy',n_jobs=-1),n_estimators = 20)
	classifierAB.fit(x_train, y_train)
	pred = classifierAB.predict(X_ul)


	#Catboost Classifier

	classifierCB=CatBoostRegressor(iterations=20, depth=5, learning_rate=0.1, loss_function='RMSE',silent=True)
	classifierCB.fit(x_train, y_train,eval_set=(Xi_test, yi_test))
	pred = classifierCB.predict(X_ul)
	th=0.5
	#this is done as catboost provides answer in fractions like 1.02,0.98,etc
	pred[pred>th]=1
	pred[pred<=th]=0


	#Classifier that can use variable weights from all above classifiers
	# classifierVC = VotingClassifier(estimators=[('rf', classifierRF),('svm', classifierSVM),('lr',classifierLR ), ('nb', classifierNB),('knn', classifierKNN),('bg', classifierBG),('xgb',classifierXGB),('gb', classifierGB),('ab', classifierAB)],voting='soft', weights=[1,1,1,1,1,1,1,1,1])
	# classifierVC.fit(x_train, y_train)
	# pred = classifierVC.predict(X_ul)



	#Results from various classifiers; Catboost is not included as it does not provide output in the required format
	for clf, label in zip([classifierRF,classifierSVM,classifierLR,classifierNB,classifierKNN,classifierBG,classifierXGB,classifierGB,classifierAB],#classifierVC],
	['RF', 'SVM', 'LR', 'NB','KNN','BG','XGB','GB','AB']):#,'VT']):
		scores = cross_val_score(clf, X, [round(i) for i in y], cv=10, scoring='accuracy')#k to be increased for better performance
		print("Accuracy: %0.4f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))

	#After identifying the best model using the above report, all other models can be commented
		
	Sum = Sum + pred
	print(pred)

print("\nprediction: %d" %int(Sum/4))

if(Sum < 2):
	print("The leaf is sufficiently healthy!")
else:
	print("The leaf is infected!")

print("\nKeypress on any image window to terminate")

#from sklearn.metrics import classification_report, confusion_matrix  

#print(classification_report(yi_test,y_pred))
#print "\n Average precision percentage: %.2f"  %avg_pred + "%"
cv2.waitKey(0)
