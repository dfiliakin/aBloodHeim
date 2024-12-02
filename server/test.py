from repository import db
from repository.user.crud import get_user_by_login


session = next(db.get_db())
print(get_user_by_login(db=session, login="admin").name)
