# Επικυρώνεται ότι ο αριθμός των κύβων θα είναι πάνω από 4 στην αρχή του παιχνιδιού
def validM(inp):
    M = int(inp)
    if (M >= 4):
        return M
    else:
        print('try again with an integer bigger than 3.')
# Επικυρώνεται ότι ο αριθμός των κύβων που μπορεί να πάρει ένας παίκτης θα είναι πάνω από 2 και μικρότερος από την αρχική στοίβα
def validK(inpK):
    K = int(inpK)
    if (K > 2) and (K < M):
        return K
    else:
        print(f'You need to insert an integer in the range of 3 to {M - 1}!')
#Αξιολόγηση του παίκτη MAX που είναι ο υπολογιστής, όπου αν δεν υπάρχουν κύβοι στο τραπέζι και είναι η σειρά του κερδιζει (+10), ενώ
# σε αντίθεση περίπτωση η στοίβα αξιολογείται με -10
def eval(state,player):
    if (state == 0):
        if (player == MAX):
            return +10
        else:
            return -10
    elif (state < 0):
        if (player == MAX):
            return -10
        else:
            return +10
#Κυρίως παιχνίδι. όπου ανάλογα τις επιλογές των παικτών κάνει καταμέτρηση των υπολειπόμενων κύβων και
# μετράει το score έτσι ώστε να γίνει και ανάλογη αξιολόγηση ΜΑΧ ΜΙΝ
def MinMax(state,player):
    if (state <=0):
        return [eval(state,player), 0]
    availChoice = []
    for i in range(len(choices)):
        score,move = MinMax(state-choices[i],player)
        availChoice.append(score)
    if player == MAX:
        score =max(availChoice)
        move = [i for i, value in enumerate(availChoice) if value == score]
        # for i, value in enumerate(availChoice):
        #     if value == score:
        return [score,move[0]]
    else:
        score = max(availChoice)
        move = [i for i, value in enumerate(availChoice) if value == score]
        # for i, value in enumerate(availChoice):
        #     if value == score:
        return [score,move[0]]
# Κλήση της συνάρτησης για την επίδειξη του νικητή
def endGame(remainingCubes,player):
    if (remainingCubes == 0):
        if (player == MAX):
            print('You lost')
        else:
            print('Congrats! You win!!')
    #return True
#Επικυρώνει ότι ο αριθμός κύβων που θα διαλέξει ο χρήστης είναι επιτρεπόμενος, εφόσον υπάρχουν κύβοι στο τραπέζι
def validInput(inpUser):
    userTurn = int(inpUser)
    if(userTurn in choices):
        if(M-userTurn >= 0):
            return userTurn
        else:
            print(f'There are no {userTurn} available cubes. Try to pick up less..')
    else:
        print(f'Wrong! Available options are: 1 or 2 or {K}: ')




#MAIN

print('There are M availiable cubes on the table. Both players are allowed to remove 1, 2 or K cubes at the same time. '
      'You will set the M & K variables.')
print ('The player who removes the last cube off the table will be the winner.')
#Τρόπος καταμέτρησης κατά τη διάρκεια του παιχνιδιού ώστε να βγεί η τελική αξιολόγηση
MAX = +1
MIN = -1
inp = input('Please insert an initial number of cubes (M) available on the table: ')
inpK = input('Please insert an integer K, 2 < K < M:')
M = validM(inp)
K = validK(inpK)
choices = [1,2,K]
print(f'The game begins with {M} cubes and each player can pick 1, 2 or {K}')
# Τρόπος επιλογής κύβων εως ότου αδειάσει το τραπέζι. Αφαιρούνται κάθε φορά από κάθε παικτη οι ανάλογοι κύβοι που έχει επιλέξει
# μέχρι να τελειώσει το παιχνίδι.
while M > 0:
    score, move = MinMax(M,MAX)
    M = M - choices[move]

    print(f'Pc chose to remove {choices[move]} off the table. Remaining cubes are {M}.')
    if ((endGame(M,MAX))):
        break
    else:
        inpUser = input(f'How many cubes would you like to pick up (1, 2 ή {K}): ')
        userTurn = validInput(inpUser)
        M = M - (userTurn)
        print(f'You chose to remove {userTurn} from the table. Remaining cubes are {M}.')
        if ((endGame(M, MIN))): break