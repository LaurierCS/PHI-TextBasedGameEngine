# YamlUtil


a static utility class, all utility functions with no better place to live should go in here 

## Methods


### load_yaml_data


Load yaml data from a file and applies custom rules (like include) 

#### Parameters
name | description | default
--- | --- | ---
filename | the name of the yaml file to load | 





### get_yaml_object


Wrapper method for yaml.safe_load(), loads an object from a yaml file 

#### Parameters
name | description | default
--- | --- | ---
filename | the name of the file to load from | 





### get_yaml_filename


Helper function to get either a .yml or .yaml file given the name 

#### Parameters
name | description | default
--- | --- | ---
directory | the directory to look in | 
name_prefix | the expected file name without extension | 




#### Throws



### parse_minmax_object


Parses a value from a yaml object, returns a dictionary with two entries: min and max   


#### Parameters
name | description | default
--- | --- | ---
obj | the dict to search in | 
key | the key to look for | 
transform | method to apply to the result (e.g. int to convert to integers) | lambda x
default | default value to use if the key is not found | None




#### Throws


