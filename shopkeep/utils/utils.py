import yaml

# Create a function for writing values off to a yaml file
def write(dictionary, path):
    with open(path, 'w') as outfile:
        yaml.dump(dictionary, outfile, sort_keys=False)
