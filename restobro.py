import datetime
from itertools import groupby
from collections import OrderedDict

ENCOUNTER_START_MESSAGE = 'ENCOUNTER_START'
ENCOUNTER_END_MESSAGE = 'ENCOUNTER_END'

def shift_time(encounter_start, current_line):
    current_time = datetime.datetime.strptime(current_line, '%H:%M:%S.%f') - datetime.datetime.strptime(encounter_start, '%H:%M:%S.%f')
    return str(current_time).split(':')[1]+':'+str(current_time).split(':')[2].split('.')[0]


class RestoBro():
    def __init__(self, logfile='WoWCombatLog.txt'):
        self.log = logfile
        self.fights = self.parse_fights()

    def show_fights(self):
        print('USE PULL NUMBER TO CALL CLASS METHODS WITH \'pull_index\' VARIABLE REQUIRED')
        for fight in self.fights:
                try:
                    fight_duration = datetime.datetime.strptime(self.fights[fight]['end_time'], '%H:%M:%S.%f') - datetime.datetime.strptime(self.fights[fight]['start_time'], '%H:%M:%S.%f')
                    fight_duration_normalized = str(fight_duration).split(':')[1]+':'+str(fight_duration).split(':')[2].split('.')[0]
                    print('PULL #%s | ENCOUNTER : %s | DURATION %s | TOTAL LINES : %s' % (fight, self.fights[fight]['encounter'],
                    fight_duration_normalized, str(int(self.fights[fight]['end_line'])-int(self.fights[fight]['start_line']))))
                except KeyError:
                    print('PULL #%s CAN\'T BE PARSED' % (fight,))

    def parse_fights(self):
        """
        Method parses logfile to define pulls as lines range.
        Returns dict object with keys as pull number and values as pull information
        """
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
            try:
                for line in range(ranges[r]['start'], ranges[r]['end']):
                    try:
                        if log[line].split('  ')[1].split(',')[10] == '"Омоложение"':
                            if log[line].split('  ')[1].split(',')[0] == 'SPELL_AURA_APPLIED':
                                print('%s | Омоложение APPLIED @ %s' % (shift_time(log[0].split(' ')[1], log[line].split(' ')[1]), log[line].split('  ')[1].split(',')[6]))
                        if log[line].split('  ')[1].split(',')[10] == '"Жизнецвет"':
                            if log[line].split('  ')[1].split(',')[0] == 'SPELL_AURA_APPLIED':
                                print('%s | Жизнецвет APPLIED @ %s' % (shift_time(log[0].split(' ')[1], log[line].split(' ')[1]), log[line].split('  ')[1].split(',')[6]))
                        if log[line].split('  ')[1].split(',')[10] == '"Буйный рост"':
                            if log[line].split('  ')[1].split(',')[0] == 'SPELL_CAST_SUCCESS':
                                print('%s | Буйный рост CAST' % (shift_time(log[0].split(' ')[1], log[line].split(' ')[1]),))
                        if log[line].split('  ')[1].split(',')[10] == '"Спокойствие"':
                            if log[line].split('  ')[1].split(',')[0] == 'SPELL_AURA_APPLIED':
                                print('%s | Спокойствие CAST' % (shift_time(log[0].split(' ')[1], log[line].split(' ')[1]),))
                    except IndexError:
                        pass
            except KeyError:
                pass

    def track_mushrooms_explosions(self, pull_index, actor):
        self.parse_single_fight(pull_index, actor)
        log = open('tmp.txt', encoding='utf-8').readlines()
        lines = []
        explosions = []
        for line in log:
            if 'SPELL_HEAL' and '"Дикий гриб: лечение"' in line:
                if line.split('  ')[1].split(',')[0] == 'SPELL_HEAL':
                    i = []
                    for item in line.split(' '):
                        i.append(item)
                    lines.append(i)
        for k, line in groupby(lines, lambda x: x[1]):
            explosions.append(dict(date=k, data=list(l for l in line)))
        for e in explosions:
            print('MUSHROOM EXPLOSION @ %s' % (shift_time(log[0].split(' ')[1], e['date'])))
            print('TOTAL TARGETS FOR EXPLOSION : %s' % (len(e['data']),))
            total_mushroom = 0
            for unit in e['data']:
                target = unit[3].split(',')[6]
                total_heal = unit[5].split(',')[10]
                overheal = unit[5].split(',')[11]
                real_heal = int(total_heal) - int(overheal)
                total_mushroom = total_mushroom + real_heal
                print('%s HEALED FOR %s | %s overheal' % (target, real_heal, overheal))
            print('MUSHROOM TOTAL HEAL %s' % (total_mushroom,))
            print('-'*40)

    def cleave_tracker(self, pull_index, actor, show_all=False):
        self.parse_single_fight(pull_index, actor)
        log = open('tmp.txt', encoding='utf-8').readlines()
        cleaves = []
        data = []
        for line in log:
            if 'SPELL_HEAL' and '"Рассекающий удар"' in line:
                if line.split('  ')[1].split(',')[0] == 'SPELL_HEAL':
                    i = []
                    for item in line.split(' '):
                        i.append(item)
                    cleaves.append(i)
        for k, line in groupby(cleaves, lambda x: x[1]):
            data.append(dict(date=k, data=list(l for l in line)))
        healed = 0
        for item in data:
            total_cleave_heal = 0
            total_cleave_overheal = 0
            for unit in item['data']:
                try:
                    heal = unit[4].split(',')[10]
                    overheal = unit[4].split(',')[11]
                    real_heal = int(heal) - int(overheal)
                    total_cleave_heal = total_cleave_heal + int(real_heal)
                    total_cleave_overheal = total_cleave_overheal + int(overheal)
                except IndexError:
                    pass
            if show_all is True:
                if total_cleave_heal > 0:
                    healed = healed + 1
                print('CLEAVE @ %s | HEAL : %s | OVERHEAL : %s | TOTAL TARGETS : %s' % (shift_time(log[0].split(' ')[1], item['date']), total_cleave_heal, total_cleave_overheal, len(item['data'])))
            else:
                if total_cleave_heal > 0:
                    healed = healed + 1
                    print('CLEAVE @ %s | HEAL : %s | OVERHEAL : %s | TOTAL TARGETS : %s' % (shift_time(log[0].split(' ')[1], item['date']), total_cleave_heal, total_cleave_overheal, len(item['data'])))
        print('TOTAL PROCKS : %s | EFFECTIVE : %s' % (len(data), healed))

    def rejuvenation_tracker(self, pull_index, actor):
        self.parse_single_fight(pull_index, actor)
        log = open('tmp.txt', encoding='utf-8').readlines()
        rejuvenations_applied = {}
        for line in log:
            if '"Омоложение"' in line:
                if line.split('  ')[1].split(',')[0] == 'SPELL_AURA_APPLIED':
                    time = shift_time(log[0].split(' ')[1], line.split(' ')[1])
                    target = line.split('  ')[1].split(',')[6]
                    key = time+' '+target
                    rejuvenations_applied[key] = {'start': log.index(line), 'start_time': line.split(' ')[1]}
        for rj in rejuvenations_applied:
            target = rj.split(' ')[1]
            for line in range(rejuvenations_applied[rj]['start'], len(log)):
                try:
                    if 'SPELL_AURA_REMOVED' in log[line]:
                        if log[line].split('  ')[1].split(',')[10] == '"Омоложение"':
                            if log[line].split('  ')[1].split(',')[6] == target:
                                rejuvenations_applied[rj]['end'] = line
                                rejuvenations_applied[rj]['end_time'] = log[line].split(' ')[1]
                                break
                except IndexError:
                    pass
        for rj in rejuvenations_applied:
            ticks = []
            for line in range(rejuvenations_applied[rj]['start'], rejuvenations_applied[rj]['end']):
                if '"Омоложение"' in log[line]:
                    if log[line].split('  ')[1].split(',')[0] == 'SPELL_PERIODIC_HEAL':
                        if log[line].split('  ')[1].split(',')[6] == rj.split(' ')[1]:
                            heal = log[line].split('  ')[1].split(',')[20]
                            overheal = log[line].split('  ')[1].split(',')[21]
                            real_heal = int(heal) - int(overheal)
                            if log[line].split('  ')[1].split(',')[23] == 1:
                                critical = True
                            else:
                                critical = False
                            data = [real_heal, overheal, critical]
                            ticks.append(data)
            rejuvenations_applied[rj]['ticks'] = ticks
        for rj in rejuvenations_applied:
            print('%s REJUVENATION APPLIED @ %s' % (shift_time(log[0].split(' ')[1], rejuvenations_applied[rj]['start_time']), rj.split(' ')[1]))

            for item in enumerate(rejuvenations_applied[rj]['ticks']):
                print('TICK #%s | HEAL %s | OVERHEAL %s | CRITICAL %s' % (item[0], item[1][0], item[1][1], item[1][2]))
