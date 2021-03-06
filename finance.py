import sympy as sp
import math

sp.init_printing()
x,eq_to_solve,output,fv,pv,c,r,g,n,m = sp.symbols('x,eq_to_solve,output,fv,pv,c,r,g,n,m')
ls = sp.Function('ls')
rs = sp.Function('rs')

#Future value simple intrest
def fv_si(pv, r, n):

   fv_si = pv*(1+n*r)

   return fv_si


#Present value simple intrest
def pv_si(fv, r, n):

   pv_si = fv/(1+n*r)

   return pv_si
   

#Future value compound intrest
def fv_ci(pv, r, n):

   fv_ci = pv*(pow(1+r,n))

   return fv_ci

#Present value compound intrest
def pv_ci(fv, r, n):

   pv_ci = fv/(pow(1+r,n))

   return pv_ci

def pv_p(c, r):

   pv_p = c/r

   return pv_p

def pv_dp(c,r,n):

   pv_dp = (c/r)*(1/pow(1+r,n))

   return pv_dp

#works
def pv_oa(c,r,n):

   pv_oa = c/r * (1-1/pow(1+r,n))

   return pv_oa


#Future value of an ordinary annuity
def fv_oa(c,r,n):

   fv_oa = (c/r)*(pow((1+r),n) - 1)

   return fv_oa
   
def pv_ad(c,r,n):

   pv_ad = c/r * (1-1/pow(1+r,n))*(1+r)

   return pv_ad

def fv_ad(c,r,n):

   fv_ad = (c/r)*(pow(1+r,n)-1)*(1+r)

   return fv_ad

def pv_gp(c,r,g):

   pv_gp = c/(r-g)

   return pv_gp

def pv_goa(c, r, g, n):
   
   if(g==x or r == x):
      print("Sorry if I take a while to solve its really hard")

   pv_goa = (c/(r-g))*(1-pow((1+g)/(1+r),n))

   return pv_goa

def fv_goa(c, r, g, n):

   if(g==x or r == x):
      print("Sorry if I take a while to solve this one its really hard for me...")

   fv_goa = (c/(r-g))*(1-pow((1+g)/(1+r),n))*pow(1+r,n)

   return fv_goa

#used when the cash flows don't match the compounding
def rate_per_cash_flows(rate_per_year, compounds_per_year, cash_flows_per_year):

   rate_per_cash_flows = pow(1+rate_per_year/compounds_per_year, compounds_per_year/cash_flows_per_year)-1

   return rate_per_cash_flows

#Effective intrest continous compounding
#used when the cash flows don't match the compounding
def re_c(r):

   re = pow(math.e, r) - 1

   return re

def pv_cb(c, fv, rd, n):

   pv_cb = (c/rd)*(1-1/pow(1+rd,n))+fv/pow(1+rd,n)

   return pv_cb

def pv_ds(fv, rd, n):
   
   return fv/(1+(n/365)*rd)

def pe_leading(payout_ratio, re, g):
   return payout_ratio/(re-g)


def pe_trailing(payout_ratio, re, g):
   return (payout_ratio*(1+g))/(re-g)

#pv_pn is the value of dividend before it has grown const
def pv_pn(dn_plus_one, re, g):
   return dn_plus_one/(re  - g)



#works
def solver(ls, rs):
   
   eq_to_solve = sp.Eq(ls, rs)

   output = sp.solve(eq_to_solve,x)
   #try:
   print("x = ", float(output[0]))
   print("and to two decimal places x = ", round(float(output[0]),2))
   #except:
   #   print("I don't know how to do this yet :(")



print("""
   Functions avaliable:
   fv_si(pv, r, n)
   pv_si(fv, r, n)
   pv_ci(fv, r, n)
   pv_p(c, r)
   pv_dp(c,r,n)
   pv_oa(c,r,n)
   fv_oa(c,r,n)
   pv_ad(c,r,n)
   pv_gp(c,r,g)
   pv_goa(c, r, g, n)
   fv_goa(c, r, g, n)
   rate_per_cash_flows(rate_per_year, compounds_per_year, cash_flows_per_year)
   re_c(r)
   """)


ls = eval(input("left side of equation? "))
rs = eval(input("right side of equation? "))

solver(ls,rs)

