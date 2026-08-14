from app.domain.entities.conversation import Conversation
from app.domain.entities.message import Messages
from app.domain.entities.user import User

from datetime import datetime,timezone

def test_user():
  user=User(
    id=1,
    created_at=datetime.now(timezone.utc)
  )
  assert user.id==1

def test_conversation():
  conversation=Conversation(
    id=1,
    user_id=1,
    created_at=datetime.now(timezone.utc)
  )
  assert conversation.user_id==1
  
def test_messages():
  messages=Messages(
    id=1,
    conversation_id=1,
    role="user",
    content="hai isan",
    created_at=datetime.now(timezone.utc)
  )
  assert messages.role=="user"
  assert messages.content=="hai isan"
