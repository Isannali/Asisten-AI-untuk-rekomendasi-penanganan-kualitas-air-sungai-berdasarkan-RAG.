from dataclasses import dataclass
from datetime import datetime

@dataclass
class Messages:
  id:int
  conversation_id:int
  role:str
  content:str
  created_at:datetime
  

