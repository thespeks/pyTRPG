

class _Base:
    _items = ()
    
    def __get__(self):  return self._items
    def __iter__(self): return iter(self.__get__())
    def __contains__(self): return x in self.__iter__()
    

class DictBase(_Base):
    _items = {}
