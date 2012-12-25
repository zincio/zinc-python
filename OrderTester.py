import requests,json
import sys,argparse
import time,datetime
import logging

from zinc import ZincClient

order = {
    "address" : {
        "address_line2" : None,
        "city" : "Washington",
        "address_line1" : "1600 Pennsylvania Ave",
        "name" : "Barack Obama",
        "country" : "US",
        "state" : "DC",
        "zip_code" : "20500" 
    },
    "gift_ship" : True,
    "max_total" : 4500,
    "merchant" : "amazon_all",
    "mode" : "live",
    "products" : [
        {
            "pid_type" : "ASIN",
            "pid" : "B000PM96NA",
            "qty" : 1 
        }
    ],
    "shipping_method" : "standard"
}

parser = argparse.ArgumentParser(description='Zinc API test script')
parser.add_argument('-k','--key',dest='apikey',help='API key')
parser.add_argument('-v',dest='verbose',action='store_true',help='Output verbose debugging information')
parser.add_argument('--create-order',dest='create_order',action='store_true',help='Create a new order (object specified in python file) - wait until it finishes.')
parser.add_argument('--cancel-order',dest='cancel_order',help='Cancel the order with this ID - wait until it finishes.')
parser.add_argument('--get-order',dest='get_order',help='Print the order object with this ID.')
parser.add_argument('--get-last-order',dest='get_last_order',action='store_true',help='Print the most recent order object.')
parser.add_argument('--get-all-orders',dest='get_all_orders',action='store_true',help='Print all order objects')
parser.add_argument('--get-cancellation',dest='get_cancellation',help='Print the cancellation object with this order ID.')
parser.add_argument('--get-user',action='store_true',dest='get_user',help='Print the User object.')
parser.add_argument('--verify-https',action='store_true',dest='verify_https',help='Force HTTPS verification (off by default).')
parser.add_argument('--base-url',dest='base_url',default='api.zinc.io',help='Specify a base url (default api.zinc.io)')
args = parser.parse_args()

client = ZincClient(api_key=args.apikey,verify_https=args.verify_https,base=args.base_url)
if args.verbose:
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)

if args.get_user:
    print 'User object:'
    print client.get_user()
if args.create_order:
    print 'Creating an order...'
    client.create_order(order)
if args.cancel_order:
    print 'Cancelling an order...'
    client.get_order(args.cancel_order).cancel()
if args.get_last_order:
    print 'Last order:'
    print client.get_all_orders()[-1]
if args.get_all_orders:
    print 'All orders:'
    for p in client.get_all_orders():
        print p
if args.get_order:
    print 'Order object:'
    print client.get_order(args.get_order)
if args.get_cancellation:
    print 'Cancellation:'
    print client.get_order(args.get_cancellation).get_cancellation()


