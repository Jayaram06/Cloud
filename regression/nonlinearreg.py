#non linear regression
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1,25,63,102,190])

degree = 2
Pfeatures = PolynomialFeatures(degree=degree)
Xp = Pfeatures.fit_transform(x)

model = LinearRegression()
model.fit(Xp,y)

newY = model.predict(Xp)

plt.scatter(x, y, color='green', label='Original data')
plt.plot(x, newY, color='red', label='Non linear regression curve')
plt.legend()
plt.show()

