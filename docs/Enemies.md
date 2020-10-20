# Enemies

Enemies are defined in the `enemies.yaml` file.  
It is important to note that enemies defined in this file are *templates*, not actually enemies themselves.

For example, if there is 1 "spider" enemy defined in `enemies.yaml`, there could be any number of spider enemies generated in a playthrough of the game. This is because an entry in `enemies.yaml` defines an enemy template: a blueprint for how to generate enemies in game. This blueprint format makes it very easy to create many different types of enemies that can be spawned. It also allows for variety in the attack power, XP, defence, and other traits of the enemy.


## Yaml Format

`enemies.yaml` is expected to be a YAML list of enemy objects.
Enemy objects have the following specification

Property | Description | Supports min/max | Optional | Default
---- | ---- | ---- | ---- | ----
name | The name of the enemy  | no | no
health | Number of health points | yes | no
attack | How much damage the enemy deals | yes | no
defence | Number of defence points | yes | yes | 0
xp | Number of xp points to award for beating this enemy | yes | yes | 0


An example `enemies.yaml` file could look like:

```yaml
- name: Spider
  min_health: 2
  max_health: 4
  defence: 0
  xp: 3
```

This creates an enemy named "Spider", any spider encountered in the game will have between 2 and 4 HP, will always award 3 XP, and will always have 0 defence.

