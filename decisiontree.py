from json import load
from sklearn.datasets import load_iris
from sklearn import tree
iris=load_iris()
X=iris.data
y=iris.target
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,y)
tree.plot_tree(clf)
