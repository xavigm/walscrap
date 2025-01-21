docker stop walscrap-luxa
docker rm walscrap-luxa
git pull
docker build . -t walscrap-luxa
docker run -d -p 8086:5000 --restart unless-stopped --name walscrap-luxa walscrap-luxa
