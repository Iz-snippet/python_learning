# # write a program to fill in a  letter template given below with name and date.
# letter_template =Dear {name},
#  your are selected
# Date: {date}
# Thank you
# 

letter=""" Dear <|name|> 
your are selected
Date: <|date|>
Thank you
"""

print(letter.replace("<|name|>", "Ishake" ).replace("<|date|>", "10/10/2023" ))
