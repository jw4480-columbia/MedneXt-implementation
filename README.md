# MedneXt-implementation
Private usage and customized data processing scripts based on MedneXt, and extension of nnUNet

Reference listed below:

> Roy, S., Koehler, G., Ulrich, C., Baumgartner, M., Petersen, J., Isensee, F., Jaeger, P.F. & Maier-Hein, K. (2023).
MedNeXt: Transformer-driven Scaling of ConvNets for Medical Image Segmentation. 
International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI), 2023.

> Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2020). 
nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature Methods, 1-9.

## General Usage
To install the github repo and implement MedneXt as a regular nnUNet training pipeline, follow instruction and search for tutorial respectively:

> https://github.com/MIC-DKFZ/MedNeXt

Notice that MedneXt is design to work on 3D database only, therefore the original nnUNet repo is also strongly recommanded to be installed, as some precedure might require nnUNet command instead of MedneXt command, the 2 repositories should be installed parallel to each other and in the same environment, if any.

## Practical procedure of preparing a 2D database for training
If, like in this project, MedneXt need to be trained under a raw 2D database in, suppose png format, then 2 basic data prepocessing is required:

### Pack data in a given format
We invoke the prepocessing python script for task120:
>https://github.com/MIC-DKFZ/MedNeXt/blob/main/nnunet_mednext/dataset_conversion/Task120_Massachusetts_RoadSegm.py
which is design for 2d prepocessing and easy to rewrite.

First, save a new copy and rename after task name, which should be in format `TaskXXX_Taskname.py` and put it in folder `/nnunet_mednext/dataset_conversion``, then rewrite python codes below:

```
base = 'path/to/your/dataset/'
task_name = 'TaskXXX_Taskname'
```

Make sure that '''task_name''' aligns with your task name and the naming of this script. This script will transform your png files into nifti format, and is necessary since the nnUNet pipeline can only work with nifti format, notice that by the end of the day your dataset is still 2D images, but z axis is set to 1 rather that None, so that the matrix representing the image data is `(Z,X,Y)` rather than `(X,Y)` with Z set to 1.

Then prepare the raw database, it is assumed that the dataset should have four components, images and labels in the training set, and that in the testing set, the naming format, which is to be identical with the naming in the python script, should like this:

```
Your_dataset_name/
├── training/
│   ├── input/
│   │   ├── image_001.png
│   │   ├── ...
│   │   └── image_XXX.png
│   └── ouput/
│   │   ├── label_001.png
│   │   ├── ...
│   │   └── label_XXX.png
└── training/
    ├── input/
    │   ├── image_XXX+1.png
    │   ├── ...
    │   └── image_XXX.png
    └── ouput/
        ├── label_XXX+1.png
        ├── ...
        └── label_XXX.png
```
        

Of course it can be named otherwise, but the namespace in the script should also be the same.

Finally double check if the mask files in yout database is binary or grayscale, if in grayscale, then the script should be ready to run, if your mask file is already in binary scale, then comment out the following codes:


```
# the labels are stored as 0: background, 255: road. We need to convert the 255 to 1 because nnU-Net expects
        # the labels to be consecutive integers. This can be achieved with setting a transform
        convert_2d_image_to_nifti(input_segmentation_file, output_seg_file, is_seg=True,
                                  transform=lambda x: (x == 255).astype(int))
        convert_2d_image_to_nifti(input_segmentation_file, output_seg_file, is_seg=True,
                                  transform=lambda x: (x == 255).astype(int))
```





