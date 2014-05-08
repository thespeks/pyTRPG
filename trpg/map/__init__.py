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



def get_new_blank_map(size_x, size_y, empty='.'):
    """Return a new blank map."""
    if (size_x and size_y) > 1:
        x = join([empty]*size_x)
        return tuple(x for i in range(size_y)
    else: raise ValueError("Invalid size for map. Sizes must be > 1.")

def build_coords_dict(map_matrix, dict_of_cell_types=None, empty='.'):
    """Return a new dict of (x, y) coords mapped to non-empty chars."""
    d = {}
    if dict_of_cell_classes == None:
        for y in matrix:    # y axis
            for char in y:   # x axis
                if char != empty:    # skip empty
                    d[y.index(char), matrix.index(y)] = char
                    
    elif (isinstance(dict_of_cell_types, dict) or 
        (hasattr(dict_of_cell_types, '_items') and 
        isinstance(dict_of_cell_types._items, dict))):
        for y in matrix:    # y axis
            for char in y:   # x axis
                if char != empty:    # skip empty
                    d[y.index(char), matrix.index(y)] = \ 
                        dict_of_cell_types[char]
    else:
        raise TypeError('Expected instance of dict type for dict_of_cell_classes')
    return d


class MapCell:
    __slots__ = '_d', '_doors'
    def __init__(self, d, doors=()):
        self._d = d
        self._doors = doors
        
    def get_coords(self):
        """The x,y coords of this cell."""
        for i in self._d.keys():
            if self._d[i] == self: return i
            
    def get_adj_cell_coords(self, x, y):
        for i in self._d.keys()
            if self._d[i] == self:
                if (i[0]+x, i[1]+y) in self._d:
                    return (i[0]+x, i[1]+y)
                return None, None
                
    def get_adjacent_cell(self, direction):
        if direction == ('N' or 'North'):    
            return self._self.get_adj_cell_coords(0, 1)]
        elif direction == ('E' or 'East'):  
            return self._d[self.get_adj_cell_coords(1, 0)]
        elif direction == ('S' or 'South'):  
            return self._d[self.get_adj_cell_coords(0, -1)]
        elif direction == ('W' or 'West'):  
            return self._d[self.get_adj_cell_coords(-1, 0)]
        else: raise ValueError('Invalid direction {}'.format(direction))
           
    

        
        
