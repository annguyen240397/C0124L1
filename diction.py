tu_dien = {
    'ten' : 'Nguyen Thien An',
    'tuoi': 26,
    'can_nang': 52
}
print(tu_dien['ten'])
print(tu_dien['tuoi'])
print(tu_dien.get('ten'))
tu_dien.update({'so_thich':'da banh'})
print(tu_dien['so_thich'])
tu_dien.pop('ten')
print(tu_dien)
tu_dien['can_nang'] = 50
print(tu_dien)