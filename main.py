Str = input()
first_word = Str[:Str.find(" ")]
second_word = Str[Str.find(" ")+1:]
print({second_word}, " ", "!", " ", {first_word})
