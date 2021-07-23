# Data Loop



## Background

Data Loops are crucial for effective learning and faster learning intervals.

They provides our system with constant feedback about its performance and assist us to train more customized models for your needs.

In addition, Data Loops are an excellent tool to assess the overall performance, and aggregate success metrics that deliver both transparency and in-depth understanding of the UX.



## Endpoint

```http
PUT

https://api.gemina.co.il/v1/business_documents
```



## JSON Payload Parameters



#### Sample JSON Payload

```json
{
    "external_id": "== YOUR INVOICE ID ==",
    "client_id": "== YOUR CLIENT KEY ==",
    "total_amount": 117.0,
    "net_amount": 100.0,
    "vat_amount": 17.0,
    "document_number": "IL7890",
    "issue_date": "2021-07-22",
    "business_number": "EUR-514713288",
    "supplier_name": "Five Straps",
    "document_type": "invoice_receipt",
    "expense_type": "fuel",
    "payment_method": "credit_card",
    "currency": "usd",
}

```



### Parameters



##### external_id

Type: String

Description: The document's External Id that has been assigned earlier. It is used to identify that document before updating its metadata.



##### client_id

Type: Integer

Description: Your provided Client Id



##### total_amount

Type: Float

Description: The document's total amount for update



##### net_amount

Type: Float

Description: The document's net amount for update



##### vat_amount

Type: Float

Description: The document's VAT amount for update



##### document_number

Type: String

Description: The Document Number

*Can contain characters/letters as well.*



##### issue_date

Type: Date

Description: A string that contains the updated Issue Date

*Format (String): YYYY-MM-DD*



##### business_number

Type: String

Description: The supplier's business-number

*Can contain characters/letters as well.*



##### supplier_name

Type: String

Description: The supplier's name for the update 

*Supports all languages.*



##### document_type

Type: Enum

Description: The document's type

*Must be a single value from the list below:*

```json
[
    "unknown",
    "invoice",
    "delivery_note",
    "invoice_receipt",
    "receipt",
    "payment_confirmation",
    "donation_receipt",
    "credit_note"
]
```



##### expense_type

Type: Enum

Description: The document's expense-type 

*Must be a single value from the list below:*

```json
[
	"fuel",
	"basic_inventory",
	"vehicle_maintenance_and_transport",
	"other_expenses",
	"professional_services",
	"electricity_and_water",
	"local_merchandise",
	"travel",
	"advertising_and_promotion",
	"credit_card_fees",
	"mail_and_communication",
	"consumables",
	"rent_and_property_management",
	"education_and_professional_literature",
	"office",
	"maintenance_and_repairs",
	"other_fixed_assets",
	"additional_wages",
	"outsource_and_subcontractors",
	"packaging",
	"raw_and_building materials",
	"refreshments_gifts_donations_fines",
	"Computers_and_data_processing_equipment",
	"maintenance_and_cleanliness",
	"international_merchandise",
	"management_fee",
	"furniture_and_accessories",
	"taxes_and_fees",
	"delivery_and_storage",
	"wages",
	"other",
	"legal",
	"research_and_development",
	"international_travel",
	"vehicle",
	"Work_clothes",
	"tenders_fairs_exhibitions",
	"insurance",
	"depreciation",
	"banking",
	"fuel_reimbursement"
]
```



##### payment_method

Type: Enum

Description: The used payment-method to pay for services / merchandise.

*Must be a single value from the list below:*

```json
[
    "cheque",
    "wire_transfer",
    "credit_card",
    "paypal",
    "cash",
    "app",
    "other"
]
```



##### currency

Type: Enum

Description: The used currency for payment

*Must be a single value from the list below:*

```json
[
    "ils",
    "usd",
    "eur",
    "sek",
    "gbp",
    "czk",
    "zar",
    "cad",
    "jpy",
    "rub",
    "sgd",
    "pln",
    "aud",
    "inr",
    "hkd",
    "thb",
    "mxn",
    "chf",
    "try",
    "dkk",
    "krw",
    "cny",
    "brl",
    "ron",
    "hrk",
    "nok"
]
```







## Sample Response

Response Code: **200**

```json
{
    "business_number": "EUR-514713288",
    "currency": "usd",
    "document_number": "IL7890",
    "document_type": "invoice_receipt",
    "expense_type": "fuel",
    "external_id": "ex_id_e12bcf79-505d-4920-b8f6-d5da28b1acd7",
    "issue_date": "2021-07-22",
    "net_amount": 100.0,
    "payment_method": "credit_card",
    "supplier_name": "Five Straps",
    "total_amount": 117.0,
    "vat_amount": 17.0
}
```



## Example Code



#### Code

```python
def send_labeled_data(image_id):
    url = f"{GEMINA_API_URL}{BUSINESS_DOCUMENTS_URL}"
    token = f"Basic {API_KEY}"  # Mind the space between 'Basic' and the API KEY
    headers = {"Authorization": token}
    json_data = {
        "external_id": INVOICE_ID,
        "client_id": CLIENT_ID,
        "document_type": "invoice_receipt", # from a closed list
        "total_amount": 117.0, # can be either string or number
        "net_amount": 100.0, # can be either string or number
        "vat_amount": 17.0, # can be either string or number
        "document_number": "IL7890", # Can contain characters as well
        "issue_date": "2021-07-22", # YYYY-MM-DD
        "business_number": "EUR-514713288", # can contain characters as well
        "supplier_name": "Five Straps", # any language
        "expense_type": "fuel", # from a closed list
        "payment_method": "credit_card", # from a closed list
        "currency": "usd", # from a closed list
    }

    response = requests.put(url, headers=headers, json=json_data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

```



#### Execution

```python
    ### Step III:  Send Labeled Image Date and Close the Data Loop ###
    ### Perform this operation when users validate the prediction. ###

    labeled_data = send_labeled_data(INVOICE_ID)
    if labeled_data:
        print(f"Successfully updated the labeled data for Invoice Image {INVOICE_ID}:")
        print(json.dumps(labeled_data, sort_keys=True, indent=4))
    else:
        print(f"Failed to update labeled data for Invoice Image {INVOICE_ID}.")

```



#### Output

```
Response Status Code: 200
Response Text: {"issue_date": "2021-07-22", "external_id": "ex_id_e12bcf79-505d-4920-b8f6-d5da28b1acd7", "net_amount": 100.0, "business_number": "EUR-514713288", "total_amount": 117.0, "supplier_name": "Five Straps", "currency": "usd", "expense_type": "fuel", "payment_method": "credit_card", "vat_amount": 17.0, "document_type": "invoice_receipt", "document_number": "IL7890"}

Successfully updated the labeled data for Invoice Image ex_id_e12bcf79-505d-4920-b8f6-d5da28b1acd7:
{
    "business_number": "EUR-514713288",
    "currency": "usd",
    "document_number": "IL7890",
    "document_type": "invoice_receipt",
    "expense_type": "fuel",
    "external_id": "ex_id_e12bcf79-505d-4920-b8f6-d5da28b1acd7",
    "issue_date": "2021-07-22",
    "net_amount": 100.0,
    "payment_method": "credit_card",
    "supplier_name": "Five Straps",
    "total_amount": 117.0,
    "vat_amount": 17.0
}

```



The full example code is available here:

[Data Loop](https://github.com/tommyil/gemina-examples/blob/master/data_loop.py)



