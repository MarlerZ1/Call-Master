from apps.utils.main import config


def test_config():
    assert config.DB_USER == 'root'
    assert config.MYSQL_ROOT_PASSWORD == '00000000'
    assert config.DB_HOST == 'db'
    assert config.DB_PORT == 3306
    assert config.MYSQL_DATABASE == 'callmaster_db1'
    assert config.MYSQL_ROOT_HOST == '%'
    assert config.SECRET_KEY == 'XvYvP_c4gBDLCLbjgz6Hc47ND_BcoMYt3Cz5pAKx1qQ='