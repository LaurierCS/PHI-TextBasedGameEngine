# Yaml File Format

Since there will be a lot of different options, this file will break down how to format your games using YAML.

## Basic File Structure

In general, you should have a directory structure that looks like the following

```
my_game
  - enemies.yaml
  - rooms.yaml
  - items.yaml
  - player.yaml
```

Where `enemies.yaml` contains definitions for your enemies, `rooms.yaml` contains room definitions, and so on.


## Includes

If you have a large game, putting it all into the above files could make for some very large files. For this reason, we have added an include statement. By using include, you can write additional yaml files and include them in your main.

Here is an example enemies.yaml using includes only:

```yaml
include
  - weak_enemies.yaml
  - bosses/boss_1.yaml
  - bosses/boss_.yaml
```

This file simply contains a yaml list of all files to include. The files will be read at once as if they are all one large file.

## Enemies.yaml

`enemies.yaml` is expected to be a YAML list of enemies, each enemy should have the following properties:

* `name` - The name of the enemy
* `min_health` - Minimum number of health points
* `max_health` - Maximum number of health points
* `min_defence` - Minimum number of defence points
* `max_defence` - Same as above for defence
* `min_xp` - Minimum experience points to award for beating this enemy
* `max_xp` - Maximum experience points to award for beating this enemy

An example `enemies.yaml` file could look like:

```yaml
- name: Spider
  min_health: 2
  max_health: 4
  min_defence: 0
  max_defence: 0
  min_xp: 3
  max_xp: 3
```

For values which have the same min/max, you can aggregate them into one field (dropping the min/max prefix). For example, the above could be rewritten as:

```yaml
- name: Spider
  min_health: 2
  max_health: 4
  defence: 0
  xp: 3
```


This creates an enemy named "Spider", any spider encountered in the game will have between 2 and 4 HP, will always award 3 XP, and will always have 0 defence.

For more information on enemies, see the [enemy documentation](Enemies.md).
