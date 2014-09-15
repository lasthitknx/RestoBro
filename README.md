#RestoBro#

RestoBro это утилита для глубокого анализа действий игрока во время боя с рейдовым боссом.

*На данный момент RestoBro является консольной утилитой, и методы RestoBro не имеют интерфейсов т.е. просто выводят результат своей работы и ничего не возвращают ( Впрочем Вы можете самостоятельно добавить интерфейсы методов, для дальнейшей обработки данных )*

Начать использовать RestoBro очень просто:
```
from restobro import RestoBro
bro = RestoBro(logifle='WoWCombatLog.txt')
```
Достаточно просто создать объект класса `RestoBro` и передать ему путь к файлу с логами

Посмотреть какие бои RestoBro нашел в файле логов можно посмотреть с помощью метода `show_fights()`
```
bro.show_fights()

USE PULL NUMBER TO CALL CLASS METHODS WITH 'pull_index' VARIABLE REQUIRED
PULL #11 | ENCOUNTER : "Идеалы клакси" | DURATION 11:16 | TOTAL LINES : 167234
PULL #10 | ENCOUNTER : "Идеалы клакси" | DURATION 06:43 | TOTAL LINES : 92453
PULL #1 CAN'T BE PARSED
PULL #0 CAN'T BE PARSED
PULL #3 | ENCOUNTER : "Идеалы клакси" | DURATION 03:12 | TOTAL LINES : 46122
PULL #2 | ENCOUNTER : "Идеалы клакси" | DURATION 01:18 | TOTAL LINES : 14584
PULL #5 | ENCOUNTER : "Идеалы клакси" | DURATION 05:01 | TOTAL LINES : 67075
PULL #4 | ENCOUNTER : "Идеалы клакси" | DURATION 05:17 | TOTAL LINES : 73489
PULL #7 | ENCOUNTER : "Идеалы клакси" | DURATION 06:01 | TOTAL LINES : 82473
PULL #6 | ENCOUNTER : "Идеалы клакси" | DURATION 08:01 | TOTAL LINES : 102375
PULL #9 | ENCOUNTER : "Идеалы клакси" | DURATION 04:19 | TOTAL LINES : 57973
PULL #8 | ENCOUNTER : "Идеалы клакси" | DURATION 07:46 | TOTAL LINES : 119517
```

Метод `applied_without_harmony` ( *неактуально в Warlords of Draenor* ) покажет касты ХоТов и Спокойствия без баффа Гармонии.

Передаем в метод номер пула и ник нашего персонажа (*обратите внимание что номер пула необходимо передавать в виде строки*):
```
bro.applied_without_harmony('10', 'Свирм')

03:02 | Омоложение APPLIED @ "Пираморфикс"
03:03 | Омоложение APPLIED @ "Бествишез"
04:56 | Омоложение APPLIED @ "Свирм"
05:04 | Омоложение APPLIED @ "Слышащий"
05:27 | Жизнецвет APPLIED @ "Рилси"
05:27 | Омоложение APPLIED @ "Свирм"
```

Метод `track_mushrooms_explosions()` ( *неактуально в Warlords of Draenor* ) покажет детальную информацию по все взрывам гриба :

Передаем в метод номер пула и ник нашего персонажа (*обратите внимание что номер пула необходимо передавать в виде строки*):
```
bro.track_mushrooms_explosions('11', 'Свирм')

MUSHROOM EXPLOSION @ 06:43
TOTAL TARGETS FOR EXPLOSION : 3
"Бенигг" HEALED FOR 76605 | 578057 overheal
"Бэндэрок" HEALED FOR 17694 | 636070 overheal
"Пандапро" HEALED FOR 103649 | 552464 overheal
MUSHROOM TOTAL HEAL 197948
----------------------------------------
MUSHROOM EXPLOSION @ 08:35
TOTAL TARGETS FOR EXPLOSION : 12
"Слышащий" HEALED FOR 0 | 501347 overheal
"Томириска" HEALED FOR 0 | 500319 overheal
"Бенигг" HEALED FOR 0 | 497843 overheal
"Рилси" HEALED FOR 0 | 498912 overheal
"Голдфинч" HEALED FOR 17672 | 483722 overheal
"Зверь" HEALED FOR 0 | 499846 overheal
"Жора" HEALED FOR 0 | 548451 overheal
"Хил-тараши" HEALED FOR 0 | 500926 overheal
"Бакэнэко" HEALED FOR 0 | 550928 overheal
"Дынчик" HEALED FOR 0 | 552325 overheal
"милионтыщдпс" HEALED FOR 0 | 550138 overheal
"реалполитик" HEALED FOR 0 | 548620 overheal
MUSHROOM TOTAL HEAL 17672
```

To be continued


