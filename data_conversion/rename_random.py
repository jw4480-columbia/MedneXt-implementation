import os
import random

# 设置目标文件夹路径
folder_path = 'data'  # 替换成你的文件夹路径

# 获取所有 png 文件
files = [f for f in os.listdir(folder_path) if f.lower().endswith('.png')]

# 打乱顺序
random.shuffle(files)

# 为避免重名覆盖，先改成临时名字
for i, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    tmp_path = os.path.join(folder_path, f'tmp_{i}.png')
    os.rename(old_path, tmp_path)
    print(f"✅ {filename} → {f'tmp_{i}.png'}")

# 再按顺序重命名为 1.png、2.png、...
tmp_files = [f for f in os.listdir(folder_path) if f.startswith('tmp_') and f.endswith('.png')]
tmp_files.sort()  # tmp_0.png, tmp_1.png,... 按顺序排列
for i, filename in enumerate(tmp_files, start=117):
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, f'case_{i:05d}.png')
    os.rename(old_path, new_path)
    print(f"✅ {filename} → {f'case_{i:05d}.png'}")

print("重命名完成！")
