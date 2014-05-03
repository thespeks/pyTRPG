
class Item:
    def __init__(self, name, type, base_value):
        self._name =        name
        self._type =        type
        self._base_value =  base_value
        
    def __eq__(self, x): 
        return ((self._type or self._name == x) or self is x)

    def __eq__(self, x): 
        return ((self._type or self._name != x) or self is not x)
        
    @property
    def name(self):
        """The name of this item."""
        return self._name
        
    @property
    def type(self):
        """The type of this item."""
        return self._type  
        
    @property
    def base_value(self):
        """The base value of this item."""
        return self._base_value
        

from _bc import Type
class ItemType(Type):
    def __init__(self, type, max_qty_slot):
        if max_slot_qty >= 0:   
            self._type = type
            self._max_slot_qty    
    
    @property
    def max_slot_qty(self):
        """The maximum quantity a single slot of this type can hold."""
        return self._max_slot_qty
