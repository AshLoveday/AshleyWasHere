TAXRATE = 0.06

def calcSalesTax(x):
    salesTax = x * 0.06
    return round(salesTax, 2)

def calcTotal(x):
    salesTax = x * 0.06
    total = salesTax + x
    return round(total, 2)

# the main() function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    for price in range( 20, 100, 250):
        print("Tax on", price, "is", calcSalesTax(price), "and total is", calcTotal(price))
# if this module is the main module, call the main() function
# to test the other functions
if __name__ == "__main__":
    main()
