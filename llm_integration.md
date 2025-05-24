# Gemina LLM Integration Guide

## Introduction

Gemina is excited to announce the integration of Large Language Model (LLM) technology into our Automated Invoice Data Capture service. This cutting-edge feature enhances our ability to process Hebrew financial documents with unprecedented accuracy.

## Key Improvements

- **Increased Accuracy**: Up to 10% improvement in key fields, with overall accuracy boosted from 85-87% to 90-95%.
- **Advanced Confidence Scoring**: Our new scoring system provides highly reliable confidence levels for predictions.
- **Continuous Learning**: Faster improvement cycles when using our feedback loop.

## Implementation

### How to Activate LLM

To use the LLM-powered analysis, simply add the following line to your [JSON payload](https://github.com/tommyil/gemina-examples?tab=readme-ov-file#step-1---upload-invoice):

```json
"use_llm": true
```

For example:
```json
{ 
    "external_id": "ext_id", 
    "client_id": "Your Client Id", 
    "url": "http://www.website.com/blob/your_invoice_image_url.jpg", 
    "client_business_number": "123456789",
    "use_llm": true  // <-- add that
}
```

### Performance Considerations

While the LLM model provides superior accuracy, it does require more processing time:
* Standard processing: 2-3 seconds per document
* LLM processing: 4-6 seconds per document

This makes the LLM feature ideal for reactive use cases where real-time results aren't critical.

## Benefits

1. **Higher Accuracy**: Significant improvements in fields like Business Number, Document Number, Supplier Name, and Issue Date.
2. **Reliable Automation**: High-confidence results can be directly integrated into your systems without manual verification.
3. **Adaptive Learning**: The model improves faster with consistent use of our [feedback loop](https://github.com/tommyil/gemina-examples/blob/master/data_loop.md).

## Best Practices

* Use LLM for tasks where accuracy is more critical than speed.
* Implement the feedback loop to continually improve the model's performance for your specific use cases.
* For time-sensitive operations, consider using our standard models and reserving LLM for more complex or important documents.

## Support

For detailed integration instructions or support, please visit: [https://www.gemina.co.il/contact](https://www.gemina.co.il/contact)

Our team is available to assist you with implementing this new feature and optimizing it for your specific needs.

---

Gemina: Leading the way in AI-powered Hebrew financial document processing.


------



## More Resources



Response Types - https://github.com/tommyil/gemina-examples/blob/master/response_types.md

Data Loop - https://github.com/tommyil/gemina-examples/blob/master/data_loop.md

Line Item Integration - https://github.com/tommyil/gemina-examples/blob/master/line_items.md

Python Implementation - https://github.com/tommyil/gemina-examples

C# Implementation - https://github.com/tommyil/gemina-examples-cs

Node.js/TypeScript Implementation - https://github.com/tommyil/gemina-examples-ts

