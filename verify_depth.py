# # -*-coding:utf-8-*-
# #
# #
# #
# import cv2
# import numpy as np
# import sys
#
#
# # __stdout__ = sys.stdout
# # sys.stdout = open(r'log.txt', 'w')
#
# color_intrinsic_matrix = np.array([
#     [1082.1, 0, 958.0],
#     [0, 1067.9, 499.4],
#     [0, 0, 1.0],
# ])
#
# # 960 540
# color_intrinsic_matrix = np.array(
#     [
#     [364.531799, 0,         257.591888],
#     [0,          364.531799,210.606400],
#     [0,          0,         1.0000],
#     ])
# depth_intrinsic_matrix = np.array(
#     [
#         [338.7279, 0, 0],
#         [0, 338.5754, 0],
#         [256.7893, 217.6656, 1.0000],
#     ]).T
# depth_intrinsic_matrix = np.array(
#     [
#         [364.531799, 0, 257.591888],
#         [0, 364.531799, 210.606400],
#         [0, 0, 1.0000],
#     ])
#
#
# def map_color_xyz_xy(points):
#
#     loc_idx = np.dot(color_intrinsic_matrix, points)
#     # loc_idx = np.nan_to_num(loc_idx.T)
#     #
#     print(loc_idx.shape)
#     print(loc_idx/loc_idx[2])
#
#
#
# def map_depth_xyz_xy(filename, imagename):
#     points = load_data(filename)
#     img_mat = load_image(imagename)
#     mat = np.zeros(depth_size, np.uint8)
#     # mat = np.zeros(color_size, np.uint8)
#     #
#     #
#     # map(lambda x:x.append(1), points)
#     for idx in range(len(points)):
#         tmp = list(map(lambda x: float(x), points[idx]))
#         points[idx] = tmp
#     pointss = np.array(points)
#     loc_idx = np.dot(depth_intrinsic_matrix, pointss.T)
#     loc_idx = np.nan_to_num(loc_idx.T)
#     #
#     print(loc_idx.shape)
#     for idx in range(DEPTH_HEIGHT * DEPTH_WIDTH):
#         height = idx // DEPTH_WIDTH
#         width = idx % DEPTH_WIDTH
#
#         if loc_idx[idx][2] < 1e-5:
#             continue
#         w, h = int(loc_idx[idx][0] / loc_idx[idx][2] + 0.5), int(loc_idx[idx][1] / loc_idx[idx][2] + 0.5)
#         if (h < 0 or h >= DEPTH_HEIGHT) or (w < 0 or w >= DEPTH_WIDTH):
#             continue
#         # if idx % 1000 == 0:
#         #     print(idx,loc_idx[idx]/loc_idx[idx][2])
#         #     print('---')
#         zz = int(loc_idx[idx][2] * 1000 + 0.5)
#         mat[h][w] = 255 - (256 * ((zz & 0xfff8) >> 3) / 0x0fff);
#         print(height, width, loc_idx[idx], h, w, )
#
#     cv2.imshow("Image", mat)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     return points, loc_idx, mat, img_mat
#
#
#
# filename = "depth/00081.txt"
# imagename = "rgb/00081.png"
#
# test_data=np.array([0.5432537198066711, -0.413615345954895, 2.826000213623047])
# test_data=np.array([-0.1175,-0.1791, 0.8680])
# map_color_xyz_xy(test_data)
# print("asdf")

# 绘制图像深度信息
import cv2
import numpy as np
WIDTH=960
HEIGHT=540
PATH = "C:\\Users\\lenovo\\Desktop\\code\\markRGBD\\app\\static\\data\\newspaper_1\\depth\\"
FILE = "00064.txt"
camera_space_point_type = np.dtype({
	'names':['x', 'y', 'z'],
	'formats':['f','f', 'f']}, align= True )
data = np.fromfile(PATH + FILE, dtype=camera_space_point_type)
Z = list(map(lambda x :int(255-256*(x[2] * 1000)/4096) if not(-np.inf ==x[2] or np.inf == x[2]) else 0,data.tolist()))

img = np.zeros((HEIGHT, WIDTH, 1), np.uint8)
for h in range(HEIGHT):
    for w in range(WIDTH):
        img[h,w,0] = Z[h*WIDTH + w] #np.random.randint(0,255)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()