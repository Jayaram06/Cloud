#linear regression
import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8]
y = [2,3,3.5,4.6,5.7,6.7,7.9,9.0]


meanX = sum(x)/len(x)
meanY = sum(y)/len(y)

# y = mx + c

numerator = sum((x[i] - meanX) * (y[i] - meanY) for i in range(len(x)))
denominator = sum((x[i] - meanX) ** 2 for i in range(len(x)))

m = numerator / denominator
c = meanY - m * meanX

#newX = 7
#newY = m * newX + c
#print(f"Predicted Y for X={newX}: {newY}")

Y_pred = [c + m * x_i for x_i in x]
newx = 21
newy = c + m * newx

print(newy)

plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(y, Y_pred, color='red', label='Linear Regression Line')
plt.legend()
plt.show()
