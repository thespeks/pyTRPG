location_data = _Location_Data()
__all__ = "location_data"


class _Location_Data:
    """Storage dict class for mapping location names to location objects."""
    __slots__= '_items'
    def __init__(self, name_class_pairs={}):
        self._items = name_class_pairs
        
    def __contains__(self, x):  return x in self._items
    def __iter__(self, x):      return iter(self._items.keys())
    
    def location_names(self):
        """Return an iteration of locations."""
        return iter(self._items.keys()
        
    def get_location(self, location_name):
        """Return the location object from a location name."""
        return self._items[location]


class Location:
    """Generic location class for text based RPGs."""
    def __init__(self, floors, location_name=""):
        if len(floors) >= 1:
            self._floors = floors
            self._loc_name = location_name
        
    @property
    def location_name(self):
        """The name of this location."""
        return self._loc_name
        
    def floors(self):
        """Return floors for this location."""
        return self._floors
        
    def get_floor_index(self, floor):
        """Return the floor index for a given floor."""
        return self._floors.index(floor)
        
    def get_cells(self, floor):
        """Return a tuple of cells from given floor."""
        try: return floor._cells        # if floor is object
        except:
            try: return self._floors[floor]._cells     # if floor is index
            except:
                raise IndexError(
                "Got floor as index ({0}). but is out of range (0, {1}) ".format(
                    floor, len(self._floors)))
                    

class Floor:
    """Generic floor class for text based RPGs."""    
    __slots__ = '_cells', '_name'
    def __init__(self, cells, name=""):
        self._cells = Cells()
        self._name = name
        
    @property
    def name(self):
        """The name descriptor for this floor."""
        return self._name
        
    def get_cell_from_coords(x, y):
        """Return a cell using it's x,y coords."""
        for i in iter(self._cells):
            if (i.x == x and i.y == y): return i
        
        
class Cell:
    """Class for generic 'room' like objects for text based RPGs."""
    __slots__ = '_x', '_y', '_doors', '_name'
    def __init__(self, x, y, doors=(), name=""):
        self._x = x
        self._y = y
        if isinstance(doors, Doors):    self._doors = doors
        else:   self._doors = Doors()
        self._name = name
    
    def __eq__(self, x):    return x is self
    def __ne__(self, x):    return x is not self
    
    @property
    def name(self):
        """The name of this cell."""
        return self._name
        
    @property
    def doors(self):
        """Return the doors object for this cell."""
        return self._doors
        
    @property
    def coords(self):
        """The x,y coords of this cell."""
        return self._x, self._y

    def get_adjacent_cell(self, direction):
        if direction == 'N':    
            return self._floor.get_cell_from_coords(self._x, self._y+1)
        elif direction == 'E':  
            return self._floor.get_cell_from_coords(self._x+1, self._y)
        elif direction == 'S':  
            return self._floor.get_cell_from_coords(self._x, self._y-1)
        elif direction == 'W':  
            return self._floor.get_cell_from_coords(self._x-1, self._y)
        else: raise ValueError('Invalid direction {}'.format(direction))


class Cells:
    """Storage class for cells."""
    __slots__ = '_items', '_item_ct'
    def __init__(self, cells):
        self._pack(cells)
    
    def __contains__(self, x):  return x in self._items.keys()
    def __iter__(self): return iter(self._items.keys())
    
    def __len__(self): return self._len
    
    def _pack(self, cells):
        if not isinstance(cells, dict): # dont pack if already a dict
            self._item_ct = 0
            for i in cells: 
                self._items[i.coords_as_str()] = i
                self._item_ct += 1
        else: self._item_ct = len(self._items)
    
    def coords(self):
        return self._items.keys()
        
    def cells(self):
        return self._items.values()
    
    def get_cell_from_str(self, string):
        """Return a cell from a string."""
        return self._items[string]
        
    def get_cell_from_coords(self, coords):
        """Return a cell from x, y coords."""
        if isinstance(coords, str): return self._items[coords]
        else: return self._items[str(coords)]
        
    def get_adjacent(self, cell, direction):
        """Get an adjacent cell."""
        if isinstance(cell, str):
            return self._items[string].get_adjacent(direction)
        else:
            self._items[cell.coords_as_str()].get_adjacent(direction)

            
