def inverte_string(string):
    string_invertida = ''
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string_original = "roma"
string_invertida = inverte_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
