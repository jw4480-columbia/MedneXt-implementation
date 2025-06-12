import os
import cv2
import numpy as np

def binarize_png_folder(input_folder,output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    png_files= [f for f in os.listdir(input_folder) if f.endswith('.png') ]
    print(f'found {len(png_files)} png files.')

    for png_file in png_files:
        path=os.path.join(input_folder, png_file)
        print(f'Processing {png_file}')

        img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)

        img_T=np.transpose(img)

        out_path=os.path.join(output_folder,png_file)
        cv2.imwrite(out_path,img_T)

        print(f'Saved {out_path}')

if __name__=='__main__':
    input_folder= 'Task502_Wire_results/folds_all_gray'
    output_folder='Task502_Wire_results/folds_all_gray_transpose'

    binarize_png_folder(input_folder,output_folder)