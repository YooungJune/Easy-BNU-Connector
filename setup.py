'''
Author: GasinAn
'''
import os
import sys


print('Installing Requests and BeautifulSoup4...')
if os.system('conda install requests beautifulsoup4') is 0:
    pass
elif os.system('pip install requests beautifulsoup4') is 0:
    pass
elif os.system('pip3 install requests beautifulsoup4') is 0:
    pass
else:
    raise OSError('FAILED!')

print('Installing Js2Py...')
if os.system('pip install requests beautifulsoup4') is 0:
    pass
elif os.system('pip3 install requests beautifulsoup4') is 0:
    pass
else:
    raise OSError('FAILED!')

print('Setting up...')
easy_bnu_connector_path = sys.path[5]+'\\easy_bnu_connector'
os.system('mkdir '+easy_bnu_connector_path)
os.system('move /y easy_bnu_connector\\* '+easy_bnu_connector_path)
os.system('rmdir easy_bnu_connector')
with open('Easy-BNU-Connector.cmd', 'w') as f:
    f.write('python '+easy_bnu_connector_path+'\\login.py')
os.system('del setup.cmd')
os.system('del setup.py')