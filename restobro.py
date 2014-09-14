import datetime

ENCOUNTER_START_MESSAGE = 'ENCOUNTER_START'
ENCOUNTER_END_MESSAGE = 'ENCOUNTER_END'


class RestoBro():
    def __init__(self, logfile='WoWCombatLog.txt', initialize=True):
        self.log = logfile
        if initialize is False:
            self.fights = self.parse_fights()
        else:
            self.fights = self.parse_fights(initialize=True)

    def parse_fights(self, initialize=False):
        fights = {}
        key = '0'
        current_fight = {}
        log = open(self.log, encoding='utf-8').readlines()
        for line in log:
            if ENCOUNTER_START_MESSAGE in line:
                date = line.split(',')[0].split(' ')[0]
                time = line.split(',')[0].split(' ')[1]
                encounter = line.split(',')[2]
                current_fight['encounter'] = encounter
                current_fight['start_line'] = log.index(line)
                current_fight['start_time'] = time
                current_fight['start_date'] = date
            if ENCOUNTER_END_MESSAGE in line:
                date = line.split(',')[0].split(' ')[0]
                time = line.split(',')[0].split(' ')[1]
                current_fight['end_line'] = log.index(line)
                current_fight['end_time'] = time
                current_fight['end_date'] = date
                fights[key] = current_fight
                key = str(int(key) + 1)
                current_fight = {}
        if initialize is True:
            print('USE PULL NUMBER TO CALL CLASS METHODS WITH \'pull_index\' VARIABLE REQUIRED')
            for fight in fights:
                try:
                    fight_duration = datetime.datetime.strptime(fights[fight]['end_time'], '%H:%M:%S.%f') - datetime.datetime.strptime(fights[fight]['start_time'], '%H:%M:%S.%f')
                    fight_duration_normalized = str(fight_duration).split(':')[1]+':'+str(fight_duration).split(':')[2].split('.')[0]
                    print('PULL #%s | ENCOUNTER : %s | DURATION %s | TOTAL LINES : %s' % (fight, fights[fight]['encounter'],
                    fight_duration_normalized, str(int(fights[fight]['end_line'])-int(fights[fight]['start_line']))))
                except KeyError:
                    print('PULL #%s CAN\'T BE PARSED' % (fight,))
        return fights

    def parse_single_fight(self, pull_index, actor):
        log = open(self.log, encoding='utf-8').readlines()
        tmp = open('tmp.txt', 'w', encoding='utf-8',)
        for line in range(self.fights[pull_index]['start_line'], self.fights[pull_index]['end_line']):
            if actor in log[line] or ENCOUNTER_START_MESSAGE in log[line] or ENCOUNTER_END_MESSAGE in log[line]:
                tmp.write(log[line]+'\n')

    def applied_without_harmony(self, pull_index, actor):
        self.parse_single_fight(pull_index, actor)
        log = open('tmp.txt', encoding='utf-8').readlines()
        ranges = {}
        current_range = {}
        key = '0'
        for line in log:
            if ENCOUNTER_START_MESSAGE in line or 'Гармония' in line:
                if line.split(',')[0].split(' ')[3] == 'SPELL_AURA_REMOVED':
                    current_range['start'] = log.index(line)
            if ENCOUNTER_END_MESSAGE in line or 'Гармония' in line:
                if line.split(',')[0].split(' ')[3] == 'SPELL_AURA_APPLIED':
                    current_range['end'] = log.index(line)
                    ranges[key] = current_range
                    key = str(int(key) + 1)
                    current_range = {}
        for r in ranges:
            for line in range(ranges[r]['start'], ranges[r]['end']):
                try:
                    if log[line].split('  ')[1].split(',')[10] == '"Омоложение"':
                        if log[line].split('  ')[1].split(',')[0] == 'SPELL_AURA_APPLIED':
                            print(log[line])
                    if log[line].split('  ')[1].split(',')[10] == '"Жизнецвет"':
                        if log[line].split('  ')[1].split(',')[0] == 'SPELL_AURA_APPLIED':
                            print(log[line])
                    if log[line].split('  ')[1].split(',')[10] == '"Буйный рост"':
                        if log[line].split('  ')[1].split(',')[0] == 'SPELL_CAST_SUCCESS':
                            print(log[line])
                    if log[line].split('  ')[1].split(',')[10] == '"Спокойствие"':
                        if log[line].split('  ')[1].split(',')[0] == 'SPELL_CAST_SUCCESS':
                            print(log[line])
                except IndexError:
                    pass







