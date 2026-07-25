# Zinc API Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fzincio%2Fzinc-python)
[![pypi](https://img.shields.io/pypi/v/zinc)](https://pypi.python.org/pypi/zinc)

**`zinc`** is the official TypeScript SDK for the [Zinc API](https://www.zinc.com/docs) —
search, buy, track, and return products from major online retailers
(Amazon, Walmart, and more) through a single, type-safe API.

Keywords: e-commerce API, place an order, buy products programmatically,
Amazon ordering API, checkout automation, order tracking, returns,
product search, AI agent commerce, autonomous purchasing, MPP / HTTP 402.

Every method is fully typed. Instantiate `ZincClient` once and call
resource methods like `zinc.orders.createOrder(...)` or `zinc.search.search(...)`.


## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Environments](#environments)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install zinc
```

## Reference

A full reference for this library is available [here](https://github.com/zincio/zinc-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from zincio import ZincioApi, OrderProduct, Address

client = ZincioApi(
    api_key="<value>",
)

client.orders.create_order(
    products=[
        OrderProduct(
            url="https://www.amazon.com/dp/B07JGBW826",
        )
    ],
    shipping_address=Address(
        first_name="first_name",
        last_name="last_name",
        address_line1="address_line1",
        city="city",
        postal_code="postal_code",
        phone_number="phone_number",
    ),
    max_price=1,
)
```

## Environments

This SDK allows you to configure different environments for API requests.

```python
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    environment=ZincioApiEnvironment.PRODUCTION,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from zincio import AsyncZincioApi

client = AsyncZincioApi(
    api_key="<value>",
)


async def main() -> None:
    await client.orders.create_order(
        products=[
            OrderProduct(
                url="https://www.amazon.com/dp/B07JGBW826",
            )
        ],
        shipping_address=Address(
            first_name="first_name",
            last_name="last_name",
            address_line1="address_line1",
            city="city",
            postal_code="postal_code",
            phone_number="phone_number",
        ),
        max_price=1,
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from zincio.core.api_error import ApiError

try:
    client.orders.create_order(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from zincio import ZincioApi

client = ZincioApi(...)
response = client.orders.with_raw_response.create_order(...)
print(response.headers)  # access the response headers
print(response.status_code)  # access the response status code
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

Which status codes are retried depends on the `retryStatusCodes` generator configuration:

**`legacy`** (current default): retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#server_error_responses) (All server errors, including 500)

**`recommended`**: retries on
- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409) (Conflict)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [502](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502) (Bad Gateway)
- [503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) (Service Unavailable)
- [504](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/504) (Gateway Timeout)

Use the `max_retries` request option to configure this behavior.

```python
client.orders.create_order(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python
from zincio import ZincioApi

client = ZincioApi(..., timeout=20.0)

# Override timeout for a specific method
client.orders.create_order(..., request_options={
    "timeout": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from zincio import ZincioApi

client = ZincioApi(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
