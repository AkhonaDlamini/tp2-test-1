list_of_parties = []

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


"""
2.3 Implement a function called “update_voter_info” where each key is a voter_id and the 
value is another dictionary containing name, voting_district and has_voted. The function 
should update the voter's information or add a vote if not already voted. Very important hint: 
you should think of best practices for source code management and collaboration using git, 
for instances; is it a good practice to answer this question under the directories that are already 
existing or you should create a feature branch for development. From this question onwards 
you won't be guided like you have been on questions prior to this. Always think best practices 
for software development as discussed in class. Create a new file, new directory, new feature 
branch where necessary.   
"""

def update_voter_info(voter_id,name,voting_district,has_voted):

    list_of_parties.append({'Voter Id':{'Name':name,'District':voting_district,'Has Voted:':has_voted}})
    return list_of_parties

voter_id = input("Enter your id number:")
name = input("Enter your name:")
voting_district = input("Enter the district you are voting in:")
has_voted = input("Have you voted:")
