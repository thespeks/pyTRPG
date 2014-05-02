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
            
            
class Game:
    def __init__(self):
        self._saved =   False
        self._savable = False
        self._game = None
        self._config = Config()
    
    def __get__(self):  return self._game
    
    def _get_savable(self): return self._is_savable
    def _set_savable(self, savable): self._is_savable = bool(savable)
    is_savable = property(_get_savable, _set_savable,
        doc="A state which stores whether this game can be saved.")
    
    def _can_exit(self, dest):
        if self._saved == False: return self.can_exit(dest))
        return True
    
    def get_available_choices(self):
        yield 'config'
        if self.can_save: yield 'save'
    
    def can_save(self):
        """Return True if this game can be currently saved."""
        return (self._game is not None and self.is_savable)
    
    def new(self, reuse_config=True):
        """Start a new game."""
        if self._can_exit(dest='new'):  
            self._game = self.on_new_game(reuse_config)
    
    def load(self):
        """Load a saved game."""
        self._can_exit(dest='load'): return self.on_load_game()
            
    def save(self):
        """Save this game."""
        if self.can_save(): return self.on_save_game()
        pass
        
    def can_exit(self, dest):
        """Override this to handle game exit parameters."""
        # TODO Add more descriptive docstring
        raise NotImplementedError
        
    # game events
    def on_new_game(self, reuse_config):
        raise NotImplementedError
    
    def on_load_game(self):
        raise NotImplementedError
    
    def on_save_game(self):
        raise NotImplementedError
        

from trpg._bases import DictBase    
class Config(DictBase):
    self._items = {}
            
    def reset(self):
        """Override this to add a reset method."""
        pass
    
    
