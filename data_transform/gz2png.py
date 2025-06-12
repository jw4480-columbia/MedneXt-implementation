import cv2
import nibabel as nib
import os
import numpy  as np

def nii2png_batch(nii_folder,output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    nii_files= [f for f in os.listdir(nii_folder) if f.endswith('.nii.gz') ]
    print(f'found {len(nii_files)} nii.gz files.')

    for nii_file in nii_files:
        nii_path=os.path.join(nii_folder, nii_file)
        print(f'Processing {nii_file}')

        img=nib.load(nii_path)
        data = img.get_fdata()

        slice_2d=data[:,:,0]

        base_name=nii_file[:-7]

        out_path=os.path.join(output_folder,base_name+ '.png')
        cv2.imwrite(out_path,slice_2d)

        print(f'Saved {out_path}')

if __name__=='__main__':
    nii_folder= 'Task502_Wire_results/folds_all_gz'
    output_folder='Task502_Wire_results/folds_all_png'

    nii2png_batch(nii_folder,output_folder)




