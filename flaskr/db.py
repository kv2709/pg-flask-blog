from psycopg2 import connect


# import sqlite3
# from flask.cli import with_appcontext
# import click
# from flask import current_app, g


# def get_db():
#     """Connect to the application's configured database. The connection
#     is unique for each request and will be reused if this is called
#     again.
#     """
#     if "db" not in g:
#         g.db = sqlite3.connect(
#             current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row
#
#     return g.db
#
#
# def close_db(e=None):
#     """If this request connected to the database, close the
#     connection.
#     """
#     db = g.pop("db", None)
#
#     if db is not None:
#         db.close()
#

# def init_db():
#     """Clear existing data and create new tables."""
#     db = get_db()
#
#     with current_app.open_resource("schema.sql") as f:
#         db.executescript(f.read().decode("utf8"))


# @click.command("init-db")
# @with_appcontext
# def init_db_command():
#     """Clear existing data and create new tables."""
#     init_db()
#     click.echo("Initialized the database.")


# def init_app(app):
#     """Register database functions with the Flask app. This is called by
#     the application factory.
#     """
#     app.teardown_appcontext(close_db)
#     # app.cli.add_command(init_db_command)


def tp_to_dict(fetch_cur_in, cursor_in):
    """ Преобразуем полученный из базы кортежей fetch_cur_in, взяв
        дескриптор куросра базы cursor_in в словарь, ключами которого
        являются имена полей, а значениями - значания полей базы
    """
    descr = cursor_in.description
    rec = fetch_cur_in
    d = {}
    enu = enumerate(descr)
    for idx, colum in enu:
        d[colum[0]] = rec[idx]
    return d


def list_tp_to_list_dict(fetch_cur_in, cursor_in):
    """ Преобразуем полученный из базы список кортежей или
        кортеж fetch_cur_in, взяв дескриптор куросра базы cursor_in
        в список словарей, ключами которого являются имена полей,
        а значениями - значания полей базы. Работает как для fetchall
        так и для fetchone
    """
    descr = cursor_in.description
    dict_lst = []
    cur_lst_in = []
    if type(fetch_cur_in) == tuple:
        cur_lst_in.append(fetch_cur_in)
    else:
        cur_lst_in = fetch_cur_in
    for rec in cur_lst_in:
        d = {}
        enu = enumerate(descr)
        for idxt, colum in enu:
            d[colum[0]] = rec[idxt]
        dict_lst.append(d)
    return dict_lst


def get_conn_db():
    db_name = 'd2rqo5613re182'
    user_name = 'ntrfylfbzpwopk'
    host_name = 'ec2-174-129-240-67.compute-1.amazonaws.com'
    passwd = '8b2413c9d453644338573e79a45949c75db862fca0c10c4190e3d50f82fef780'
    port_num = '5432'
    conn = connect(dbname=db_name, user=user_name, host=host_name, password=passwd, port=port_num)

    # conn = connect(dbname='test_bd', user='usr_bd', host='127.0.0.1', password='usr_pwd', port='5432')

    return conn


