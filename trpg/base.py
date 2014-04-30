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


class _BaseAttribs:
    """Storage class for base attributes."""
    _hidden = False
    _name =   ""
    
    @property
    def name(self):
        """Return the name of this."""
        return self._name
    
    def is_hidden(self):
        """return True if this is hidden"""
        return self._hidden
        
        

class Entity(_BaseAttribs):
    """Generic Entity class."""
    _loc = EntityLocation()
    
    
    @property
    def location(self):
        """Access the location attributes for this entity."""
        return self._loc
        
    
    class EntityLoc:
        """Class for storing variables about a characters location."""
        _loc = None
        _floor_idx = None
        _cell = None
        
        @property
        def name(self):
            """The name of this entity's location."""
            return self._loc.name
            
        def set_location(self, location, cell, floor_idx):
            if self._location != location:
                from location import Location
                if data.__class__ == Location: self._loc = loc
                else:
                    # try to set from location name
                    if isinstance(location, str)
                    from location import location_data
                    self._loc = location_data.get_location(location)
            self.floor_idx = floor_idx
            self.cell = cell
            
        @property
        def location(self): 
            "The location of this entity."
            return self._loc
            
        def _get_cell(self): return self._cell
        def _set_cell(self, data):
            if self._cell != data:
                from location import Cell
                if data.__class__ == Cell: self._cell = cell
                else:
                    # try to set from coords
                    self._cell = self._loc.floors()[self._floor_idx].get_cell_from_coords(data)
                    raise Exception("Location and floor must be set before " 
                    "a cell location can be set using coordinants.")
            cell = property(_get_cell, _set_cell, 
            doc="The cell this entity is currently in.")
        
        def _get_floor_idx(self): return self._floor_idx
        def _set_floor_idx(self, floor_idx): 
            if self._floor_idx != floor_idx
                # make sure we have a valid floor
                if 0 <= floor_idx <= len(self._loc._floors): 
                    self._floor_idx = int(floor_idx)
        floor_index = property(_get_floor_idx, _set_floor_idx,
            doc="The floor this entity is currently on.")
            
            
            
