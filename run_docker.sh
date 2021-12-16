echo Down with servers
docker-compose down -v

echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d

echo run docker-compose
docker-compose up