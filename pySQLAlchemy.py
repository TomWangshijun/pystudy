# -*- coding: utf-8 -*-

#import 
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#base class
Base = declarative_base()

#User class
class User(Base):
	# table name
	__tablename__ = 'user'

	# table struct
	id = Column(String(20),primary_key=True)
	name = Column(String(20))

# create a database link
engine = create_engine('sqlite:///test.db')

DBsession = sessionmaker(bind=engine)
#add a record id=5,name=Tom Wang
#session = DBsession()

#new_user = User(id='5',name='Tom Wang')

#session.add(new_user)

#session.commit()

#session.close()

#query a record where id=5,only one record
session = DBsession()
user = session.query(User).filter(User.id=='5').one()
print 'type:',type(user)
print user.name
session.close()


#query records where name=Tom Wang, many records
session = DBsession()
user = session.query(User).filter(User.name=='Tom Wang').all()
print len(user)
print user[2].id,user[-1].id
session.close()
