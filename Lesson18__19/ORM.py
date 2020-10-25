from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Lesson18__19 import parser

engine = create_engine('''sqlite:///database.db''', echo=True)
Base = declarative_base()


class DataParse(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    link = Column(String)
    model = Column(String)
    price = Column(Integer)
    old_price = Column(Integer)

    def __init__(self, link, model, price, old_price=0):
        self.link = link
        self.model = model
        self.price = price
        self.old_price = old_price

    def __str__(self):
        return f'{self.id}, {self.link}, {self.model}, {self.price}, {self.old_price}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_data(link, model, price, old_price=0):
    dp = DataParse(link, model, price, old_price)
    session.add(dp)
    session.commit()


if __name__ == '__main__':
    # data = parser.run()
    # for i in data:
    #     add_data(i['link'], i['model'], i['price'], i['old_price'])
    pass
