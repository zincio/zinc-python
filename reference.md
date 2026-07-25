# Reference
## Orders
<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">validate_bulk_upload</a>(...) -> BulkValidateResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">list_bulk_uploads</a>(...) -> BulkBatchListResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">create_bulk_upload</a>(...) -> BulkBatchResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">get_bulk_upload</a>(...) -> BulkBatchResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">download_bulk_results</a>(...) -> typing.Any</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">list_orders</a>(...) -> OrderListResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">create_order</a>(...) -> OrderResponse</code></summary>
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
from zincio import ZincioApi, OrderProduct, Address
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">list_test_products</a>() -> typing.Dict[str, typing.Any]</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">get_order</a>(...) -> OrderResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">get_order_timeline</a>(...) -> OrderTimelineResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.orders.<a href="src/zincio/orders/client.py">cancel_order</a>(...)</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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
<details><summary><code>client.products.<a href="src/zincio/products/client.py">search_products</a>(...) -> ProductSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for products on a retailer.
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
)

client.products.search_products(
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

**retailer:** `SearchProductsProductsSearchGetRequestRetailer` — Retailer identifier
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for pagination
    
</dd>
</dl>

<dl>
<dd>

**free_shipping:** `typing.Optional[bool]` — Only return items that ship for free (Walmart: ship price of 0). Currently a no-op for Amazon: the upstream search data under-reports Prime, so filtering on it would drop valid items — Amazon results are returned unfiltered. Filtering happens after v1 pagination, so per-page counts vary; use `next_page` in the response to keep paging — an empty page with a non-null `next_page` is not the end of results.
    
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

<details><summary><code>client.products.<a href="src/zincio/products/client.py">get_product_offers</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get offers for a product from a retailer.
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
)

client.products.get_product_offers(
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

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `GetProductOffersProductsProductIdOffersGetRequestRetailer` — Retailer identifier
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds (mutually exclusive with newer_than)
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp (mutually exclusive with max_age)
    
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

<details><summary><code>client.products.<a href="src/zincio/products/client.py">get_product_details</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a product from a retailer.
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
)

client.products.get_product_details(
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

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**retailer:** `GetProductDetailsProductsProductIdGetRequestRetailer` — Retailer identifier
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds (mutually exclusive with newer_than)
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp (mutually exclusive with max_age)
    
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
<details><summary><code>client.search.<a href="src/zincio/search/client.py">search</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for products across retailers; returns orderable zn_sku_ listings.
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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
<details><summary><code>client.managed_accounts.<a href="src/zincio/managed_accounts/client.py">list_retailer_credentials</a>(...) -> RetailerCredentialsListResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.managed_accounts.<a href="src/zincio/managed_accounts/client.py">create_retailer_credentials</a>(...) -> RetailerCredentialsResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.managed_accounts.<a href="src/zincio/managed_accounts/client.py">update_retailer_credentials</a>(...) -> RetailerCredentialsResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.managed_accounts.<a href="src/zincio/managed_accounts/client.py">delete_retailer_credentials</a>(...)</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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
<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">create_mpp_order</a>(...) -> OrderResponse</code></summary>
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
from zincio import ZincioApi, OrderProduct, Address
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">search</a>(...) -> SearchResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">search_post</a>(...) -> SearchResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
)

client.agent.search_post(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">product_search</a>(...) -> ProductSearchResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">product_search_post</a>(...) -> ProductSearchResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
)

client.agent.product_search_post(
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

**retailer:** `AgentProductSearchPostRequestRetailer` — Retailer: amazon or walmart
    
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

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">product_offers</a>(...) -> typing.Any</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

**max_age:** `typing.Optional[int]` — Max response age in seconds
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp
    
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

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">product_offers_post</a>(...) -> typing.Any</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
)

client.agent.product_offers_post(
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

**retailer:** `AgentProductOffersPostRequestRetailer` — Retailer: amazon or walmart
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp
    
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

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">product_details</a>(...) -> typing.Any</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

**max_age:** `typing.Optional[int]` — Max response age in seconds
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp
    
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

<details><summary><code>client.agent.<a href="src/zincio/agent/client.py">product_details_post</a>(...) -> typing.Any</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
)

client.agent.product_details_post(
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

**retailer:** `AgentProductDetailsPostRequestRetailer` — Retailer: amazon or walmart
    
</dd>
</dl>

<dl>
<dd>

**max_age:** `typing.Optional[int]` — Max response age in seconds
    
</dd>
</dl>

<dl>
<dd>

**newer_than:** `typing.Optional[int]` — Minimum retrieval timestamp
    
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
<details><summary><code>client.returns.<a href="src/zincio/returns/client.py">list_return_requests</a>(...) -> ReturnRequestListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.returns.<a href="src/zincio/returns/client.py">create_return_request</a>(...) -> ReturnRequestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zincio import ZincioApi, ReturnRequestItem
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

<details><summary><code>client.returns.<a href="src/zincio/returns/client.py">get_return_request</a>(...) -> ReturnRequestResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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
<details><summary><code>client.retailers.<a href="src/zincio/retailers/client.py">list_retailers</a>(...) -> PublicRetailerListResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Usage
<details><summary><code>client.usage.<a href="src/zincio/usage/client.py">get_my_usage</a>(...) -> UserUsageResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

## Tracking
<details><summary><code>client.tracking.<a href="src/zincio/tracking/client.py">get_public_tracking</a>(...) -> PublicTrackingResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

## Health
<details><summary><code>client.health.<a href="src/zincio/health/client.py">get_public_health</a>() -> PublicHealthResponse</code></summary>
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
from zincio import ZincioApi
from zincio.environment import ZincioApiEnvironment

client = ZincioApi(
    api_key="<value>",
    environment=ZincioApiEnvironment.PRODUCTION,
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

