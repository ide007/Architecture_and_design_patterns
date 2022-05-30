Architecture and design patterns in Python

Домашние задания по курсу "Архитектура и шаблоны проектирования на Python"

Урок № 1. Паттерны веб-представления

1. Создать репозиторий для нового проекта (gitlab, github, ...).
2. С помощью uwsgi или gunicorn запустить пример simple_wsgi.py, проверить, что
   он работает
   (Эти библиотеки работают на linux-системах, документацию по ним можно найти
   в дополнительных материалах).
3. Написать свой WSGI-фреймворк, используя паттерны Page Controller и Front
   Controller. Описание работы фреймворка:
   a. возможность отвечать на get-запросы пользователя (код ответа +
   html-страница); b. для разных url-адресов отвечать разными страницами; c.
   page controller — возможность без изменения фреймворка добавить view для
   обработки нового адреса; d. front controller — возможность без изменения
   фреймворка менять обработку всех запросов.
4. Реализовать рендеринг страниц с помощью шаблонизатора Jinja2. Документацию
   по этой библиотеке можно найти в дополнительных материалах.
5. Добавить любый полезный функционал в фреймворк, например обработку наличия
   (отсутствия) слеша в конце адреса, и так далее.
6. Добавить для демонстрации две любые разные страницы (например, главная и
   about, или любые другие).
7. Сдать задание в виде ссылки на репозиторий.
8. В readme указать пример, как запустить фреймворк с помощью uwsgi и/или
   gunicorn.

_______________________________________________________________________________

Урок № 2. Архитектура python-приложений

1. Добавить в свой wsgi-фреймворк возможность обработки post-запроса.
2. Добавить в свой wsgi-фреймворк возможность получения данных из post запроса.
3. Дополнительно можно добавить возможность получения данных из get запроса.
4. В проект добавить страницу контактов на которой пользователь может отправить
   нам сообщение (пользователь вводит тему сообщения, его текст, свой email).
5. После отправки реализовать сохранение сообщения в файл, либо вывести
   сообщение в терминал (базу данных пока не используем).

для запуска на windows: waitress-serve --listen=127.0.0.1:8001 main:app для
запуска на unix: gunicorn main:app
_______________________________________________________________________________

Урок 3. Принципы проектирования

1. Внести изменения в wsgi-фреймворк, которые позволят использовать механизм
   наследования и включения шаблонов.
2. Создать базовый шаблон для всех страниц сайта.
3. Если нужно создать один или несколько включенных шаблонов.
4. Добавить на сайт меню, которое будет отображаться на всех страницах.
5. Улучшить имеющиеся страницы с использованием базовых и включенных шаблонов.
6. Проверить что фреймворк готов для дальнейшего использования при желании
   добавить какой-либо полезный функционал.

_______________________________________________________________________________

Урок 4. Порождающие паттерны

1. Добавить следующий функционал:
* Создание категории курсов
* Вывод списка категорий
* Создание курса
* Вывод списка курсов.

2. Далее можно сделать всё или одно на выбор, применив при этом один из
   порождающих паттернов, либо аргументировать почему данные паттерны не были
   использованы:
* На сайте могут быть курсы разных видов: офлайн (в живую) курсы (для них
  указывается адрес проведения) и онлайн курсы (вебинары), для них указывается
  вебинарная система. Также известно, что в будущем могут добавиться новые виды
  курсов;
* Реализовать простой логгер (не используя сторонние библиотеки). У логгера
  есть имя. Логгер с одним и тем же именем пишет данные в один и тот же файл, а
  с другим именем в другой;
* Реализовать страницу для копирования уже существующего курса (Для того чтобы
  снова с нуля не создавать курс, а скопировать существующий и немного
  отредактировать).