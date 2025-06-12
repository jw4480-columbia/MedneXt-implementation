import os
import json
import numpy as np
from PIL import Image
import labelme

input_folder = 'data\images'  # <<< 修改成你的文件夹路径
output_folder = os.path.join(input_folder, 'masks')
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if not filename.endswith('.json'):
        continue

    json_path = os.path.join(input_folder, filename)

    # 加载 JSON 内容
    with open(json_path, 'r') as f:
        data = json.load(f)

    # 如果 imageData 缺失，则从文件加载
    if data.get('imageData') is None:
        image_path = os.path.join(input_folder, data['imagePath'])
        with open(image_path, 'rb') as f:
            image_bytes = f.read()
        imageData = labelme.utils.img_data_to_base64(image_bytes).decode('utf-8')
        data['imageData'] = imageData

    image = labelme.utils.img_b64_to_arr(data['imageData'])

    # 生成 label_name_to_value 字典（包括背景）
    label_name_to_value = {'_background_': 0}
    for shape in data['shapes']:
        label_name = shape['label']
        if label_name not in label_name_to_value:
            label_name_to_value[label_name] = len(label_name_to_value)

    # 生成 mask
    label_mask, _ = labelme.utils.shapes_to_label(
    img_shape=image.shape,
    shapes=data['shapes'],
    label_name_to_value=label_name_to_value
    )

    # 保存 mask 图像（灰度图）
    mask = Image.fromarray(label_mask.astype(np.uint8), mode='L')
    output_path = os.path.join(output_folder, filename.replace('.json', '.png'))
    mask.save(output_path)

    print(f"Saved: {output_path}")

print("全部 JSON 文件处理完成！")
