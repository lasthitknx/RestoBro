RestoBro
========
RestoBro это утилита для глубокого анализа действий игрока во время боя с рейдовым боссом
Подключить RestoBro очень просто :
```
from restobro import RestoBro
```
Начало работы с RestoBro:
```
bro = RestoBro(logfile='WoWCombatLog.txt', initialize=False)
```
Передаем RestoBro путь к нашему файлу с логом и, если хотим посмотреть какие бои есть в логе устанавливаем `initialize=True`.
RestoBro покажет нам какие бои он нашел в логе :
```
USE PULL NUMBER TO CALL CLASS METHODS WITH 'pull_index' VARIABLE REQUIRED
PULL #10 | ENCOUNTER : "Идеалы клакси" | DURATION 06:43 | TOTAL LINES : 92453
PULL #11 | ENCOUNTER : "Идеалы клакси" | DURATION 11:16 | TOTAL LINES : 167234
PULL #6 | ENCOUNTER : "Идеалы клакси" | DURATION 08:01 | TOTAL LINES : 102375
PULL #7 | ENCOUNTER : "Идеалы клакси" | DURATION 06:01 | TOTAL LINES : 82473
PULL #4 | ENCOUNTER : "Идеалы клакси" | DURATION 05:17 | TOTAL LINES : 73489
PULL #5 | ENCOUNTER : "Идеалы клакси" | DURATION 05:01 | TOTAL LINES : 67075
PULL #2 | ENCOUNTER : "Идеалы клакси" | DURATION 01:18 | TOTAL LINES : 14584
PULL #3 | ENCOUNTER : "Идеалы клакси" | DURATION 03:12 | TOTAL LINES : 46122
PULL #0 CAN'T BE PARSED
PULL #1 CAN'T BE PARSED
PULL #8 | ENCOUNTER : "Идеалы клакси" | DURATION 07:46 | TOTAL LINES : 119517
PULL #9 | ENCOUNTER : "Идеалы клакси" | DURATION 04:19 | TOTAL LINES : 57973
```
Это лишь форматированный вывод данных которые храняться в атрибуте RestoBro - `bro.fights`
Данные храняться в словаре, вида :
```
{'end_line': 531989, 'end_date': '9/11', 'end_time': '22:12:11.652', 'start_time': '22:06:10.232', 'encounter': '"Идеалы клакси"', 'start_date': '9/11', 'start_line': 449516}
```
Посмотреть более детальную информацию можно так :
```
for fight in bro.fights:
  print(fight+' '+str(bro.fights[fight]))
```
Получим вот такой результат:
```
9 {'end_line': 713396, 'end_time': '22:30:31.961', 'end_date': '9/11', 'start_time': '22:26:12.609', 'start_line': 655423, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
11 {'end_line': 976551, 'end_time': '22:55:09.765', 'end_date': '9/11', 'start_time': '22:43:52.870', 'start_line': 809317, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
5 {'end_line': 343605, 'end_time': '21:53:28.907', 'end_date': '9/11', 'start_time': '21:48:27.083', 'start_line': 276530, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
4 {'end_line': 273448, 'end_time': '21:44:01.732', 'end_date': '9/11', 'start_time': '21:38:44.709', 'start_line': 199959, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
7 {'end_line': 531989, 'end_time': '22:12:11.652', 'end_date': '9/11', 'start_time': '22:06:10.232', 'start_line': 449516, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
6 {'end_line': 447976, 'end_time': '22:04:13.733', 'end_date': '9/11', 'start_time': '21:56:12.197', 'start_line': 345601, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
1 {'end_line': 101609, 'end_time': '21:12:39.328', 'end_date': '9/11'}
0 {'end_line': 91, 'end_time': '20:53:42.553', 'end_date': '9/11'}
3 {'end_line': 197397, 'end_time': '21:34:20.941', 'end_date': '9/11', 'start_time': '21:31:08.859', 'start_line': 151275, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
2 {'end_line': 149895, 'end_time': '21:29:21.958', 'end_date': '9/11', 'start_time': '21:28:03.085', 'start_line': 135311, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
10 {'end_line': 807791, 'end_time': '22:40:06.732', 'end_date': '9/11', 'start_time': '22:33:22.861', 'start_line': 715338, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
8 {'end_line': 653428, 'end_time': '22:23:53.738', 'end_date': '9/11', 'start_time': '22:16:06.988', 'start_line': 533911, 'encounter': '"Идеалы клакси"', 'start_date': '9/11'}
```



Метод `applied_without_harmony` принимает порядковый номер пула и ник исследуемого друида и возвращает строки из файла лога соответсвующие кастам хотов и "Спокойствия" без баффа "Гармония" :

```
bro.applied_without_harmony('10', 'Свирм')
```
Получаем результат :
```
9/11 22:38:19.454  SPELL_AURA_APPLIED,0x0780000004547DD3,"Свирм",0x511,0x0,0x0780000004547DD3,"Свирм",0x511,0x0,774,"Омоложение",0x8,BUFF

9/11 22:38:27.361  SPELL_AURA_APPLIED,0x0780000004547DD3,"Свирм",0x511,0x0,0x078000000453BFEC,"Слышащий",0x40512,0x0,774,"Омоложение",0x8,BUFF

9/11 22:36:25.064  SPELL_AURA_APPLIED,0x0780000004547DD3,"Свирм",0x511,0x0,0x07800000050289D0,"Пираморфикс",0x514,0x0,774,"Омоложение",0x8,BUFF

9/11 22:36:26.233  SPELL_AURA_APPLIED,0x0780000004547DD3,"Свирм",0x511,0x0,0x0780000004A256E0,"Бествишез",0x514,0x0,774,"Омоложение",0x8,BUFF

9/11 22:38:49.907  SPELL_AURA_APPLIED,0x0780000004547DD3,"Свирм",0x511,0x0,0x078000000598EAE3,"Рилси",0x40512,0x0,33763,"Жизнецвет",0x8,BUFF

9/11 22:38:50.730  SPELL_AURA_APPLIED,0x0780000004547DD3,"Свирм",0x511,0x0,0x0780000004547DD3,"Свирм",0x511,0x0,774,"Омоложение",0x8,BUFF
```
###TBC###
