# CSC478-EagerMOT-on-KITTI

This repository has already the directories structured for run EagerMOT using KITTIMOT data using RRC,TrackRCNN and PointGNN. Go inside each directory and store the data linked in `instructions.txt` files rspectively.

Once the all the data has been stored in the respective directories, you need to first run `python adopt_kitti_motsfusion_input` to adapt the kitti data to motsfusion's structure. Then you can run the tracking algorithm by running: `python run_tracking.py` in the EagerMOT directory. The configuration files are already set up to run on the downloaded data. 

Note: You may run into an error   `frame_int = int(file_name.split('.')[0]) ValueError: invalid literal for int() with base 10: ''` due to temporary hidden files. Simply rerun `run_tracking.py` and it should run without any issues the second time. 

The 3D tracking outputs from my execution of the algorithm on is also available in `tracking_det_0_0_seg_0.0_0.9_bbox_0.01_0.01_kf_dist_2d_full_[-3.5_-0.3]_0.3_a3_3_h1_2_2d_age_3_3_cleaning_0_3d`

# Supplementary Documents
My project proposal, report and presentation can be found in the `additional_documents` directory

# References: 
The original EagerMOT implementation:

```
@inproceedings{Kim21ICRA,
  title     = {EagerMOT: 3D Multi-Object Tracking via Sensor Fusion},
  author    = {Kim, Aleksandr, O\v{s}ep, Aljo\v{s}a and Leal-Taix{'e}, Laura},
  booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},
  year      = {2021}
}
```
