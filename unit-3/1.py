import numpy as np

# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Add arrays
print(np.add(a, b))

# Check conditions
print(np.all(a > 0))
print(np.greater(b, a))
print(np.less_equal(a, b))
print(np.equal(a, a))

# Create zeros and ones
print(np.zeros(3))
print(np.ones(3))

# Linspace and convert to list
print(np.linspace(0, 1, 5).tolist())
