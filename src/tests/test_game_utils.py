from gameobjects.GameObject import GameObject

class MockGameObject(GameObject):
	attributes = {
		'name': (True, lambda x: x),
		'prop': (False, lambda x: x)
	}
	def __init__(self):
		super().__init__()

def create_object(name=None, prop=None):
	obj = MockGameObject()
	obj.name = name
	obj.prop = prop
	return obj

def set_gameobject_id(id: int):
	GameObject._id = id
