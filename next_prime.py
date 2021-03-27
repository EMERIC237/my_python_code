def is_prime(x):
    if x == 2:
        return True
    if x%2 == 0:
        return False
    for i in range(3,int(x**0.5),2):
        if x%i == 0:
            return False
            
    return True
    
    
def genprime(current_prime):
    new_prime = current_prime+1
    
    while True:
        if not is_prime(new_prime):
            new_prime += 1
        else:
            break
    return new_prime

def main():
    current_prime = 2
    
    while True:
        answer = input("would you like to see the next prime number(yes/no)? ")
        if answer.lower().startswith('y'):
            print(current_prime)
            current_prime = genprime(current_prime)
        else:
            break
if __name__ == '__main__':
    main()
