import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('main_file', type=str,
            help='The main YAML file to load')
    # TODO: Add more args with different options

    args = parser.parse_args()

    # TODO: Create a Game object from yaml file and run it
