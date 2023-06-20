from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_models = [User, State, City, Amenity, Place, Review]


class DBStorage:
    """ DB Storage engine for MySQL storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiate a new db storage instance """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB
            ),
            pool_pre_ping=True
        )
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ returns a dictionary """
        object_dict = {}
        if cls:
            for object in self.__session.query(cls).all():
                key = "{}.{}".format(type(cls).__name__, object.id)
                object_dict[key] = object
        else:
            for class_model in class_models:
                print(class_model.__name__)
                for object in self.__session.query(class_model).all():
                    key = "{}.{}".format(type(object).__name__, object.id)
                    object_dict[key] = object
        
        return object_dict
    
    def new(self, obj):
        """ adds obj to session """
        self.__session.add(obj)

    def save(self):
        """ commits changes to the current db """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj from the current db session """
        if obj == None:
            return
        
        self.__session.delete(obj)

    def reload(self):
        """ creates all tables in th db session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False
            )
        self.__session = scoped_session(session)
    
    def close(self):
        """ Dispose the current session if active """
        self.__session.remove()