def calcMonthlyFee() :
  theAmount = amount - initialPayment
  theAmount = theAmount - finalPayment
  result = theAmount / months

  print('--------------------------')
  print('MonthlyFee:' + str(round(result, 2)))
  print('--------------------------')
#


def calcRefiFinalpayment() :

  print('--------------------------')
  for month in refiFinalPaymentMonths:
    result = finalPayment / month
    print('Refi-> ' + str(month) + ': ' + str(round(result, 2)))
  #
  print('--------------------------')
#

amount = 450.1
months = 60
initialPayment = 100.0
finalPayment = 100.0
refiFinalPayment = True
refiFinalPaymentMonths = [6, 12]

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