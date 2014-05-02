



class ChoiceHandler:
    def __init__(self, all_choices, choice_returns):
        self._all_choices = all_choices
        self._choice_returns
        
    def is_available(self, choice):
        """Return True if given choice is available."""
        return choice in self._get_available()
        
    @property
    def all_choices(self):
        """Return all possible choices."""
        return self._all_choices
    
    def available(self):
        """Return an iterable of all possible choices."""
        return self._get_available()
            
    def _get_available(self):
        """
        Override this so that it returns an iterable of currently available 
            choices
        """
        raise NotImplementedError
        
    def get_handled(self, choice, fallback=None, *fallback_args, 
        use_fallback=False):
        for i in enumerate(self._get_available()):
            if choice == i[1]:
                try: 
                    return self._choice_returns[i[0]][0](
                        self._choice_returns[i[0][1])
                except: 
                    # func only
                    try: return self._choice_returns[i[0]]()  
                    # non callable (str, int, etc.)
                    except: return self._choice_returns[i[0]] 
        if use_fallback:    
            try: fallback(fallback_args)
            except return fallback
        raise IndexError("'choice' not found in 'in_seq'.")
