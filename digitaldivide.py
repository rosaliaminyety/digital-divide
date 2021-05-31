class Market(object):

    def __init__(self, state, market_name, street_address, zip_code, city):
        self.state = state
        self.market_name = market_name
        self.street_address = street_address
        self.zip_code = zip_code
        self.city = city

    def __str__(self):
        return "{}<br/>{}<br/>{}, {} {}".format(self.market_name, \
            self.street_address, self.city, self.state, self.zip_code)
        
    def __repr__(self):
        return str(self)

def read_markets(filename):

    f = open(filename,'r')
    
    market_dictionary = {}

    for line in f:
        new_line = line.strip().split('#')
        
        market_instance = Market(new_line[0], new_line[1], new_line[2], \
                                 new_line[4], new_line[3])
        
        if new_line[4] not in market_dictionary:
            market_dictionary[new_line[4]] = [market_instance]
        
        else:
            market_dictionary[new_line[4]].append(market_instance)
    
    return market_dictionary
    
def main():
    
    variable = read_markets("digitaldivide.txt")
    
    user_zip_code = 12345
    
    while user_zip_code != "quit":
        user_zip_code = input("Enter a 5 digit zip code: ")
        
        if user_zip_code == "":
            continue
        
        if user_zip_code in variable:
            
            for market_variable in variable[user_zip_code]:
                if len(variable[user_zip_code]) == 1:    
                    print(market_variable)
                else:
                    print(market_variable)
                    print("\n")
                
        elif user_zip_code == "quit":
            break
        
        else:
            print("No places found in your zip code.")
    
    return

if __name__ == "__main__":
    

    main()