
class _Base:
    _items = ()
    
    def __get__(self):  return self._items
    def __iter__(self): return iter(self.__get__())
    def __contains__(self): return x in self.__iter__()
    
    def __eq__(self, x):    return x == self.__get__()
    def __ne__(self, x):    return x != self.__get__()

class DictBase(_Base):
    _items = {}
