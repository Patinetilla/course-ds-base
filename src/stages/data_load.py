import yaml 
import argparse

def data_load(config_path: Text) -> None: 
    config=yaml.safe_load(open(config_path))
    raw_data_path = config['data_load']['raw_data_path']
    data.to_csv(config['dataset_processed_path'])

if __name__ == '__main__':
    args_parser = argparser.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)