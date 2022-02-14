# ASSIGNMENT 3                                                -> BY RAVINOOR (21104081), EE

# CODE FOR QUESTION 1
INPUT = str(input('PLEASE TYPE YOUR STRING :\n').lower())
LIST = INPUT.split()  # CONVERTING STRING WORDS TO A LIST
DICT = dict()         # DEFINING AN EMPTY DICTIONARY
if len(LIST) > 1 :
    for ELEMENTS in LIST :
        if ELEMENTS in DICT :
            DICT[ELEMENTS] +=1      # ADDING 1 FOR A SINGLE REPETITION
        else:
            DICT[ELEMENTS] = 1
    print("WORD COUNT OF YOUR STRING IS\n",DICT)
elif len(LIST) == 1:
    LETTERS_LIST = list(INPUT)       # CONVERTING THE LETTER OF SINGLE WORD INTO LIST
    for LETTERS in LETTERS_LIST :
        if LETTERS in DICT :
            DICT[LETTERS] +=1        # SAME PROCESS
        else:
            DICT[LETTERS] = 1
    print("LETTER COUNT OF YOUR WORD IS\n",DICT)



# CODE FOR QUESTION 2
DATE = int(input('TYPE DATE [1-31] :'))
MONTH = int(input('TYPE MONTH [1-12] :'))
YEAR = int(input('TYPE YEAR [1800-2025] :'))

# CONDITIONS APPLIED FOR LEAP YEAR :
if (YEAR % 400 == 0):
    LEAP_YEAR = True
elif (YEAR % 100 == 0):
    LEAP_YEAR = False
elif (YEAR % 4 == 0):
    LEAP_YEAR = True
else:
    LEAP_YEAR = False

if 1800<=YEAR<=2025 :                # APPLIED BOUNDARIES ON YEAR
    # DEFINING MONTH LENGTHS
    global MONTH_LENGTH
    if MONTH ==2 :
        if LEAP_YEAR :
            MONTH_LENGTH = 29
        else:
            MONTH_LENGTH = 28
    elif MONTH in (1,3,5,7,8,10,12) :
        MONTH_LENGTH = 31
    elif MONTH in (4,6,9,11) :
        MONTH_LENGTH = 30
    else:
        print("ERROR")

    # NOW FOR NEXT DATES OF INPUT
    global NEW_DATE                   #
    global NEW_MONTH                  # MAKING ALL LOCAL VARIABLES GLOBAL
    global NEW_YEAR                   #
    if DATE < MONTH_LENGTH :
        NEW_DATE = DATE + 1
        NEW_MONTH = MONTH
        NEW_YEAR = YEAR
    elif DATE == MONTH_LENGTH :
        if MONTH == 12 :
            NEW_DATE = 1
            NEW_MONTH = 1
            NEW_YEAR = YEAR + 1
        else:
            NEW_DATE = 1
            NEW_MONTH = MONTH + 1
            NEW_YEAR = YEAR
    else:
        print("ERROR")
    print("NEXT DATE OF THE INPUT DATE IS :\n",NEW_DATE,"/",NEW_MONTH,"/",NEW_YEAR)
else:
    print("ERROR")        # FOR YEAR GOING OUT OF RANGE GIVEN



# CODE FOR QUESTION 3
USER_LIST = []                      # DEFINING EMPTY LIST
LIST_SIZE = int(input('ENTER THE TOTAL (NUMBERS/TUPLES) YOU WANT IN LIST :\n'))
for NUMBER in range(0,LIST_SIZE) :                     # LOOP FOR TAKING ALL NUMBERS FROM USER
    print("ENTER NUMBER ",NUMBER + 1," :")
    INP_ = float(input())
    USER_LIST.append(INP_)                          # FILLING ELEMENTS IN EMPTY LIST
print("USER LIST IS :",USER_LIST)
OUTPUT_LIST = [(VALUE , VALUE**2) for VALUE in USER_LIST]
print("FINAL LIST IS :\n", OUTPUT_LIST)



# CODE FOR QUESTION 4
GRADE_OF_USER = int(input('PLEASE TYPE YOUR GRADE POINTS :\n'))
if GRADE_OF_USER == 4 :
    print("YOUR GRADE IS 'D' AND PERFORMANCE IS POOR.")
elif GRADE_OF_USER == 5 :
    print("YOUR GRADE IS 'C' AND PERFORMANCE IS BELOW AVERAGE.")
elif GRADE_OF_USER == 6 :
    print("YOUR GRADE IS 'C+' AND PERFORMANCE IS AVERAGE.")
