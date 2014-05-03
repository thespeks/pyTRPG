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

class BaseValue:
    """
    Single numeric storage primitive base class.
    Has only type conversion and comparison methods.
    """
    
    def __str__(self):      return str(self._value)
    def __bool__(self):     return self._value != 0
    
    def __hex__(self):      return hex(self._value)
    def __oct__(self):      return oct(self._value)
    def __float__(self):    return float(self._value)
    def __long__(self):     return long(self._value)
    def __int__(self):      return int(self._value)
    
    def __hash__(self):     return hash(id(self))
    
    def __abs__(self):      return abs(self._value)
    def __invert__(self):   return ~self._value
    def __neg__(self):      return -self._value
    def __pos__(self):      return self._value
    
    def __eq__(self, x):    return self._value == x
    def __ne__(self, x):    return self._value != x
    def __gt__(self, x):    return self._value > x
    def __ge__(self, x):    return self._value >= x
    def __lt__(self, x):    return self._value < x
    def __le__(self, x):    return self._value <= x
    

class Value(BaseValue):
    """Generic single numeric value storage base class."""
    
    def __add__(self, x):   return self._value + x
    __radd__ = __add__
    
    def __sub__(self, x):   return self._value - x
    def __rsub__(self, x):  return x - self._value
    
    def __mul__(self, x):   return self._value * x
    __rmul__ = __mul__
    
    def __div__(self, x):   return self._value // x
    def __rdiv__(self, x):  return x // self._value

    def __truediv__(self, x):   return self._value // x
    def __rtruediv__(self, x):  return x // self._value
    
    def __floordiv__(self, x):  return self._value / x
    def __rfloordiv__(self, x): return x / self._value
    
    def __pow__(self, x):   return self._value**x
    def __rpow__(self, x):  return x**self._value
    
    def __divmod__(self, x):    return divmod(self._value, x)
    def __rdivmod__(self, x):   return divmod(x, self._value)
    
    def __mod__(self, x):       return self._value % x
    def __rmod__(self, x):      return x % self._value
    
    def __iadd__(self, x):  self._value = self.__add__()
    def __isub__(self, x):  self._value = self.__sub__()
    def __idiv__(self, x):  self._value = self.__div__()
    def __imul__(self, x):  self._value = self.__mul__()
    
    
# -- LoopValue --------------------------------------------------------------- #
class _LoopValueBase(_ValueBase):
    
    def __get__(self): return self._val
    def __set__(self, x):
        if x == 'next': self.__iadd__(1)
        elif x == 'prev': self.__isub__(1)
        elif self.in_range(x): self._value = x
        else: raise ValueError("Unknown Value")
        
    def __add__(self, x):
        if self._value == self.max: return self.min
        return self._value + x
    __radd__ = __add__
        
    def __sub__(self, x):
        if self._value == self.min: return self.max
        return self._value - x
        
    def __rsub__(self, x):
        if x == self.min: return self.max
        return x - self._value
        
    def __iadd__(self, x): self._val = self.__add__(x)
    def __isub__(self, x): self._val = self.__sub__(x)
    
    @property
    def min(self):
        """The lowest index possible."""
        return 0
        
    @property
    def max(self):
        return
    
    
class CurrentIndex(_LoopValueBase):
    """
Class for storing an index of a container.
Useful for anything that needs navagation methods like next and prev.
"""
    __slots__ = '_container', '_val'
    def __init__(self, container, index=0):
        if hasattr(container, '__iter__'):
            self._container = container
            self._value = index
        else: raise Exception("Container must be iterable.")
    
    def __get__(self): return self._idx
    def __set__(self, x):
        if x == 'next': self.__iadd__(1)
        elif x == 'prev': self.__isub__(1)
        elif self.in_range(x): self._value = x
        elif x in self._container: self._value = self._container.index(x)
        else: raise ValueError("Unknown value.")
        

    @property
    def max(self):
        """The highest index possible."""
        return len(self._container)
        
    def in_range(self, x):
        """Return True if x is in the range from first index to last index."""
        return 0 <= x <= len(self._container)
        
        
