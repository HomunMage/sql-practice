export MY_UID=$(id -u)
export MY_GID=$(id -g)

docker compose exec py2db python app.py