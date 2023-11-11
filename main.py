import random
words = ['вес', 'оранжевый', 'освободить', 'здание', 'пообещать', 'отвернуться', 'чеченский', 'взаимный', 'яркий', 'рисовать']
def game (word, tr, res):
    for i in range(len(word)):
        if word[i] == tr:
            res[i] = tr
    return res

def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \\
        |
        |  DEAD!

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]

def start():
    print('Давай поиграем в виселицу. Я загадал слово, а ты попробуешь его угадать.')
    print('Я загадал, попробуй угадать букву')
    word = []
    word.extend(random.choice(words))
    res = ['_' for i in range(len(word))]
    answer = ''.join(word)
    trys=[]
    dead = 6
    while res != word and dead >= 0:
        counter = res.count('_')
        attempt = input()
        while attempt in trys:
            print('Вы уже пробовали эту букву, выберите другую')
            attempt = input()
        trys.append(attempt)
        res = game(word, attempt, res)
        if counter == res.count('_'):
            print(f'Не угадал, попробуй еще раз. Осталось {dead} попыток')
            print(display_hangman(dead))
            dead -= 1
        else:
            print('Вот, где эта буква в слове')
            print(*res)
    else:
        if res == word:
            print(f'Ты выиграл, загаданное слово {answer}')
        else:
            print(f'Ты не угадал, загаданным словом было {answer}')
start()