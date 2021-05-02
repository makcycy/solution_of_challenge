# import os
# import sys
# sys.path.append('FullSubNet/recipes/dns_interspeech_2020')
#
# os.system('python FullSubNet/recipes/dns_interspeech_2020/inferencer.py '
#           '-C FullSubNet/recipes/dns_interspeech_2020/fullsubnet/inference.toml '
#           '-M FullSubNet/recipes/dns_interspeech_2020/fullsubnet_best_model_58epochs.tar '
#           '-O dataset/clean')


from transformers import AutoModel, AutoTokenizer

model_name = 'haoxiangsnr/FullSubNet-DNS-INTERSPEECH-2020'

model = AutoModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

inputs = tokenizer('Hello', return_tensors='pt')
outputs = model(**inputs)