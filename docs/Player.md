# Player

Ah yes, the player object. This is a unique and interesting object since it represents the playable user. Luckily, that also means it doesn't need too much work, since their is only 1 user.

## Yaml Format

Property | Description | Supports min/max | Optional | Default
---- | ---- | ---- | ---- | ----
health | Number of health points the user has | no\*
attack | Base attack points | yes | yes | 0
defence | Base defence points | yes | yes | 0
xp | How much xp the user starts with | no | yes | 0
inventory_size | maximum # of items that fit into inventory | no | yes | 0
inventory | List of items that start in the player inventory | no | yes | empty

\### TODO: Add more fields? Player characters probably need more than this

## How is attack calculated?

We use the formula:

`damage = attack * attack / (attack + defence)`

Where damage, attack, and defence are all integers, rounded down if there is a remainder.

If `attack == defence` then the damage will be `attack/2`. As defence decreases damage scale up quickly, and as defence increases damage scales down slowly. To completely mitigate an attack with defence alone, you need `defence = attack*attack`.

### Min/Max Values

If any min/max types are being used, a random value between the min and max (inclusive) will be selected.  
For example, suppose you have `3 min, 5 max` attack. Your attack damage will be `3, 4, or 5`, selected randomly.

### Attack and Defence Bonuses

If you have a bonus to attack or defence, the number is added before any calculations are made. Additionally, if you have a min/max for these, the bonus is added to both.  
For example, suppose you have `4 min, 10 max` for attack with a bonus of 3. Then your attack will be treated as being `7 min, 13 max`.


\* Health does not support min/max for player since the player does not spawn like enemies.


## Examples

```yaml
health: 50
damage: 
defence: 10
xp: 0
inventory_size: 10
inventory:
  - potion
  - potion
  - sword
```

where `potion` and `sword` are the `name` property of items. See [items](Items.md) for more info.
Notice that you need to list multiple of an item if you want multiple.

\### TODO: in the future, we could add a `quantity` field and use that.
