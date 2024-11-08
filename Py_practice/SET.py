numbers = [1, 2, 6, 3, 1, 1, 5] 

unique_nums = set(numbers)
print(unique_nums)


artist = {'Chagall', 'Kandinskij', 'Dalí', 'da Vinci', 'Picasso', 'Warhol', 'Basquiat'}

print('Turner' in artist) # check if there is Turner in the set artist
artist.add('Turner')
print(artist.pop()) #remove the last item
