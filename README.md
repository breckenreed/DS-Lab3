##DS LAB-3 


logging-service працюватиме у підмережі докера, тому міняємо сокети в HazelcastClient з локальної мережі на мережу докера <br />
Змінна ``PYTHONUNBUFFERED`` передається через docker run для корректної роботи потоків stdout та stderr, і відповідно, функції print <br />
У facade-service додано рандомізацію вибору екзмепляру logging-service, на який полетить запит <br />



Завдання <br />
Запустити три екземпляра logging-service (локально їх можна запустити на різних портах), відповідно мають запуститись також три екземпляра Hazelcast <br />

У папці ``logging_service_alt``

```
docker run -d -p 8011:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW1 --network hazelcast-network-1 logging-service_alt <br />

docker run -d -p 8012:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW2 --network hazelcast-network-1 logging-service_alt <br />

docker run -d -p 8013:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW3 --network hazelcast-network-1 logging-service_alt <br />
```

<img width="958" alt="image" src="https://github.com/breckenreed/DS-Lab3/assets/62158298/f93921cd-f45b-4ab7-924e-21422ed54966">


Через HTTP POST записати 10 повідомлень msg1-msg10 через facade-service <br />







Показати які повідомлення отримав кожен з екзмеплярів logging-service (це має бути видно у логах сервісу) <br />
Через HTTP GET з facade-service прочитати повідомлення <br />
Вимкнути один/два екземпляри logging-service (разом з ним мають вимикатись й ноди Hazelcast) та перевірити чи зможемо прочитати повідомлення <br />
