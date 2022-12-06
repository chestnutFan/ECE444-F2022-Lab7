# ECE444-F2022-Lab7 
Deployed a machine learning model to the cloud using AWS Elastic Beanstalk. Input a sentence and the API will judge whether it's fake news or not (return 0 if real, and 1 if fake).
## Test 1
| Test Input                                                | Expected Response | Actual Response | Average Latency Over 100 Calls |
| --------------------------------------------------------- | ----------------- |-----------------| ------------------------------ |
| “Mark Zuckerberg is unveiled to be an alien.”             | 1                 |   1             | 118 ms                         |

## Test 2
| Test Input                                                | Expected Response | Actual Response | Average Latency Over 100 Calls |
| --------------------------------------------------------- | ----------------- |-----------------| ------------------------------ |
| “UofT has changed its full name to University of Tears.”  | 1                 |   1             | 121 ms                         |

## Test 3
| Test Input                                                             | Expected Response | Actual Response | Average Latency Over 100 Calls |
| ---------------------------------------------------------------------- | ----------------- |-----------------| ------------------------------ |
| “The Federal Reserve will continue to raise interest rates in 2023.”   | 0                 |   0             | 120 ms                         |

## Test 4
| Test Input                                                             | Expected Response | Actual Response | Average Latency Over 100 Calls |
| ---------------------------------------------------------------------- | ----------------- |-----------------| ------------------------------ |
| “Salesforce Co-CEO Bret Taylor is going to step down.”                 | 0                 |   0             | 121 ms                         |


