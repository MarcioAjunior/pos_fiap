import matplotlib.pyplot as plt
import numpy as np
import random

random.seed(5)

image = [
    [random.randint(10,220) for i in range(5)]
    ,[random.randint(10,220) for i in range(5)]
    ,[random.randint(10,220) for i in range(5)]
    ,[random.randint(10,220) for i in range(5)]
    ,[random.randint(10,220) for i in range(5)]
]

print(image)

image_array = np.array(image)

plt.imshow(image_array, cmap='gray', vmin=0, vmax=255)
plt.colorbar
plt.show()