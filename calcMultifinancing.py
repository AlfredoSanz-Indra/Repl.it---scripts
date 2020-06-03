def calcMonthlyFee() :
  theAmount = amount - initialPayment
  theAmount = theAmount - finalPayment
  result = theAmount / months

  print('--------------------------')
  print('MonthlyFee:' + str(round(result, 4)))
  print('--------------------------')
#


def calcRefiFinalpayment() :

  print('--------------------------')
  for month in refiFinalPaymentMonths:
    result = finalPayment / month
    print('Refi-> ' + str(month) + ': ' + str(round(result, 4)))
  #
  print('--------------------------')
#

amount = 800.0
months = 36
initialPayment = 210.0
finalPayment = 200
refiFinalPayment = True
refiFinalPaymentMonths = [6]

print('totalAmount:' + str(amount))
print('months:' + str(months))
print('initialPayment:' + str(initialPayment))
print('finalPayment:' + str(finalPayment))

calcMonthlyFee()
print('*                        *')

if refiFinalPayment:
  print('refiFinalPaymentMonths: ' + repr(refiFinalPaymentMonths))  
  calcRefiFinalpayment()
#