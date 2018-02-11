country = {'Ukraine':'ua', 'France' : 'fr','Spain' : 'es', 'Belarus' : 'be', 'Russia' :'ru'}
city = {'ua' : 'Kyiv', 'fr' : "Paris", 'es' : 'Madrid', 'be' : 'Minsk', 'ru' :'Moscow'}
for state, domain in country.items():
    print(state, city[domain])

#def halve_evens_only(nums):
 #     return [i/2 for i in nums if not i % 2] #має повертати лише парні int