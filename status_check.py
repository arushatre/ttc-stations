#someone's an MP has to be a canadian citizen and at least 18 yrs old
#a senator must be a cad. citizen, at least 30yrs, and under 75, and must have a networth of at least $4000


def mp_elig(is_citizen, age):
    min_age = 18
    result = is_citizen and age >= min_age
    return result

def senator_elig(is_citizen, age, net_worth):
    min_age = 30
    netW = 4000
    result = is_citizen and age >= min_age and net_worth >= netW


def main():
    is_citizen = True
    age = 55
    net_worth = 5000

can_be_mp = None
can_be_senator = None

print("Eligible to be an MP?", can_be_mp)
print("Eligible to be a senator?", can_be_senator)

main()