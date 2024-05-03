from sklearn.linear_model import LinearRegression
import numpy as np

np.random.seed = 5

X = np.array([
        [1]
        ,[2]
        ,[3]
        ,[4]
        ,[5]
    ])
y = np.array([2,4,6,8,10])

model = LinearRegression()

model.fit(X,y)

prediction = model.predict([
        [7]
    ])

print(f'Regressão linear prediction : {prediction[0]}')