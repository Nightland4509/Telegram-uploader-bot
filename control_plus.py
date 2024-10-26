import socket
import dns.resolver
import random
import string
from colorama import Fore, Style, init
import speedtest

# Initialize colorama
init(autoreset=True)

# List of common names for generating usernames
names = ["david", "john", "michael", "sarah", "jessica", "emma", "chris", "alex", "linda", "james"]

def get_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def get_nameservers(domain):
    try:
        resolver = dns.resolver.Resolver()
        resolver.lifetime = 5
        resolver.timeout = 5
        answers = resolver.resolve(domain, 'NS')
        nameservers = [str(rdata.target) for rdata in answers]
        return nameservers
    except Exception as e:
        print(f"{Fore.RED}Error fetching nameservers: {e}")
        return None

def web_scanner():
    while True:
        print(f"{Fore.RED}Enter domain (or type 'exit' to quit): {Style.RESET_ALL}", end="")
        domain = input(f"{Fore.GREEN}")
        
        if domain.lower() == 'exit':
            print("Exiting Web Scanner.")
            break
        
        ip_address = get_ip(domain)
        if ip_address:
            print(f"{Fore.BLUE}IP Address: {ip_address}")
        else:
            print(f"{Fore.BLUE}IP not found.")

        nameservers = get_nameservers(domain)
        if nameservers:
            print(f"{Fore.BLUE}Nameservers:")
            for ns in nameservers:
                print(f"{Fore.BLUE}{ns}")
        else:
            print(f"{Fore.BLUE}Nameservers not found.")
        
        retry = input(f"{Fore.RED}Enter '1' to try a new domain or any other key to return to main menu: {Style.RESET_ALL}")
        if retry != '1':
            break

def password_generator():
    while True:
        try:
            length = int(input(f"{Fore.RED}Enter password length (between 4 and 8): {Style.RESET_ALL}"))
            if 4 <= length <= 8:
                print(f"{Fore.BLUE}Generated Passwords:")
                for _ in range(20):
                    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
                    print(f"{Fore.BLUE}{password}")
                break
            else:
                print(f"{Fore.RED}Please enter a number between 4 and 8.")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a valid number.")

def username_generator():
    while True:
        try:
            length = int(input(f"{Fore.RED}Enter username length (between 5 and 13): {Style.RESET_ALL}"))
            if 5 <= length <= 13:
                print(f"{Fore.BLUE}Generated Usernames:")
                for _ in range(20):
                    name = random.choice(names)  # Select a common name
                    number_length = max(0, length - len(name))  # Calculate how many numbers to add
                    numbers = ''.join(random.choices("0123456789", k=number_length))
                    username = name + numbers
                    print(f"{Fore.BLUE}{username}")
                break
            else:
                print(f"{Fore.RED}Please enter a number between 5 and 13.")
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a valid number.")

def internet_speed_test():
    print(f"{Fore.YELLOW}Running speed test for 10 seconds...")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        print(f"{Fore.BLUE}Download speed: {download_speed:.2f} Mbps")
    except Exception as e:
        print(f"{Fore.RED}Error running speed test: {e}")

def main_menu():
    print(f"{Fore.YELLOW}")
    print("  _|_|_|    _|            _|                            ")
    print("  _|    _|  _|_|_|_|      _|_|_|_|    _|_|_|    _|_|_|  ")
    print("  _|    _|  _|    _|      _|    _|    _|    _|  _|    _| ")
    print("  _|    _|  _|    _|      _|    _|    _|    _|  _|    _| ")
    print("  _|_|_|    _|    _|      _|    _|    _|    _|  _|    _| ")
    print("                            _|    _|                    ")
    print(f"{Style.RESET_ALL}")

    while True:
        print(f"{Fore.YELLOW}Choose an option:")
        print("1. Website Scanner")
        print("2. Password Generator")
        print("3. Username Generator")
        print("4. Internet Speed Test")
        print("5. Exit")

        choice = input(f"{Fore.GREEN}Enter your choice: {Style.RESET_ALL}")
        
        if choice == '1':
            web_scanner()
        elif choice == '2':
            password_generator()
        elif choice == '3':
            username_generator()
        elif choice == '4':
            internet_speed_test()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
