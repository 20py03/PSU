with open('spam.txt', 'r') as file:
    ham_br = 0
    ham_sum = 0
    spam_br = 0
    spam_sum = 0
    excl_br = 0
    for line in file:
        type, message = line.split('\t')
        words = len(message.split())
        
        if type == 'ham':
            ham_br += 1
            ham_sum += words
        else:
            spam_br += 1
            spam_sum += words
            if message[-2] == '!': 
                excl_br += 1
    ham_av = ham_sum / ham_br
    spam_av = spam_sum / spam_br
    print()
    print('Prosjecan broj rijeci tipa ham: ',ham_av)
    print('Prosjecan broj rijeci tipa spam: ',spam_av)
    print('Broj spam poruka koje zavrsavaju usklicnikom: ',excl_br)
