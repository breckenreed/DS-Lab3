##DS LAB-3 


logging-service працюватиме у підмережі докера, тому міняємо сокети в HazelcastClient з локальної мережі на мережу докера
Змінна PYTHONUNBUFFERED передається через docker run для корректної роботи потоків stdout та stderr, і відповідно, функції print
У facade-service додано рандомізацію вибору екзмепляру logging-service, на який полетить запит


docker run -d -p 8011:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW1 --network hazelcast-network-1 logging-service_alt

docker run -d -p 8012:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW2 --network hazelcast-network-1 logging-service_alt

docker run -d -p 8013:8001 --env "PYTHONUNBUFFERED=1" --name logging-serviceNEW3 --network hazelcast-network-1 logging-service_alt




Завдання
Запустити три екземпляра logging-service (локально їх можна запустити на різних портах), відповідно мають запуститись також три екземпляра Hazelcast
Через HTTP POST записати 10 повідомлень msg1-msg10 через facade-service
Показати які повідомлення отримав кожен з екзмеплярів logging-service (це має бути видно у логах сервісу)
Через HTTP GET з facade-service прочитати повідомлення
Вимкнути один/два екземпляри logging-service (разом з ним мають вимикатись й ноди Hazelcast) та перевірити чи зможемо прочитати повідомлення 
