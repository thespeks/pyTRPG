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

def build_coords_dict(map_matrix, empty='.'):
    """Return a new dict of (x, y) coords mapped to non-empty chars."""
    d = {}
    for y in matrix:
          for i in y:
              if i != empty:
                  d[y.index(i), matrix.index(y)] = y[y.index(i)]
    return d
