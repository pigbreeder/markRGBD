# 图像标记程序

使用kinect采集深度图和彩色图，对齐后输出彩色图对应的深度图。
通过相机标定得到图片的内部矩阵。

然后人工标定每帧中关键点的位置变化.

## 使用流程

---
1. 采集深度和彩色图数据
2. 相机标定获取内部矩阵
3. 将数据分为`package_name/rgb,package_name/depth`放到app/static/data下
4. 在app/config.py中输入对应的参数
5. gen_file_config.py 完成
6. 在根目录运行程序进行标定。最后结果存储在config.py中设置的路径中。
7. 运行 nohup uwsgi --http 0.0.0.0:5000 --file run.py --callable app --master --processes 1 --threads 12 --stats 127.0.0.1:9191