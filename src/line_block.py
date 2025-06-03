from PIL import Image, ImageDraw
import numpy as np
from skimage.segmentation import slic
from skimage.color import rgb2gray
import sys
import os
from tqdm import tqdm


line_thickness = 2
density_scale = 0.1
block_size = 48
if len(sys.argv) > 1:
    line_thickness = int(sys.argv[1])
if len(sys.argv) > 2:
    density_scale = float(sys.argv[2])
if len(sys.argv) > 3:
    block_size = int(sys.argv[3])


def get_files():
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    return files


def adaptive_line_conversion(input_path,
                            line_thickness=2,
                            density_scale=0.1,
                            block_size=48):
    """
    分块自适应线条化算法
    参数：
    block_size: 分块尺寸（建议32-128）
    density_scale: 密度缩放系数（0.01-1.0）
    """
    output_path = 'output_line_block.png'

    # 读取图像并转为灰度
    img = Image.open(input_path).convert('RGB')
    width, height = img.size
    gray_img = rgb2gray(np.array(img))
    
    # 使用SLIC算法进行超像素分割
    segments = slic(np.array(img), 
                   n_segments=(width*height)//(block_size**2), 
                   compactness=10)
    
    # 创建画布
    result = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(result)
    
    # 遍历每个超像素区块
    print('开始处理...')
    for i in tqdm(np.unique(segments)):
        # 获取区块蒙版
        mask = (segments == i)
        y_indices, x_indices = np.where(mask)
        
        if len(y_indices) == 0:
            continue
            
        # 计算区块特征
        y_min, y_max = y_indices.min(), y_indices.max()
        x_min, x_max = x_indices.min(), x_indices.max()
        block_height = y_max - y_min
        avg_gray = np.mean(gray_img[mask])
        
        # 动态密度计算（非线性映射）
        base_density = 1 - avg_gray  # 颜色越深密度越大
        scaled_density = (base_density ** 2) * density_scale
        
        # 计算线条间距
        if scaled_density * block_height == 0:
            spacing = 65535  # 线条最小密度为0
        else:
            spacing = max(1, int(round(block_height / (scaled_density*block_height))))
        if spacing > (x_max - x_min) // 3:
            spacing = 65535  # 线条最小密度为0
        
        # 生成垂直线条（示例为纵向线条）
        for x in range(x_min, x_max+1):
            if x % spacing == 0:
                line_points = []
                current_y = y_min
                while current_y <= y_max:
                    if mask[current_y, x]:
                        line_points.append((x, current_y))
                    current_y += 1
                if line_points:
                    draw.line(line_points, fill='black', width=line_thickness)
    
    result.save(output_path)


if __name__ == '__main__':
    files = get_files()
    if len(files) == 0:
        print('No input image found.')
    else:
        adaptive_line_conversion(input_path=files[0],
                                line_thickness=line_thickness,
                                density_scale=density_scale,
                                block_size=block_size)
