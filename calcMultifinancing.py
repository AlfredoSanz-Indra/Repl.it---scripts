def calcMonthlyFee() :
  theAmount = amount - initialPayment
  theAmount = theAmount - finalPayment
  result = theAmount / months

  print('MonthlyFee:' + str(result))
#


def calcRefiFinalpayment() :

  for month in refiFinalPaymentMonths:
    result = finalPayment / month

    print('Refi-> ' + str(month) + ': ' + str(result))
  #
#



amount = 789.23
months = 36
initialPayment = 150
finalPayment = 26.99
refiFinalPayment = True
refiFinalPaymentMonths = [12, 24]

print('totalAmount:' + str(amount))
print('months:' + str(months))
print('initialPayment:' + str(initialPayment))
print('finalPayment:' + str(finalPayment))


calcMonthlyFee()
if refiFinalPayment:
  calcRefiFinalpayment()
#