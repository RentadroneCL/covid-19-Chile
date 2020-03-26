from database import db
from orator import Model

Model.set_connection_resolver(db)


class DailyReport(Model):

    __table__ = 'daily_reports'

