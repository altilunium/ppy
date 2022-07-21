import sys
import whois
w = whois.whois(sys.argv[1])
print(w)