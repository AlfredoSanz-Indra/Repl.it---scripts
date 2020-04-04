def calcMonthlyies() :
  theAmount = amount - initialPayment
  theAmount = theAmount - finalPayment
  result = theAmount / months

  return result
#



amount = 100.23
months = 36
initialPayment = 10
finalPayment = 26.99

print('Monthly=' + str(calcMonthlyies()))
