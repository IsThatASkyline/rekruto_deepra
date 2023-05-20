# Тестовое задание Intern/Junior Python backend developer
Можно проверить онлайн, перейдя на https://rekrutodeepra-production.up.railway.app/?name=Rekruto&message=Давай%20дружить! 

## Задание
Создать веб-сервис, который будет выводить "Rekruto! Давай дружить!". URL с GET запросом, который будет выводиться уже на странице: 
урл должен быть таким xx.xx.xx.xx./?name=Rekruto&message=Давай дружить! и выводилось на странице Hello {name}!{message}!

## Решение
Я сделал сервис, используя FastAPI. В ответ попросили ссылку на сервис, я не понял надо ссылку на гитхаб или на задеплоенное приложение, поэтому сделал и так, и так

## Установка и запуск
#### Клонируем репозиторий и заходим в него
```
git clone https://github.com/artklk12/rekruto_deepra.git
cd rekruto_deepra
```
#### Устанавливаем зависимости и запускаем
Используя консоль
```
pip install -r requirements.txt
uvicorn main:app --reload
```
либо, используя docker
```
docker build -t rekruto .
docker run -p 8000:8000 rekruto
```
