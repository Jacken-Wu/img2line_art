from PIL import Image, ImageDraw
import numpy as np
from skimage.segmentation import slic
from skimage.color import rgb2gray
import sys
import os
from tqdm import tqdm


# 默认参数
point_size = 2  # 点的大小（直径）
density_scale = 0.1
block_size = 48
dots_density = 0.1
if len(sys.argv) > 1:
    point_size = int(sys.argv[1])
if len(sys.argv) > 2:
    density_scale = float(sys.argv[2])
if len(sys.argv) > 3:
    block_size = int(sys.argv[3])
if len(sys.argv) > 4:
    dots_density = float(sys.argv[4])

def get_files():
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    return files

def adaptive_dot_conversion(input_path,
                            point_size=2,
                            density_scale=0.2,
                            block_size=48,
                            dots_density=0.1):
    """
    分块自适应点阵化算法
    参数：
    block_size: 分块尺寸（建议32-128）
    density_scale: 密度缩放系数（0.1-1.0）
    """
    output_path = 'output_dot_block.png'

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
        mask = (segments == i)
        y_indices, x_indices = np.where(mask)
        
        if len(y_indices) == 0:
            continue
            
        # 计算区块特征
        y_min, y_max = y_indices.min(), y_indices.max()
        x_min, x_max = x_indices.min(), x_indices.max()
        area = len(y_indices)  # 区块有效像素数
        avg_gray = np.mean(gray_img[mask])
        
        # 动态密度计算（非线性映射）
        base_density = 1 - avg_gray  # 颜色越深密度越大
        scaled_density = (base_density ** 2) * density_scale
        
        # 计算点的数量
        n_points = int(area * scaled_density)
        # 点密度过低，不绘制
        if n_points / block_size < dots_density:
            continue
        
        # 在mask区域内随机选点
        coordinates = list(zip(x_indices, y_indices))
        selected_indices = np.random.choice(len(coordinates), n_points, replace=False)
        
        # 绘制点
        for idx in selected_indices:
            x, y = coordinates[idx]
            # 绘制圆形点
            draw.ellipse([
                (x - point_size/2, y - point_size/2),
                (x + point_size/2, y + point_size/2)
            ], fill='black')
    
    result.save(output_path)

if __name__ == '__main__':
    files = get_files()
    if len(files) == 0:
        print('No input image found.')
    else:
        adaptive_dot_conversion(input_path=files[0],
                               point_size=point_size,
                               density_scale=density_scale,
                               block_size=block_size,
                               dots_density=dots_density)
