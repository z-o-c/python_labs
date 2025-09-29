def find_word(test):
    end = ""
    count_1 = 0
    count_2 = 0
    for i in test:
        count_1 += 1
        if i.isupper():
            end += i
            break
    
    for i in test:
        count_2 += 1
        if i.isdigit():
            break
    
    end += test[count_2::count_2 - count_1 + 1]
    return end

test = "thisisabracadabraHt1eadljjl12ojh."
print(find_word(test))