# Zinc API Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fzincio%2Fzinc-python)
[![pypi](https://img.shields.io/pypi/v/zinc)](https://pypi.python.org/pypi/zinc)

**`zinc`** is the official SDK for the [Zinc API](https://www.zinc.com/docs) —
search, buy, track, and return products from major online retailers
(Amazon, Walmart, and more) through a single, type-safe API.

Keywords: e-commerce API, place an order, buy products programmatically,
Amazon ordering API, checkout automation, order tracking, returns,
product search, AI agent commerce, autonomous purchasing, MPP / HTTP 402.

Every method is fully typed. Instantiate `ZincClient` once and call resource
methods on it — placing an order, searching for a product, and tracking a
shipment are each a single call. (Method names follow each language's
convention: `createOrder` in TypeScript, `create_order` in Python.)


## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Authentication](#authentication)
- [Test Mode](#test-mode)
- [Faq](#faq)
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

## Authentication

Most endpoints require a Zinc API key (prefixed `zn_`), sent as the
`Authorization` header. The value is forwarded **verbatim**, so pass the
`Bearer ` prefix yourself:

```python
import os
from zinc import ZincClient

client = ZincClient(
    api_key=f"Bearer {os.environ['ZINC_API_KEY']}",  # "zn_..."
    # base_url defaults to https://api.zinc.com
)
```

The `client.agent.*` endpoints need **no Zinc account** — they are paid
per-call via MPP (HTTP 402), so an agent can order without one. They raise
`PaymentRequiredError` until payment is attached.


## Test mode

Use a **test API key** (`zn_test_...`) to hit the sandbox — same client,
same base URL; the key prefix routes you to test data:

```python
client = ZincClient(api_key=f"Bearer {os.environ['ZINC_TEST_KEY']}")
```

`client.orders.list_test_products()` returns product URLs that trigger
specific sandbox scenarios.


## FAQ

**Which version should I use?** The package version mirrors the Zinc
API version (CalVer, e.g. `2026.7.17` = API `2026-07-17`). Pin an exact
version or take the latest.

**Do I need an account to place orders as an agent?** No.
`client.agent.create_mpp_order(...)` settles payment via MPP (HTTP 402) —
no API key required.

**How is `max_price` interpreted?** In cents. It's a ceiling; the order
is not finalized above it.

**Where are the full API docs?** https://www.zinc.com/docs


## Usage

Instantiate and use the client with the following:

```python
from zinc import ZincClient, OrderProduct, Address

client = ZincClient(
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
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    environment=ZincClientEnvironment.PRODUCTION,
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from zinc import AsyncZincClient

client = AsyncZincClient(
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
from zinc.core.api_error import ApiError

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
from zinc import ZincClient

client = ZincClient(...)
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
from zinc import ZincClient

client = ZincClient(..., timeout=20.0)

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
from zinc import ZincClient

client = ZincClient(
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
