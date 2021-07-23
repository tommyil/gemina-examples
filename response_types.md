# Gemina Response Types



## Full Json Response

```json
{
  "vat_amount": {
    "value": 228.41,
    "coordinates": {
      "normalized": [
        [
          189,
          909
        ],
        [
          241,
          910
        ],
        [
          241,
          924
        ],
        [
          189,
          923
        ]
      ],
      "original": [
        [
          251,
          1210
        ],
        [
          321,
          1211
        ],
        [
          321,
          1230
        ],
        [
          251,
          1228
        ]
      ]
    },
    "confidence": "high"
  },
  "document_type": {
    "value": "invoice",
    "coordinates": null,
    "confidence": "high"
  },
  "document_number": {
    "value": 7890,
    "coordinates": {
      "normalized": [
        [
          412,
          291
        ],
        [
          501,
          294
        ],
        [
          500,
          327
        ],
        [
          411,
          324
        ]
      ],
      "original": [
        [
          548,
          387
        ],
        [
          667,
          391
        ],
        [
          665,
          435
        ],
        [
          547,
          431
        ]
      ]
    },
    "confidence": "high"
  },
  "net_amount": {
    "value": 1343.59,
    "coordinates": {
      "normalized": [
        [
          173,
          880
        ],
        [
          244,
          880
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
          1171
        ],
        [
          325,
          1171
        ],
        [
          325,
          1192
        ],
        [
          230,
          1192
        ]
      ]
    },
    "confidence": "high"
  },
  "primary_document_type": {
    "value": "invoice",
    "coordinates": null,
    "confidence": "high"
  },
  "total_amount": {
    "value": 1572,
    "coordinates": {
      "normalized": [
        [
          157,
          938
        ],
        [
          242,
          938
        ],
        [
          242,
          959
        ],
        [
          157,
          959
        ]
      ],
      "original": [
        [
          209,
          1248
        ],
        [
          322,
          1248
        ],
        [
          322,
          1276
        ],
        [
          209,
          1276
        ]
      ]
    },
    "confidence": "high"
  },
  "external_id": "Form_64a1da38-6111-4561-8d99-f0dce152a63f_invoice.png",
  "issue_date": {
    "value": "31/08/2020",
    "coordinates": {
      "normalized": [
        [
          782,
          819
        ],
        [
          885,
          820
        ],
        [
          885,
          836
        ],
        [
          782,
          835
        ]
      ],
      "original": [
        [
          1041,
          1090
        ],
        [
          1178,
          1091
        ],
        [
          1178,
          1113
        ],
        [
          1041,
          1111
        ]
      ]
    },
    "confidence": "high"
  },
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
  },
  "supplier_name": {
    "value": "חמשת הפסים קלין בע\"מ",
    "coordinates": null,
    "confidence": "high"
  },
  "timestamp": 1624270976.531311,
  "created": "2021-06-21T10:22:56.531311"
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



#### 

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

