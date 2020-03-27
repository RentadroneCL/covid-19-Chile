from database import db
from orator import Model

Model.set_connection_resolver(db)


class Total(Model):

    __table__ = 'totals'

