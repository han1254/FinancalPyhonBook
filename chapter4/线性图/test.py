import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("车次上车人数统计表.xlsx")

plt.rcParams['font.sans-serif'] = 'SimHei'

tb1 = data.loc[data['车次']=='D02', ['日期', '上车人数']]

tb2 = data.loc[data['车次']=='D03', ['日期', '上车人数']]

x = np.arange(1, len(tb1['日期']) + 1)

y1 = tb1['上车人数']
y2 = tb2['上车人数']

plt.figure(1)

plt.xticks([1, 5, 10, 15, 20, 24], tb1['日期'].values[[0, 4, 9, 14, 19, 23]], rotation=30)
plt.xlabel('日期')
plt.ylabel('人数')

bar_width = 0.35
plt.bar(x - bar_width/2, y1, bar_width)
plt.bar(x + bar_width/2, y2, bar_width)

plt.legend(['D02', 'D03'])

plt.title('D02和D03上车人数统计表')