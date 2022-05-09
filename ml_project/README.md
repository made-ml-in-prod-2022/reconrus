Homework 1
==============================

Next instructions assume that your terminal's working directory is ml_project 

### Installation:
~~~
conda create -n vy_made_ml_in_production_hw1 python=3.9.2
conda activate vy_made_ml_in_production_hw1
pip install -e .
~~~

### Usage

Configure ml_project/configs/train_config and launch
~~~
python ml_project/train_pipeline.py
~~~

Similar for `predict_pipeline`. To get predictions modify predict_config.yaml file:

1) Set correct `data_path` that leads to your test set
2) Set `features_to_drop: []` if data file does not already have a target column

### Test:
~~~
pytest tests/
~~~

### Self-assessment
- 0) В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код. (1 балл) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+0 баллов :( </span>.
- 1) В пулл-реквесте проведена самооценка, распишите по каждому пункту выполнен ли критерий или нет и на сколько баллов(частично или полностью) (1 балл) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+1 балл </span>.
- 2) Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (1 балл)  <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+1 балл, смотреть папку reports</span>.  
Вы так же можете построить в ноутбуке прототип(если это вписывается в ваш стиль работы)  
Можете использовать не ноутбук, а скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (за это + 1 балл) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+1 балл, смотреть папку visualization</span>.
- 3) Написана функция/класс для тренировки модели, вызов оформлен как утилита командной строки, записана в readme инструкцию по запуску (3 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+3 балла</span>.
- 4) Написана функция/класс predict (вызов оформлен как утилита командной строки), которая примет на вход артефакт/ы от обучения, тестовую выборку (без меток) и запишет предикт по заданному пути, инструкция по вызову записана в readme (3 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+3 балла</span>.
- 5) Проект имеет модульную структуру (2 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+2 балла </span>.  
- 6) Использованы логгеры (2 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+2 балла </span>.
- 7) Написаны тесты на отдельные модули и на прогон обучения и predict (3 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold"> +0.5 балл </span>.
- 8) Для тестов генерируются синтетические данные, приближенные к реальным (2 балла)
    * можно посмотреть на библиотеки https://faker.readthedocs.io/en/, https://feature-forge.readthedocs.io/en/latest/  
    * можно просто руками посоздавать данных, собственноручно написанными функциями
    <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+1 балл. Данные генерируются по большей части при помощи faker, но не очень похожи на данные, на которых решалась задача</span>.
- 9) Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+3 балла, смотреть configs</span>.
- 10) Используются датаклассы для сущностей из конфига, а не голые dict (3 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+3 балла, смотреть entities</span>.
- 11) Напишите кастомный трансформер и протестируйте его (3 балла) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+2.5 балла, смотреть features/build_features. Написан самостоятельно, но тестов маловато</span>.
- 12) В проекте зафиксированы все зависимости (1 балл) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+1 балл </span>.
- 13) Настроен CI(прогон тестов, линтера) на основе github actions  (3 балла - доп баллы (будем проходить дальше в курсе, но если есть желание поразбираться - welcome) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+0 баллов :( </span>.

- доп*. Используется hydra  (https://hydra.cc/docs/intro/) (3 балла - доп баллы) <span style="color:#f54275;font-weight: bold">|</span> <span style="color:#4245f5;font-weight: bold">+3 балла</span>.

Итого: 28 баллов