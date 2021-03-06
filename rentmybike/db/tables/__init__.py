from __future__ import unicode_literals
from datetime import datetime
from random import choice
import uuid
from itertools import cycle

from sqlalchemy import MetaData
from sqlalchemy import (
    Table, Boolean, Column, DateTime, Unicode, ForeignKey, Integer)


metadata = MetaData()


def id_generator():
    return str(uuid.uuid1())


generator = cycle([
    'fixie', 'hybrid', 'road', 'touring'
])


def bike_generator():
    return generator.next()


users = Table('users', metadata,
    Column('guid', Unicode, primary_key=True, default=id_generator),
    Column('created_at', DateTime, default=datetime.utcnow(),
        nullable=False),
    Column('updated_at', DateTime, default=datetime.utcnow(),
        onupdate=datetime.utcnow(), nullable=False),

    Column('password_hash', Unicode),
    Column('has_password', Boolean, default=False, nullable=False),
    Column('name', Unicode),
    Column('email_address', Unicode, nullable=False, unique=True),

    # balanced uri of the Balanced account
    Column('account_uri', Unicode),
)

listings = Table('listings', metadata,
    Column('id', Integer, primary_key=True),
    Column('created_at', DateTime, default=datetime.utcnow(),
        nullable=False),
    Column('bike_type', Unicode, default=bike_generator),
)

rentals = Table('rentals', metadata,
    Column('guid', Unicode, primary_key=True, default=id_generator),
    Column('created_at', DateTime, default=datetime.utcnow(),
        nullable=False),
    Column('bike_guid', Unicode),
    Column('debit_uri', Unicode),
    # no foreign keys, we're going ghetto style!
    Column('owner_guid', Unicode),
    Column('buyer_guid', Unicode),
)
