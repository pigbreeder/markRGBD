#-*-coding:utf-8-*-
import os,sys,json
import datetime,time
from app.config import *
import numpy as np

save_interval = 1 * 10

class ImageData(object):
	def __init__(self):
		self.cache_data = {}
		self.image_3D_coordinate = {}
		with open(save_file) as f:
			self.cache_data = json.load(f)
		with open(image_3D_coordinate_file) as f:
			self.image_3D_coordinate = json.load(f)
		self.cache_data['insert_time'] = time.time()
			
	def get_image_adjoin(self, video_name='',image_id=''):
		if not self.cache_data.get(video_name, None):
			return [-1,-1]
		lst = self.cache_data['videos'][video_name]['data'].keys()	
		idx = lst.index[image_id]
		st=idx-1
		ed=idx+1
		if idx < 0:
			st = -1
		else:
			st = lst[st]	
		if idx >= len(lst):
			ed = -1	
		else:
			ed = lst[ed]
		return [st, ed]

	def get_videos(self):
		return list(self.cache_data['videos'].keys())

	def get_images(self, video_name=''):
		if self.cache_data['videos'].get(video_name, None):
			return list(self.cache_data['videos'][video_name]['data'].keys())
		else:
			return []

	def get_3d_coordinate(self, video_name='', image_id=''):
		return self.image_3D_coordinate['videos'][video_name][image_id]

	def get_image_mark(self, video_name='', image_id=''):
		if self.cache_data['videos'].get(video_name, None):
			return list(self.cache_data['videos'][video_name]['data'][image_id])
		return []

	def mark_image(self, video_name='', image_id='',mark_list=[]):
		self.cache_data['videos'][video_name]['data'][image_id] = mark_list
		t_time = self.cache_data['insert_time']
		tt_time = time.time()
		self.cache_data['insert_time'] = tt_time
		if tt_time - t_time > 60:
			self.save()	
	def save(self, times):
		cmd = 'mv %s %s' % (save_file, save_file + str(times))
		with open(save_file,'w') as f:
			f.write(json.dumps(self.cache_data)) 
