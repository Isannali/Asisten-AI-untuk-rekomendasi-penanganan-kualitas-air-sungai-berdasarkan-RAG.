from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
  id:int
  created_at:datetime