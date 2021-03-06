#RestoBro#

RestoBro это утилита для глубокого анализа действий игрока во время боя с рейдовым боссом.

*На данный момент RestoBro является консольной утилитой, и методы RestoBro не имеют интерфейсов т.е. просто выводят результат своей работы и ничего не возвращают ( Впрочем Вы можете самостоятельно добавить интерфейсы методов, для дальнейшей обработки данных )*

Начать использовать RestoBro очень просто:
```
from restobro import RestoBro
bro = RestoBro(logifle='WoWCombatLog.txt')
```
Достаточно просто создать объект класса `RestoBro` и передать ему путь к файлу с логами

Посмотреть какие бои RestoBro нашел в файле логов можно с помощью метода `show_fights()`
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

Метод `show_totals()` покажет общий хил и оверхил каждой способности в указанном бою

Передаем в метод номер пула и ник нашего персонажа (*обратите внимание что номер пула необходимо передавать в виде строки*):
```
bro.show_totals('11', 'Свирм')

"Омоложение" | HEALING  : 21,568,617 | OVERHEALING : 69,867,776
"Период цветения" | HEALING  : 12,580,539 | OVERHEALING : 32,329,929
"Буйный рост" | HEALING  : 12,280,548 | OVERHEALING : 39,724,238
"Природная чуткость" | HEALING  : 8,501,537 | OVERHEALING : 4,667,677
"Жизнецвет" | HEALING  : 6,532,375 | OVERHEALING : 19,414,907
"Дух Чи-Цзи" | HEALING  : 5,957,677 | OVERHEALING : 6,222,724
"Спокойствие" | HEALING  : 5,188,138 | OVERHEALING : 25,744,175
"Рассекающий удар" | HEALING  : 3,831,328 | OVERHEALING : 39,245,411
"Дар Изеры" | HEALING  : 3,432,936 | OVERHEALING : 594,519
"Быстрое восстановление" | HEALING  : 2,478,393 | OVERHEALING : 5,249,641
"Целительное прикосновение" | HEALING  : 1,612,070 | OVERHEALING : 2,391,320
"Семя жизни" | HEALING  : 1,188,458 | OVERHEALING : 819,415
"Восстановление" | HEALING  : 786,667 | OVERHEALING : 5,412,215
"Покровительство Природы" | HEALING  : 425,616 | OVERHEALING : 3,617,831
"Дикий гриб: лечение" | HEALING  : 215,620 | OVERHEALING : 7,999,968
```


Метод `rejuvenation_tracker()` покажет все касты Омоложения и информацию по каждому тику

Передаем в метод номер пула и ник нашего персонажа (*обратите внимание что номер пула необходимо передавать в виде строки*):
```
bro.rejuvenation_tracker('11', 'Свирм')

06:08 REJUVENATION APPLIED @ "Дезвин"
TICK #0 | HEAL 59973 | OVERHEAL 0
TICK #1 | HEAL 33295 | OVERHEAL 92471 | CRITICAL !
TICK #2 | HEAL 0 | OVERHEAL 59974
TICK #3 | HEAL 0 | OVERHEAL 59973
TICK #4 | HEAL 0 | OVERHEAL 59973
TICK #5 | HEAL 59973 | OVERHEAL 0
TICK #6 | HEAL 0 | OVERHEAL 59973
...
08:15 REJUVENATION APPLIED @ "Кокси"
TICK #0 | HEAL 94140 | OVERHEAL 0 | CRITICAL !
TICK #1 | HEAL 44892 | OVERHEAL 0
TICK #2 | HEAL 0 | OVERHEAL 44892
TICK #3 | HEAL 0 | OVERHEAL 44892
TICK #4 | HEAL 0 | OVERHEAL 94140 | CRITICAL !
TICK #5 | HEAL 0 | OVERHEAL 94140 | CRITICAL !
TICK #6 | HEAL 0 | OVERHEAL 44892
```

Метод `applied_without_harmony()` ( *неактуально в Warlords of Draenor* ) покажет касты ХоТов и Спокойствия без баффа Гармонии.

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

Метод `track_mushrooms_explosions()` ( *неактуально в Warlords of Draenor* ) покажет детальную информацию по всем взрывам гриба :

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

Метод `cleave_tracker()` ( *неактуально в Warlords of Draenor* ) покажет детальную информацию по каждому проку тринкета *Изъеденный кислотой зуб Тока* . 

Передаем в метод номер пула и ник нашего персонажа и если хотим посмотреть проки которые полностью ушли в оверхил устанавливаем параметр `show_all=True`. По умолчанию RestoBro покажет только эффективные проки 
```
bro.cleave_tracker('11', 'Свирм')

CLEAVE @ 00:28 | HEAL : 12382 | OVERHEAL : 37146 | TOTAL TARGETS : 5
CLEAVE @ 00:34 | HEAL : 47993 | OVERHEAL : 143979 | TOTAL TARGETS : 4
CLEAVE @ 00:44 | HEAL : 24764 | OVERHEAL : 99056 | TOTAL TARGETS : 5
CLEAVE @ 01:01 | HEAL : 9868 | OVERHEAL : 19736 | TOTAL TARGETS : 3
...
CLEAVE @ 10:01 | HEAL : 53332 | OVERHEAL : 79998 | TOTAL TARGETS : 5
CLEAVE @ 10:05 | HEAL : 256104 | OVERHEAL : 128052 | TOTAL TARGETS : 3
CLEAVE @ 10:05 | HEAL : 53332 | OVERHEAL : 53332 | TOTAL TARGETS : 5
CLEAVE @ 10:07 | HEAL : 35497 | OVERHEAL : 200103 | TOTAL TARGETS : 5
TOTAL PROCKS : 313 | EFFECTIVE : 95
```



To be continued


