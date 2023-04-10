import numpy as np
import time
import os
from configs.local_variables import SPLIT

file_path = f'..\\data_tracking_oxts_imu\\{SPLIT}\\oxts\\'
timestamp_file_name = 'timestamps.txt'
to_radian = np.pi / 180
radius = 6371*10**3

def initial_loader(filename):
	f = open(filename,'r')
	data = f.read()
	data = data.split(' ')
	ax = float(data[11])
	wz = float(data[19])
	f.close()
	return [0,0,0,ax,0,wz]


def timestamp_loader(filename):
	time_list = []
	f = open(filename,'r')
	data = f.read()
	data = data.split('\n')
	start_time = float(data[0].split(':')[-1])
	for i in range(len(data)-1):
		cur_time = float(data[i].split(':')[-1])
		time_list.append(cur_time-start_time)
	f.close()
	return time_list

def oxts_dataloader(filename):
	f = open(filename,'r')
	data = f.read()
	data = data.split(' ')
	lat = float(data[0])
	lon = float(data[1])
	ax = float(data[11])
	wz = float(data[19])
	f.close()
	return lat, lon, ax, wz

def lat_lon_to_x_y(lat_0,lon_0,lat,lon):
	lat_0, lon_0, lat, lon = lat_0*to_radian, lon_0*to_radian, lat*to_radian, lon*to_radian
	delta_lat, delta_lon = lat - lat_0, lon - lon_0
	x_ = np.cos(lat_0)*np.sin(lat) - np.sin(lat_0)*np.cos(lat)*np.cos(delta_lon)
	y_ = np.sin(delta_lon)*np.cos(lon)
	theta = np.arctan2(y_,x_)
	haversine_distance = 2*radius*np.arcsin(np.sqrt(np.sin(delta_lat/2)**2 + np.cos(lat_0)*np.cos(lat)*np.sin(delta_lon/2)**2))
	x = haversine_distance*x_ / np.sqrt(x_**2 + y_**2)
	y = haversine_distance*y_ / np.sqrt(x_**2 + y_**2)
	return x,y

def dataloader():
	try:
		dataset = []
		# timestamp = timestamp_loader(file_path + timestamp_file_name)
		file_name_list = os.listdir(file_path)
		# if len(timestamp) != len(file_name_list):
		# 	raise RuntimeError
		X_init = initial_loader(os.path.join(file_path, file_name_list[0]))
		return X_init

	except RuntimeError as err:
		print("data size doesn't match with timestamps!")

if __name__ == '__main__':
	dataloader()