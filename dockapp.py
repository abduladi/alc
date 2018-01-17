import subprocess
import os

subprocess.call('git clone https://github.com/abduladi/UserManager.git', shell=True)

os.chdir('UserManager/')

print ''
print 'Creating .env file'
print ''

subprocess.call('echo "PORT=3000" > .env', shell=True)

subprocess.call('echo "DB_URL=\'mongodb://localhost:27017/test\'" >> .env', shell=True)

subprocess.call('docker build -t user-manager .', shell=True)

subprocess.call('docker run -d -p 3000:3000 user-manager', shell=True)

print 'open http://localhost:3000/ in your browser to access application'