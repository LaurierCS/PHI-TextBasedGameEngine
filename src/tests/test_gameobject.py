import pytest
from gameobjects.GameObject import GameObject

def set_gameobject_id(id: int):
	GameObject.id = id

class ValidGameObject(GameObject):
	attributes = {
		'name': (True, lambda x: x)
	}

	def __init__(self):
		super().__init__()


def test_load_from_template():
	template = {'name': 'test_name'}
	id = 5
	
	set_gameobject_id(id)
	obj = GameObject.load_from_template(template, ValidGameObject)
	
	assert obj.name == 'test_name'
	assert obj.id == id

def test_instantiate_gameobject_subclass():
	id = 5

	set_gameobject_id(id)
	obj = ValidGameObject()

	assert obj.name == None
	assert obj.id == id

def test_missing_required_attribute():
	template = {}
	id = 5

	with pytest.raises(AttributeError) as errinfo:
		obj = GameObject.load_from_template(template, ValidGameObject)

	assert str(errinfo.value) == 'missing required attribute "name"'

def test_unexpected_attribute():
	template = {'name': 'test_name', 'test': ''}
	id = 5

	with pytest.raises(AttributeError) as errinfo:
		obj = GameObject.load_from_template(template, ValidGameObject)

	assert str(errinfo.value) == 'Unexpected attribute "test"'

