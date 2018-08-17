from epoch_weekly import epoch_week_creator as ewc
import copy
import requests
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# teenmom 1346198401 1503189601
# TeenMomOGandTeenMom2 1503189601 46weeks
before_and_after_dict=ewc(1503189601, 45)
print(before_and_after_dict)
subreddit='&subreddit='
after='&after='
before='&before='
limit='&limit=1000'
teen_mom_stats={}
teen_mom_list=[]
subreddit_name='TeenMom'
deep_copy_before_and_after=copy.deepcopy(before_and_after_dict)
for k, v in deep_copy_before_and_after.items():
    new_list=[(k,v)]
    new_before_after=new_list[0][1]
    for before_after in new_before_after:
        print(before_after[0], before_after[1])
        # base_url='https://api.pushshift.io/reddit/submission/search/?title='
        base_url='https://api.pushshift.io/reddit/submission/search/?='
        api_call=requests.get(base_url + subreddit + subreddit_name + after + str(before_after[0]) + before + str(before_after[1]) + limit)
        print(api_call)
        teen_mom_text=json.loads(api_call.text)
        x=len(teen_mom_text['data'])
        if x == 0:
            print('length 0')
            exit()
        teen_mom_list.append(x)
        teen_mom_stats['posts']=teen_mom_list
    # print(teen_mom_list)
# print(teen_mom_stats)
df=pd.DataFrame(teen_mom_stats)
print(df)
df.to_csv('TeenMom_subreddit.csv')

# ax=df.plot(legend=None, color='orange')
# ax.set_xlabel('Inception(08/19/2017) until now by week')
# ax.set_ylabel('Total Posts')
# ax.locator_params(integer=True)
# plt.title('Teen Mom OG and Teen Mom 2')
# # plt.legend_=None
# plt.show()
