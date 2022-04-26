import requests, json

todos = requests.get('http://jsonplaceholder.typicode.com/todos')

dataDict = todos.json()
print(len(dataDict), 'todos')
if len(dataDict) > 0:
    print('Keys:')
    for key in dataDict[1]:
        print('-', key, '({})'.format(type(key)))

    todos = str(json.dumps(dataDict[1], indent=4))
    print(str(json.dumps(dataDict[1], indent=4)))

Datalog = open('Datalog', 'w')
Datalog.write(todos)
Datalog.close()
