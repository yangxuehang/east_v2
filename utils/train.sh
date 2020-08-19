python multigpu_train.py \
--gpu_list=0,1 \
--input_size=512 \
--batch_size_per_gpu=8 \
--checkpoint_path=/home/jd/xsl_workspace/EAST/output/verti_text/ \
--text_scale=512 \
--max_steps=180000 \
--training_data_path=/home/jd/xsl_workspace/EAST/vertical_data/book_jiajia/vbook_train_data \
--geometry=RBOX \
--learning_rate=0.0001 \
--num_readers=24 \
--restore=False \
--pretrained_model_path=/home/jd/xsl_workspace/EAST/EAST/pretrained_model/resnet_v1_50.ckpt
