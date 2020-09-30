**WARNING: this repository is deprecated. If you are interested in using the Zinc Automatic Ordering API, please see zinc.io/docs.**



zinc-python
===========

A lightweight python library for e-commerce on Zinc.io. Full API documentation is available at [the Zinc docs page](https://zinc.io/docs).

Check out the OrderTester.py program's for some example usage. 

ZincClient Object
-----------------
    
    zinc.ZincClient(api_key,version=1,base='api.zinc.io',verify_https=True)
    - Create a new ZincClient instance
    ZincClient.create_order(order_dict)
    - Create a new ZincOrder from a dictionary.
    ZincClient.get_order(order_id)
    - Return a ZincOrder from the given order id
    ZincClient.get_orders(limit=None,offset=0)
    - Return a list of all known ZincOrder objects. Limit and offset default to Zinc API defaults.
    ZincClient.get_order_count()
    - Returns the count of all Zinc orders. For use with pagination in get_orders.
    ZincClient.get_order()
    - Returns a ZincUser object for the current user.

Zinc Wrapped Objects
--------------------

All of the JSON objects wrapped by the client library have a similar interface.

    Obj[key]
    - Returns the value of the named parameter in the wrapped dictionary.
    Obj.dict()
    - Returns the wrapped dictionary in raw form.
    Obj.update()
    - Updates the object from the server.

ZincOrder Object
----------------

A wrapped object representing an order. Besides the common methods shared by all wrapped objects:

    ZincOrder.cancel()
    - Returns a ZincCancellation object created by attempting to cancel the order.
    ZincOrder.get_cancellation()
    - Returns an existing ZincCancellation object (or throws an exception).

ZincCancellation Object
-----------------------

A wrapped object representing an order cancellation. Besides the common methods shared by all wrapped objects:

    ZincCancellation.get_order()
    - Returns the corresponding ZincOrder object.

Example Interactive Session
---------------------------

    >>> from zinc import ZincClient
    >>> zc = ZincClient(api_key='dev-f0fe73b8dc4e402696964abecb79dbce')
    >>> o = zc.create_order({
            "merchant": "amazon",
            "shipping_method": "standard",
            "products": [
                {
                    "pid": "0833030477",
                    "pid_type": "ASIN",
                    "qty": 1
                }
            ],
            "address": {
                "name": "Norman Borlaug",
                "address_line1": "77 Massachusetts Ave.",
                "zip_code": "02139",
                "city": "Cambridge",
                "state": "MA",
                "country": "US"
            }
        })
    >>> o
    ZincOrder({
        "_type": "order", 
        "address": {
            "_type": "address", 
            "address_line1": "77 Massachusetts Ave.", 
            "address_line2": null, 
            "city": "Cambridge", 
            "country": "US", 
            "name": "Norman Borlaug", 
            "state": "MA", 
            "zip_code": "02139"
        }, 
        "address_original": null, 
        "address_suggestion": null, 
        "address_suggestion_choice": "fail", 
        "created_date": 1356840773, 
        "delivery_date": null, 
        "delivery_date_estimate": null, 
        "fee": null, 
        "gift_ship": true, 
        "id": "64tzviy7qr", 
        "max_total": null, 
        "merchant": "amazon", 
        "mode": "dev", 
        "order_total": null, 
        "products": [
            {
                "_type": "product", 
                "pid": "0833030477", 
                "pid_type": "ASIN", 
                "qty": 1
            }
        ], 
        "ship_date": null, 
        "ship_date_estimate": null, 
        "shipping_cost": null, 
        "shipping_method": "standard", 
        "status": {
            "_type": "status", 
            "code": "pending", 
            "message": "Order has passed initial checks and has been queued for processing.", 
            "state": "active"
        }, 
        "tracking_number": null, 
        "tracking_type": null
    })
    >>> o.update()
    ZincOrder({
        "_type": "order", 
        "address": {
            "_type": "address", 
            "address_line1": "77 Massachusetts Ave.", 
            "address_line2": null, 
            "city": "Cambridge", 
            "country": "US", 
            "name": "Norman Borlaug", 
            "state": "MA", 
            "zip_code": "02139"
        }, 
        "address_original": null, 
        "address_suggestion": null, 
        "address_suggestion_choice": "fail", 
        "created_date": 1356840773, 
        "delivery_date": null, 
        "delivery_date_estimate": null, 
        "fee": null, 
        "gift_ship": true, 
        "id": "64tzviy7qr", 
        "max_total": null, 
        "merchant": "amazon", 
        "mode": "dev", 
        "order_total": null, 
        "products": [
            {
                "_type": "product", 
                "pid": "0833030477", 
                "pid_type": "ASIN", 
                "qty": 1
            }
        ], 
        "ship_date": null, 
        "ship_date_estimate": null, 
        "shipping_cost": null, 
        "shipping_method": "standard", 
        "status": {
            "_type": "status", 
            "code": "passed_tests", 
            "message": "The dev mode order is complete, and no immediate problems have been found.", 
            "state": "complete"
        }, 
        "tracking_number": null, 
        "tracking_type": null
    })
    >>> o2 = zc.get_order(o['id'])
    >>> o2 == o
    True
    >>> c = o.cancel()
    >>> c
    ZincCancellation({
        "_type": "cancellation", 
        "created_date": 1356840930, 
        "order_id": "64tzviy7qr", 
        "status": {
            "_type": "status", 
            "code": "pending", 
            "message": "Cancellation has been queued for processing. This usually begins in less than 60 seconds.", 
            "state": "active"
        }
    })
    >>> c.update()
    ZincCancellation({
        "_type": "cancellation", 
        "created_date": 1356840930, 
        "order_id": "64tzviy7qr", 
        "status": {
            "_type": "status", 
            "code": "passed_tests", 
            "message": "The dev mode cancellation is complete, and no immediate problems have been found.", 
            "state": "complete"
        }
    })
    >>> c2 = o.get_cancellation()
    >>> c2 == c
    True
