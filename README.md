# DS LAB-3 


logging-service працюватиме у підмережі докера, тому міняємо сокети в HazelcastClient з локальної мережі на мережу докера <br />
Змінна ``PYTHONUNBUFFERED`` передається через docker run для корректної роботи потоків stdout та stderr, і відповідно, функції print <br />
У facade-service додано рандомізацію вибору екзмепляру logging-service, на який полетить запит <br />



Завдання <br />
### 1. Запустити три екземпляра logging-service (локально їх можна запустити на різних портах), відповідно мають запуститись також три екземпляра Hazelcast <br />

У папці ``logging_service_alt``

```
docker network create hazelcast-network-1

docker build -t logging-service_alt .

docker run -d -p 8011:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW1 --network hazelcast-network-1 logging-service_alt <br />

docker run -d -p 8012:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW2 --network hazelcast-network-1 logging-service_alt <br />

docker run -d -p 8013:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW3 --network hazelcast-network-1 logging-service_alt <br />
```
якщо контейнери кластеру Hazelcast та Hazelcast MC наразі не запущені, то потрібно запуситити і їх: <br />

```
docker run \
    -d \
    --name firstmember \
    --network hazelcast-network-1 \
    -e HZ_CLUSTERNAME=dev \
    -p 5701:5701 hazelcast/hazelcast:latest-snapshot 

second
docker run \
    -d \
    --name secondmember --network hazelcast-network-1 \
    -e HZ_CLUSTERNAME=dev \
    -p 5702:5701 hazelcast/hazelcast:latest-snapshot

third
docker run \
    -d \
    --name thirdmember --network hazelcast-network-1 \
    -e HZ_CLUSTERNAME=dev \
    -p 5703:5701 hazelcast/hazelcast:latest-snapshot

docker run \
    -d \
    --network hazelcast-network-1 \
    -p 8080:8080 hazelcast/management-center:latest-snapshot
```


<img width="958" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/f93921cd-f45b-4ab7-924e-21422ed54966">


### 2. Через HTTP POST записати 10 повідомлень msg1-msg10 через facade-service <br />

<img width="779" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/6517bb02-a3a6-4a5c-984c-bb80f438067e">

Вміст ``data.json`` почергово змінювався для кожного повідомлення.  <br />

### 3. Показати які повідомлення отримав кожен з екзмеплярів logging-service (це має бути видно у логах сервісу) <br />

Бачимо, що наші logging-service отримали повідомлення:<br />
<img width="1189" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/376be39c-b8a8-41f1-b627-97f966b8a370"><br />
<img width="1198" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/07743584-6bbc-49f8-a6f9-558d6a6231e2"><br />
<img width="1184" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/b83bd9f7-7d47-4c16-986e-d4a8d95d302a"><br />

Також повідомлення успішно завантажилися у мапу:
<img width="1234" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/37d4533d-a027-42ce-99d0-ceabceab7fc5">

### 4. Через HTTP GET з facade-service прочитати повідомлення <br />

Я випадково записав ще одне десяте повідомлення в процесі виконання, але нічого страшного, оскільки у нього відмінний uuid <br />
<img width="1135" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/2425f9bc-5930-47fd-b92a-5035b8facbb0"> <br />


### 5. Вимкнути один/два екземпляри logging-service (разом з ним мають вимикатись й ноди Hazelcast) та перевірити чи зможемо прочитати повідомлення <br />
<img width="1157" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/f0ca4fd9-567f-48c7-ba98-91423230fc8f">
 
Якщо GET приходить на вимкнений екзмепляр, то бачимо помилку: <br />
<img width="1147" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/e210dad3-f2c1-4bd0-b6f5-ae3c5aeb55e6"> <br />

Якщо GET приходить на увімкнений екземпляр, повідомлення успішно читаються:<br />
<img width="1141" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/fa56077a-4bea-47db-a21b-9881df150fab"> <br />
<img width="1233" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/00ff5a9b-4426-40d3-947f-dc649228970e"> <br />
