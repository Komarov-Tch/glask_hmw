from flask import Flask
from static.data import db_session
from static.data.users import User
from static.data.news import News
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = ';dskjfo23 u94089iAAA kopdf s9 if0wo3lds'


def f():
    user = User()
    user.name = 'Пользователь 1'
    user.about = 'Биография пользователя 1'
    user.email = 'email1@email.ru'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

def main():
    db_session.global_init("static/db/blogs.db")
#    app.run()
#    f()
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id==1).first()
    for news in user.news:
        print(news)

if __name__ == '__main__':
    main()
