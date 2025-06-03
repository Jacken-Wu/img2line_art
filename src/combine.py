import cv2
import numpy as np
import sys


is_dot = 'N'
if len(sys.argv) > 1:
    is_dot = sys.argv[1]

img2_path = "output_line_block.png"
if is_dot == 'Y':
    img2_path = "output_dot_block.png"


def overlay_images(img1_path, img2_path, output_path):
    # 读取为灰度图
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    
    if img1.shape != img2.shape:
        raise ValueError("图片尺寸不一致")
    
    # 创建空白画布（白色背景）
    combined = np.full_like(img1, 255)
    
    # 通过矢量化运算生成掩模
    mask = (img1 < 255) | (img2 < 255)  # 检测非白色像素（即黑色图案）
    combined[mask] = 0  # 将图案区域设为黑色
    
    cv2.imwrite(output_path, combined)


# 使用示例
if __name__ == '__main__':
    overlay_images("output_edge.png", img2_path, "combined.png")
