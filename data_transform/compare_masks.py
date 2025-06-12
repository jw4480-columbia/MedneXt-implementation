import os
import cv2
import numpy as np

index_background=[255,255,255]
index_overlap=[0,0,0]
index_blue=[255,0,0]
index_red=[0,0,255]


def compare_ground_truth_prediction(ground_truth_folder,prediction_folder,output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    png_files= [f for f in os.listdir(ground_truth_folder) if f.endswith('.png') ]
    print(f'found {len(png_files)} png files.')

    for png_file in png_files:
        
        ground_truth_path=os.path.join(ground_truth_folder, png_file)
        prediction_path=os.path.join(prediction_folder, png_file)
        print(f'Processing {png_file}')

        img_ground_truth=cv2.imread(ground_truth_path,cv2.IMREAD_GRAYSCALE)
        img_prediction=cv2.imread(prediction_path,cv2.IMREAD_GRAYSCALE)


        if img_ground_truth.shape != img_prediction.shape:
            raise ValueError("两张图像尺寸不一致，无法逐像素比较。")

        height, width = img_prediction.shape[:]
        print(img_ground_truth.shape)
        print(img_prediction.shape)
        img_comparison=np.zeros((height, width, 3), dtype=np.uint8)

        for x in range(height):
            for y in range(width):
                #print(f'index now is : {[x,y]}')
                if img_ground_truth[x,y]==0:
                    if img_prediction[x,y]==img_ground_truth[x,y]:
                        img_comparison[x,y]=index_background#both background
                    else :img_comparison[x,y]=index_blue#false positive
                elif img_ground_truth[x,y]==255:
                    if img_prediction[x,y]==img_ground_truth[x,y]:
                        img_comparison[x,y]=index_overlap#both_wire
                    else :
                        img_comparison[x,y]=index_red#false_negative
                        #print('false negative!')

                



        

        #img[img==1]=255

        out_path=os.path.join(output_folder,png_file)
        cv2.imwrite(out_path,img_comparison)

        print(f'Saved {out_path}')

if __name__=='__main__':
    ground_truth_folder= 'Task502_Wire_results\ground_truth_gray'
    prediction_folder='Task502_Wire_results/folds_all_gray_transpose'
    output_folder='Task502_Wire_results/folds_all_comparison'

    compare_ground_truth_prediction(ground_truth_folder,prediction_folder,output_folder)
