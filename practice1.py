letter = ''' Dear <|Name|>,
            you are selected!
            <|Date|> '''

print(letter.replace("<|Name|>", "Qasim").replace("<|Date|>" ,"24 sep 2025"))