from random import randint
from operator import itemgetter
from game.GameError import GameError
from gameobjects.GameObject import GameObject
from typing import List

def tokenize(effect, error):
    tok, toks = '', []
    capture = False
    effect = re.sub(' +', ' ', effect.lower().strip())
    for ch in effect:
        if ch == ' ' and not capture:
            toks.append(tok)
            tok = ''
        elif ch == '(':
            capture = True
        elif ch == ')':
            if capture:
                capture = False
            else:
                error()
                return
        else:
            tok += ch
    return toks

class Item(GameObject):
    """
    An item object enables developers to add usable/interactable that the player
    can pickup, drop, and use.

    @author Nausher Rao (SherRao#8509)
    @author Jacob Heard
    """
    
    attributes = {
        'name': (True, lambda x: x),
        'description': (False, lambda x: x),
        'uses': (True, int),
        'effects': (True, lambda x: Item.parse_effects)
    }

    def __init__(self):
        super().__init__()

    def use(self, game_ctx):
        self.uses -= 1
        if self.uses == 0:
            game_ctx.destroy(self)
        for effect in self.effects:
            effect(game_ctx)

    @staticmethod
    def parse_effects(effects: List[str]):
        return [Item.parse_effect(e) for e in effects]

    @staticmethod
    def parse_effect(effect: str):
        def add(ctx, obj, *args):
            obj[args[1]] += args[2]
        def sub(ctx, obj, *args):
            obj[args[1]] -= args[2]
        
        MODIFIERS = {
            'add': add,
            'sub': sub,
            'use': lambda ctx, obj, *args: obj.use(ctx),
            'say': lambda ctx, obj, *args: ctx.send(args[2]),
            'spawn': lambda ctx, obj, *args: ctx.spawn(args[0]),
            'destroy': lambda ctx, obj, *args: ctx.destroy(obj)
        }
        WHICH = {
                # f for function, e for entities
                'all': lambda e: list(range(len(e))),
                'any': lambda e: 0,
                'random': lambda e: [e[randint(0, len(e)-1)]],
                'min': lambda e: [min(enumerate(e), key=itemgetter(1))[0]],
                'max': lambda e: [max(enumerate(e), key=itemgetter(1))[0]]
        }

        def raise_err():
            raise GameError(f'Invalid formatting: "{effect}" in object {self.name}')
        toks = tokenize(effect, error=raise_err)
        if len(toks) == 0:
            return None

        # First arg must always be a modifier
        # TODO: error checking/handling below
        if toks[0] not in MODIFIERS:
            raise GameError(f'Invalid modifier {toks[0]}')
        modifier = MODIFIERS[toks[0]]
        i = 1
        if toks[i].lstrip("-+").isdigit():
            value = int(toks[i])
            i += 1
        else:
            value = 0
        if toks[i] in WHICH:
            which = WHICH[toks[i]]
            i += 1
        else:
            which = WHICH['any']
        if '.' in toks[i]:
            name, prop = toks[i].split()
        else:
            name, prop = toks[i], None

        def call(game_ctx):
            matches = [obj for obj in game_ctx.entities if obj['name'] == name]
            values = matches if prop is None else [obj[prop] for obj in matches]
            indices = which(values)
            args = [name, prop, value]
            # TODO: Some cases may have no contextual results (e.g. spawn)
            for    i in indices:
                modifier(game_ctx, game_ctx.entities[i], *args)
        return call

