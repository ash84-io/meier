docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker pull ash84/meier:latest
docker run -p 2368:2368 -d --env-file .env ash84/meier:latest
