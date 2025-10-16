import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

fig, axs = plt.subplots(1, 3, figsize=(10, 3))
axs[0].scatter(x, y)
axs[0].set_title('Scatter')
axs[1].plot(x, y)
axs[1].set_title('Line')
axs[2].bar(x, y)
axs[2].set_title('Bar')
plt.tight_layout()
plt.show()
