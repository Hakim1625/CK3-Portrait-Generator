import json

genes = {

'gender': ['male', 'female', 'boy', 'girl'],
'age': ['age'],

'gene_chin_forward': ['chin_forward_neg', 'chin_forward_pos'],
'gene_chin_height': ['chin_height_neg', 'chin_height_pos'],
'gene_chin_width': ['chin_width_neg', 'chin_width_pos'],

'gene_eye_angle': ['eye_angle_neg', 'eye_angle_pos'],
'gene_eye_depth': ['eye_depth_neg', 'eye_depth_pos'],
'gene_eye_height': ['eye_height_neg', 'eye_height_pos'],
'gene_eye_distance': ['eye_distance_neg', 'eye_distance_pos'],
'gene_eye_shut': ['eye_shut_neg', 'eye_shut_pos'],

'gene_forehead_angle': ['forehead_angle_neg', 'forehead_angle_pos'],
'gene_forehead_brow_height':['forehead_brow_height_neg', 'forehead_brow_height_pos'],
'gene_forehead_roundness': ['forehead_roundness_neg', 'forehead_roundness_pos'],
'gene_forehead_width': ['forehead_width_neg', 'forehead_width_pos'],
'gene_forehead_height': ['forehead_height_neg', 'forehead_height_pos'],
'gene_head_height': ['head_height_neg', 'head_height_pos'],
'gene_head_width': ['head_width_neg', 'head_width_pos'],
'gene_head_profile': ['head_profile_neg', 'head_profile_pos'],
'gene_head_top_height': ['head_top_height_neg', 'head_top_height_pos'],
'gene_head_top_width': ['head_top_width_neg', 'head_top_width_pos'],

'gene_jaw_angle': ['jaw_angle_neg', 'jaw_angle_pos'],
'gene_jaw_forward': ['jaw_forward_neg', 'jaw_forward_pos'],
'gene_jaw_height': ['jaw_height_neg', 'jaw_height_pos'],
'gene_jaw_width': ['jaw_width_neg', 'jaw_width_pos'],

'gene_mouth_corner_depth': ['mouth_corner_depth_neg', 'mouth_corner_depth_pos'],
'gene_mouth_corner_height': ['mouth_corner_height_neg', 'mouth_corner_height_pos'],
'gene_mouth_forward': ['mouth_forward_neg', 'mouth_forward_pos'],
'gene_mouth_height': ['mouth_height_neg', 'mouth_height_pos'],
'gene_mouth_width': ['mouth_width_neg', 'mouth_width_pos'],
'gene_mouth_upper_lip_size': ['mouth_upper_lip_size_neg', 'mouth_upper_lip_size_pos'],
'gene_mouth_lower_lip_size': ['mouth_lower_lip_size_neg', 'mouth_lower_lip_size_pos'],
'gene_mouth_open': ['mouth_open_neg', 'mouth_open_pos'],

'gene_neck_length': ['neck_length_neg', 'neck_length_pos'],
'gene_neck_width': ['neck_width_neg', 'neck_width_pos'],

'gene_bs_cheek_forward': ['cheek_forward_neg', 'cheek_forward_pos'],
'gene_bs_cheek_height': ['cheek_height_neg', 'cheek_height_pos'],
'gene_bs_cheek_width': ['cheek_width_neg', 'cheek_width_pos'],

'gene_bs_ear_angle': ['ear_angle_neg', 'ear_angle_pos'],
'gene_bs_ear_bend': ["ear_lower_bend_pos", "ear_upper_bend_pos", "ear_both_bend_pos"],
'gene_bs_ear_inner_shape': ['ear_inner_shape_pos'],
'gene_bs_ear_outward': ['ear_outward_neg', 'ear_outward_pos'],
'gene_bs_ear_size': ['ear_size_neg', 'ear_size_pos'],

'gene_bs_eye_corner_depth': ['eye_corner_depth_neg', 'eye_corner_depth_pos'],
'gene_bs_eye_fold_shape': ['eye_fold_shape_neg', 'eye_fold_shape_pos'],
'gene_bs_eye_size': ['eye_size_neg', 'eye_size_pos'],
'gene_bs_eye_upper_lid_size': ['eye_upper_lid_size_neg', 'eye_upper_lid_size_pos'],

'gene_bs_forehead_brow_curve': ['forehead_brow_curve_neg', 'forehead_brow_curve_pos'],
'gene_bs_forehead_brow_forward': ['forehead_brow_forward_neg', 'forehead_brow_forward_pos'],
'gene_bs_forehead_brow_inner_height': ['forehead_brow_inner_height_neg', 'forehead_brow_inner_height_pos'],
'gene_bs_forehead_brow_outer_height': ['forehead_brow_outer_height_neg', 'forehead_brow_outer_height_pos'],
'gene_bs_forehead_brow_width': ['forehead_brow_width_neg', 'forehead_brow_width_pos'],

'gene_bs_jaw_def': ['jaw_def_neg', 'jaw_def_pos'],

'gene_bs_mouth_lower_lip_def': ['mouth_lower_lip_def_pos'],
'gene_bs_mouth_lower_lip_full': ['mouth_lower_lip_full_neg', 'mouth_lower_lip_full_pos'],
'gene_bs_mouth_lower_lip_pad': ['mouth_lower_lip_pad_neg', 'mouth_lower_lip_pad_pos'],
'gene_bs_mouth_lower_lip_width': ['mouth_lower_lip_width_neg', 'mouth_lower_lip_width_pos'],
'gene_bs_mouth_philtrum_def': ['mouth_philtrum_def_pos'],
'gene_bs_mouth_philtrum_shape': ['mouth_philtrum_shape_neg', 'mouth_philtrum_shape_pos'],
'gene_bs_mouth_philtrum_width': ['mouth_philtrum_width_neg', 'mouth_philtrum_width_pos'],
'gene_bs_mouth_upper_lip_def': ['mouth_upper_lip_def_pos'],
'gene_bs_mouth_upper_lip_full': ['mouth_upper_lip_full_neg', 'mouth_upper_lip_full_pos'],
'gene_bs_mouth_upper_lip_profile': ['mouth_upper_lip_profile_neg', 'mouth_upper_lip_profile_pos'],
'gene_bs_mouth_upper_lip_width': ['mouth_upper_lip_width_neg', 'mouth_upper_lip_width_pos'], 

'gene_bs_nose_forward': ['nose_forward_neg', 'nose_forward_pos'],
'gene_bs_nose_height': ['nose_height_neg', 'nose_height_pos'],
'gene_bs_nose_length': ['nose_length_neg', 'nose_length_pos'],
'gene_bs_nose_nostril_height': ['nose_nostril_height_neg', 'nose_nostril_height_pos'],
'gene_bs_nose_nostril_width': ['nose_nostril_width_neg', 'nose_nostril_width_pos'],
'gene_bs_nose_profile': ["nose_profile_neg", "nose_profile_pos", "nose_profile_hawk", "nose_profile_hawk_pos"],
'gene_bs_nose_ridge_angle': ['nose_ridge_angle_neg', 'nose_ridge_angle_pos'],
'gene_bs_nose_ridge_width': ['nose_ridge_width_neg', 'nose_ridge_width_pos'],
'gene_bs_nose_size': ['nose_size_neg', 'nose_size_pos'],
'gene_bs_nose_tip_angle': ['nose_tip_angle_neg', 'nose_tip_angle_pos'],
'gene_bs_nose_tip_forward': ['nose_tip_forward_neg', 'nose_tip_forward_pos'],
'gene_bs_nose_tip_width': ['nose_tip_width_neg', 'nose_tip_width_pos'],

'face_detail_cheek_def': ["cheek_def_01", "cheek_def_02"],
'face_detail_cheek_fat': ["cheek_fat_01_pos", "cheek_fat_02_pos", "cheek_fat_03_pos", "cheek_fat_04_pos",  "cheek_fat_01_neg"],
'face_detail_chin_cleft': ["chin_cleft",  "chin_dimple"],
'face_detail_chin_def': ['chin_def_neg', 'chin_def'],
'face_detail_eye_lower_lid_def': ['eye_lower_lid_def'],
'face_detail_eye_socket': ["eye_socket_01", "eye_socket_02", "eye_socket_03", 'eye_socket_color_01', 'eye_socket_color_02', 'eye_socket_color_03'],
'face_detail_nasolabial': ["nasolabial_01", "nasolabial_02", "nasolabial_03", "nasolabial_04"],
'face_detail_nose_ridge_def': ["nose_ridge_def_pos", "nose_ridge_def_neg"],
'face_detail_nose_tip_def': ['nose_tip_def'],
'face_detail_temple_def': ['temple_def'],

'expression_brow_wrinkles': ["brow_wrinkles_01", "brow_wrinkles_02", "brow_wrinkles_03", "brow_wrinkles_04"],
'expression_eye_wrinkles': ["eye_wrinkles_01", "eye_wrinkles_02", "eye_wrinkles_03"],
'expression_forehead_wrinkles': ["forehead_wrinkles_01", "forehead_wrinkles_02", "forehead_wrinkles_03"],
'expression_other': ["cheek_wrinkles_left_01", "cheek_wrinkles_right_01", "cheek_wrinkles_both_01", "nose_wrinkles_01"],

'complexion': ["complexion_1", "complexion_2", "complexion_3", "complexion_4", "complexion_5", "complexion_6", "complexion_7", "complexion_beauty_1", "complexion_ugly_1"],

'gene_bs_body_type': ["body_average", "body_fat_head_fat_low", "body_fat_head_fat_medium", "body_fat_head_fat_full"],

'gene_age': ['old_1', 'old_2', 'old_3', 'old_4', 'old_beauty_1'],

'gene_eyebrows_fullness': ["no_eyebrows", "layer_2_avg_thickness", "layer_2_high_thickness", "layer_2_low_thickness", "layer_2_lower_thickness"],
'gene_eyebrows_shape': ["no_eyebrows",  "avg_spacing_avg_thickness", "avg_spacing_high_thickness", "avg_spacing_low_thickness", "avg_spacing_lower_thickness", "far_spacing_avg_thickness", "far_spacing_high_thickness", "far_spacing_low_thickness", "far_spacing_lower_thickness", "close_spacing_avg_thickness", "close_spacing_high_thickness", "close_spacing_low_thickness", "close_spacing_lower_thickness"],

'eyelashes_accessory': ["no_eyelashes", "normal_eyelashes", "asian_eyelashes"]
}

def get_lengths(genes=genes):
    return [len(sub_genes) for sub_genes in list(genes.values())]


if __name__ == '__main__':
    json = json.dumps(genes)

    f = open("./utils/dependencies/gene_dicts.json","w")
    f.write(json)
    f.close()