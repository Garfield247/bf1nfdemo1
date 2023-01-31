# -*- coding: utf-8 -*-
# 导入类库
from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_moment import Moment

from flask_redis import FlaskRedis


# 创建对象
bootstrap = Bootstrap()
redis_cli = FlaskRedis(decode_responses=True)
# db = SQLAlchemy()
# moment = Moment()
# migrate = Migrate(db=db)



# 初始化
def config_extensions(app):
    bootstrap.init_app(app)
    redis_cli.init_app(app)
    # db.init_app(app)
    # moment.init_app(app)
    # migrate.init_app(app)

