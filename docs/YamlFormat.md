# Yaml File Format

Since there will be a lot of different options, this file will break down how to format your games using [YAML](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html).

## Basic File Structure

In general, you should have a directory structure that looks like the following

```
my_game
  - enemies.yaml
  - rooms.yaml
  - items.yaml
  - player.yaml
  - config.yaml
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

This file simply contains a yaml list of all files to include. The included files will treated as if they are all one large file.

## Min and Max Values

For properties which could be generated randomly, a range can be provided. This is done by replacing the property name with `min_<property>` and `max_property`.

**Example:** If some enemy has
```yaml
health: 10
```
Could be replaced by
```yaml
min_health: 5
max_health: 15
```
Now, instead of every spider enemy spawning with 10 health, they will be created with health varying between 5 and 15 points.


## Specific File & Object formats

Documentation on specific file formats can be found below:

* [Enemies](Enemies.md)
* [Rooms](Rooms.md)
* [Items](Items.md)
* [Player](Player.md)
* [Config](Config.yaml)
