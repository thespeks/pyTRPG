# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software: you can redistribute it and/or modify     #
#     it under the terms of the GNU General Public License as published by     #
#     the Free Software Foundation, either version 3 of the License, or        #
#     (at your option) any later version.                                      #
#                                                                              #
#     This program is distributed in the hope that it will be useful,          #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#     GNU General Public License for more details.                             #
#                                                                              #
#     You should have received a copy of the GNU General Public License        #
#     along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

"""Base classes for trpg."""

class _Base:
    
    def __get__(self):          return ()
    def __getitem__(self, i):   return self._get__()[i]
    
    def __len__(self):          return len(self.__get__())
    def __iter__(self):         return iter(self.__get__())
    def __contains__(self):     return x in self.__iter__()
    
    def __eq__(self, x):        return x == self.__get__()
    def __ne__(self, x):        return x != self.__get__()

    # length comparison
    def __gt__(self, x):    return self.__len__() > x
    def __ge__(self, x):    return self.__len__() >= x
    def __lt__(self, x):    return self.__len__() < x
    def __le__(self, x):    return self.__len__() <= x
    

class NamedBase(_Base):

    @property
    def name(self):
        return self._name
    
    
class Type:
    """Mixin class for anything with a '_type' attribute"""
    def __get__(self):      return self._type
    def __eq__(self, x):    return (self._type == x or self._type == x._type)
    def __ne__(self, x):    return (self._type != x or self._type != x._type)   
    

class DictBase(_Base):
    __slots__ = '_items'
    def __init__(self, items={}):
        self._items = items


class ValueDict(DictBase):
    __slots__ = DictBase.__slots__
    
    def __getitem__(self, i):
        try: return self._items[i]
        except: return 0    # non existing
    
    def is_eq(self, i, v):
        try: return self._items[i] == v
        except: return False
        
    def is_ne(self, i, v):
        try: return self._items[i] != v
        except: return False
    
    def is_lt(self, i, v):
        try: return self._items[i] < v
        except: return False
        
    def is_le(self, i, v):
        try: return self._items[i] <= v
        except: return False
        
    def is_gt(self, i, v):
        try: return self._items[i] > v
        except: return False
        
    def is_ge(self, i, v):
        try: return self._items[i] >= v
        except: return False
        
    def clamp_add(self, i, amt, min=0, max=100):
        self._items[i] = clamped(self._items[i] + amt, min, max)
        
    def clamp_sub(self, i, amt, min=0, max=100):
        self._items[i] = clamped(self._items[i] - amt, min, max)
        
    def clamp_mul(self, i, amt, min=0, max=100):
        self._items[i] = clamped(self._items[i] * amt, min, max)
        
    def clamp_div(self, i, amt, min=0, max=100):
        self._items[i] = clamped(self._items[i] // amt, min, max)
        
    def clamp_truediv(self, i, amt, min=0, max=100):
        self._items[i] = clamped(self._items[i] / amt, min, max)
        
