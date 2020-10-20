from game.GameContext import GameContext
from gameobjects.GameObject import GameObject
from tests.test_game_utils import *

def test_add():
	ctx = GameContext()
	id = 5
	set_gameobject_id(id)
	obj = MockGameObject()

	ctx.add(obj)

	assert id in ctx.objects
	assert ctx.objects[id] == obj

def test_destroy():
	ctx = GameContext()
	id = 5
	set_gameobject_id(id)
	obj = MockGameObject()
	
	ctx.add(obj)
	assert id in ctx.objects
	result = ctx.destroy(obj)

	assert result is True
	assert id not in ctx.objects

def test_destroy_nothing():
	ctx = GameContext()
	obj = MockGameObject()
	
	result = ctx.destroy(obj)

	assert result is False
	assert ctx.objects == {}

def test_get_by_name_1():
	ctx = GameContext()
	names = ('a', 'b', 'c')
	for name in names:
		ctx.add(create_object(name))

	result = ctx.get_by_name('a')

	assert len(result) == 1
	assert result[0].name == 'a'

def test_get_by_prop_1():
	ctx = GameContext()
	argses = (('a', 1), ('b', 2), ('c', 3))
	for args in argses:
		ctx.add(create_object(*args))

	result = ctx.get_by_prop('prop', 1)

	assert len(result) == 1
	assert result[0].name == 'a'
	assert result[0].prop == 1

def test_get_by_prop_0():
	ctx = GameContext()
	argses = (('a', 1), ('b', 2), ('c', 3))
	for args in argses:
		ctx.add(create_object(*args))

	result = ctx.get_by_prop('prop', 0)

	assert len(result) == 0

def test_get_by_name_0():
	ctx = GameContext()
	names = ('a', 'b', 'c')
	for name in names:
		ctx.add(create_object(name))

	result = ctx.get_by_name('d')

	assert len(result) == 0

def test_get_by_predicate_1():
	ctx = GameContext()
	argses = argses = (('a', 1), ('b', 2), ('c', 3))
	for args in argses:
		ctx.add(create_object(*args))
	
	result = ctx.get_by_predicate(lambda x: x.prop > 2)
	
	assert len(result) == 1
	assert result[0].name == 'c'
	assert result[0].prop == 3

def test_get_by_predicate_0():
	ctx = GameContext()
	argses = argses = (('a', 1), ('b', 2), ('c', 3))
	for args in argses:
		ctx.add(create_object(*args))
	
	result = ctx.get_by_predicate(lambda x: x.prop > 4)
	
	assert len(result) == 0

def test_get_by_id_1():
	ctx = GameContext()
	id = 5
	set_gameobject_id(id)
	names = ('a', 'b', 'c')
	for name in names:
		ctx.add(create_object(name))
	
	result = ctx.get_by_id(id)
	
	assert result is not None
	assert result.name == 'a'
	assert result.id == id

def test_get_by_id_0():
	ctx = GameContext()
	id = 5
	set_gameobject_id(id)
	names = ('a', 'b', 'c')
	for name in names:
		ctx.add(create_object(name))
	
	result = ctx.get_by_id(0)
	
	assert result is None
