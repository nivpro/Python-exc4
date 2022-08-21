''' Exercise #4. Computational Thinking and Programming.'''

#########################################
# Question 1 - do not delete this comment
#########################################
n = 1925874023 # Replace ??? with an integer of your choice.
# Write the rest of the code for question 1 below here.
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        break
if n%i==0:
    print(f'{n} is NOT a prime number')
else:
    print(f'{n} is a prime number')
    


#########################################
# Question 2 - do not delete this comment
#########################################
m = 4 # Replace ??? with an integer of your choice.
n = 9 # Replace ??? with an integer of your choice.
# Write the rest of the code for question 2 below here.
big = m
small = n
if n>m:
    # can we do it shorter? hint: min, max
    big = n
    small = m
    
total = 0
num_of_odds = 0
for num in range(small+1, big):
    if num%2==1:
        total += num
        num_of_odds += 1
if num_of_odds == 0: # we don't want to divide by zero
    print(float(total))
else:
    print(f"{total/num_of_odds}")


#########################################
# Question 3 - do not delete this comment
#########################################
p = 5 # Replace ??? with an integer of your choice.
# Write the rest of the code for question 3 below here.
for i in range(p,0,-1):
    for j in range(i):
        print(i, end='')
    print('')
# instead of all this we can just use:
for i in range(p,0,-1):
    print(f'{i}'*i)


#########################################
# Question 4 - do not delete this comment
#########################################
lst4 = [0, 5.4, 0, 7, 6, 8.1, 3, 6, 0, 3] # Replace ??? with a list of your choice.
# Write the rest of the code for question 4 below here.
new_list = []
for elem in lst4:
    if elem in new_list:
        continue
    new_list.append(elem)

print(f'New list is {new_list}')


#########################################
# Question 5 - do not delete this comment
#########################################
lst5 = ['hi', 'ho', 'ho', 'ho', 'no', 1, 1, 'do', 'you', 'copy'] # Replace ??? with a list of your choice.
# Write the rest of the code for question 5 below here.
repetition = False
for i in range(1,len(lst5)):
    if lst5[i]==lst5[i-1]:
        print(lst5[i])
        repetitions = True
if not repetitions:
    print('No repetitions were found!')
