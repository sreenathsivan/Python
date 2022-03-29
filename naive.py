from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
irisdataset=load_iris()

X=irisdataset.data
y=irisdataset.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=0)
gnb=GaussianNB()
gnb.fit(X_train,y_train)
print(gnb.predict(X_test))
x_new=[[5,5,4,4]]

print("predicted output for [5,5,4,4]",gnb.predict(x_new))
print("Naive bayes score:",gnb.score(X_test,y_test))
