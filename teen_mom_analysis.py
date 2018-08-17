from epoch_weekly import epoch_week_creator as ewc
import copy
import requests
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

before_and_after_dict=ewc(1503189601, 39)
teen_mom_og=['Farrah', 'Amber', 'Catelynn', 'Maci']
teen_mom_2=['Briana', 'Kailyn', 'Leah', 'Jenelle', 'Chelsea']
# 'Jenelle','Chelsea','Leah','Kailyn'
subreddit='&subreddit='
after='&after='
before='&before='
limit='&limit=1000'
teen_mom_stats={}
score_avg_df={}
subreddit_name='TeenMomOGandTeenMom2'
deep_copy_before_and_after=copy.deepcopy(before_and_after_dict)

for name in teen_mom_2:
    teen_mom_list=[]
    overall_score_avg=[]
    sum_of=0
    for k, v in deep_copy_before_and_after.items():
        new_list=[(k,v)]
        new_before_after=new_list[0][1]
        for before_after in new_before_after:
            # print(before_after[0], before_after[1])
            time.sleep(1)
            base_url='https://api.pushshift.io/reddit/submission/search/?title='
            api_call=requests.get(base_url + name + subreddit + subreddit_name + after + str(before_after[0]) + before + str(before_after[1]) + limit)
            # print(base_url + name + subreddit + subreddit_name + after + str(before_after[0]) + before + str(before_after[1]) + limit)
            teen_mom_text=json.loads(api_call.text)
            print(teen_mom_text['data'])
            x=len(teen_mom_text['data'])
            comment_count=0
            score=0
            # overall_score_avg=0
            for  y in teen_mom_text['data']:
                print(name )
                comment_count+=y['num_comments']
                score+=y['score']
                print(score)
                teen_mom_list.append(comment_count)
                # overall_score_avg.append(score)
                sum_of=score/x
                print(sum_of)
            overall_score_avg.append(score/2)

        teen_mom_stats[name]=teen_mom_list
        score_avg_df[name]=overall_score_avg
        print(overall_score_avg)
    # df=pd.DataFrame(teen_mom_stats)


    df2=pd.DataFrame(score_avg_df)
    print(df2)
    ax=df2.plot()


    # df2.to_csv(name + '_bar_graph_post_score_avg.csv')
    # df2.plot(ax=ax)
    ax.set_xlabel('Week of 2018')
    ax.set_ylabel('Post Average with Name in Title')
    # ax.locator_params(integer=True)
    plt.title('Teen Mom 2/TeenMomOGandTeenMom2')
fig1 = plt.gcf()

plt.show()
fig1.savefig('teen_mom_2_avg_bar_graph_post_score.png')

# ax = tm_df['posts'].plot()
# tmog2_df['posts'].plot(ax=ax)
# l=plt.legend()
# l.get_texts()[0].set_text('Teen Mom')
# l.get_texts()[1].set_text('TMOG&TM2')
# ax.set_xlabel('Since Longname Created(08/19/2017) by week')
# ax.set_ylabel('Total Posts')
# plt.show()
# plt.save
