from flask import Blueprint, render_template, abort, request, jsonify
from jinja2 import TemplateNotFound
from app.op_mark import ImageData
from flask import current_app
from app.my_debug import debug_print
import json
image_data = ImageData()

simple_page = Blueprint('simple_page', __name__,
        template_folder='templates')
@simple_page.route('/')
@simple_page.route('/index')
def index():
    return render_template('main.html')
@simple_page.route('/add')
def add():
    a = request.args.get('a',0,type=int)
    b = request.args.get('b',0,type=int)
    return jsonify(result=a+b)

@simple_page.route('/video', methods=['GET','POST'])
def video():
    if request.method  == 'POST':
        #videos={'videos':['a','b']}
        videos = image_data.get_videos()
        current_app.logger.debug(videos)
        return jsonify(videos=videos)
    videos = image_data.get_videos()
    return render_template('video.html')

@simple_page.route('/image',methods=['GET','POST'])
def image():
    if request.method == 'POST':
        video_name = request.form.get("video_name","")
        # images = {'':'null','a':['img1','img2','img3'],'b':['ha1','ha2']}
        # images = images[video_name]
        images = image_data.get_images(video_name)
        lens = image_data.get_images_marks(video_name)
        return jsonify({'images':images,'lens':lens})
    return render_template('image.html')

@simple_page.route('/mark',methods=['GET','POST'])
def mark():
    return render_template('mark.html')

@simple_page.route('/mark/adjoin',methods=['GET','POST'])
def mark_adjoin():
    video_name = request.form.get("video_name","")
    image_id = request.form.get("image_id","")
    marks = [1,1]
    marks = image_data.get_image_adjoin(video_name,image_id)
    return jsonify(marks)

@simple_page.route('/mark/list', methods=['POST'])
def mark_list():
    video_name = request.form.get("video_name","")
    image_id = request.form.get("image_id","")
    # marks = [{'x':'100','y':'200'},{'x':'150','y':'300'}]
    marks = image_data.get_image_mark(video_name, image_id)
    return jsonify(marks)

@simple_page.route('/mark/save', methods=['POST'])
def mark_save():
    # video_name = request.form.get("video_name","")
    # image_id = request.form.get("image_id","")
    # mark_list = request.form.get("mark_list","")
    data = json.loads(request.data)
    debug_print(data)
    # with open('debug','a+') as f:
    #     print(request.data,file=f)
    #     print(data,file=f)
    image_data.mark_image(data['video_name'],data['image_id'],data['mark_list'],data['coordinate_list'])
    return jsonify({'success':'1'})

@simple_page.route('/mark/check', methods=['POST'])
def mark_check():
    # video_name = request.form.get("video_name","")
    # image_id = request.form.get("image_id","")
    # mark = request.form.get("mark","")
    data = json.loads(request.data)
    ret = image_data.mark_check(data['video_name'],data['image_id'],data['mark'])
    debug_print(ret)
    # ret = image_data.mark_check(video_name, image_id, mark)
    return jsonify(ret)