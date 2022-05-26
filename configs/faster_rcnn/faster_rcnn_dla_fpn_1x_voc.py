_base_ = [
    '../_base_/models/faster_rcnn_dla_fpn.py',
    '../_base_/datasets/voc07.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

resume_from = './tutorial_exps/latest.pth'  # Resume checkpoints from a given path, the training will be resumed from the epoch when the checkpoint's is saved.
dataset_type = 'VOCDataset'
work_dir = './tutorial_exps'
device = 'cuda'
evaluation = dict(  # The config to build the evaluation hook, refer to https://github.com/open-mmlab/mmdetection/blob/master/mmdet/core/evaluation/eval_hooks.py#L7 for more details.
    interval=1)

optimizer = dict(type='SGD', lr=0.0005, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
# actual epoch = 3 * 3 = 9
lr_config = dict(policy='step', step=[3])
# runtime settings
runner = dict(
    type='EpochBasedRunner', max_epochs=4)  # actual epoch = 4 * 3 = 12
