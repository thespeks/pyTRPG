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
    _items = ()
    
    def __get__(self): return self._items
    def __iter__(self): return iter(self.__get__())
    def __contains__(self): return x in self.__iter__()
    
    def __eq__(self, x): return x == self.__get__()
    def __ne__(self, x): return x != self.__get__()

class DictBase(_Base):
    _items = {}
