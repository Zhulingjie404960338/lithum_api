from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zabbix:pass@172.16.29.59/zabbix'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class tablenames(db.Model):
    __tablename__ = 'valuemaps'
    valuemapid = db.Column(db.INT, primary_key=True)
    name = db.Column(db.String(99))

    def __init__(self, valuemapid, name):
        self.valuemapid = valuemapid
        self.name = name

#查询
# print(db.session.query(tablenames).filter_by(valuemapid=18).value('name'))
# print(db.session.query(tablenames).count())

#插入
# data = tablenames(21, '112233')
# db.session.add(data)
# db.session.commit()

#删除
# db.session.query(tablenames).filter_by(valuemapid=20, name='1122334455').delete()
# db.session.commit()

#修改
# db.session.query(tablenames).filter_by(valuemapid=20, name='11223344').update({'name':'1122334455'})
# db.session.commit()

import pdb;pdb.set_trace()
print(app.config)