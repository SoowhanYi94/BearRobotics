from dataclasses import dataclass
import string

@dataclass
class Cashbin:
    company: string = "Hyosung"
    cash: int = None
    def __init__(self):
        self.cash = 999999999999999999999
        
 