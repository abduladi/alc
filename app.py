import subprocess
import os

subprocess.call('git clone https://github.com/abduladi/UserManager.git', shell=True)

os.chdir('UserManager/')
print ''
print 'Input your sudo password for admin operations'
print ''
subprocess.call('sudo npm install', shell=True)

print ''
print 'Creating .env file'
print ''
print 'open http://localhost:3000/users in your browser to see all users in the DB'
subprocess.call('echo "PORT=3000" > .env', shell=True)

subprocess.call('echo "DB_URL=\'mongodb://localhost:27017/test\'" >> .env', shell=True)

subprocess.call('sudo npm start', shell=True)