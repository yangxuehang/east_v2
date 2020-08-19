#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 8/19/2020 3:41 PM
# @Author: Yang Xuehang
# @File  : config.py

# dataset params.
min_area_not_validate = 20

# label params.
shrink_ratio = 0.3
min_text_size = 8


# model params.
checkpoint_path = './ckpts/'
pretrained_model_path = './pretrained_model/resnet_v1_50.ckpt' # None
restore = False # whether to restore from checkpoint
save_checkpoint_steps = 1000
save_summary_steps = 100

# training params.
num_readers = 16
batch_size_per_gpu = 14
learning_rate = 0.0001
max_steps = 100000
moving_average_decay = 0.997
gpu_list = '0,1'
input_size = 512

train_data_path = ['./demo_data.txt', ]

# testing params.
text_rescale = 512


