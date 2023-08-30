# LogReader

Authors: 
  [Peter Ashley](https://www.linkedin.com/in/petersouleashley/)

The purpose of this repository is to experment with ML AI based log ingestion and recognition

Basic steps planned involve:
- Identify or generate training data
  - Samples of different log types
  - Samples of different entity types (names, IPs, ports, numbers)
  - Schema definitions for different types of information (netflow, endpoint)
  - ChatGPT or other based sample data generation
- Classify a log as a different type (syslog, csv, windows, CEF ...)
- Split or parse basic fields into map using log type
- Entity recognition of data values and/or field names
- Classify log to a schema
- Guess mapping of field name/number to schema field

  
