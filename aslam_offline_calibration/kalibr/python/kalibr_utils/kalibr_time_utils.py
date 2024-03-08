import time
import collections
# from pywayne


__time_elapsed_dict = collections.defaultdict(float)
__save_path = ''

def save_time_consumption_to_file(path: str):
	__save_path = path

def TIC(tag: str):
	print(f'TIC: {tag}')
	__time_elapsed_dict[tag] = time.time()

def TOC(tag: str):
	print(f'TOC: {tag}')
	cur_timestamp = time.time()
	elapsed_time = cur_timestamp - __time_elapsed_dict[tag]
	__time_elapsed_dict.pop(tag)
	# with open(__save_path, 'r') as f:
	# 	save_str_list = [
	# 		str(cur_timestamp),
	# 		tag,
	# 		str(elapsed_time)
	# 	]
	# 	f.writelines(','.join(save_str_list))

	# print(elapsed_time)
	return elapsed_time
