def character_count(word):
  word = word.lower()
  charater_statistic = {}

  for charater in word:
    if charater in charater_statistic:
      charater_statistic[charater] += 1
    else:
      charater_statistic[charater] = 1


  return charater_statistic
assert character_count('hello') == {'h':1, 'e':1, 'l':2, 'o':1}
print(character_count('Smiles'))