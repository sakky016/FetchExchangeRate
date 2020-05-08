import requests
import sys

def Usage():
	print("<exec> <base> <currency>")
	print("<base> and <currency> can be INR, HKD, CAD, AUD, IDR, JPY, EUR, GBP etc.")


###############################################################################
# main
###############################################################################
if (len(sys.argv) != 3):
	Usage()
else:
	base = sys.argv[1]
	currency = sys.argv[2]
	res = requests.get("https://api.exchangeratesapi.io/latest", params = {"base" : base, "symbols" : currency})
	if (res.status_code != 200):
		print("ERROR: API request failed!")	
	else:
		jsonData = res.json()
		rate = jsonData["rates"][currency]
		date = jsonData["date"]
		print (f"1 {base} = {rate} {currency} as on {date}")
