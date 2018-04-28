#阿里云 oss 地址
import os
env_dict = os.environ
alicdnserver = env_dict.get('ALICDNSERBER')
appid = env_dict.get('APPID')
appscred = env_dict.get('APPSCRED')
spiderurl = env_dict.get('SPIDERURL')
connect_str = env_dict.get('MYSQL_CONNECTIONSTRING')