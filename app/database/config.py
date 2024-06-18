from configparser import ConfigParser

# database.ini local only for user. create your own database.ini
def config():
    return{
        'host' : 'roundhouse.proxy.rlwy.net',
        'database' : 'railway',
        'user' : 'postgres',
        'password' : 'QMEuewUATBcArKmbDSxPsWmqvgVwoOtD',
        'client_encoding' : 'utf-8',
        'port' : '43898',
    }
