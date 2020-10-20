# Game Objects In Code

Below is a very simple example of a GameObject subclass:
```py
def parse_bool(s):
	return s.lower() in ('y', 'yes', 'true')

class User(GameObject):
	attributes = {
		'name': (True, lambda x: x),
		'is_connected': (True, parse_bool),
		'xp': (False, int),
		'birthday': (False, lambda x: strptime(x, '%y-%m-%d')),
		'usernames': (False, lambda x: x)
	}
    def __init__(self):
		super().__init__()
```

This is the minimum required to create a GameObject class. Specifically, a GameObject requires:
1. `attributes` - This is required by any GameObject subclass, it defines the attributes to be added to your class. You do not define them in `__init__()` like you regularly would.
2. The `__init__()` method must not take any arguments besides `self`
3. `super().__init__()` must be called in `__init__()`. Once this is called, your attributes will be loaded into your class.

Notice that we can use a variety of different types in our class, as long as we can parse them from the input. See the following for how to instantiate this object. 

```py
template = {
	'name': 'John',
	'is_connected': 'yes',
	'xp': '125',
	'birthday': '1992-02-29',
	'usernames': [
		'john1415265',
		'john04',
		'john.lastname'
	]
}
user = GameObject.load_from_template(template, User)
```

Notice that we never call `User()` directly. `GameObject.load_from_template()` sets up the User instance, calling `User()` will create a GameObject instance with all attributes set to `None` (except `id`, which will have a unique id among GameObjects).


## Default Attributes

If you want to set default values for your attributes, you can do so in `__init__()`. Below is an example.

```py
class User(GameObject):
	attributes = {
		'name': (True, lambda x: x),
		'default_val': (False, int)
	}
    def __init__(self):
		super().__init__()
		# Set defaults AFTER super() init
		self.default_val = 10
```

Keep in mind all default values need to have `False` for the required field in `attributes`. If the field is set to `True` then when your template is loaded it will raise an error, even if a default is set.

