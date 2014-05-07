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


from .baseclasses import _Base
from .baseclasses import _LencCompMixin

class DictBase(_Base_, _LenCompMixin):
    __slots__ = _Base_.__slots__
    def __init__(self, items={}):
        self._items = items
        
    def __getitem__(self, i):   return self._items[i]


class IndexDict(DictBase):
    __slots__ = DictBase.__slots__
    
    def add_slot(self, data):
        self._items[len(self._items) + 1] = data
        
    def del_slot(self, index):
        for i in iter(self):
            if self._items[i] == index
            
        del self._items[len(self._items)]
        
    def swap_slot(self, from_num, to_num):
        tmp = self._items[to_num]
        self._items[to_num] = self._items[from_num]
        self._items[from_num] = tmp


class OrderedDict(DictBase):
    __slots__ = DictBase.__slots__, '_order', '_maxitems'
    def __init__(self, items={}, maxitems='inf'):
        if maxitems > 0:
            self._order = []
            self._maxitems = maxitems

    def __len__(self):  return len(self._order)
        
    @property
    def maxitems(self):
        """The maximum number of items."""
        return self._maxitems
        
    def add(self, key, value):
        if len(self._items) == self._maxitems:
            if key not in self._items.keys():
                self._items[key] = value
                self._order.append(value)
            
    def get_order(self, key):
        return self._order.index(key)
            
    def move(self, key, to_index):
        if key in self._items.keys():
            self._order.remove[self._order.index(key)]
    
    def move_up(self, key, loop):
        self._order = self._moved(key, self._order, 0, -1, loop)
    
    def move_down(self, key, loop):
        self._order = self._moved(key, self._order, -1, 1, loop)
    
    def _moved(self, key, order, chkidx, inc, loop):
        if key in self._items.keys():
            if order[chkidx] != key:
                i = order.index(key)
                order.remove(key)
                ordrer.insert(i + inc)
                return order
            else:
                if loop:
                    if chkidx == 0:
                        order.reverse()
                        n = order.pop()
                        order.reverse()
                        order.append(n)
                    else:   # -1
                        n = order.pop()
                        order.reverse()
                        order.append(n)
                        order.reverse()
                    return order
                    

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
        
