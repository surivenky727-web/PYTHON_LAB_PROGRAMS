import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'A': [1, 3, 2, 4],
    'B': [4, 2, 3, 1]
})

plt.plot(data['A'])
plt.title('Line Plot of A')
plt.show()

plt.plot(data['B'])
plt.title('Line Plot of B')
plt.show()
