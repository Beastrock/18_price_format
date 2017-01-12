# Price Formatter

Function that converts string, integer or float value  to easy-viewer price format string. 
 
## Getting Started  

Clone repository:   
`$ git clone https://github.com/Beastrock/18_price_format.git`    

## Usage
###Adding to projects:  
`from format_price import format_price`  
`formatted_price = format_price(price_value)`   

###Manually from console:
 
`python format_price.py --price PRICE`   


## Tests  

To run tests:  
`python tests.py`

To work correctly the format_price function is tested on input type values, input  values format and output string type:  

|      TEST CASES      	|                                   INPUT VALUES                                   	| STATUS \ RAISED ERROR |
|:--------------------:	|:--------------------------------------------------------------------------------:	|:---------------------:|
|   Valid types  	|                              integer, float, string                              	| OK                    |
|  Invalid types 	|             Types except string, int and float. In this case - list.             	| TypeError             |
|  Valid format  	|                        string with comma, string with dot                        	| OK                    |
| Invalid format 	| negative number, string containing letters,</br> string with double separators  	| ValueError            |
|   Output string type  	|                 Any valid types and formats. In this case - int.                 	| OK                    |  


## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)