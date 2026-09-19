# Reference
## Orders
<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">validate_bulk_upload</a>(...) -> BulkValidateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Dry-run a CSV upload: validate every row and report estimated spend.

No orders are placed. Use this to show the confirmation preview before
calling POST /orders/bulk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.validate_bulk_upload()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BulkUploadRequest` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">list_bulk_uploads</a>(...) -> BulkBatchListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the current user's bulk-upload batches, newest first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.list_bulk_uploads()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">create_bulk_upload</a>(...) -> BulkBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a bulk-upload batch and place its rows asynchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.create_bulk_upload()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BulkUploadRequest` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">get_bulk_upload</a>(...) -> BulkBatchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a batch with per-row results and live order statuses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.get_bulk_upload(
    batch_id="batch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">download_bulk_results</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the batch results as a CSV (status + echoed custom columns).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.download_bulk_results(
    batch_id="batch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">list_orders</a>(...) -> OrderListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of orders for the current user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.list_orders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of orders to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of orders to skip
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `typing.Optional[str]` — Filter by order ID (partial match)
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Partial match on order ID OR tracking number
    
</dd>
</dl>

<dl>
<dd>

**merchant_order_id:** `typing.Optional[str]` — Filter by the retailer's own order number (e.g. an Amazon `113-…` ID), matched exactly against any of the order's order-placing jobs. Exact, not partial — dashes in the term are matched both as typed and stripped.
    
</dd>
</dl>

<dl>
<dd>

**status_filter:** `typing.Optional[str]` — Filter by order status
    
</dd>
</dl>

<dl>
<dd>

**tracking_status:** `typing.Optional[str]` — Filter to orders having at least one tracking number with this status
    
</dd>
</dl>

<dl>
<dd>

**has_tracking:** `typing.Optional[bool]` — If true, only orders with at least one tracking number; if false, only orders with none
    
</dd>
</dl>

<dl>
<dd>

**return_status:** `typing.Optional[str]` — Filter by return-request status. `open` → orders with at least one open return. `closed` → orders with at least one approved or denied return. Omit for no filter.
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only orders created at/after this instant (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only orders created before this instant (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**metadata_key:** `typing.Optional[str]` — Top-level `metadata` key to match, e.g. `po_number`. Must be sent together with `metadata_value`. Nested paths are not supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata_value:** `typing.Optional[str]` — Exact value `metadata_key` must equal. Matching is exact, not partial, and case-sensitive. Must be sent together with `metadata_key`.
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `typing.Optional[str]` — Filter to orders placed by one org teammate, matched as a case-insensitive substring of their email. Only ever narrows within the caller's organization; a solo user can only match their own address.
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional expansions. `tracking_events` embeds the full carrier checkpoint timeline (and latest status) on each tracking number; omitted by default to keep list payloads small.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">create_order</a>(...) -> OrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Posts an order to a queue for processing
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient, OrderProduct, Address
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrderCreate` 
    
</dd>
</dl>

<dl>
<dd>

**zinc_client:** `typing.Optional[str]` — Which assistant the buyer is using (claude, chatgpt, codex, …). Only used when the order needs a payment page, so it can send the buyer back afterwards.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">export_orders_csv</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream the current user's orders as a CSV file.

Takes the same filters as ``GET /orders`` (via the shared
``_visible_orders_filter``) so an export always contains exactly the rows
the caller was looking at — but no ``limit``/``offset``: the export covers
the whole filtered set, paged internally so memory stays flat.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.export_orders_csv()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `typing.Optional[str]` — Filter by order ID (partial match)
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Partial match on order ID OR tracking number
    
</dd>
</dl>

<dl>
<dd>

**status_filter:** `typing.Optional[str]` — Filter by order status
    
</dd>
</dl>

<dl>
<dd>

**merchant_order_id:** `typing.Optional[str]` — Filter by the retailer's own order number (exact match)
    
</dd>
</dl>

<dl>
<dd>

**tracking_status:** `typing.Optional[str]` — Filter to orders having at least one tracking number with this status
    
</dd>
</dl>

<dl>
<dd>

**has_tracking:** `typing.Optional[bool]` — Only orders with (true) or without (false) tracking
    
</dd>
</dl>

<dl>
<dd>

**return_status:** `typing.Optional[str]` — `open` or `closed` return requests; omit for no filter
    
</dd>
</dl>

<dl>
<dd>

**created_after:** `typing.Optional[datetime.datetime]` — Only orders created at/after this instant (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Only orders created before this instant (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**metadata_key:** `typing.Optional[str]` — Top-level `metadata` key to match; send with `metadata_value`
    
</dd>
</dl>

<dl>
<dd>

**metadata_value:** `typing.Optional[str]` — Exact value `metadata_key` must equal; send with `metadata_key`
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `typing.Optional[str]` — Filter to orders placed by one org teammate, matched as a case-insensitive substring of their email. Only ever narrows within the caller's organization; a solo user can only match their own address.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">list_test_products</a>() -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of test products for sandbox testing.

Returns list of test product URLs that can be used with test API keys
to trigger different test scenarios.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.list_test_products()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">get_order</a>(...) -> OrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves an order by its ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.get_order(
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">get_order_timeline</a>(...) -> OrderTimelineResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Customer-facing lifecycle timeline for an order.

Derived on read from existing data — no dedicated storage. Merges the
placement outcome (OrderLog) with carrier tracking state (TrackingNumber /
TrackingCheckpoint) into an ordered list of milestones. This is the order's
story to the customer, distinct from the admin-only job/automation log.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.get_order_timeline(
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.orders.<a href="src/zinc/orders/client.py">cancel_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel an order by its ID. Orders can only be cancelled if they are pending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.orders.cancel_order(
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Products
<details><summary><code>client.products.<a href="src/zinc/products/client.py">search_products</a>(...) -> ProductSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for products on a retailer.

**Best Buy returns a partial page.** Best Buy server-renders only about 4 of
the ~24 products on a search page and loads the rest in the browser, so each
page yields roughly 4 results rather than a full page. Ranking, pricing and
availability are Best Buy's own; there are simply fewer items per page. Page
through with `next_page` to collect more — `next_page` reflects whether Best
Buy has further results, not how many came back in this response.

**Shopify stores are their own retailer**: pass the store's domain as
`retailer` (e.g. `retailer=yetch.studio`; any Shopify-powered storefront
works). Results are the store's own top matches (~10) and there is no
pagination, so `next_page` is always null and `page` must be omitted or 1.
`product_id` is the store-scoped product handle to pass to the details
endpoint with the same `retailer`.

**Etsy search covers US shops, priced in USD.** Etsy sellers price in their
own currency and a single page routinely mixes several, which makes `price`
incomparable across a result set — so search is narrowed to US-located
shops and any remaining non-USD listing is dropped. `currency_code` is set
on every result and is always `USD` here, and prices are never converted,
so the number is what the seller charges. Because the currency check runs
after Etsy paginates, **a page can come back short while more results still
exist** — page on with `next_page`. (Details is neither narrowed nor
filtered: it returns any listing, in its own currency.)

Etsy results carry no `stars`/`num_reviews` — Etsy publishes a rating for
the *shop*, not the listing, and reporting a seller's rating as the
product's would be misleading; `brand` carries the shop name, and the
details endpoint reports the shop's rating explicitly. `product_id` is the
numeric listing id.

**Billing.** This is a metered data call: $0.01 is drawn from your wallet per successful request, before any order is placed. An empty wallet gets `402` instead. Sandbox (`zn_test_`) calls are free and never touch the live wallet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.products.search_products(
    query="query",
    retailer="retailer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Search term
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `str` — Retailer identifier: amazon, walmart, bestbuy, etsy, or a Shopify store's domain (e.g. retailer=yetch.studio)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**free_shipping:** `typing.Optional[bool]` — Only return items that ship for free (Walmart and Best Buy: ship price of 0). Currently a no-op for Amazon: the upstream search data under-reports Prime, so filtering on it would drop valid items — Amazon results are returned unfiltered. Filtering happens after pagination, so per-page counts vary; use `next_page` in the response to keep paging — an empty page with a non-null `next_page` is not the end of results. Rejected for Shopify stores: their search data carries no shipping information, so the filter cannot be honored.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/zinc/products/client.py">get_product_offers</a>(...) -> GetProductOffersProductsProductIdOffersGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get offers for a product from a retailer.

Not available for Shopify stores: a storefront lists one seller (itself),
so per-variant price and availability live on the details endpoint instead.

**Billing.** This is a metered data call: $0.01 is drawn from your wallet per successful request, before any order is placed. An empty wallet gets `402` instead. Sandbox (`zn_test_`) calls are free and never touch the live wallet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.products.get_product_offers(
    product_id="product_id",
    retailer="retailer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `str` — Retailer identifier: amazon, walmart, bestbuy, etsy, or a Shopify store's domain (e.g. retailer=yetch.studio)
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds, at least 31 (mutually exclusive with newer_than)
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp, as a unix time (mutually exclusive with max_age). Windows shorter than 31s are widened to it.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — Return immediately with status=processing
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/zinc/products/client.py">get_product_details</a>(...) -> GetProductDetailsProductsProductIdGetResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a product from a retailer.

**Best Buy is addressed by `bsin`**, not by the numeric SKU — the bsin is the
trailing id in a Best Buy product URL (`/product/{slug}/{bsin}`). Search
results return the SKU as `product_id` and also carry the bsin, so pass the
bsin here. The response repeats the SKU as `sku` for cross-referencing.

Unlike `/search`, a Best Buy detail response is complete: detail pages are
fully server-rendered, so nothing is withheld for client-side loading.

**Shopify is addressed by (store, handle)**: pass the store's domain as
`retailer` (e.g. `retailer=yetch.studio`) and the product handle — the slug
in `/products/{handle}`, returned as `product_id` by search — as the path
parameter. The response includes per-variant price and availability.
`async` is not supported for Shopify stores.

**Etsy is addressed by the numeric listing id** (returned as `product_id` by
search). `price` is in minor units of `currency_code`, not converted to USD.

Etsy ratings are the **shop's**, reported as `shop_review_average` /
`shop_review_count`, and both cover only the **past year** — an established
shop with no recent sales reports 0, and an unrated shop reports a null
average rather than 0.0 stars. `stars` and `num_reviews` are deliberately
not set: they mean a product's rating everywhere else in this API, and a
seller's rating is a different claim.

`listing_type` is `physical`, `download` or `both` — a download has nothing
to ship. `available` accounts for the shop being on vacation as well as
stock, so it can be false on an in-stock active listing; `shop_is_vacation`
says which it was. `variants` is populated only when Etsy exposes a
listing's inventory matrix — check `has_variations` to tell "no variants"
from "variants not visible". `taxonomy_id` is Etsy's raw category id; there
is no category name yet. `async` is not supported for Etsy.

**Billing.** This is a metered data call: $0.01 is drawn from your wallet per successful request, before any order is placed. An empty wallet gets `402` instead. Sandbox (`zn_test_`) calls are free and never touch the live wallet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.products.get_product_details(
    product_id="product_id",
    retailer="retailer",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `str` — Retailer identifier: amazon, walmart, bestbuy, etsy, or a Shopify store's domain (e.g. retailer=yetch.studio)
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds, at least 31 (mutually exclusive with newer_than)
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp, as a unix time (mutually exclusive with max_age). Windows shorter than 31s are widened to it.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — Return immediately with status=processing
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Search
<details><summary><code>client.search.<a href="src/zinc/search/client.py">search</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for products across retailers; returns orderable zn_sku_ listings.

**Billing.** This is a metered data call: $0.01 is drawn from your wallet per successful request, before any order is placed. An empty wallet gets `402` instead. Sandbox (`zn_test_`) calls are free and never touch the live wallet.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.search.search(
    q="q",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Search term
    
</dd>
</dl>

<dl>
<dd>

**min_price:** `typing.Optional[int]` — Cents. Drop results priced below this.
    
</dd>
</dl>

<dl>
<dd>

**max_price:** `typing.Optional[int]` — Cents. Drop results priced above this. Pass the `max_price` you intend to send to POST /orders and every result returned fits it. Results with no known price are dropped when a clamp is set.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ManagedAccounts
<details><summary><code>client.managed_accounts.<a href="src/zinc/managed_accounts/client.py">list_retailer_credentials</a>(...) -> RetailerCredentialsListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all retailer credentials for the current user.
If is_global=True (admin only), list global credentials instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.managed_accounts.list_retailer_credentials()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (default 50, max 500). Responses include `total` for paging past it.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of credentials to skip
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Partial match on email or retailer
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.managed_accounts.<a href="src/zinc/managed_accounts/client.py">create_retailer_credentials</a>(...) -> RetailerCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new retailer credentials for the current user.
If is_global=True (admin only), creates global credentials owned by the system user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.managed_accounts.create_retailer_credentials(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `typing.Optional[str]` — Retailer name (e.g., 'amazon'). If null, applies as default credentials.
    
</dd>
</dl>

<dl>
<dd>

**totp_secret:** `typing.Optional[str]` — TOTP secret key for 2FA (will be encrypted at rest).
    
</dd>
</dl>

<dl>
<dd>

**retailer_config:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.managed_accounts.<a href="src/zinc/managed_accounts/client.py">update_retailer_credentials</a>(...) -> RetailerCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update retailer credentials for the current user.
Admins can also update global credentials.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.managed_accounts.update_retailer_credentials(
    short_id="short_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**short_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**totp_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**retailer_config:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.managed_accounts.<a href="src/zinc/managed_accounts/client.py">delete_retailer_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete retailer credentials for the current user.
Admins can also delete global credentials.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.managed_accounts.delete_retailer_credentials(
    short_id="short_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**short_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent
<details><summary><code>client.agent.<a href="src/zinc/agent/client.py">create_mpp_order</a>(...) -> OrderResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Place an order via the Machine Payments Protocol (MPP).

No Zinc account required. Payment is made upfront via MPP.
Supports multiple payment methods (e.g. Tempo, Stripe).
If no valid payment credential is provided, returns HTTP 402
with payment challenges for all configured methods.

Payment is the gate, but only for a genuine discovery probe: a bodyless
POST (from a registry like mppscan) is parsed leniently and reaches the 402
challenge instead of a 422. A *present-but-invalid* body, by contrast —
including malformed JSON and non-object JSON — is a real order attempt
and is rejected with a 422 up front, before any payment
challenge is issued or honored. Otherwise an agent could settle an on-chain
payment against the challenge and then be rejected on the retry, with no way
to refund the settlement (the MPP layer cannot verify or reverse a payment
whose retry body no longer matches the challenge).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient, OrderProduct, Address
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.agent.create_mpp_order(
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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `OrderCreate` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[str]` — Restrict the 402 to a single payment method (e.g. 'stripe', 'tempo', or 'x402'). Omit to advertise every configured method. Use this when your client can satisfy only one rail — it avoids returning multiple WWW-Authenticate challenges, which many HTTP clients mishandle.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zinc/agent/client.py">search</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Beta** — response shape may change. Cross-retailer product search for agents. Returns orderable listings whose
`url` can be passed straight to POST /agent/orders.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.agent.search(
    q="q",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Search term
    
</dd>
</dl>

<dl>
<dd>

**min_price:** `typing.Optional[int]` — Cents. Drop results priced below this.
    
</dd>
</dl>

<dl>
<dd>

**max_price:** `typing.Optional[int]` — Cents. Drop results priced above this. Pass the `max_price` you intend to send to POST /orders and every result returned fits it. Results with no known price are dropped when a clamp is set.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zinc/agent/client.py">product_search</a>(...) -> ProductSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Per-retailer product search for agents (amazon | walmart).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.agent.product_search(
    query="query",
    retailer="amazon",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Search term
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `AgentProductSearchRequestRetailer` — Retailer: amazon or walmart
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**free_shipping:** `typing.Optional[bool]` — Only return items that ship for free (Walmart: ship price of 0). Currently a no-op for Amazon: the upstream search data under-reports Prime, so Amazon results are returned unfiltered. Applied per-page after pagination; use `next_page` in the response to keep paging — an empty page with a non-null `next_page` is not the end of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zinc/agent/client.py">product_offers</a>(...) -> AgentProductOffersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Offers/pricing for a specific product on a retailer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.agent.product_offers(
    product_id="product_id",
    retailer="amazon",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` — Product identifier (e.g. ASIN)
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `AgentProductOffersRequestRetailer` — Retailer: amazon or walmart
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds, at least 31 (mutually exclusive with newer_than)
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp, as a unix time (mutually exclusive with max_age). Windows shorter than 31s are widened to it.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — Return immediately with status=processing
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zinc/agent/client.py">product_details</a>(...) -> AgentProductDetailsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Full product details for a specific product on a retailer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.agent.product_details(
    product_id="product_id",
    retailer="amazon",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` — Product identifier (e.g. ASIN)
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `AgentProductDetailsRequestRetailer` — Retailer: amazon or walmart
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds, at least 31 (mutually exclusive with newer_than)
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp, as a unix time (mutually exclusive with max_age). Windows shorter than 31s are widened to it.
    
</dd>
</dl>

<dl>
<dd>

**async:** `typing.Optional[bool]` — Return immediately with status=processing
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Returns
<details><summary><code>client.returns.<a href="src/zinc/returns/client.py">list_return_requests</a>(...) -> ReturnRequestListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.returns.list_return_requests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size (default 50, max 500). Responses include `total` for paging past it.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of returns to skip
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Partial match on order ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by return status
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.returns.<a href="src/zinc/returns/client.py">create_return_request</a>(...) -> ReturnRequestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient, ReturnRequestItem
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.returns.create_return_request(
    order_id="order_id",
    items=[
        ReturnRequestItem(
            order_item_id="order_item_id",
            quantity=1,
        )
    ],
    reason="damaged",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.List[ReturnRequestItem]` — Per-product lines being returned
    
</dd>
</dl>

<dl>
<dd>

**reason:** `ReturnRequestReason` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.returns.<a href="src/zinc/returns/client.py">get_return_request</a>(...) -> ReturnRequestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.returns.get_return_request(
    return_request_id="return_request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**return_request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Retailers
<details><summary><code>client.retailers.<a href="src/zinc/retailers/client.py">list_retailers</a>(...) -> PublicRetailerListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the retailers Zinc supports — the public "what do you support?" catalog.

No authentication required. One flat object per retailer brand: identifier,
domain, countries shipped to, and the free-shipping policy. International
marketplaces (e.g. amazon.com / amazon.de) are grouped under one brand with
the country listed in `supported_countries`. Optionally filter by name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.retailers.list_retailers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of retailers to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of retailers to skip
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by name (case-insensitive partial match)
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[str]` — Pass `all` to include the long tail Zinc has ordered from but not curated (hundreds of brands). Omit for the curated set. This selects how much of the catalog to return; it is not a filter on an entry's `support` tier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.retailers.<a href="src/zinc/retailers/client.py">check_retailer</a>(...) -> RetailerCheckResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Can Zinc buy from this store, and ship it to this country?

No authentication. This is the question `GET /retailers` cannot answer: the
list is the curated set, while the order path accepts most stores, so a
caller holding an arbitrary URL has no way to find out from the list alone.

`orderable` is the answer. `support` says how much we know:

| tier | meaning |
|---|---|
| `verified` | curated, and its daily test order is passing |
| `active` | real orders succeeded here in the last 90 days |
| `observed` | Zinc has attempted orders here |
| `untested` | never seen — and Zinc will still attempt it |
| `unsupported` | Zinc refuses; `unsupported_reason` says why |

Read-only: asking never adds a store to the catalog.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.retailers.check_retailer(
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — A product or store URL, e.g. https://shop.aloyoga.com/products/x
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Destination country as an ISO 3166-1 alpha-2 code (e.g. 'US', 'GB'). Case-insensitive. Longer spellings such as 'USA' are rejected — the error names the code to use. Omit to skip the shipping check. Runs the same gate `POST /orders` applies, so the two cannot disagree.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Usage
<details><summary><code>client.usage.<a href="src/zinc/usage/client.py">get_my_usage</a>(...) -> UserUsageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The caller's own data-API usage over a trailing window, per endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.usage.get_my_usage()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**window_days:** `typing.Optional[int]` — Trailing window in days (max 90).
    
</dd>
</dl>

<dl>
<dd>

**recent:** `typing.Optional[int]` — How many recent calls to return.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Wallet
<details><summary><code>client.wallet.<a href="src/zinc/wallet/client.py">get_wallet</a>(...) -> WalletResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get your wallet balance.

All amounts are integer cents. `balance` is the ledger balance;
`spendable_balance` is what `POST /orders` actually checks against (the two
differ only for Zinc Connect accounts with in-flight holds). An order needs
`max_price + order_fee_cents` spendable, so compare against that before
placing one instead of discovering a shortfall as a 402. Bulk-deal customers
(`billed_by_invoice: true`) are invoiced monthly and skip the balance check.

Under a `zn_test_` key (or `X-Test-Mode`) this reads the sandbox wallet,
which sandbox orders never draw down. Funds are added from the dashboard.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.wallet.get_wallet()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Stats
<details><summary><code>client.stats.<a href="src/zinc/stats/client.py">get_delivery_map</a>() -> DeliveryMapResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Recent delivered orders as anonymized, city-level map points.

Public and unauthenticated — feeds the marketing site's globe. Points are
ZIP-centroid coordinates rounded to two decimals with a curated category
emoji; deduplicated and capped. Cached for about an hour.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.stats.get_delivery_map()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.stats.<a href="src/zinc/stats/client.py">get_lifetime_stats</a>() -> LifetimeStatsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Zinc's all-time successful-order count and GMV.

Public and unauthenticated. Top-level numbers are v2 (this service);
``v1`` is the worker-computed legacy snapshot (seed until the first
compute lands); ``combined`` sums both. Cached for about a day.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.stats.get_lifetime_stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tracking
<details><summary><code>client.tracking.<a href="src/zinc/tracking/client.py">get_public_tracking</a>(...) -> PublicTrackingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public tracking view for a single order, keyed by its UUID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.tracking.get_public_tracking(
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payments
<details><summary><code>client.payments.<a href="src/zinc/payments/client.py">get_pending_payment</a>(...) -> PendingPaymentResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Where a card payment stands; poll it after a 402 ``payment_required``.

``requires_action`` until the buyer pays on ``pay_url``; then ``authorized``
and, as soon as the order is created from the parked draft, ``placed`` with
``order_id``. The poll itself does the creating when it gets there before
the webhook, so a buyer who pays and comes straight back sees the order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.payments.get_pending_payment(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payments.<a href="src/zinc/payments/client.py">create_checkout_session</a>(...) -> CheckoutSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The Stripe-hosted payment page for a pending payment.

Called by pay.zinc.com when the buyer clicks through, not by the 402 itself,
so a link nobody opens never creates a Stripe session. Idempotent per
payment: a session already open is returned again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.payments.create_checkout_session(
    payment_id="payment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sandbox
<details><summary><code>client.sandbox.<a href="src/zinc/sandbox/client.py">create_sandbox_key</a>(...) -> SandboxKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mint a provisional sandbox user + test API key. No account needed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient, SandboxKeyCreate
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.sandbox.create_sandbox_key(
    request=SandboxKeyCreate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[SandboxKeyCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox.<a href="src/zinc/sandbox/client.py">claim_sandbox</a>(...) -> SandboxClaimResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fold a provisional sandbox into the authenticated account.

Always a merge: Stytch's callback creates a real user row on first login,
so a caller reaching this endpoint already has an account. The agent's key
is reassigned rather than revoked, so whatever it has hardcoded keeps
working — that is the point of claiming rather than starting over.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.sandbox.claim_sandbox(
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox.<a href="src/zinc/sandbox/client.py">get_sandbox_status</a>(...) -> SandboxStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Whether the sandbox this key belongs to has been claimed yet.

An agent hands its claim URL to a human and then has no way to learn what
happened — a device-code grant would tell it for free (issue #825). Until
we have one, polling this closes the loop.

Still provisional means nobody has claimed it. Past that, "not provisional"
alone would be a lie — every ordinary account would read as claimed — so
the answer comes from the claim event written on the account, which is
also the only durable evidence a claim happened once the provisional row
is deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.sandbox.get_sandbox_status()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox.<a href="src/zinc/sandbox/client.py">get_quickstart</a>() -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The agent quickstart, served as plain markdown.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.sandbox.get_quickstart()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Device
<details><summary><code>client.device.<a href="src/zinc/device/client.py">create_device_code</a>(...) -> DeviceCodeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mint a device code. No account needed.

Send your `zn_test_` sandbox key as the bearer and the sandbox comes along:
when the owner approves, its orders and key move onto their account and
your sandbox key keeps working, alongside the live key you receive.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient, DeviceCodeCreate
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.device.create_device_code(
    request=DeviceCodeCreate(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[DeviceCodeCreate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device.<a href="src/zinc/device/client.py">describe_device_code</a>(...) -> DeviceCodeInfo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Public on purpose: it holds only what the agent said about itself, and
the approval page needs it before the human has signed in.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.device.describe_device_code(
    user_code="user_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device.<a href="src/zinc/device/client.py">decide_device_code</a>(...) -> DeviceApproveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The human's decision. A machine credential must never make it: an API
key approving a device code would be a key minting a key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.device.decide_device_code(
    user_code="user_code",
    granted=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**granted:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.device.<a href="src/zinc/device/client.py">redeem_device_code</a>(...) -> ApiKeyExchangeResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.device.redeem_device_code(
    device_code="device_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**device_code:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/zinc/webhooks/client.py">get_webhook_endpoint</a>(...) -> WebhookEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The URL Zinc delivers this account's webhooks to, and the HMAC secret
that signs them. Both are null until ``PUT /webhooks/endpoint`` is called.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.webhooks.get_webhook_endpoint()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/zinc/webhooks/client.py">set_webhook_endpoint</a>(...) -> WebhookEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register (or replace) the webhook URL for this account.

Every order and return event Zinc emits for the account is POSTed to this
URL. A signing secret is generated on first registration and returned so
the caller can verify the ``X-Webhook-Signature`` header; replacing the URL
keeps the existing secret, so a URL move never invalidates verification.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.webhooks.set_webhook_endpoint(
    url="https://example.com/zinc/webhook",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — Absolute http(s) URL that receives order and return events.
    
</dd>
</dl>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/zinc/webhooks/client.py">clear_webhook_endpoint</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop webhook delivery for this account by clearing the URL.

The signing secret is kept, so re-registering a URL later resumes
deliveries signed with the same secret the caller already verifies against.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.webhooks.clear_webhook_endpoint()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**authorization:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Health
<details><summary><code>client.health.<a href="src/zinc/health/client.py">get_public_health</a>() -> PublicHealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Customer-facing platform health.

No auth. Cached in-process for 4 minutes — at the marketing site's 5-min
cron cadence, the DB is touched at most ~once per tick.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zinc import ZincClient
from zinc.environment import ZincClientEnvironment

client = ZincClient(
    api_key="<value>",
    environment=ZincClientEnvironment.PRODUCTION,
)

client.health.get_public_health()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

