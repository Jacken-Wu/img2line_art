from flask import Flask, render_template, request, jsonify, send_file
from src import *
import os
import webbrowser

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')  # 渲染主页


@app.route('/get_image')
def get_image():
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到图片文件'}), 400
    else:
        return send_file(files[0])


@app.route('/get_edge')
def get_edge():
    files = list(filter(lambda x: x == 'output_edge.png', os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到线稿文件'}), 400
    else:
        return send_file(files[0])


@app.route('/get_line')
def get_line():
    files = list(filter(lambda x: x == 'output_line_block.png', os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到线图文件'}), 400
    else:
        return send_file(files[0])
    
    
@app.route('/get_dot')
def get_dot():
    files = list(filter(lambda x: x == 'output_dot_block.png', os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到点图文件'}), 400
    else:
        return send_file(files[0])


@app.route('/get_combine')
def get_combine():
    files = list(filter(lambda x: x == 'combined.png', os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到合并图文件'}), 400
    else:
        return send_file(files[0])


@app.route('/upload', methods=['POST'])
def upload():
    # 检查请求中是否包含文件
    if 'image' not in request.files:
        return jsonify({'error': '没有文件部分'}), 400

    file = request.files['image']

    # 如果用户没有选择文件，浏览器可能会提交一个空的文件名
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400

    # 删除旧文件
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    for f in files:
        os.remove(f)

    # 保存文件
    filename = "input." + str(file.filename.split('.')[-1])
    file_path = os.path.join("./", filename)
    file.save(file_path)

    return jsonify({'message': '文件上传成功', 'file_path': file_path}), 200


@app.route('/run_edge', methods=['POST'])
def run_edge():
    print(1)
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到图片文件'}), 400
    
    arg1 = request.json['arg1']
    arg2 = request.json['arg2']
    print(arg1)
    edge(files[0], int(arg1), int(arg2))
        
    return jsonify({'message': '边缘检测完成'}), 200


@app.route('/run_line', methods=['POST'])
def run_line():
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到图片文件'}), 400
    
    arg1 = request.json['arg1']
    arg2 = request.json['arg2']
    arg3 = request.json['arg3']
    line_block(files[0], int(arg1), float(arg2), int(arg3))
        
    return jsonify({'message': '线块分割完成'}), 200


@app.route('/run_dot', methods=['POST'])
def run_dot():
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到图片文件'}), 400
    
    arg1 = request.json['arg1']
    arg2 = request.json['arg2']
    arg3 = request.json['arg3']
    arg4 = request.json['arg4']
    dot_block(files[0], int(arg1), float(arg2), int(arg3), float(arg4))
        
    return jsonify({'message': '点块分割完成'}), 200


@app.route('/run_combine', methods=['POST'])
def run_combine():
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    if len(files) == 0:
        return jsonify({'error': '没有找到图片文件'}), 400
    
    if not os.path.exists("output_edge.png"):
        return jsonify({'error': '没有找到线稿文件'}), 400
    
    combine_type = request.json['type']
    img2_path = "output_line_block.png"  # 默认line
    if combine_type == 'N':  # line
        if not os.path.exists("output_line_block.png"):
            return jsonify({'error': '没有找到线图文件'}), 400
    if combine_type == 'Y':  # dot
        img2_path = "output_dot_block.png"
        if not os.path.exists("output_dot_block.png"):
            return jsonify({'error': '没有找到点图文件'}), 400

    combine_images("output_edge.png", img2_path, "combined.png")
    return jsonify({'message': '图片合并完成'}), 200


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5145/')  # 打开浏览器
    app.run(port=5145)  # 在5145端口启动应用
