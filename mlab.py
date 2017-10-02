import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds151014.mlab.com:51014/howtogetgirls

host = "ds151014.mlab.com"
port = 51014
db_name = "howtogetgirls"
user_name = "batphoneip5pass"
password = "stupiddog"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
