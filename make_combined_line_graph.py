import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

tm_df=pd.read_csv('teenmom_subreddit.csv', 'r', header=0, delimiter=',')
tmog2_df=pd.read_csv('TeenMomOGandTeenMom2_subreddit.csv', 'r', header=0, delimiter=',')
print(tmog2_df['posts'])
# with open('teenmom_subreddit.csv') as f:
#     x=f.readlines()
#     print(x)
# tm_df['posts'].plot()
# tm_df['posts'].set_label("D")

# l = ax.get_legend_handles_labels()
ax = tm_df['posts'].plot()
tmog2_df['posts'].plot(ax=ax)
l=plt.legend()
l.get_texts()[0].set_text('Teen Mom')
l.get_texts()[1].set_text('TMOG&TM2')
ax.set_xlabel('Since Longname Created(08/19/2017) by week')
ax.set_ylabel('Total Posts')
plt.show()
