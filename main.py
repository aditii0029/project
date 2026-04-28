with open('students.json','r') as f:
    print(f.read())
    
f.write('Existing Record of Students')
f.close()
print(f)

f.newlines()
f.write('New Updated Record of Students')

