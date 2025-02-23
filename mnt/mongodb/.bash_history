mongosh "mongodb://app_user:secure_password123@localhost:27017/compass"
mongosh --host mongodb --port 27017 -u "gacarvalho" -p "santand@r" --authenticationDatabase "admin"
mongosh "mongodb://app_user:secure_password123@localhost:27017/compass"
mongosh --host mongodb --port 27017 -u "gacarvalho" -p "santand@r" --authenticationDatabase "admin"
mongosh "mongodb://app_user:secure_password123@localhost:27017/compass"
mongosh --host mongodb --port 27017
mongosh --host mongodb --port 27017 -u "root" -p "root_password" --authenticationDatabase "admin"
mongosh --host mongodb --port 27017
mongosh --host mongodb --port 27017 -u "gacarvalho" -p "santand@r" --authenticationDatabase "admin"
mongosh --host mongodb --port 27017 -u "gacarvalho" -p "santand@r" --authenticationDatabase "admin"
mongosh --host mongodb --port 27017 -u "gacarvalho" -p "santand@r" --authenticationDatabase "admin"
mongosh --host mongodb --port 27017 -u "gacarvalho" -p "santand@r" --authenticationDatabase "admin"
--eval 'db.adminCommand({getCmdLineOpts:1})'
mongosh -u admin -p sua_senha_segura --eval 'db.adminCommand({getCmdLineOpts:1})'
mongosh -u gacarvalho -p santand%40r --eval 'db.adminCommand({getCmdLineOpts:1})'
mongosh -u gacarvalho -p "santand@r" --eval 'db.adminCommand({getCmdLineOpts:1})'
openssl genrsa -out mongodb.key 4096  
openssl req -new -x509 -days 365 -key mongodb.key -out mongodb.crt  
cat mongodb.key mongodb.crt > mongodb.pem
ls
ls /etc/ssl/
ls /data/configdb
mv mongodb.pem /data/configdb
ls /data/configdb
ls /etc/ssl/
ls -la /etc/ssl/
ls
cp /data/configdb/mongodb.pem /etc/ssl/
ls /etc/ssl/
ls
ls -l /certs/ca.pem
ls -l /certs/
