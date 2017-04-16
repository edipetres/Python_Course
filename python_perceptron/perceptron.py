%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
from sklearn import datasets
# https://appliedgo.net/perceptron/

iris = datasets.load_iris()
colors = 'bgr'
for idx, name in enumerate(iris.target_names):
    sepal_length = iris.data[iris.target == idx][:,0]
    sepal_width = iris.data[iris.target == idx][:,1]
    
    plt.scatter(sepal_length, sepal_width, c=colors[idx], label=name)
    
plt.title('Iris Sepal Characteristics')
plt.xlabel('sepal length')
plt.ylabel('sepal width')

plt.legend()
plt.show()




