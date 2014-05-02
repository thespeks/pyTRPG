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


main = None

__all__ = 'main'

def init_run(main=Main):
    if main != None:  main = Main()


class Main:
    """The main class for TRPG."""
    def __init__(self):
        self._main_init
        
    def _main_init(self):
        self._rs = _RS()
        self._cur_game = None    
        self._config = Config()
    
    @property
    def game(self):
        """The current game."""
        return self._game
        
    @property
    def global_config(self):
        """
        The global configuration.
            (for game exclusive config see main.game.config)
        """
        return self._config
    
    class _RS:
        """Run state handler for TRPG."""
        def __init__(self):
            self._running = False
            self._run
            
        def _run(self):
            self._running = True
            
            
