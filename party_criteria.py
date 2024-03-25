"""
2.1 Write a python function named “register_party” that takes a list of parties. Each party 
must be presented by key value pairs. The keys should be “party_name”, “reg_number”, 
“member_count”). The function should check if the new party has acceptable number of 
members for it to be registered as per the requirements narrated in the scenario. Note: this 
function must be written under the git branch that you created in question 1.4 above.
"""

"""
2.2 Now a new party called MK party which has 5300 members wants to apply to register the 
party for the next election. Write python statements that will show how will the function that 
you created in question 2.1 be executed such that it registers the MK party if it meets the 
criteria as per IEC regulations. Assume that the last party that was registered had a registration 
number 10003318, and every new party that is being registered will be generated a registration 
number that increments the last registered party by 1. 
"""

def register_party(list_of_parties):

    if list_of_parties['member_count'] > 1000:
        print("New party has an acceptable number of members for it to be registered.")
        list_of_parties['reg_number']+=1
    else:
        print("The number of members is below the required number")

    return list_of_parties['member_count'] > 1000

answer = register_party({'party_name':'AFF','reg_number':10003318,'member_count':500})
result = register_party({'party_name':'MK party','reg_number':10003318,'member_count':5300})
print(answer)
print(result)
