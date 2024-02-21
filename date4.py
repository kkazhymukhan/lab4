import datetime
x=datetime.datetime(2018 , 6 , 1)
y=datetime.datetime(2018 , 6 , 2)
z=x-y
sum=z.day*86400+z.month*2419200+z.year*2419200*12

print(sum)