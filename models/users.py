from peewee import Model, SqliteDatabase, CharField, ForeignKeyField

db = SqliteDatabase(r'C:\Users\moawe\Desktop\dicegame\models\db\users.db')

class User(Model):
    chat_id = CharField(unique=True)
    username = CharField(null=True)
    joined_at = CharField()
    invite_link = CharField()
    coins = CharField()

    class Meta:
        database = db

class Invitation(Model):
    inviter = ForeignKeyField(User, backref='invitations')
    invited_user = ForeignKeyField(User, backref='invited_by')

    class Meta:
        database = db

db.connect()
db.create_tables([User, Invitation], safe=True)