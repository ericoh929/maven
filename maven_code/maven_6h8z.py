import os

for i in range(2):
    os.system('CUDA_VISIBLE_DEVICES=1 python3 src/main.py --config=noisemix_smac --env-config=sc2 with env_args.map_name=micro_focus t_max=8050000')