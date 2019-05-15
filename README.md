[![Build Status](https://travis-ci.com/akopianDA/GAME.svg?branch=master)](https://travis-ci.com/akopianDA/GAME)
# A simple game for our project simple project for a programming technogis course in MIPT

# Как играть.

Есть юниты 3ех типов. Изначально они подразумевались как студенты, семинаристы и лекторы.
Суть игры в том, что сражаются 2 команды лекторов и студентов. Сначала ходят все юниты из одной команды, потом из другой. Во время хода одного юнита он подсвечивается синим цветом, клетки, на которые он может сходить - белым, враги, которых он может ударить - красным, союзники, которых он может подлечить - зеленым. При этом, чтобы закончить ход юнит должен либо ударить/полечиться, либо игрок должен ажать пробел. Все юниты могут лечить/убивать только юнитов в соседних клетках, но лектор может наносить урон любому на карте. Также можно нажать правой кнопкой мыши в основании юнита и увидешь его статы 



# Использованные паттерны

Для создания юнитов были использованы  абстрактные фабрики(лекторов, экзаменаторов, семинаристов). Паттерн команда, чтобы передавать команды. Цепочка обязанностей, чтобы в отдельных функциях проверить, что юнит может выполнить действие, а потом, если может, сделать его. Паттерн стратегия, чтобы мы могли высчитывать урон юнитов по разным формулам. Паттерн адаптер, потому что мы в ходе программы одинакого обрабатываем и экзаменаторов и студентов, но в функции атаки передается и атакующий и тот, кого бьют и номер, кто же из них атакует. При этом там важно, что первый аргумент это экзаменатор, а второй это студент. Вобщем адаптер меняет порядок юнитов на нужный.

# Аргументированный отказ от паттернов

Мы не использовали компановщик так как нет вложенных структур
Не использовали декоратор так как нет особых бафов, которые иногда встречаются
Не используем Observer, так как мы можем позволить себе бегать по всему и использование этого паттерна незаметно для конечного пользователя.


# Как запускать?

Чтобы установить ./install.sh, чтобы играть ./play.sh и только на линуксе

# Архитектура
Архитектура частей создание юнитов и всего остального в соответствующих текстовых файлах в ветках Task1 и Task2 соответственно
