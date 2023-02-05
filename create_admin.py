from bike_app.models import Users
from bike_app import db, create_app
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__),'.', '.env'))

app = create_app()
env_username=os.getenv('USERNAME')
env_password=os.getenv('PASSWORD')

def create_admin_user(new_username, new_password):
    new_user = Users(
        username=new_username,
        password=generate_password_hash(new_password)
    )

    with app.app_context():
        db.session.add(new_user)
        db.session.commit()



if __name__ == "__main__":
    create_admin_user(env_username, env_password)