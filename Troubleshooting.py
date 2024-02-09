#!/usr/bin/env python3
from NetFunctions import ping_host, dns_lookup, check_port

def main():
    print("Welcome to Networking Tools!\n")
    while True:
        print("Select an option:")
        print("1. Ping a host")
        print("2. Perform a DNS lookup")
        print("3. Check port status")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            host = input("Enter the host to ping: ")
            ping_host(host)
        elif choice == "2":
            hostname = input("Enter the hostname to perform DNS lookup: ")
            dns_lookup(hostname)
        elif choice == "3":
            host = input("Enter the host to check port status: ")
            port = int(input("Enter the port to check: "))
            check_port(host, port)
        elif choice == "4":
            print("Exiting Networking Tools. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()