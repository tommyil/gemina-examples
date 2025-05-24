# Gemina Response Types



## Full Json Response

```json
{
    "assignment_number": {
        "confidence": "high",
        "coordinates": null,
        "value": null
    },  
    "business_number": {
        "confidence": "high",
        "coordinates": {
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
            ],
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
            "relative": [
                [
                    0.15,
                    0.11
                ],
                [
                    0.25,
                    0.11
                ],
                [
                    0.25,
                    0.13
                ],
                [
                    0.15,
                    0.13
                ]
            ]
        },
        "value": 514713288
    },
    "created": "2022-01-05T14:46:29.397518",
    "currency": {
        "confidence": "medium",
        "coordinates": null,
        "value": "ils"
    },
    "document_number": {
        "confidence": "high",
        "coordinates": {
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
            ],
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
            "relative": [
                [
                    0.33,
                    0.16
                ],
                [
                    0.4,
                    0.17
                ],
                [
                    0.4,
                    0.19
                ],
                [
                    0.33,
                    0.18
                ]
            ]
        },
        "value": 7890
    },
    "document_type": {
        "confidence": "high",
        "coordinates": null,
        "value": "invoice"
    },
    "expense_type": {
        "confidence": "medium",
        "coordinates": null,
        "value": "other"
    },
    "external_id": "ex_id_37a328f0-7aac-4fac-8bd5-00fef6459cc3",
    "issue_date": {
        "confidence": "high",
        "coordinates": {
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
            ],
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
            "relative": [
                [
                    0.63,
                    0.46
                ],
                [
                    0.71,
                    0.47
                ],
                [
                    0.71,
                    0.48
                ],
                [
                    0.63,
                    0.48
                ]
            ]
        },
        "value": "31/08/2020"
    },
    "net_amount": {
        "confidence": "high",
        "coordinates": {
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
            ],
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
            "relative": [
                [
                    0.14,
                    0.5
                ],
                [
                    0.2,
                    0.5
                ],
                [
                    0.2,
                    0.51
                ],
                [
                    0.14,
                    0.51
                ]
            ]
        },
        "value": 1343.59
    },
    "payment_method": {
        "confidence": "medium",
        "coordinates": null,
        "value": "wire_transfer"
    },
    "primary_document_type": {
        "confidence": "high",
        "coordinates": null,
        "value": "invoice"
    },
    "supplier_name": {
        "confidence": "high",
        "coordinates": null,
        "value": "\u05d7\u05de\u05e9\u05ea \u05d4\u05e4\u05e1\u05d9\u05dd \u05e7\u05dc\u05d9\u05df \u05d1\u05e2\"\u05de"
    },
    "timestamp": 1641393989.397518,
    "total_amount": {
        "confidence": "high",
        "coordinates": {
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
            ],
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
            "relative": [
                [
                    0.13,
                    0.53
                ],
                [
                    0.2,
                    0.53
                ],
                [
                    0.2,
                    0.55
                ],
                [
                    0.13,
                    0.55
                ]
            ]
        },
        "value": 1572.0
    },
    "vat_amount": {
        "confidence": "high",
        "coordinates": {
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
            ],
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
            "relative": [
                [
                    0.15,
                    0.52
                ],
                [
                    0.19,
                    0.52
                ],
                [
                    0.19,
                    0.53
                ],
                [
                    0.15,
                    0.53
                ]
            ]
        },
        "value": 228.41
    }
}
```



## Predicated Value

The Predicted Value is nested within the full json response. Each one of the returned values is represented by this field.



#### Values:

**Original Coordinates:** Integer coordinates for the designated value within the uploaded image. If the system fails to identify the coordinates, this value is set to null.

**Normalized Coordinates:** The same, but within the processed cloud-image, which has been normalized in terms of width and height.

**Relative Coordinates:** The same coordinates, normalized as a relative percentage from the top left. The range is from 0 to 1. For example: the middle-point of the document is represented by the coordinate (0.5, 0.5).

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



#### Assignment Number

Number represented as string - with 9 digits or more



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

The document's used currency.

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



#### Expense Type

