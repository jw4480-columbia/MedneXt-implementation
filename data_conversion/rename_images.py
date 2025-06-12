import os

# 修改为你图片所在的目录
folder = "data"  # 比如：images 或 ./data/training/input

# 可选：自定义前缀
prefix = "case_"

# 获取所有 PNG 文件
png_files = sorted([f for f in os.listdir(folder) if f.endswith(".png")])

# 重命名
for idx, filename in enumerate(png_files, start=107):
    new_name = f"{prefix}{idx:05d}.png"  # 生成 image_001.png 这类名字
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, new_name)
    os.rename(src, dst)
    print(f"✅ {filename} → {new_name}")

print("批量重命名完成！")