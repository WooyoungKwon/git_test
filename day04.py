e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print(e2f['walrus'])

f2e = {v: k for k, v in e2f.items()}
print(f2e['chien'])

[print(key) for key in e2f.keys()]