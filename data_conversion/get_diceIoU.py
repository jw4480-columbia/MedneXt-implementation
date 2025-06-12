import os
import cv2
import numpy as np
from tqdm import tqdm

def load_mask(path):
    mask = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return (mask == 255).astype(np.uint8)  # 将255转成1

def dice_score(pred, gt):
    intersection = np.sum(pred * gt)
    return (2. * intersection) / (np.sum(pred) + np.sum(gt) + 1e-8)

def iou_score(pred, gt):
    intersection = np.sum(pred * gt)
    union = np.sum(pred) + np.sum(gt) - intersection
    return intersection / (union + 1e-8)

def evaluate_masks(gt_dir, pred_dir):
    dice_list = []
    iou_list = []

    filenames = sorted(os.listdir(gt_dir))
    for filename in tqdm(filenames, desc="Evaluating"):
        gt_path = os.path.join(gt_dir, filename)
        pred_path = os.path.join(pred_dir, filename)
        
        if not os.path.exists(pred_path):
            print(f"⚠️ Prediction missing for: {filename}")
            continue

        gt = load_mask(gt_path)
        pred = load_mask(pred_path)

        dice = dice_score(pred, gt)
        iou = iou_score(pred, gt)

        dice_list.append(dice)
        iou_list.append(iou)

    dice_array = np.array(dice_list)
    iou_array = np.array(iou_list)

    print(f"\n✅ Evaluation Results:")
    print(f"Mean Dice: {dice_array.mean():.4f} ± {dice_array.std():.4f}")
    print(f"Mean IoU : {iou_array.mean():.4f} ± {iou_array.std():.4f}")

if __name__ == "__main__":
    ground_truth_dir = "Task502_Wire_results\ground_truth_gray"
    prediction_dir = "Task502_Wire_results/folds_all_gray_transpose"
    evaluate_masks(ground_truth_dir, prediction_dir)
