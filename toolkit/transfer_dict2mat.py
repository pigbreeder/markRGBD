# newspaper_2 216
# post_olm 112
# 矩阵转置再拉长
import json
import scipy.io as sio
with open('/home/xsy/markRGBD/app/static/result/haha') as f:
    test = json.load(f)
mat_file = {}
base_path = 'app/static/data/'
for video in ['post_olm','post_bjtu','newspaper_2','shirt_1']:#test['videos']:
    vv = base_path + video
    mat_file[vv] = {}
    for jpg in test['videos'][vv]['data']:
        # mat_file[vv][jpg] 
        # test['videos'][vv]['data'][jpg]['point'] 
        mat_file[vv][jpg] = list(map(lambda x:[x[0]['x'], x[0]['y'], float(x[1]['x']), float(x[1]['y']), float(x[1]['z'])], zip(test['videos'][vv]['data'][jpg]['mark_list'], test['videos'][vv]['data'][jpg]['coordinate_list'])))

t_mat=mat_file[vv].items()
newspaper_2={}    
newspaper_2['files']=list(map(lambda x:x[0], t_mat['newspaper_2']))
newspaper_2['data']=list(map(lambda x:x[1], t_mat['newspaper_2']))
scipy.io.savemat('/home/xsy/newspaper_2.mat',newspaper_2)

import json
import numpy as np
base_path = 'app/static/data/'
vv = base_path + 'shirt_1'
for jpg in test['videos'][vv]['data']:
    print(jpg)
    test['videos'][vv]['data'][jpg]['mark_list'] = np.array(test['videos'][vv]['data'][jpg]['mark_list']).reshape(10,10).T.reshape(1,-1).tolist()
    test['videos'][vv]['data'][jpg]['coordinate_list'] = np.array(test['videos'][vv]['data'][jpg]['coordinate_list']).reshape(10,10).T.reshape(1,-1).tolist()