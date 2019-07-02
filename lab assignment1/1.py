def Convert(tup,di):
    for a,b in tup:
        di.setdefault(a,[]).append(b)
    return di
#here taking static input list of tuples
tups=[('John',('Physics',80)),('Daniel',('Science',90)),('John',('Science',95)),
      ('Mark',('Maths',100)),('Daniel',('History',75)),('Mark',('Social',95))]
#sorting out the tuple before converting into dictionary
tups.sort(key=lambda elem:elem[1])

dictionary={}
#converting tuples into dictionary by calling the function
dictionary=Convert(tups,dictionary)
print(dictionary)
