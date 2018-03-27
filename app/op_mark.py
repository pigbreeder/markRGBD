#-*-coding:utf-8-*-
from app.my_debug import debug_print
import os
import sys
import json
import datetime
import time
from app.config import *
import numpy as np
from collections import OrderedDict

save_interval = 1 * 10
camera_space_point_type = np.dtype({
	'names':['x', 'y', 'z'],
	'formats':['f','f', 'f']}, align= True )

class ImageData(object):
	def __init__(self):
		self.cache_data = OrderedDict()
		self.image_3D_coordinate = OrderedDict()
		with open(save_file) as f:
			self.cache_data = json.load(f)
		# with open(image_3D_coordinate_file) as f:
		# 	self.image_3D_coordinate = json.load(f)
		self.cache_data['insert_time'] = time.time()

	def get_image_adjoin(self, video_name='', image_id=''):
		if not self.cache_data['videos'].get(video_name, None):
			return [-1, -1]
		lst = list(self.cache_data['videos'][video_name]['data'].keys())
		idx = lst.index(image_id)
		# debug_print(idx)
		st = idx - 1
		ed = idx + 1
		if st < 0:
			st = -1
		else:
			st = lst[st]
		if ed >= len(lst):
			ed = -1
		else:
			ed = lst[ed]
		return {'tot':len(lst),'idx':idx,'st':st, 'ed':ed}

	def get_videos(self):
		return list(self.cache_data['videos'].keys())

	def get_images(self, video_name=''):
		if self.cache_data['videos'].get(video_name, None):
			return list(self.cache_data['videos'][video_name]['data'].keys())
		else:
			return []
	def get_images_marks(self, video_name=''):
		if self.cache_data['videos'].get(video_name, None):
			ret = []
			for k in self.cache_data['videos'][video_name]['data'].keys():
				ret.append(len(self.cache_data['videos'][video_name]['data'][k]['mark_list']))
			return ret
		else:
			return []
	def get_3d_coordinate(self, video_name='', image_id=''):
		return self.image_3D_coordinate['videos'][video_name][image_id]
	def mark_check(self, video_name='', image_id='', mark_point=''):
		if self.image_3D_coordinate.get(image_id, None) == None:
			self.image_3D_coordinate[image_id] = np.fromfile(video_name + '/depth/' + image_id[:-4] + '.txt', dtype=camera_space_point_type)
		h, w = mark_point.split(',')
		idx = int(float(h)) * WIDTH + int(float(w))
		ok = not (np.inf in self.image_3D_coordinate[image_id][idx] or -np.inf in self.image_3D_coordinate[image_id][idx])
		# 差值计算
		if not ok:
			coordinate = self.cal_difference_value(image_id, w, idx)
			return {'ok':'true','coordinate':list(map(lambda x:str(x),coordinate)) }
		else:
			return {'ok':'true','coordinate':list(map(lambda x:str(x),self.image_3D_coordinate[image_id][idx].tolist())) }
	def cal_difference_value(self, image_id, w, index):
		for i in range(int(w)):
			idx1 = index - i
			idx2 = index + i
			if not (np.inf in self.image_3D_coordinate[image_id][idx2] or -np.inf in self.image_3D_coordinate[image_id][idx2]) and \
				not (np.inf in self.image_3D_coordinate[image_id][idx1] or -np.inf in self.image_3D_coordinate[image_id][idx1]):
				# debug_print((type(self.image_3D_coordinate[image_id][idx1].tolist()),'---',self.image_3D_coordinate[image_id][idx2]))
				# debug_print(type((self.image_3D_coordinate[image_id][idx1] + self.image_3D_coordinate[image_id][idx2])/2))
				ret_lst = []
				for a, b in zip(self.image_3D_coordinate[image_id][idx1], self.image_3D_coordinate[image_id][idx2]):
					ret_lst.append((float(a) + float(b))/2)
				return ret_lst
		return
		

	def get_image_mark(self, video_name='', image_id=''):
		if self.cache_data['videos'].get(video_name, None):
			return self.cache_data['videos'][video_name]['data'][image_id]
		return {'mark_list':[],'coordinate_list':[]}

	def mark_image(self, video_name='', image_id='', mark_list=None, coordinate_list=None):
		if mark_list == None:
			mark_list = []
		if coordinate_list == None:
			coordinate_list = []
		self.cache_data['videos'][video_name]['data'][image_id] = {'mark_list':mark_list, 'coordinate_list':coordinate_list}
		t_time = self.cache_data['insert_time']
		tt_time = time.time()
		self.cache_data['insert_time'] = tt_time
		# if tt_time - t_time > 60:
		self.save(tt_time)

	def save(self, times):
		cmd = 'mv %s %s' % (save_file, save_file + str(times))
		with open(save_file, 'w') as f:
			f.write(json.dumps(self.cache_data))
