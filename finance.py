def fv_si():
   pv = float(input("Present value? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))
   fv_si = pv*(1+n*r)

   print("Your future value is: ")
   print(fv_si)
   return fv_si

def pv_si():

   fv = float(input("Future value? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))

   pv_si = fv/(1+n*r)


   print("Your present value is: ")
   print(pv_si)

   return pv_si


def fv_ci():

   pv = float(input("Present value? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))


   fv_ci = pv*(pow(1+r,n))
   print("Your compound intrest future value is: ")
   print(fv_ci)

   return fv_ci



def fv_oa():

   #inputting d
   # ata
   c = float(input("Cash flows? "))
   r = float(input("Rate per period? "))
   n = float(input("Time periods? "))


   #formula for
   #  fv_oa
   fv_oa = (c/r)*(pow((1+r),n) - 1)


   print("Your ordinary annuity's future value is: ")
   print(fv_oa)

   return fv_oa




