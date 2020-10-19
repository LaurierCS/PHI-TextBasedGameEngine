# Items

Items are defined in the `items.yaml` file.  
It is important to note that items defined in this file are *templates*, not actually items themselves.

For example, we could define an item "health potion", which can be spawned in game.


## Yaml Format

`items.yaml` is expected to be a YAML list of item objects.
Item objects have the following specification.

Property | Description | Supports min/max | Optional | Default
--- | --- | --- | --- | ---
name | The name of the item | no | no
description | Description of the item | no | yes
uses | The number of times the object can be used (-1) for infinite | yes | yes | -1 
effect | What happens when the object is used. See [effects](#effects) | no | yes

An example `items.yaml` file could look like:

```yaml
- name: Big potion
  uses: 2
  effect:
    - +25 health
```


## Effects

The `effect` property is unique among properties. It takes an ordered list of effects, which are in the format `modifier [value] [which] name[.property]`. Effects are not case-sensitive.

All effects on items and enemies work within the current context. For example, if you use the effect `sub 5 spider.health` to damage a spider create, the effect will look for a spider creature in the current context. If there is no spider creature, the effect will be ignored. For how to handle multiple spider creatures, see [the "which" clause](#the-which-clause).


### Modifiers

The modifier in an effect is what the effect does. Below are all valid modifiers

+ `add`
  + Add a number to the property of name
+ `sub`
  + Subtract a number from the property of name
+ `use`
  + Use an item
+ `say`
  + Output some text to the screen
+ `spawn`
  + Spawn an item or creature into the current context. Items spawn into the player's inventory.
  + Can be used with or without the `value` clause. See [examples](#examples)
+ `destroy`
  + Remove an item or creature in the current context. Does not trigger any effects.


### The "which" Clause

Sometimes we run into situations where it is not clear which object(s) we want our effect to act on. In these cases, the `which` clause comes in handy. `which` allows us to select 1 or more objects based on certain conditions.

In the following list we say object(s) when we mean objects that match the `name[.property]` clause in the current context. The valid values for `which` are as follows:

+ `all` - affect all objects
+ `any` - affect any 1 object; selects the 1st object found
+ `random` - affect any 1 randomly selected object
+ `min` - affect the property with minimum value (only valid for numeric properties)
+ `max` - affect the property with maximum value (only valid for numeric properties)

If a `which` is not specified, `any` is used by default. For example `use potion` will behave exactly the same as `use any potion`: use the first potion it finds 1 time only.

### Examples

+ `add 25 player.health`
  + This will add the value `25` to the property `health` of the `player` object
+ `use health potion`
  + This will use a `health potion` item from the player's inventory
+ `sub 1 (health potion).uses`
  + This will subtract 1 from the `uses` property of a `health potion` in the player's inventory. Note that the brackets around "health potion" are required since there is a space in the name.
+ `spawn 5 spider`
  + Spawns 5 spider enemies into the current context
+ `spawn health potion`
  + Spawns a single health potion into the player's inventory
