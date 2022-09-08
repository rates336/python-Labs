# Testing zone
print('\nTesting zone\n')
tax = (1, 2, 3, 'elo')
taxList = list(tax)
print(tax)
taxList.append(6)
# tax = taxList
tax2 = ('test', 'alfa')
tax = tax2
print(tax)
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
