currencies= {
    "Pound Sterling": 1, 
    "Euro": 1.2, 
    "US Dollar": 1.6, 
    "Japanese Yen": 200
    }

short_hand = {
    "GBP": "Pound Sterling",
    "EUR": "Euro",
    "USD": "US Dollar",
    "JPY": "Japanese Yen"
    }
    
c_type1 = raw_input("What Currency are you converting from? GBP/EUR/USD/JPY: ")

if c_type1 == "GBP" or "EUR" or "USD" or "JPY":
    "You entered %s" %(c_type1)
else:
    print c_type1, "is not a valid input"
    c_type1 = raw_input("Please enter a valid currency to convert from- GBP/EUR/USD/JPY: ")
    
c_type2 = raw_input("What Currency are you converting to? GBP/EUR/USD/JPY: ")

if c_type2 != "GBP" or "EUR" or "USD" or "JPY":
    "You entered %s" %(c_type1)
else:
    print c_type2, "is not a valid input"
    c_type2 = raw_input("Please enter a valid currency to convert to- GBP/EUR/USD/JPY: ")

def rate(c_type1, c_type2):
    if c_type1 == "GBP":
        print "exchange rate is", currencies["Pound Sterling"]
    if c_type1 == "EUR":
        print "exchange rate is", currencies["Euro"]
    if c_type1 == "USD":
        print "exchange rate is", currencies["US Dollar"]
    if c_type1 == "JPY":
        print "exchange rate is", currencies["Japanese Yen"]
    if c_type2 == "GBP":
        print "to", currencies["Pound Sterling"]
    if c_type2 == "EUR":
        print "to", currencies["Euro"]
    if c_type2 == "USD":
        print "to", currencies["US Dollar"]
    if c_type2 == "JPY":
        print "to", currencies["Japanese Yen"]

rate(c_type1, c_type2)

numb1 = float(raw_input("How much %s do you wish to convert? " %c_type1))

def conversion(fromCurr, toCurr, value):
    if fromCurr == "GBP":
        answer = value * float(currencies[short_hand[toCurr]])
        return answer
    elif toCurr == "GBP":
        answer = value / float(currencies[short_hand[fromCurr]])
    else:
        answer = value / float(currencies[short_hand[fromCurr]])
        answer = value * float(currencies[short_hand[toCurr]]) 
        return answer

print "%2.f %s is %2.f %s" %(numb1, short_hand[c_type1], conversion(c_type1, c_type2, numb1), short_hand[c_type2])
#[GBP]


# if var1 == pounds and var2 == dollars:
#     sumusd1 = var3 * 1.64
#     print("You will recieve, ", sumusd)
# elif something != somethingelse: 
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == pounds and var2 == euro:
#     sumeuro = var3 * 1.22
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == pounds and var2 == yen:
#     sumyen = var3 * 171.53
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[USD]
# if var1 == dollars and var2 == pounds:
#     sumpounds = var3 * 0.61
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == dollars and var2 == euro:
#     sumeuro = var3 * 0.74
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == dollars and var2 == yen:
#     sumyen = var3 * 104.16
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[EURO]
# if var1 == euro and var2 == dollars:
#     sumusd2 = var3 * 1.64
#     print("You will recieve, ", sumusd)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == euro and var2 == pounds:
#     sumpounds = var3 * 0.82
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == euro and var2 == yen:
#     sumyen = var3 * 141.24
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[YEN]
#     if var1 == yen and var2 == dollars:
#         sumusd3 = var3 * 0.0096
#     print("You will recieve, ", sumusd3)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == yen and var2 == euro:
#     sumeuro = var3 * 0.0071
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == yen and var2 == pounds:
#     sumpounds = var3 * 0.0058
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)