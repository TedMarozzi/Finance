#python -c 'import finance; finance.pv_ci()'

#Future value simple intrest
def fv_si():
   pv = float(input("Present value? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))
   fv_si = pv*(1+n*r)

   print("Your future value is: ")
   print(fv_si)
   return fv_si

#Present value simple intrest
def pv_si():

   fv = float(input("Future value? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))

   pv_si = fv/(1+n*r)

   print("Your present value was: ")
   print(pv_si)

   return pv_si

#Future value compound intrest
def fv_ci():

   pv = float(input("Present value? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))

   fv_ci = pv*(pow(1+r,n))
   print("Your compound intrest future value is: ")
   print(fv_ci)

   return fv_ci

#Present value compound intrest
def pv_ci():

   fv = float(input("Future value? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))

   pv_ci = fv/(pow(1+r,n))
   print("Your compound intrest present value was: ")
   print(pv_ci)

   return pv_ci

def pv_p():
   c = float(input("Cash flows? "))
   r = float(input("Rate per period? "))

   pv_p = c/r

   print("Your perpituity's present value is: ")
   print(pv_p)
   return pv_p

def pv_dp():
   c = float(input("Cash flows? "))
   r = float(input("Rate per period? "))    
   n = float(input("Time periods? "))

   pv_dp = (c/r)*(1/pow(1+r,n))

   print("Your deffered perpituity's present value is: ")
   print(pv_dp)
   return pv_dp

def pv_oa():
   c = float(input("Cash flows? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))

   pv_oa = c/r * (1-1/pow(1+r,n))

   print("Your ordinary annuity's present value is: ")
   print(pv_oa)

   return pv_oa


#Future value of an ordinary annuity
def fv_oa():

   #inputting data
   c = float(input("Cash flows? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))

   #formula for fv_oa
   fv_oa = (c/r)*(pow((1+r),n) - 1)

   print("Your ordinary annuity's future value is: ")
   print(fv_oa)

   return 
   
def pv_ad():
   c = float(input("Cash flows? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))

   pv_ad = c/r * (1-1/pow(1+r,n))(1+r)

   print("Your annuity due's present value is: ")
   print(pv_ad)
   
   return pv_ad