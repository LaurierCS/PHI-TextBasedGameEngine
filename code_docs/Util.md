# Util

## Functions

### load_yaml_data

Load yaml data from a file and applies custom rules (like include) 

#### Parameters
name | description | default
---|---|---
filename |  | 


### get_yaml_object

Wrapper method for yaml.safe_load(), loads an object from a yaml file 

#### Parameters
name | description | default
---|---|---
filename |  | 


### get_yaml_filename

Helper function to get either a .yml or .yaml file given the name 

#### Parameters
name | description | default
---|---|---
directory |  | 
name_prefix |  | 


### parse_minmax_object

Parses a value from a yaml object, returns a dictionary with two entries: min and max 

#### Parameters
name | description | default
---|---|---
obj |  | 
key |  | 
transform |  | <_ast.Lambda object at 0x7f341d4b49a0>
default |  | <_ast.Constant object at 0x7f341d4b4a60>


