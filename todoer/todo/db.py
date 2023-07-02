import mysql.connector

import click
# utilizaremos g para almacenar el usuario
from flask import current_app, g

# Esto servira cuando estemos ejecutando el script de la base de datos
from flask.cli import with_appcontext

from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )

        # Creacion del cursor de manera global
        g.c = g.db.cursor(dictionary=True)

    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)
    
    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')

def init_app(app):

    # Ejecuta funciones enviadas como argumento despues de terminar una accion
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

