import os

os.system('CUDA_VISIBLE_DEVICES=3 python3 src/main.py --config=noisemix_smac --env-config=sc2 with env_args.map_name=micro_corridor t_max=8050000')