from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Type, Callable, Dict, Tuple

class GameObject(ABC):
	"""
	Base class to be used for all in-game instantiable objects
	@author Jacob Heard
	"""
	_id = 1

	attributes : Dict[str, Tuple[bool, Callable[[Any], Any]]]
	"""
	Collection of templates which must be define by all child classed of GameObject
	The Dict must be in the format { 'property': (required, parser) }

	@param property (str) a property of the object
	@param required (bool) whether the property is required
	@param parser (func) a function which take the expected input value and parses it. For example, an integer value may be input as '13', so the int() function would used to parse it.
	"""
	
	
	def __init__(self):
		assert type(self) is not GameObject, 'GameObject class is not instantiable'

		self.id = GameObject._id
		GameObject._id += 1

		for attr in self.__class__.attributes:
			if hasattr(self, attr):
				raise AttributeError(f'Invalid or duplicate attribute {attr} in class {self.__class__.__name__}')
			setattr(self, attr, None)

	@staticmethod
	def load_from_template(template: Dict[str, Any], _class: Type['GameObject']):
		"""
		Instantiate a GameObject of type `_class` from a template.
		@param template template of (attribute, value) pairs to populate the object
		@param _class Class of the object to populate. Must be subclass of GameObject
		"""
		# Validate the input template
		for key in _class.attributes:
			if key not in template:
				required = _class.attributes[key][0]
				if required:
					raise AttributeError(f'missing required attribute "{key}\"')
		for key in template:
			if key not in _class.attributes:
				raise AttributeError(f'Unexpected attribute "{key}"')

		instance = _class()
		for key in template:
			f = _class.attributes[key][1]
			setattr(instance, key, f(template[key]))

		return instance
