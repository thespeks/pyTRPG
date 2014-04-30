
location_data = _Location_Data()
__all__ = "location_data"

class _Location_Data:
    """Storage dict class for mapping location names to location objects."""
    def __init__(self, dict_of_items={}):
        self._items = dict_of_items
        
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
        return self._floors
        
    def get_floor_index(self, floor):
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
    def __init__(self, cells, name=""):
        self._cells = cells
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
    
    def __init__(self, x, y, floor, doors=(), name=""):
        self._x = x
        self._y = y
        self._floor = floor
        self._doors = Doors()
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


