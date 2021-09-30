# Gemina Response Types



## Full Json Response

```json
{
  "total_amount": {
    "coordinates": {
      "original": [
        [
          208,
          1246
        ],
        [
          322,
          1246
        ],
        [
          322,
          1275
        ],
        [
          208,
          1275
        ]
      ],
      "normalized": [
        [
          156,
          936
        ],
        [
          242,
          936
        ],
        [
          242,
          958
        ],
        [
          156,
          958
        ]
      ]
    },
    "value": 1572,
    "confidence": "high"
  },
  "vat_amount": {
    "coordinates": {
      "original": [
        [
          251,
          1206
        ],
        [
          321,
          1207
        ],
        [
          321,
          1231
        ],
        [
          251,
          1230
        ]
      ],
      "normalized": [
        [
          189,
          906
        ],
        [
          241,
          907
        ],
        [
          241,
          925
        ],
        [
          189,
          924
        ]
      ]
    },
    "value": 228.41,
    "confidence": "high"
  },
  "created": "2021-08-19T14:28:49.938383",
  "timestamp": 1629383329.938383,
  "primary_document_type": {
    "coordinates": null,
    "value": "invoice",
    "confidence": "high"
  },
  "external_id": "Form_610845c3-43a7-43b7-8fb8-b8bb2ca17f25_invoice.png",
  "currency": {
    "coordinates": null,
    "value": "ils",
    "confidence": "medium"
  },
  "business_number": {
    "coordinates": {
      "original": [
        [
          242,
          265
        ],
        [
          405,
          268
        ],
        [
          405,
          297
        ],
        [
          242,
          294
        ]
      ],
      "normalized": [
        [
          182,
          199
        ],
        [
          304,
          201
        ],
        [
          304,
          223
        ],
        [
          182,
          221
        ]
      ]
    },
    "value": 514713288,
    "confidence": "high"
  },
  "issue_date": {
    "coordinates": {
      "original": [
        [
          1041,
          1086
        ],
        [
          1178,
          1090
        ],
        [
          1176,
          1117
        ],
        [
          1039,
          1113
        ]
      ],
      "normalized": [
        [
          782,
          816
        ],
        [
          885,
          819
        ],
        [
          884,
          839
        ],
        [
          781,
          836
        ]
      ]
    },
    "value": "31/08/2020",
    "confidence": "high"
  },
  "document_type": {
    "coordinates": null,
    "value": "invoice",
    "confidence": "high"
  },
  "document_number": {
    "coordinates": {
      "original": [
        [
          548,
          385
        ],
        [
          667,
          389
        ],
        [
          665,
          434
        ],
        [
          547,
          430
        ]
      ],
      "normalized": [
        [
          412,
          289
        ],
        [
          501,
          292
        ],
        [
          500,
          326
        ],
        [
          411,
          323
        ]
      ]
    },
    "value": 7890,
    "confidence": "high"
  },
  "net_amount": {
    "coordinates": {
      "original": [
        [
          230,
          1167
        ],
        [
          325,
          1167
        ],
        [
          325,
          1192
        ],
        [
          230,
          1192
        ]
      ],
      "normalized": [
        [
          173,
          877
        ],
        [
          244,
          877
        ],
        [
          244,
          896
        ],
        [
          173,
          896
        ]
      ]
    },
    "value": 1343.59,
    "confidence": "high"
  },
  "supplier_name": {
    "coordinates": null,
    "value": "חמשת הפסים קלין בע\"מ",
    "confidence": "high"
  }
}
```



## Predicated Value

The Predicted Value is nested within the full json response. Each one of the returned values is represented by this field.



#### Values:

**Original Coordinates:** Integer coordinates for the designated value within the uploaded image. If the system fails to identify the coordinates, this value is set to null.

**Normalized Coordinates:** The same, but within the processed cloud-image, which has been normalized in terms of width and height.

**Value:** The predicted value

**Confidence:** The assessed confidence level of the prediction



Confidence Levels:

```json
[
	"high",
	"medium",
	"low"
]
```



Example:

```json
 "business_number": {
    "value": 514713288,
    "coordinates": {
      "normalized": [
        [
          182,
          200
        ],
        [
          304,
          202
        ],
        [
          304,
          223
        ],
        [
          182,
          221
        ]
      ],
      "original": [
        [
          242,
          266
        ],
        [
          405,
          269
        ],
        [
          405,
          297
        ],
        [
          242,
          294
        ]
      ]
    },
    "confidence": "high"
  }
```





## String Field Types



#### Supplier Name

The Name of the supplier or the document issuer



## Non-String Field Types



#### Issue Date

Date Type in European Format - `dd//mm//yyyy`



#### Business Number

Integer from 5 to 11 digits



#### Document Number

Long Integer



#### Total Amount, Net Amount , VAT Amount

Floats



#### Document Type

Possible Values:

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



#### Primary Document Type

This field was created to simplify post-processing for some vendors. It can largely be ignored.



Possible Values:

```json
[
    "unknown",
    "invoice",
    "delivery_note",
    "payment_confirmation",
    "credit_note"
]
```



#### Currency

This will provide the document's used currency.

Optional values:

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





## Future Fields

These fields are not yet supported, but will be available in the near future



#### Expense Type

This will represent the expense classification and will contain one of the following values:



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



#### Payment Method

This will provide the used payment method.

Optional values:



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





## Errors

Errors are returned in a constructed Json format, and are assigned with the coresponding status code.

 

#### Field Names

By and large, the errors contain the following fields:



##### 1. Message

Contains a short  description of the failure reason.

In the Json body is appears at `message`.



##### 2. Success

Indicated whether an operation was successful or not. In errors, it will always be set to false.

In the Json body it appears as `success`.



#### Exceptions

There are exceptions where API calls are rejected in preceding layers, prior to the API Views Layer (where calls are usually handled). In that case, multiple errors will be stored in the `messages` field and the structure will be plain. In addition, a 422 error code ("*Unprocessable Entity*") will be assigned to the response.



#### Error Codes

The most important status of Error Responses are the Error Response Codes. These will reveal the nature of the error and the way you should handle it.

To a large extent, Gemina follows industry standards and common practices when error codes are assigned.



As a rule of thumb:



**Status Codes from 200 to 299:**

The request has been processed successfuly.



**Status Codes from 400 to 499:**

There is a problem either with the uploaded document, or the API is not used properly.

In other words, the problem is on your end and under your responsibility.

Common errors include, but not limited to:

<u>401 - Illegal Credential</u>s

<u>422 - Invoice page-length cannot be longer than 6 pages.</u>

```
{
  "external_id": "Form_9799f10d-eb5c-4abb-9e68-ccd6255ba69f_Document.pdf",
  "client_id": 65,
  "message": "Failed to predict for Image Form_9799f10d-eb5c-4abb-9e68-ccd6255ba69f_Document.pdf: Unprocessable Error: PDF Error: Invoice page-length cannot be longer than 6 pages. Image Id: Form_9799f10d-eb5c-4abb-9e68-ccd6255ba69f_Document.pdf",
  "success": false
}
```

<u>422 Unprocessable Entity:</u> The request was well-formed but was unable to be followed due to semantic errors. {'client_business_number': ['Must be greater than or equal to 10000000 and less than or equal to 999999999.']}

And more...

Generally, it is safe to assume that 422 responses can be forwarded to the end user.



**Status Codes from 500 to 599:**

There is an internal problem within the Gemina servers, i.e. the problem is on our end and should be fixed by us.

If you encounter one such error, please inform us immediately.

