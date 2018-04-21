import json
import numpy as np
import scipy.io as sio
filename='haha'
savefile='shirt_1'
#savefile='newspaper_2'
frames=216
point_num=100

with open(filename) as f:
    data = json.load(f)
kvs = data['videos']['app/static/data/'+savefile]['data'].items()
kvss = sorted(kvs)
save_data = {}
data_lst = list(map(lambda x:list(zip(x[1]['mark_list'],x[1]['coordinate_list'])),kvss))
st_f=0
#st_f=112
ed_f=len(kvss)

lst=[]
for imgs in range(len(kvss)):
    t_lst = []
    for point in range(len(data_lst[imgs])):
                t_lst.append([float(data_lst[imgs][point][0]['x']),float(data_lst[imgs][point][0]['y']),float(data_lst[imgs][point][1]['x']),float(data_lst[imgs][point][1]['y']),float(data_lst[imgs][point][1]['z'])])
                #data_lst[imgs][point] =[float(data_lst[imgs][point][0]['x']),float(data_lst[imgs][point][0]['y']),float(data_lst[imgs][point][1]['x']),float(data_lst[imgs][point][1]['y']),float(data_lst[imgs][point][1]['z'])]
        #data_lst[imgs][point] = [list(map(lambda x:float(x),data_lst[imgs][point][0])), list(map(lambda x:float(x),data_lst[imgs][point][1]))]
    lst.append(t_lst)

tt = np.array(lst)
print(tt.shape)
save_data['data'] = lst[st_f:ed_f]
save_data['file'] = list(map(lambda x:x[0], kvss))[st_f:ed_f]

sio.savemat(savefile+'.mat',save_data)
