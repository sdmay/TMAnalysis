import copy
import time

epoch_time_now=int(time.time())
# print(epoch_time_now)
def epoch_week_creator(epoch_start, length_of_weeks):
    if epoch_start > epoch_time_now:
        print('Lotto numbers too? How do you expect me to know the future?')
        return
    i=0
    epoch_dict={}
    epoch_list=[]
    print(length_of_weeks)
    while i < length_of_weeks:
        # print(len(epoch_dict))
        x=i-1
        week='week'
        check='week'
        week=week + str(i)
        check=check + str(x)
        epoch_week=604798
        start_point=epoch_start + i
        end_point=start_point + epoch_week
        if len(epoch_dict) == 0:
            # print('zero')
            epoch_dict[week]={(start_point, end_point),}
        if len(epoch_dict) > 0:
            deep_copy_epoch_dict=copy.deepcopy(epoch_dict)
            for k, v in deep_copy_epoch_dict.items():
                new_list=[(k, v)]
                if check in new_list[-1::][0]:
                    x= new_list[-1::][0][1]
                    for a in x:
                        new_week=a[1]+1
                        new_end=new_week + epoch_week
                        if new_week > epoch_time_now:
                            print('Getting too far ahead now...')
                            return
                        epoch_dict[week]={(new_week, new_end)}
        i+=1
    # print(epoch_dict)
    return epoch_dict
# epoch_week_creator(1514764801)
