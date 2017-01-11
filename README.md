# Price Formatter

Function that converts string, integer or float value  to easy-viewer price format. 
 
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

For proper working the format_price function is tested on correct input type value, format values and output string value. Values input test cases  are showed in a table below:   

|                                     INPUT VALUES                                    	| CORRECT SCRIPT STATUS  |
|:-----------------------------------------------------------------------------------:	|:----------------------:|
| ints, floats, strings with comma and dot separators                            	|     OK     			 |
| types except string, int and float                                                	| raises TypeError 	     |
| strings containing letters, double separators and other symbols, negative ints and floats  	| raises ValueError|



## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)