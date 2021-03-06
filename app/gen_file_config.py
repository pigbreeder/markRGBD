#-*-coding:utf-8-*-
import sys
import os
import json
import numpy as np
import cv2
from config import *
from collections import OrderedDict
##################################################################
folders = list(filter(lambda x: len(x) > 0, folders.split(',')))
folders = list(map(lambda x: base_path + '/' + x, folders))
gen_file = OrderedDict({'insert_time': 3, 'rgb_path': 'rgb', 'depth_path': 'depth'})
coordinate_file = OrderedDict()

acquire_files = 'cd %s && ls -l | grep .*png|awk \'{print $NF}\''


def cal_3d_coordinate(folder, file_lst, matrix):
	coordinate_file[folder] = OrderedDict()
	for f in file_lst:
		img_mat = cv2.imread(folder + '/depth/' + f, cv2.IMREAD_ANYDEPTH)
		depth_mat = img_mat / 1000.0
		invert_mat = np.mat(matrix).I
		coordinate = invert_mat * depth_mat
		coordinate_file[folder][f] = coordinate.tolist()
	#	coordinate_file[folder].append({})




def gen_save_file():
	gen_file['videos'] = OrderedDict()
	for folder in folders:
		output = os.popen(acquire_files % (folder + '/rgb'))
		files = list(map(lambda x: x.strip(), output.readlines()))
		gen_file['videos'][folder] = OrderedDict()
		# gen_file['videos'][folder]['matrix'] = matrix
		gen_file['videos'][folder]['data'] = OrderedDict()
		for e in files:
			gen_file['videos'][folder]['data'][e] = {'mark_list':[],'coordinate_list':[]}
		#cal_3d_coordinate(folder, files.keys(), matrix)

	output = json.dumps(gen_file)
	with open(save_file, 'w') as f:
		f.write(output)


if __name__ == '__main__':
	pass
	gen_save_file()
