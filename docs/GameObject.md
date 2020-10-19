# Game Objects In Code

TODO: Explain how to define GameObject subclasses

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

This is the minimum required to create a GameObject class.  
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