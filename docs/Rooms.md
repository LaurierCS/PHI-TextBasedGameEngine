# Rooms

Rooms are 

## Yaml Format

Property | Description | Supports min/max | Optional | Default
---- | ---- | ---- | ---- | ----
name | Used to uniquely identify the room. Player will not see this | no | no
description | Text shown to the player when they see this room | no | no
options | Options given to the player | no | no

## Options

A minimum of 1 option must be given to the player. Options have their own unique format:

```yaml
options: 
  - key:
	text: ...
	action: ...
```

Property | Description
---- | ----
key | The shorthand for the option. Usually (1,2,3), (A,B,C)
text | Short description of what the option does
action | The `name` of the room to go to, or an [action](#actions)

## Actions

Actions initiate events, move the player between rooms, start combat, etc. 

+ `goto [room]` - used to send a player to another room
  + Example: `goto room2`
+ `combat [enemy]` - spawns and begins combat with an enemy
  + Example: `combat spider`
  + TODO: multiple combat?
+ `give [item]` - gives an item to the player
  + Useful for picking up items
  + Example: `give potion`
  + TODO: How to implement this? Will need to remove the option so you can only pick up once
    + Implies rooms need to have their own inventories of sorts

\### TODO: more docs about actions

## Examples

