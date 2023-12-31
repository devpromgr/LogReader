# LogReader

Authors: 
  [Peter Ashley](https://www.linkedin.com/in/petersouleashley/)

The purpose of this repository is to experment with ML AI based log ingestion and recognition, in particular attempting to use fast.ai deep learning more that traditional methods (e.g. word frequency features) for use cases of log information processsing. 

Use Case:
- As a skilled security engineer, I want to make a custom integration for a device's log information, so that it may be processed in a standardized way by using known security information schemas. For example, use a stardard schema with various logs to write an analytic to alert on N+ failed login attempts followed by success.

Example Log: 

Authentication request succeeded syslog from Fortinet NAC:
02-28-2014 08:16:04 Auth.Notice 192.168.34.31 Feb 27 22:16:14 : 2014/02/27 22:16:14 EST,1,545570,Login Success,0,12,,,,,User root logged in.

Requirements:
- Assists a user in analyzing and constructing a log parser to turn characters into actionable information.
- Takes in device logs, identifies log type, field/entity types and then proposes a relevant schema and field mapping.

## Experiment 1 : Identify log format type (syslog, CEF, etc.) 

Log format identification was accomplished most simply with regex matching as many of the logs have formats that can be identified by signature. Sample python code was generated in a notebook that can be run on kaggle to identify the type of log.

- Kaggle URL	: https://www.kaggle.com/code/peterashley/determinelogtype
- notebook		: notebooks\determinelogtype.ipynb
- test data		: TrainingSources\LogfilesByType.csv

## Experiment 2 : Determine log device type

Identification of the log source device with deep learning was accomplished by gathering a number of log types from internet resources, especially from logpai/loghub github listed in reference section. These logs were chunked and then truncated, placed into folders by type to make a training dataset. The folder name is used as a label. The notebook makes a fast.ai pretrained text classification learner, retrains then validates it. Test phase shows 99% accuracy.

- Kaggle URL	: https://www.kaggle.com/peterashley/classifylogdevicetypes
- notebook		: notebooks\classifylogdevicetypes.ipynb
- test data		: TrainingData\logDeviceTypesVerySmall

Results: Training and test prediction

epoch	train_loss	valid_loss	accuracy	time
0	1.787571	1.282640	0.750000	00:08
epoch	train_loss	valid_loss	accuracy	time
0	0.975311	0.967853	0.880952	00:12
1	0.814063	0.392149	0.976190	00:11
2	0.684892	0.138656	0.988095	00:12
3	0.585866	0.089036	0.988095	00:12

This is a Linux file with probability 0.9866

('Linux',
tensor(5),
tensor([3.2136e-03, 1.0244e-03, 1.6429e-06, 9.5284e-05, 7.1151e-03, 9.8660e-01,
		5.0567e-04, 1.3690e-03, 3.9699e-06, 7.4702e-05]))

## Experiment 3 : Entity identification (data = IP address, name, number, date...)

Plan: Use OpenAI API to ChatGTP to generate training multiple types of entities, including some "trash" types for nonstandard tokens to bin into. Fragmentation of existing files can also be used to generate data to manually label for training. The neural net is used to train on dataset and then apply to tokens/words parsed out of log file. 

- Data Generation	: https://github.com/devpromgr/LogReader/blob/main/TrainingData/entitySamples/generateEntitySamples.py
- Generated data	: https://github.com/devpromgr/LogReader/blob/main/TrainingData/entitySamples/entityData.csv
- Kaggle URL		: 
- notebook			: 

## Experiment 4 : Log to schema mapping

Ideally I'd like to use existing logs labeled with schema type to match, but may not be able to get this data for publicly available sources. I can write the notebook and then hand off to some friends with proprietary data to test on.

- Kaggle URL	: 
- notebook		: 

## Reference:
- https://ossec.net/docs/log_samples/
- https://github.com/logpai/loghub
- https://docs.ctpx.secureworks.com/integration/customParsers/schema_antivirus/




  
