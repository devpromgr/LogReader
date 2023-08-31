# LogReader

Authors: 
  [Peter Ashley](https://www.linkedin.com/in/petersouleashley/)

The purpose of this repository is to experment with ML AI based log ingestion and recognition

Use Case:
- As a skilled security engineer, I want to make a custom integration for my uncommon devices log information, so that it may be processed in standardized way by using known security information schemas.

Example: 

Authentication request succeeded syslog from Fortinet NAC:
02-28-2014 08:16:04 Auth.Notice 192.168.34.31 Feb 27 22:16:14 : 2014/02/27 22:16:14 EST,1,545570,Login Success,0,12,,,,,User root logged in.

Requirements:
- Assists a user an analyzing and constructing a log parser to turn characters into actionable information
- Takes in various forms of logs, identifies log type, field and then proposes relevant schema and field mapping
- Low volume, minimal performance requirements
- Results will be proposed and the expectation is that review and revision will be required to achieve correctness.
- Minimization of custom engineering, use high level tools like Spark. 

Basic steps planned involve:
- Identify or generate training data
  - Samples of different log types
  - Samples of different entity types (names, IPs, ports, numbers)
  - Schema definitions for different types of information (netflow, endpoint)
  - ChatGPT or other based sample data generation
- Classify a log as a different type (syslog, csv, windows, CEF ...)
	- Convert most non-whitespace into word tokens
	- Simple bag of words type classification should be enough, or ChatGPT web call.
- Split or parse basic fields into map using log type
	- Eg CSV decode or CEF decode
- Entity recognition of data values and/or field names
	- Convert common regex type matches into type token 1.1.1.1 -> IP
	- Recognize dates, Integers
- Classify log to a schema
	- bag of words, skip gram, might be enough, but may also need more advanced word2vec, etc.
- Define and Enhance schemas
	- Additional metadata such as entity type may be required.
- Guess mapping of field name/number to schema field
	- e.g. first IP goes into first IP in schema, etc.
	- Port (e.g. number following IP)

  
