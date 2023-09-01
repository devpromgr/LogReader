# LogReader

Authors: 
  [Peter Ashley](https://www.linkedin.com/in/petersouleashley/)

The purpose of this repository is to experment with ML AI based log ingestion and recognition, in particular attempting to use fast.ai deep learning more that traditional methods (e.g. word frequency features)

Use Case:
- As a skilled security engineer, I want to make a custom integration for a device's log information, so that it may be processed in standardized way by using known security information schemas. For example, N+ failed login attempts followed by success.

Example Log: 

Authentication request succeeded syslog from Fortinet NAC:
02-28-2014 08:16:04 Auth.Notice 192.168.34.31 Feb 27 22:16:14 : 2014/02/27 22:16:14 EST,1,545570,Login Success,0,12,,,,,User root logged in.

Requirements:
- Assists a user an analyzing and constructing a log parser to turn characters into actionable information
- Takes in various forms of logs, identifies log type, field and then proposes relevant schema and field mapping
- Low volume, minimal performance requirements
- Results will be proposed and the expectation is that review and revision will be required to achieve correctness.
- Minimization of custom engineering, use high level tools like Spark. 

Plan: Basic steps involve:
- Identify or generate training data
  - Samples of different log types. (see references)
 	- Samples to determine format
	- Samples to determine schema
  - Samples of different entity types (names, IPs, ports, numbers) ChatGPT can help generate
  - Schema definitions for different types of information (netflow, endpoint)
	- Can draw from https://docs.ctpx.secureworks.com/integration/customParsers/schema_antivirus/
- Classify a log as a different type (syslog, csv, windows, CEF ...)
	- Convert most non-whitespace into word tokens
	- Use fast.ai model from lesson 3/4
		- Or simple bag of words type classification should be enough
- Split or parse basic fields into map using log type
	- Eg CSV decode or CEF decode
- Entity recognition of raw data values and/or field names
	- Convert common regex type matches into type token 1.1.1.1 -> IP
	- CEF with field names can maintain simple map of common names -> entity type
	- Dates may be a pain with many formats and whitespace embedded
- Classify log to a schema
	- bag of words, skip gram, might be enough, but may also need more advanced word2vec, etc.
	- might be easiest to generate samples of data that have a schema label and classify with deep learning
- Define and Enhance schemas
	- Create simple schemas base on use case with entity metadata (entity type, etc)
- Guess mapping of field name/number to schema field
	- e.g. first IP goes into first IP in schema, etc.
	- Port (e.g. number following IP)
- Package into gradio web applet
	- Past or drag log, present predicted type, parsed field map, predicted schema and proposed mapping
	
Reference:
- https://ossec.net/docs/log_samples/
- https://github.com/logpai/loghub
- https://docs.ctpx.secureworks.com/integration/customParsers/schema_antivirus/




  
