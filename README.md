<h1>Тестовое задание:</h1>

<p>Реализовать апи сервер на FastAPI 
с авторизацией и crud операциями для сущности (например книги) 

То есть получится типо библиотеки с авторизацией по jwt
Листингом книг, у которых есть авторы, название, описание, дата выхода
Автор должен быть реализован отдельной сущностью (полное имя, описание(кратко), дата рождения,  биография)

также нужен метод на детальный просмотр книги в котором выводится информация по автору

Неавторизованный пользователи могут только просматривать данные 

Авторизованные могут добавлять и изменять свои добавленные книги 

Соответственно нужен еще листинг "мои добавленные книги" - где только те книги которые добавил пользователь 

Задание должно быть залито на гит, и содержать инструкции к запуску (желательно обернуто в докер) 

ORM для работы с бд - sqlalchemy </p>


<h2>Для запуска:</h2>

<ol>
<li>скачать содиржимое ветки master</li>
<li>используя консоль, перейти в папку с проектом</li>
<li>создать и активировать вирутальное окружение </li>
<li>создать Docker контейнер командой <b>docker compose build</b></li>
<li>после сборки контейнера запустить командой <b>docker compose up</b></li>
<li>сервер запуститься на адресе http://0.0.0.0:8000 поменяйте порт на 9999</li>
<li>для перехода к swager к получившимуся адресу допишите /docs</li>
<li>для взаимодействия с больим количеством запросов необходимо быть зарегестрированным пользователем, по этому сперва пройдите регистрацию</li>
<li>для аутентификации в методе login в поле username используйте почту которая была указана при регистрации</li>
</ol>

<h2>ВНИМАНИЕ</h2>
<p>база данных использует порт 6543, убедитесь в том что этот порт более нигде не зайдейтсвован, в противном случае измините его в файлах .env-non-dev(переменная DB_PORT) и в файле docker-compose(разде db: command, expose)</p>
