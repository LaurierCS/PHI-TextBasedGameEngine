from gameobjects.GameObject import GameObject
from typing import Optional, Callable, List, Dict, Any

class GameContext():
	def __init__(self):
		self.objects: Dict[int, GameObject] = {}

	def add(self, obj: GameObject) -> None:
		"""
		Add a gameObject to the current context
		@param obj The object to add
		"""
		assert isinstance(obj, GameObject), "Only GameObjects can be added to context"
		self.objects[obj.id] = obj

	def destroy(self, obj: GameObject) -> bool:
		"""
		Destroys a GameObject existing in the current context
		@param obj The GameObject to destroy
		@return True if obj existed and it destroyed, False if it did not exist
		"""
		if obj.id in self.objects:
			del self.objects[obj.id]
			return True
		return False

	def get_by_name(self, name: str) -> List[GameObject]:
		"""
		Gets a list of GameObjects with matching name property
		
		@param name Name of the GameObject to match
		@return A list of 0 or more matching GameObjects
		"""

		return self.get_by_prop('name', name)

	def get_by_prop(self, prop: str, value: Any) -> List[GameObject]:
		"""
		Gets a list of GameObjects with a given property
		e.g. get_by_prop('type', 'weapon')

		@param prop Name of the property to search
		@param value Value of the property to match
		@return A list of 0 or more matching GameObjects
		"""
		objects = []
		for obj in self.objects.values():
			if hasattr(obj, prop) and value == getattr(obj, prop):
				objects.append(obj)
		return objects

	def get_by_predicate(self, predicate: Callable[[GameObject], bool]) -> List[GameObject]:
		"""
		Gets a list of GameObjects matching some predicate
		e.g. get_by_predicate(lambda x: hasattr(x, 'attack') and x.attack > 5)

		@param predicate Function that takes a GameObject and
			   returns True/False based on some condition
		@return A list of 0 or more matching GameObjects
		"""
		return [obj for obj in self.objects.values() if predicate(obj)]

	# IDs are unique to instances, this will only ever return 1
	def get_by_id(self, id: int) -> Optional[GameObject]:
		"""
		Gets a gameobject by id

		@param id ID of the GameObject to find
		@return The GameObject or None if not found
		"""
		if id in self.objects:
			return self.objects[id]
		return None