elif GRADE_OF_USER == 7 :
    print("YOUR GRADE IS 'B' AND PERFORMANCE IS GOOD.")
elif GRADE_OF_USER == 8 :
    print("YOUR GRADE IS 'B+' AND PERFORMANCE IS VERY GOOD.")
elif GRADE_OF_USER == 9 :
    print("YOUR GRADE IS 'A' AND PERFORMANCE IS EXCELLENT.")
elif GRADE_OF_USER == 10 :
    print("YOUR GRADE IS 'A+' AND PERFORMANCE IS OUTSTANDING.")
else:
    print("ERROR")



# CODE FOR QUESTION 5
GIVEN_STRING = "ABCDEFGHIJK"
ROWS = 0
while ROWS < 6 :
    COLUMN_LENGTH = len(GIVEN_STRING)
    print(GIVEN_STRING[0:COLUMN_LENGTH])
    COLUMN_LENGTH = COLUMN_LENGTH - 2
    GIVEN_STRING = " " + GIVEN_STRING[0:COLUMN_LENGTH]
    ROWS = ROWS + 1



# CODE FOR QUESTION 6
S_ID = int(input('ENTER S_ID OF STUDENT : '))
NAME = input('ENTER NAME OF STUDENT : ')
DICT = {S_ID:NAME}    # S_ID-> KEYS , NAME-> VALUES

while True :
    OPTION = input('DO YOU WANT TO ENTER ANOTHER STUDENT ENTRY (Y OR N) : ').upper()
    if OPTION == 'Y' :
        S_ID = int(input('ENTER S_ID OF STUDENT : '))
        NAME = input('ENTER NAME OF STUDENT : ')
        DICT[S_ID] = NAME
    elif OPTION == 'N' :
        break
    else:
        print('ERROR!!, PLEASE ONLY TYPE Y/N')

# PART (A)
print("DICTIONARY ACCORDING TO INPUT : ")
print("A->", DICT)

# PART (B)
print("DICTIONARY WITH SORTED NAMES : ")
print("B->", {H:M for H,M in sorted(DICT.items(), key = lambda x:x[1])})

# PART (C)
print("DICTIONARY WITH SORTED S_ID : ")
print("C->", {H:M for H,M in sorted(DICT.items())})

# PART (D)
print("SEARCH WITH S_ID")
S_ID = int(input('SEARCH NAME THROUGH SID : \n'))
print("D->",DICT[S_ID])



#  CODE FOR QUESTION 7
def REC_FIBO(n) :
    if n <= 1 :
        return n
    else:
        return( REC_FIBO(n-1) + REC_FIBO(n-2))

NO_OF_TERMS = int(input('TYPE NUMBER OF TERMS IN THE SERIES : '))
if NO_OF_TERMS <= 0 :
    print("ERROR")
else:
    print("FIBONACCI SEQUENCE :")
    SUM = 0
    for i in range(NO_OF_TERMS):
        print(REC_FIBO(i))
        SUM = SUM + REC_FIBO(i)
    AVG = float(SUM / NO_OF_TERMS)
    print(" AVEREAGE OF RESULTANT FIBONACCI SERIES IS :\n", AVG)



# CODE FOR QUESTION 8
SET_1 = { 1,2,3,4,5}
SET_2 = { 2,4,6,8}
SET_3 = { 1,5,9,13,17}

# PART (A)
UNION = SET_1.union(SET_2)
INTERSECTION = SET_1.intersection(SET_2)
PART_A = UNION - INTERSECTION
print("A=> ",PART_A)

# PART (B)
PART_B = SET_1.union(SET_2.union(SET_3)) - SET_1.intersection(SET_2) - SET_2.intersection(SET_3) - SET_3.intersection(SET_1)
print("B=> ",PART_B)

# PART (C)
PART_C = ((SET_1.intersection(SET_2)).union((SET_1.intersection(SET_3)).union(SET_2.intersection(SET_3)))) - (SET_1.intersection(SET_2.intersection(SET_3)))
print("C=> ",PART_C)

# PART (D)
PART_D = set()
for i in range (1,11) :
    if i not in SET_1 :
        PART_D.add(i)
print("D=> ", PART_D)

# PART (E)
PART_E = set()
for i in range(1,11) :
    if i not in SET_1 and i not in SET_2 and i not in SET_3 :
        PART_E.add(i)
print("E=> ", PART_E)



# ASSIGNMENT 3                                   -> BY RAVINOOR(21104081) , EE











