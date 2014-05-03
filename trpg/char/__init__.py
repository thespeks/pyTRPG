


class BaseChar:
    _ispc = False
    _party = None
    _items = {
        'name':         "",
        'gender':       None,
        'can_fight':    True,
        
    }
    def __getitem__(self, x):   return self._items[x]

    @property
    def is_pc(self):
        """True if this character is controlled by the player."""
        return self._ispc
    
    @property
    def name(self):
        """This character's name."""
        return self[name']
        
    @property
    def gender(self):
        """This character's gender."""
        return self['can_fight']
    
    @property
    def can_fight(self):
        """True if this character can fight."""
        return self['can_fight']
        
    def get_stats(self):
        for i in self._items.keys():
            if isinstance(i, StatLevel): yield i
            
            

            

from trpg.utils.math import clamp

class StatLevel:
    def __init__(self, level, min=0, max=100):
        if min < max:
            self._min = min
            self._max = max
            if min <= self._value <= max:
                self._value = value
            else: raise ValueError("""level must be greater than or equal to \\ 
min and less than or equal to max""")
        else: raise ValueError("min must be less than max")
        
    def __get__(self):      return self._value
    def __set__(self, x):   self._value = self._clamped(x)
    
    def __add__(self, x):   return self.clamped(self._value+x)
    def __sub__(self, x):   return self.clamped(self._value-x)
  
    def __iadd__(self, x):  self._value = self.__add__()
    __radd__ = self.__iadd__
    
    def __isub__(self, x):  self._value = self.__sub__()
    
    def __eq__(self, x):    return self._value == x
    def __ne__(self, x):    return self._value != x
    def __ge__(self, x):    return self._value >= x
    def __gt__(self, x):    return self._value > x
    def __le__(self, x):    return self._value <= x
    def __lt__(self, x):    return self._value < x
            
    def clamped(self, n):
        return clamp(n, self._min, self._max)

