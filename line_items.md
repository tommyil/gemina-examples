# Gemina API - Implementing Line Item Retrieval for Invoices

This guide explains how to enhance your existing Gemina API integration to retrieve detailed line items from processed invoices. This feature allows you to access granular data for each item listed on an invoice.

**Target Audience:** Developers who have already successfully integrated the basic invoice data retrieval with the Gemina API.

## Prerequisites

*   You have a working integration for submitting documents and retrieving their processed data (header-level details).
*   You are familiar with your `CLIENT_ID` and `API_KEY`.
*   You understand how to use the `external_id` to track and retrieve document processing results.

## Overview

Retrieving line items involves two main steps:

1.  **Requesting Line Item Extraction:** When you initially submit a document for processing, you'll include a new flag (`include_line_items: true`) in your request payload. This tells the Gemina service to extract line items in addition to the standard invoice data.
2.  **Retrieving Line Items:** After the document processing is complete (or while it's in progress, as line item processing might complete at a similar pace), you'll use a new, dedicated API endpoint to fetch the extracted line items using the same `external_id`.

The main document data and line item data are retrieved from separate endpoints, allowing for flexibility in how you fetch and process this information.

## Step 1: Requesting Line Item Extraction

When you submit a document for processing (typically via a `POST` request to your document submission endpoint), modify your JSON payload to include the `include_line_items` field set to `true`.

**Example Request Payload Modification:**

```json
{
  "client_id": YOUR_CLIENT_ID, // Your client ID
  "file_url": "YOUR_DOCUMENT_URL", // Or use file_content for base64
  "external_id": "YOUR_UNIQUE_EXTERNAL_ID", // The unique ID you assign
  "use_llm": true, // Or false, as per your existing setup
  "include_line_items": true // Add this line to enable line item extraction
  // ... any other parameters you currently send
}
```

**Important:**
*   Setting `include_line_items: true` flags the document for line item processing.
*   The response to this initial submission request will **not** contain the line items themselves. It will be the standard acknowledgment/processing ID response you currently receive.

## Step 2: Retrieving Processed Line Items

Once the document has been processed and line items have been extracted, you can retrieve them using a new `GET` request.

**Endpoint for Line Items:**

`[YOUR_API_BASE_URL]/[API_URI_PREFIX]/line-items/<string:external_id>`

Where:
*   `[YOUR_API_BASE_URL]` is the base URL for the Gemina API.
*   `[API_URI_PREFIX]` is the standard prefix for your API endpoints (e.g., `/api/v1/business_documents`).
*   `<string:external_id>` is the same `external_id` you used when submitting the document.

**Example based on your provided info:**
If your main retrieval endpoint is `API_URI + "/<string:external_id>"`, then the line items endpoint will be `API_URI + "/line-items/<string:external_id>"`.

**Request:**
*   **Method:** `GET`
*   **URL:** `[YOUR_API_BASE_URL]/[API_URI_PREFIX]/line-items/YOUR_UNIQUE_EXTERNAL_ID`
*   **Headers:**
    *   `Authorization: "Basic " + YOUR_API_KEY`
    *   Any other standard headers required by your API.

**Successful Response (200 OK):**

The API will return a JSON object containing the line items.

```json
{
    "client_id": 65,
    "external_id": "YOUR_EXTERNAL_ID_EXAMPLE",
    "line_item_request_id": "5163c7f8-316c-41a7-afee-74283973ebe5",
    "line_items": [
        {
            "line_no": 1,
            "item_code": "13017",
            "barcode": null,
            "description": "מגב פלסטי 40 ס\"מ",
            "packaging_info": null,
            "promo_no": null,
            "quantity": 1.0,
            "units_per_pack": null,
            "gross_unit_price": 8.0,
            "gross_line_total": 8.0,
            "discount_percent": null,
            "discount_amount": null,
            "net_unit_price": 8.0,
            "packing_base_value": null,
            "vat_rate": null,
            "vat_amount": null,
            "purchase_tax": null,
            "deposit_amount": null,
            "net_line_total": 8.0
        },
        {
            "line_no": 2,
            "item_code": "19322",
            "barcode": null,
            "description": "קופסא קרטון BO2",
            // ... other fields for item 2 ...
            "net_line_total": 175.0
        }
        // ... more line items
    ],
    "created": "2025-05-21T21:35:07.483000",
    "created_timestamp": 1747863307.484057
}
```

**Key Fields in the Response:**
*   `external_id`: Matches the ID you submitted.
*   `line_item_request_id`: A unique identifier for this specific line
    item retrieval task.
*   `line_items`: An array of objects, where each object represents a
    single line item from the invoice.
    *   Each line item object contains fields like `line_no`,
        `item_code`, `description`, `quantity`, `gross_unit_price`,
        `net_line_total`, etc.
*   `created` / `created_timestamp`: Timestamp of when the line item
    data was generated.

## Workflow Considerations

1.  **Submit Document:** Send your `POST` request to the document
    submission endpoint with `include_line_items: true`.
2.  **Poll for Status (Optional but Recommended):**
    *   You can poll the main document retrieval endpoint
        (`API_URI + "/<string:external_id>"`) for the header-level
        invoice data.
    *   Simultaneously, or once the main document processing is complete,
        you can start polling the line items retrieval endpoint
        (`API_URI + "/line-items/<string:external_id>"`) for the line
        item data.
3.  **Data Availability:**
    *   Line item processing is asynchronous. If you query the line
        items endpoint before processing is complete, you might receive
        a `404 Not Found`, a `202 Accepted` (indicating processing is
        ongoing), or an empty `line_items` array, depending on the
        API's specific behavior for pending data. Implement
        appropriate retry logic or check a status field if available.
    *   It's possible for the main document data to be ready before
        the line items, or vice-versa, or for them to be ready
        concurrently.

## Error Handling

*   **401 Unauthorized:** Ensure your `API_KEY` is correct and
    included in the headers, with a `Basic ` (mind the space) prefix.
*   **404 Not Found:**
    *   Double-check the `external_id`.
    *   Line items for this `external_id` may not have been requested
        (i.e., `include_line_items` was `false` or omitted during
        submission).
*   **Other Errors:** Refer to the general Gemina API documentation for
    other status codes.

## Updating Your Integration

1.  **Modify Submission Logic:** Update the part of your code that
    prepares the JSON payload for document submission to include the
    `"include_line_items": true` field.
2.  **Add New Retrieval Function:** Create a new function or method in
    your codebase to call the
    `GET [API_URI_PREFIX]/line-items/<string:external_id>` endpoint.
3.  **Data Handling:** Adjust your data models and processing logic to
    accommodate the new line item data structure.

## Example Code Snippets (Conceptual)

These are conceptual and language-agnostic. Adapt them to your specific
programming language and HTTP client library.

**1. Modifying Submission (Conceptual Python with `requests`):**

```python
import requests
import json

API_KEY = "Basic " + "YOUR_API_KEY"
CLIENT_ID = YOUR_CLIENT_ID # e.g., 65
GEMINA_API_SUBMIT_URL = "YOUR_GEMINA_API_SUBMIT_ENDPOINT"
# e.g., "https://api.gemina.com/api/v1/business_documents"
EXTERNAL_ID = "my_invoice_123"
FILE_URL = "http://example.com/invoice.pdf"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "client_id": CLIENT_ID,
    "external_id": EXTERNAL_ID,
    "file_url": FILE_URL,
    "use_llm": True,
    "include_line_items": True # <-- Key addition
}

# response = requests.post(
#     GEMINA_API_SUBMIT_URL,
#     headers=headers,
#     data=json.dumps(payload)
# )
# print(f"Submission response: {response.status_code}, "
#       f"{response.json()}")
```

**2. Retrieving Line Items (Conceptual Python with `requests`):**

```python
import requests

API_KEY = "Basic " + "YOUR_API_KEY"
GEMINA_API_LINE_ITEMS_URL_BASE = (
    "YOUR_GEMINA_API_LINE_ITEMS_ENDPOINT_BASE"
)
# e.g., "https://api.gemina.com/api/v1/business_documents/line-items/"
EXTERNAL_ID = "my_invoice_123" # Same ID as used in submission

headers = {
    "Authorization": API_KEY
}

# line_items_url = f"{GEMINA_API_LINE_ITEMS_URL_BASE}{EXTERNAL_ID}"
# response = requests.get(line_items_url, headers=headers)

# if response.status_code == 200:
#     line_items_data = response.json()
#     print("Line Items Retrieved:")
#     for item in line_items_data.get("line_items", []):
#         print(
#             f"  - {item.get('description')}: "
#             f"Qty {item.get('quantity')}, "
#             f"Total {item.get('net_line_total')}"
#         )
# elif response.status_code == 404:
#     print(
#         f"Line items not found for {EXTERNAL_ID}. "
#         f"Processing may not be complete or not requested."
#     )
# else:
#     print(
#         f"Error retrieving line items: {response.status_code}, "
#         f"{response.text}" # response.text could be long
#     )
```

---

## Line Item Field Data Types

When you retrieve line items, each object within the `line_items` array will contain several fields. The following table describes the expected data type for each field *when a value is present and not null*. Many fields can also be `null` if the information is not applicable or available on the invoice.

| Field Name           | Data Type             | Notes                                                                              |
|----------------------|-----------------------|------------------------------------------------------------------------------------|
| `line_no`            | Integer               | The sequential number of the line item.                                            |
| `item_code`          | String                | Product or service code.                                                           |
| `barcode`            | String                | Barcode associated with the item.                                                  |
| `description`        | String                | Description of the item.                                                           |
| `packaging_info`     | String                | Information about packaging.                                                       |
| `promo_no`           | String                | Promotion number, if applicable.                                                   |
| `quantity`           | Number (Decimal/Float)| Quantity of the item.                                                              |
| `units_per_pack`     | Integer               | Number of units per pack.                                                          |
| `gross_unit_price`   | Number (Decimal/Float)| Unit price before any discounts or taxes.                                          |
| `gross_line_total`   | Number (Decimal/Float)| Total price for the line before discounts/taxes (`quantity` * `gross_unit_price`). |
| `discount_percent`   | Number (Decimal/Float)| Discount percentage applied.                                                       |
| `discount_amount`    | Number (Decimal/Float)| Total discount amount for the line.                                                |
| `net_unit_price`     | Number (Decimal/Float)| Unit price after discounts but before taxes.                                       |
| `packing_base_value` | Number (Decimal/Float)| Base value for packing calculations.                                               |
| `vat_rate`           | Number (Decimal/Float)| VAT rate applied to the line item.                                                 |
| `vat_amount`         | Number (Decimal/Float)| Total VAT amount for the line.                                                     |
| `purchase_tax`       | Number (Decimal/Float)| Purchase tax amount for the line.                                                  |
| `deposit_amount`     | Number (Decimal/Float)| Deposit amount related to the line.                                                |
| `net_line_total`     | Number (Decimal/Float)| Final total for the line item after all calculations (discounts, taxes).           |

**Note on `null` values:** As seen in the example API response, many fields that are not applicable or not present on the source document will be returned with a value of `null`. Your client-side parsing logic should account for this possibility for all fields.

---

## Performance and Latency Considerations for Line Items

Extracting detailed line items from an invoice is a significantly more complex process compared to retrieving basic header-level invoice details. The underlying logic, data analysis, and system resources required for accurate line item parsing are substantially greater—roughly an order of magnitude (approximately 10x) more involved.

**Impact on Latency:**

Due to this increased complexity, you should expect a considerably longer processing time when `include_line_items: true` is requested.

*   **Basic Invoice Details:** Typically processed within a few seconds (e.g., up to 5 seconds).
*   **Invoice with Line Items:** May take significantly longer, potentially **between 15 seconds to 1 minute**, or even more for very complex or lengthy invoices.

**Recommendations:**

1.  **Asynchronous Polling:** It is highly recommended to implement an asynchronous polling mechanism for retrieving line item results. Do not block your primary application flow waiting for an immediate response.
2.  **Separate Retrieval:** Continue to retrieve basic invoice details from the standard endpoint (`API_URI + "/<string:external_id>"`). You can then poll the line items endpoint (`API_URI + "/line-items/<string:external_id>"`) separately and potentially less frequently, or only after the basic details are confirmed.
3.  **User Experience:** If displaying this data to end-users, manage their expectations regarding the time it might take for full line item details to become available. Consider displaying basic invoice information first, with an indicator that line items are still being processed.

Understanding and planning for this increased latency is crucial for a smooth integration and a good user experience when utilizing the line items feature.

---

By following these steps, you can successfully integrate line item
retrieval into your Gemina API workflow, providing richer and more
detailed invoice data to your users. If you encounter any issues,
please refer to the main API documentation or contact support.

------



## More Resources



Response Types - https://github.com/tommyil/gemina-examples/blob/master/response_types.md

Data Loop - https://github.com/tommyil/gemina-examples/blob/master/data_loop.md

LLM Integration - https://github.com/tommyil/gemina-examples/blob/master/llm_integration.md

Python Integration - https://github.com/tommyil/gemina-examples

C# Implementation - https://github.com/tommyil/gemina-examples-cs

Node.js/TypeScript Implementation - https://github.com/tommyil/gemina-examples-ts

Java Implementation - https://github.com/tommyil/gemina-examples-java

PHP Implementation - https://github.com/tommyil/gemina-examples-php
