# Testing zone
print('\nTesting zone\n')
tab = [1, 2, 3]
print()
print('\nEnd Testing zone\n')
# End Testing zone

bestOfTitles = ['brother in arms', 'bohemian rhapsody', 'stairway to heaven', 'riders on the storm', 'wish you were here']
print(bestOfTitles)
bestOfTitles.append('child in time')
bestOfTitles.append('again')
bestOfTitles.insert(2, 'hotel california')
bestOfTitles.insert(0, 'the sound of silence')
print(bestOfTitles)
print(bestOfTitles.index('hotel california'))

bestOfTitles.remove('hotel california')
# Alternative
# bestOfTitles.pop(bestOfTitles.index('hotel california'))

bestOfTitles[0] = 'enjoy the silence'
# Alternative
# bestOfTitles[bestOfTitles.index('the sound of silence')] = 'enjoy the silence'

print(bestOfTitles)

hitsToRead = bestOfTitles
hitsToRead.reverse()
print(hitsToRead)

# Note this is a solution to sort list to reverse quantity
hitsToRead.sort()
hitsToRead.reverse()
print(hitsToRead)

print(hitsToRead.pop(0))
print(hitsToRead.pop(0))
print(hitsToRead)

additionalSongs = ['nothing compares 2 u', 'wish you were here']
print(additionalSongs)
hitsToRead.reverse()
hitsToRead.extend(additionalSongs)
hitsToRead.reverse()
print(hitsToRead)
print('"wish you were here" been played:', hitsToRead.count('wish you were here'),
      'and "riders on the storm" been played:', hitsToRead.count('riders on the storm'))
hitsToRead.clear()
print(hitsToRead)
