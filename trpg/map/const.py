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


# Move direction
# Indexes/Dead Ends
N =     0     
E =     1     
S =     2     
W =     3
# Straightaways
NS =    N,S     # |
EW =    E,W     # -
# Corners
NE =    N,E     # |_
NW =    N,W     #      _|
SE =    S,E     # |''
SW =    W,W     #     ``|
# Crossroads
NESW =  N,E,S,W
# 'T' Sections
EWS =   E,S,W   # Down  T 
NES =   N,E,S   # Right |-
NSW =   N,S,W   # Left  -|
NEW =   N,E,W   # Up    _|_


NORTH = 'North'
EAST =  'East'
SOUTH = 'South'
WEST =  'West'
DIRECTIONS = (NORTH, EAST, SOUTH, WEST)

