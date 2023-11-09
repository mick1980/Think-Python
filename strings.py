f_dict = open('words.txt')

def find_triple_double_letter(w):
    i = len(w)-5
    j = 0
    while j < i:
        if w[j] == w[j+1] and w[j+2] == w[j+3] and w[j+4] == w[j+5]:
            print(w)
        j = j+1
    
for line in f_dict:
    word = line.strip()
    find_triple_double_letter(word)
    
