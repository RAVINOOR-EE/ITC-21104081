# ASSIGNMENT 4                                       - BY RAVINOOR (21104081) , EE

# QUESTION 1 :
def hanoi(n, fro, to , aux) :
    if n == 0 :
        return

    hanoi(n-1, fro, aux, to)
    print(f"Move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)

# FOR 3 DISKS
hanoi(3, 'A', 'C', 'B')


# QUESTION 2 :

# FOR NUMBER OF ROWS
n = int(input("PLEASE ENTER NUMBER OF ROWS IN PASCAL'S TRIANGLE : \n"))

# USING RECURSIONS
print("USING RECURSIONS : \n")
def PASCAL(n, originaln=n) :
    if n == 0 :
        return

    PASCAL(n-1, originaln)

    # FOR SPACES
    print(' '*(originaln-n), end='')

    # FRIST NUMBER IS 1
    ENTRY = 1
    for i in range(1, n+1) :
        print(ENTRY, end='  ')

        # USING BINOMIAL COEFFICIENT
        ENTRY = ENTRY * ( n - i) // i
    print()
PASCAL(n)

# USING LOOP
print("\n USING LOOPS : \n")
for LINE in range(1, n+1) :

    print(' '*(n - LINE), end='')

    x = 1
    for i in range(1, LINE+1) :

        print(x, end='  ')
        x = x * (LINE - i ) // i
    print()


# QUESTION 3 :
INP_1 = int(input('PLEASE ENTER FIRST INTEGER : '))
INP_2 = int(input('PLESE ENTER SECOND INTEGER : '))

C = INP_1 % INP_2         # C - REMAINDER
D = INP_1 // INP_2        # D - QUOTIUENT

print("THE REMAINDER IS: ", C )
print("THE QUOTIENT IS: ", D )

if (C!=0) :
    if (D!=0) :
        print("BOTH OF THE VALUES ARE NON ZERO")
    else:
        print(" ONE OF THE VALUES IS ZERO")

else:
    if (D!=0) :
        print(" ONE OF THE VALUES IS ZERO")
    else:
        print("BOTH OF THE VALUES ARE NON ZERO")

SET_1 = set()
for i in range (4,7) :
    A = C + i
    B = D + i
    if(A>4) :
        SET_1.add(A)
        print(SET_1)
    if(B>4) :
        SET_1.add(B)
        print(SET_1)

print(SET_1)
SET_2 = frozenset(SET_1)
print("IMMUTABLE SET : ", SET_2)
print("LARGEST VALUE IN THE SET: ", max(SET_2))
K = max(SET_2)
print("HASH VALUE: ", hash(K))


# CODE FOR QUESTION 4 :

class STUDENT :
    def __init__(self, STUDENT, S_ID):
        self.NAME = STUDENT
        self.S_ID = S_ID

    def __del__(self):
        print("OBJECT DESTROYED..")

# CREATING OBJECT
STUDENT_1 = STUDENT("RAVINOOR", 21104081)
print("OBJECT CREATED.")

# PRINTING THE ASSIGNED VALUES
print(f"THE NAME OF THE STUDENT IT {STUDENT_1.NAME} AND S_ID IS {STUDENT_1.S_ID}.")

# DELETING OBJECT
del STUDENT_1


# CODE FOR QUESTION 5 :

class EMPLOYEE :
    def __init__(self, NAME, SALARY):
        self.NAME = NAME
        self.SALARY = SALARY

    def __del__(self):
        print(f"EMPLOYEE {self.NAME} RECORD DELETED.")

# CREATING EMPLOYEE RECORDS
EMPLOYEE_1 = EMPLOYEE("MEHAK", 40000)
EMPLOYEE_2 = EMPLOYEE("ASHOK", 50000)
EMPLOYEE_3 = EMPLOYEE("VIREN", 60000)

# A-> UPDATING SAALARY
EMPLOYEE_1.SALARY = 70000
print(f"A) THE UPDATED SALARY OF THE EMPLOYEE {EMPLOYEE_1.NAME} IS {EMPLOYEE_1.SALARY}")

# B-> DELETING A RECORD
print("B)", end=' ')
del EMPLOYEE_3


# CODE FOR QUESTION 6 :

# WORD FROM FIRST FRIEND :-
WORD = input("ENTER THE FIRST WORD :\n")

# A MEANINGFUL WORD WITH SAME EXACT LETTERS :-
NEW_WORD = input("\n ENTER A MEANINGFUL WORD FROM LETTERS OF FIRST :\n")

# DEFINING DICTIONARY
def COUNT_IN_DICT(WORD) :
    COUNT = {}
    LIST_1 = list(WORD)

    LENGTH = len(LIST_1)
    for i in range(LENGTH):
        if LIST_1[i] in COUNT :
            COUNT[LIST_1[i]] += 1
        else:
            COUNT[LIST_1[i]] = 1
    return COUNT

# NOW TO VERIFY LETTERS OF NEW WORD
if COUNT_IN_DICT(WORD) != COUNT_IN_DICT(NEW_WORD) :
    print("THE LETTERS AREN'T EXACT, FRIENDSHIP IS FAKE.....")

# FOR SHOPKEEPER TO CHECK MEANING OF NEW WORD
def USER_INPUT() :
    ANS = input("\nDOES THE WORD HAVE MEANING ?(Y OR N), USE UPPER CASE LETTERS\n")

    if ANS == 'Y'  :
        print("THE FRIENDS PASS THE FRIENDSHIP TEST.. \n ")
    elif ANS == 'N'  :
        print("THE WORD DON'T HAVE A MEANING, FRIENDSHIP IS FAKE...")
    else:
        print("INVALID INPUT.., TRY AGAIN,,")
        USER_INPUT()
USER_INPUT()

# ASSIGNMENT OVER

#                                     - BY RAVINOOR (21104081) , EE