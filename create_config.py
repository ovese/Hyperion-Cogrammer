import configparser


config = configparser.ConfigParser()

config['Section 1'] = {'key1': 'value1', 'key2': 'value2'}

config['AppUsers'] = {}
config['AppUsers']['ovese'] = 'techuser'
config['AppUsers']['tobore'] = 'admin'
config['AppUsers']['tekkaboki'] = 'admin'
config['AppUsers']['kome'] = 'techuser'
config['AppUsers']['ona'] = 'techuser'

config['RoleSection'] = {'admin': 'superuser', 'others': 'techuser'}


with open("roles_config.ini", "w") as configfile:
   config.write(configfile)