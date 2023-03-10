# -*- coding: utf-8 -*-

import os
from app import create_app
from flask_script import Manager,Server
# from flask_migrate import MigrateCommand

# 获取配置
config_name = os.environ.get('FLASK_CONFIG') or 'default'
# 创建Flask实例
app = create_app(config_name)

# 创建命令行启动控制对象
manager = Manager(app)
# 添加数据库迁移命令
# manager.add_command('db', MigrateCommand)
# 开启Debug模式
manager.add_command("runserver", Server(use_debugger=True,host="0.0.0.0",port=8090))

# 启动项目
if __name__ == '__main__':
    manager.run()
