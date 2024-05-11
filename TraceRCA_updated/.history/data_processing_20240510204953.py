import pickle
import pandas as pd

file = r'/Users/sallyr/Downloads/TraceRCA__changed-main/test/payment_cpu_1014.pkl' 
with open(str(file),'rb') as f:
    pkl_data = pickle.load(f)
df = pd.DataFrame()
print(len(pkl_data))
for num in range(len(pkl_data)):
    print(num)
    df_new = pd.DataFrame(pkl_data[num])
    df = pd.concat([df,df_new],ignore_index=True)


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

save_dict(df,r'/Users/sallyr/Downloads/TraceRCA__changed-main/uninjection/payment_cpu_1014.pkl')


