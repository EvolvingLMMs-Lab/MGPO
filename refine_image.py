from PIL import Image
import os

# 图片文件夹路径
folder = 'images'

for filename in os.listdir(folder):
    if filename.lower().endswith('.png'):
        filepath = os.path.join(folder, filename)
        img = Image.open(filepath)
        # 只处理有透明通道的图片
        if img.mode in ('RGBA', 'LA'):
            # 创建白色背景
            background = Image.new('RGB', img.size, (255, 255, 255))
            # 粘贴原图，使用alpha通道作为mask
            background.paste(img, mask=img.split()[-1])
            # 覆盖保存为PNG（无透明通道）
            background.save(filepath)
            print(f'处理完成: {filename}')
        else:
            # 如果没有透明通道，也可以选择重新保存为无alpha的PNG
            img.convert('RGB').save(filepath)
            print(f'无透明通道，已覆盖保存: {filename}')

print('全部处理完成！')
