n = int(input('enter no of student:'))
total_percentage=0
for i in range(1, n+1):
    print(i)

    m1 = int(input('enter no of student 1:'))
    m2 = int(input('enter no of student 2:'))
    m3 = int(input('enter no of student 3:'))
    m4 = int(input('enter no of student 4:'))
    m5 = int(input('enter no of student 5:'))

    total=m1+m2+m3+m4+m5
    percentage = (total/500)*100
    print(percentage)
    total_percentage=total_percentage+1

avrage_percentage = total_percentage/n
print(avrage_percentage)
