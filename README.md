This is a simple program which will parse the JSON file containing the details of Nobel prize winners between 1901 till 2019
and displays the result as below

[Sl number] Year ---> Name of the winner  -- field of contribution

For example:

[949] 1901 ---> Emil von Behring  -- awarded for medicine

The input file is ==> NobelLaurate.json

The entire details can be obtained from Nobel prize committe's website through a REST call as below


curl -X GET http://api.nobelprize.org/v1/prize.json?category=all&year=1900&yearto=2019

The output will be in JSON string format. You can copy the output in to a file called 'NobelLaurate.json'

