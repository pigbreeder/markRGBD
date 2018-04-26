import json
import numpy as np
import scipy.io as sio
WIDTH=960
HEIGHT=540


camera_space_point_type = np.dtype({'names':['x', 'y', 'z'],'formats':['f','f', 'f']}, align= True )
filename='haha'
savefile='shirt_1'
savefile='newspaper_2'
DEPTH_PATH = "D:\\graph_data_with_depth\\"

with open(filename) as f:
    data = json.load(f)
kvs = data['videos']['app/static/data/'+savefile]['data'].items()
kvss = sorted(kvs)
data_lst = list(map(lambda x:list(zip(x[1]['mark_list'],x[1]['coordinate_list'])),kvss))

st_f=0
#st_f=112
ed_f=len(kvss)
ed_f=216

lst=[]
for imgs in range(ed_f):
    t_lst = []
    depth = np.fromfile(DEPTH_PATH + savefile + '\\depth\\' + kvss[imgs][0].split('.')[0] + '.txt',dtype=camera_space_point_type)
    print(imgs, kvss[imgs][0])
    for point in range(len(data_lst[imgs])):
        loc = WIDTH * int(data_lst[imgs][point][0]['y']) + int(data_lst[imgs][point][0]['x'])
        # print(imgs, kvss[imgs][0], depth[loc])
        t_lst.append([int(data_lst[imgs][point][0]['x']),int(data_lst[imgs][point][0]['y']),depth[loc][0],depth[loc][1],depth[loc][2]])
    lst.append(t_lst)
save_data = {}
save_data['data'] = lst[st_f:ed_f]
save_data['file'] = list(map(lambda x:x[0], kvss))[st_f:ed_f]

sio.savemat(savefile+'.mat',save_data)