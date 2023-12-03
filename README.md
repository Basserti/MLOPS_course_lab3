# MLOPS_course
Саенко Лев РИМ-220906

## Lab 3
### **План**:
* Определить какой-нибудь внешний источник получения данных и способ получения этих данных (http, curl, wget, API, SQL, SparQL, ...)
* Поставить задачу для алгоритма машинного обучения, выбрать модель и метрику
* Создать инфраструктуру, например, виртуальные машины virtualbox, установить и настроить для работы необходимое программное обеспечение, в том исле airflow и mlflow, а также venv для организации работы виртуального окружения 
Создать python скрипты для
  * Получения данных из внешнего источника
  * Преобразования данных
  * Формирования рабочего набора данных для обучения (train) и тестирования (test) модели
  * Обучения модели на тренировочных (train) данных и ее сохранения
  * Загрузки модели и проверки качества ее работы на тестовых (test) данных
* Добавить код airflow, позволяющий создавать и запускать на регулярной основе описанные операции проекта.
* Добавить код mlflow, позволяющий мониторить ход выполнения конвейера, сохранять и анализировать полученных артифакты. 


### **Other**:
* Python - 3.9.2
* Git - git version 2.30.2

## Result
Есть 2 файла с requirements.txt:
* requirements.txt - полный пакет всех библиотек 
* req.txt - ограниченный, только нужные
  
DAG
![1](https://github.com/Basserti/MLOPS_course_lab3/assets/51204419/daceebc3-9264-4f8e-ac0a-7ca8789c4eeb)
Возникла проблема с API Google - был превышал лимит запросов.
![2](https://github.com/Basserti/MLOPS_course_lab3/assets/51204419/6f61f6ed-c30b-40bb-a5ad-a5c3e72c5201)
MLFlow - get_data
![3](https://github.com/Basserti/MLOPS_course_lab3/assets/51204419/3dec499d-f61b-44b4-972a-982a4f59a25e)
MLFlow - train_model
![4](https://github.com/Basserti/MLOPS_course_lab3/assets/51204419/26f51522-add7-4d87-8aa0-0dcff99bfbae)
MLFlow - test_model
![5](https://github.com/Basserti/MLOPS_course_lab3/assets/51204419/437e68fc-c3a3-40c4-b367-1d8b91ba76dd)




