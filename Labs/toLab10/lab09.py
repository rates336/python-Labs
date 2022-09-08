# Testing zone
print('\nTesting zone\n')
countryCodes ={'PL' : 'Poland', 'DE' : 'Germany', 'FR' : 'France', 'US' : 'USA'}
print(countryCodes.get('RU'))
countryCodes.setdefault('UK')
print(countryCodes.get('PL'), countryCodes.get('UK'), sep='\t')
print(countryCodes.get('RU'))
print(countryCodes.setdefault('UA', 'Ukraine'))
print(countryCodes.get('UA'))
print(countryCodes.setdefault('UA', 'Ukraine test'))
print('\nEnd Testing zone\n')
# End Testing zone

marketingList = ['loyalty program', 'client promotion', 'market research']
marketingList.append('public relations')
print(marketingList[3])
marketingList.insert(2, 'investor relations')
print(marketingList)
emailMarketingList = marketingList.copy()
emailMarketingList.sort()
print(emailMarketingList)

internalEmails = ['internal communication']
emailMarketingList.extend(internalEmails)
print(emailMarketingList)

tupleEmails = (emailMarketingList.copy())
print(tupleEmails)

# Note
# a method to dictionary (dict)  print( dictName .setdefault(key, value) is checking that key has value
# if not setting, a default value in other case showing currently value

# Note 2
# a method to dictionary (dict) dictName .update(dict) is extends of currently dictionary
# about keys and value from dictionary indicated in brackets

marketingChannels = {'Google' : 1480, 'Email' : 300, 'Natural traffic' : 440, 'TV Spot' : 700}
print('Email result:', marketingChannels.get('Email'))
currentResultsChannels = {'Natural traffic' : 520, 'News' : 600}
marketingChannels.update(currentResultsChannels)
print(marketingChannels.keys())
print(marketingChannels.values())


marketingChannels.pop('Email')
print(marketingChannels.items())
