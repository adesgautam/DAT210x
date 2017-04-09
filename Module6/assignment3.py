#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap

X = pd.read_csv("Datasets/parkinsons.data")
y = X['status'].copy()

X = X.drop(labels=['name','status'], axis=1)
#print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)


#T = preprocessing.StandardScaler().fit(X_train)  # score: 0.932203389831  C: 1.55 gamma: 0.097
#T = preprocessing.MinMaxScaler().fit(X_train)    # score: 0.881355932203  C: 0.75 gamma: 0.098
#T = preprocessing.MaxAbsScaler().fit(X_train)    # score: 0.881355932203  C: 1.2  gamma: 0.098
#T = preprocessing.Normalizer().fit(X_train)      # score: 0.796610169492  C: 0.05 gamma: 0.001
#T = preprocessing.KernelCenterer().fit(X_train)  # score: 0.915254237288  C: 1.7  gamma: 0.006
#T = X_train                                                 # score: 0.915254237288  C: 1.65 gamma: 0.005

processor = preprocessing.StandardScaler()
processor.fit(X_train)
X_train = processor.transform(X_train)
X_test = processor.transform(X_test)

# PCA
#for i in range(4,14):
# ISOMAP
for i in range(2,5):
	for j in range(4,6):
		# pca = PCA(n_components=i)
		# T_pca = pca.fit_transform(T)
		# print("n_components(PCA): "+str(i))

		# Isomap
		iso = Isomap(n_neighbors=i, n_components=j)
		iso.fit(X_train)
		X_train = iso.transform(X_train)
		X_test = iso.transform(X_test)
		print("n_neighbors(ISOMAP): "+str(i)+ " n_components: "+str(j))

		best_score=0
		C=0
		gamma=0

		for c in np.arange(0.05,2,0.05):
			for g in np.arange(0.001,0.1,0.001):
				svc = SVC(C=c, gamma=g)
				svc.fit(X_train, y_train)		
				score = svc.score(X_test, y_test)
				if best_score<score:
					best_score=score
					C = c
					gamma = g


		print("best_score: ")
		print(best_score)
		print("C: "+str(C)+" gamma: "+str(gamma))