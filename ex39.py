states ={
'Oregon' :'OR',
'Florida' :'FL' ,
'California' : 'CA' ,
'New York' :'NY',
'Michigan' :'MI'
}

cities ={
'CA' : 'San fransisco',
'MI' : 'Detroit' ,
'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR']='Portland'

print('_._.' *10)
print("NY states has :" ,cities['NY'])
print("OR states has :" ,cities['OR'])

print('_._.'*10)
print("Michigan has :" , cities[states['Michigan']])
print("Florida's has :",cities[states['Florida']] )

print('_._.'*10)
