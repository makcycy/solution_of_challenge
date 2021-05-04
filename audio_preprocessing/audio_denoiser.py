from .FullSubNet.inference import denoise
import toml
import argparse

def model_denoise(output_path = None, model_path = None, config_path = None):
    if output_path is None:
        output_path = '../dataset/output'
    if model_path is None:
        model_path = 'audio_preprocessing/FullSubNet/fullsubnet_best_model_58epochs.tar'
    if config_path is None:
        config_path = 'audio_preprocessing/FullSubNet/fullsubnet/inference.toml'
    parser = argparse.ArgumentParser("Inference")
    parser.add_argument("-C", "--configuration", type=str, required=True, help="Configuration file.")
    parser.add_argument("-M", "--model_checkpoint_path", type=str, required=True, help="The path of your model checkpoint.")
    parser.add_argument("-O", "--output_dir", type=str, required=True, help="The path to save the enhanced speech.")

    passing_list = ['-C', config_path,
                    '-M', model_path,
                    '-O', output_path]
    args = parser.parse_args(passing_list)

    configuration = toml.load(args.configuration)
    checkpoint_path = args.model_checkpoint_path
    output_dir = args.output_dir

    denoise(configuration, checkpoint_path, output_dir)

