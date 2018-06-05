from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.dialects.postgresql import insert
from calculations.db.config import db
from calculations.db.models import Contracts, Base

dsn = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(**db)


def create_db_engine():
    return create_engine(dsn)


def upsert_contract(product_name, **kwargs):
    engine = create_db_engine()
    with engine.connect() as connection:
        ins = insert(Contracts).values(product=product_name, **kwargs)
        do_update_contract = ins.on_conflict_do_update(index_elements=['product'], set_=kwargs)
        connection.execute(do_update_contract)


def delete_contract(product_name):
    engine = create_db_engine()
    contr = Contracts.__table__
    with engine.connect() as connection:
        dlt = contr.delete().where(Contracts.product == product_name)
        connection.execute(dlt)


def get_contracts(product_name=None):
    engine = create_db_engine()
    with engine.connect() as connection:
        if not product_name:
            sel = select([Contracts])
        else:
            sel = select([Contracts]).where(Contracts.product == product_name)
        result = connection.execute(sel)
        return _convert_resultproxy_to_dictionary(result)


def _convert_resultproxy_to_dictionary(result_proxy) -> list:
    '''
    Convert ResultProxy object to list of dictionaries.
    :param ResultProxy result_proxy: ResultProxy object to convert
    :return list: list of dictionaries
    '''
    dict_result = []
    for row in result_proxy:
        dict_result.append(dict(row))
    return dict_result


Base.metadata.create_all(create_db_engine())
