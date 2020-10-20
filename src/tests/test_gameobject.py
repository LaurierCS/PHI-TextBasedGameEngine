import pytest
from gameobjects.GameObject import GameObject
from tests.test_game_utils import *

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

def test_create_multiple():
	template = {'name': 'test_name'}
	id = 5
	
	set_gameobject_id(id)
	obj1 = ValidGameObject()
	obj2 = ValidGameObject()
	obj3 = ValidGameObject()
	
	assert obj1.id == id
	assert obj2.id == id+1
	assert obj3.id == id+2

def test_load_from_template_multiple():
	template = {'name': 'test_name'}
	id = 5
	
	set_gameobject_id(id)
	obj1 = GameObject.load_from_template(template, ValidGameObject)
	obj2 = GameObject.load_from_template(template, ValidGameObject)
	obj3 = GameObject.load_from_template(template, ValidGameObject)
	
	assert obj1.id == id
	assert obj2.id == id+1
	assert obj3.id == id+2
