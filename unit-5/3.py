import matplotlib.pyplot as plt
import pandas as pd

dates = pd.date_range('2025-01-01', periods=4)
values = [100, 120, 115, 130]
plt.plot(dates, values)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time-Series Data')
plt.xticks(rotation=45)
plt.show()
