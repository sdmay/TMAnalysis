import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

tm_jenelle=pd.read_csv('Jenelle_post_score_avg.csv', 'r', header=0, delimiter=',')
tm_briana=pd.read_csv('Briana_post_score_avg.csv', 'r', header=0, delimiter=',')
tm_kailyn=pd.read_csv('Kailyn_post_score_avg.csv', 'r', header=0, delimiter=',')
tm_leah=pd.read_csv('Leah_post_score_avg.csv', 'r', header=0, delimiter=',')
tm_chelsea=pd.read_csv('Chelsea_post_score_avg.csv', 'r', header=0, delimiter=',')
print(tm_briana)
ax = tm_jenelle['Jenelle'].plot()
tm_briana['Briana'].plot(ax=ax)
tm_leah['Leah'].plot(ax=ax)
tm_kailyn['Kailyn'].plot(ax=ax)
tm_chelsea['Chelsea'].plot(ax=ax)
l=plt.legend()
l.get_texts()[0].set_text('Jenelle')
l.get_texts()[1].set_text('Briana')
ax.set_xlabel('Since Longname Created(08/19/2017) by week')
ax.set_ylabel('Avg. Post Scores')
plt.title('Teen Mom 2')
plt.show()