This field represents the expense-classification and contains one of the following values:

```json
[
    "other",
    "fuel",
    "office",
    "travel",
    "merchandise",
    "professional_services_and_subcontractors",
    "advertising_and_promotion",
    "vehicle_maintenance_and_transport",
    "mail_and_communication",
    "taxes_and_fees",
    "rent_and_property_management",
]
```



#### Payment Method

This field provides the used payment-method.

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

Errors are returned in a constructed Json format, and are assigned with a coresponding status code.

 

#### Field Names

By and large, the errors contain the following fields:



- ##### Message  (`message` in the Json)


Contains a short  description of the failure reason.



- ##### Success (`success` in the Json)


Indicated whether an operation was successful or not. With errors, it always defaults to false.



- ##### Type (`type` in the Json)

When this field contains a value, it is recommended to forward this info to the end user.

We usually populate the type in the event of PDF and image errors. In other words  - unprocessable data that users upload.

Here's the full list of types:

```python
[
    "pdf_error", # Unable to process PDF due to an error
    "thumbnail_error", # Unable to process Image thumbnail due to an error
    "not_an_image_file_error", # The uploaded file is not a valid image / PDF file
    "max_pixels_error", # The PDF image exceeds limit of 89478485 pixels.
    "image_file_is_truncated_error", # the image file is truncated and cannot be processed.
    "pdf_early_processing_failed_error" # Unable to process PDF due to an error.
    "pdf_max_pages_exceeded_error",# The PDF contains more than 6 pages, and cannot be processed.
]
```



Example:

```json
{
  "external_id": "Form_cccb3c58-35d5-468f-b7c9-5c6e4b15a6c8_Document.pdf",
  "client_id": 65,
  "type": "not_an_image_file_error",
  "message": "Failed to predict for Image Form_cccb3c58-35d5-468f-b7c9-5c6e4b15a6c8_Document.pdf: Unprocessable Error: Not an Image File Error: Image Form_cccb3c58-35d5-468f-b7c9-5c6e4b15a6c8_Document.pdf is not an image file.",
  "success": false
}
```



#### Exceptions to Error Format

There are exceptions where API calls are rejected in preceding layers, prior to the API Views Layer (where calls are usually handled). In that case, multiple errors will be stored in the `message` field and the structure will be plain.

In addition, a 422 error code ("*Unprocessable Entity*") will be assigned to the response.



Example:

```json
{
    "message": {
        "json": {
            "url": [
                "Not a valid URL."
            ],
            "client_id": [
                "Not a valid integer."
            ]
        }
    },
    "success": false
}
```



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

```json
{
  "external_id": "Form_cccb3c58-35d5-468f-b7c9-5c6e4b15a6c8_Document.pdf",
  "client_id": 65,
  "type": "not_an_image_file_error",
  "message": "Failed to predict for Image Form_cccb3c58-35d5-468f-b7c9-5c6e4b15a6c8_Document.pdf: Unprocessable Error: Not an Image File Error: Image Form_cccb3c58-35d5-468f-b7c9-5c6e4b15a6c8_Document.pdf is not an image file.",
  "success": false
}
```

<u>422 Unprocessable Entity:</u> The request was well-formed but was unable to be followed due to semantic errors. {'client_business_number': ['Must be greater than or equal to 10000000 and less than or equal to 999999999.']}

And more...

Generally, it is safe to assume that 422 responses can be forwarded to the end user.



**Status Codes from 500 to 599:**

There is an internal problem within the Gemina servers, i.e. the problem is on our end and should be fixed by us.

If you encounter one such error, please inform us immediately.



------



## More Resources



Data Loop - https://github.com/tommyil/gemina-examples/blob/master/data_loop.md

LLM Integration - https://github.com/tommyil/gemina-examples/blob/master/llm_integration.md

Line Item Integration - https://github.com/tommyil/gemina-examples/blob/master/line_items.md

Python Implementation - https://github.com/tommyil/gemina-examples

C# Implementation - https://github.com/tommyil/gemina-examples-cs

Node.js/TypeScript Implementation - https://github.com/tommyil/gemina-examples-ts
