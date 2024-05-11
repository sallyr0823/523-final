import pickle
import pandas as pd

file = r'/Users/sallyr/Downloads/TraceRCA__changed-main/uninjection/3.pkl' #下载下来的原始文件
with open(str(file),'rb') as f:
    pkl_data = pickle.load(f)


# 使用列表来收集所有 DataFrame
dataframes = [pd.DataFrame(data) for data in pkl_data]

# 一次性合并所有 DataFrame
df = pd.concat(dataframes, ignore_index=True)


source = []
target = []
for num in range(len(df)):
    source_new,target_new = df.loc[num,'s_t']
    source.append(source_new)
    target.append(target_new)
df['source'] = source
df['target'] = target

# df.to_csv(r'F:\ruijie\AIOPS\TraceRCA-main\A\uninjection\pkl_2_data.csv')

def save_dict(data, name):
    with open(name , 'wb') as f:
        pickle.dump(data, f)

save_dict(df,r'/Users/sallyr/Downloads/TraceRCA__changed-main/uninjection/3_data.pkl') #重新调整后符合代码输入格式的数据


# '''反向解析时间戳'''
# import time
# def stampToTime(stamp):
#     datatime = time.strftime('%T-%m-%d %H:%M:%S',time.localtime(float(str(int(stamp))[0:10])))
#     datatime = datatime + '.' + str(stamp)[10:]
#     return datatime
#

