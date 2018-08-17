import requests
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from epoch_weekly import epoch_week_creator as ewc


# %matplotlib inline

# Create an epoch calculator for days and months that takes in a startiong epoch date
#

teen_mom_og=['Farrah', 'Amber', 'Catelynn', 'Maci']
teen_mom_2=['briana', 'jenelle', 'amber','chelsea','leah','kailyn']
# ), 'January2':(,)
before_and_after_dict=ewc(1514764801)
print(before_and_after_dict)
# {'week0':(1514764801,1515369599), 'week1':(1515369601,1515974399), 'week3':(1515974401,1516579199), 'week4':(1516579201,1517183999),
                        # 'week5':(1517184001,1517788799),'week6':(,), 'week7':(,),'week8':(,),'week9'(,)}
                        # 'March':(1519862431,1522540771), 'April':(1522540831,1525132771), 'May':(1522540831,1527811171),'June':(1527811231,1530403171)}
subreddit='&subreddit'
after='&after='
before='&before='
limit='&limit=1000'
teen_mom_stats={}
subreddit_name='teenmomogandteenmom2'
for name in teen_mom_og:
    teen_mom_list=[]
    for k in before_and_after_dict.items():

        base_url='https://api.pushshift.io/reddit/submission/search/?title='
        # months=requests.get('https://api.pushshift.io/reddit/submission/search/?q=kailyn&subreddit=teenmom&after=1527811255&before=1530403195')
        api_call=requests.get(base_url + name + subreddit + subreddit_name + after + str(v[0]) + before + str(v[1]) + limit)
        print(api_call)
        teen_mom_text=json.loads(api_call.text)
        x=len(teen_mom_text['data'])
        teen_mom_list.append(x)
    teen_mom_stats[name]=teen_mom_list
    # print(teen_mom_list)
print(teen_mom_stats)
# df=pd.DataFrame(teen_mom_stats)
df=pd.DataFrame(teen_mom_stats, index=before_and_after_dict)
# count=0
# for k, v in before_and_after_dict.items():
#
#     quick_dict={count:k}
#     df = df.rename(index=quick_dict)
#     count+=1
print(df)
