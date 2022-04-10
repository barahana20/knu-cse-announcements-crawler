from functional import seq
from collections import namedtuple

Transaction = namedtuple('Transaction', 'reason amount')
transactions = [
    Transaction('github', 7),
    Transaction('food', 10),
    Transaction('coffee', 5),
    Transaction('digitalocean', 5),
    Transaction('food', 5),
    Transaction('riotgames', 25),
    Transaction('food', 10),
    Transaction('amazon', 200),
    Transaction('paycheck', -1000)
]

food_cost_sum = seq(transactions)\
  .filter(lambda x: x.reason == 'food')\
  .map(lambda x: x.amount).for_each(lambda x: print(x))
  
sumup = seq(["123", "456", "789"]).reduce(lambda s, e: int(s) + int(e), 100)
'''
s, e -> "s e"

" 123 456 789"

''' 

print(sumup)
