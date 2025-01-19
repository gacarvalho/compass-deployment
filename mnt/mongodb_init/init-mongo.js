// Criação do banco de dados e coleção
db = db.getSiblingDB('compass');
db.createCollection('reviews-santander-way');

db.createUser({
  user: "app_user",
  pwd: "secure_password123",
  roles: [{ role: "readWrite", db: "compass" }]
});
