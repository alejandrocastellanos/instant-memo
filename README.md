# instant-memo

django app to save sticky notes

python manage.py runserver

![](img1.png)

![](img2.png)

![](img3.png)

build Docker

docker-compose run web
docker-compose up --build
docker-compose run web python3.9 manage.py migrate
docker-compose run web python3.9 manage.py createsuperuser
docker-compose up --build
