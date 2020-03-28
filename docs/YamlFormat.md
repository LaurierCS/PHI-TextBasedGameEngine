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

