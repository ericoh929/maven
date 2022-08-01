import os

for i in range(1):
    os.system('CUDA_VISIBLE_DEVICES=2 python3 src/main.py --config=noisemix_smac --env-config=sc2 with env_args.map_name=MMM2 t_max=8050000 local_results_path=./results/mmm2')