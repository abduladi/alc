import subprocess
import urllib


print ''
print 'Enter your sudo password to create data store location for mongoDB:'
subprocess.call('sudo mkdir -p /data/db', shell=True)
print ''
print 'changing mod for  data/db directory to have read and write for user accessing mongoDB'
print ''
subprocess.call('sudo chmod 777 /data', shell=True)
subprocess.call('sudo chmod 777 /data/db', shell=True)

user = subprocess.check_output('whoami', shell=True)
user = user[:-1]
arg = 'sudo chown -R ' + user + ' /data/db/'

subprocess.call(arg, shell=True)

print 'Downloading mongoDB started .... '
subprocess.call('curl https://fastdl.mongodb.org/osx/mongodb-osx-ssl-x86_64-3.6.2.tgz --output mongodb.tgz', shell=True)


print 'Unzipping binary files'
subprocess.call('tar -zxvf mongodb.tgz', shell=True)

subprocess.call('./mongodb-osx-x86_64-3.6.2/bin/mongod')


subprocess.call('ls', shell=True)