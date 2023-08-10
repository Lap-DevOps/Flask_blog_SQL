import logging

from flask import Flask, redirect, url_for, request
from flask.cli import FlaskGroup
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand
from flask_security import SQLAlchemyUserDatastore, Security
from flask_security import current_user
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = FlaskGroup(app)
manager.add_command('db', MigrateCommand)

from models import Post, Tag, User, Role


class AdminMixin():
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class PostAdminView(AdminView, BaseModelView):
    form_columns = ['title', 'body', 'tags']


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


admin = Admin(app, 'FlaskApp', url="/", index_view=HomeAdminView('Home'))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(AdminView(User, db.session))

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)  # Устанавливаем уровень логирования

# Создаем объект логгера для SQLAlchemy
logger = logging.getLogger('sqlalchemy.engine')
handler = logging.FileHandler('sqlalchemy.log')  # Задаем файл для записи логов
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

# login
#

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
# register = RegisterForm(app, user_datastore)
