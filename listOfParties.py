"""
2.4 Using list comprehension and the filter function, write a piece of code that filters out all 
parties from a given list that have less than 1,000 members. Use ALL the parties that are on 
the ballot paper in Annexure A as your list elements, only capture their abbreviation as 
elements e.g. capture EFF on your list of elements instead of “Economic Freedom Fighters” 
as it is displayed using EFF abbreviation on the ballot paper.
 """

list_of_parties ={
    'party_name':['ASC','ATM','AASD','ANC','AGANG SA','ALJAMA','ATA,','AZAPO','APC','BRA','BLF','ZACP','CPM','CSA','COPE','DA','DLC','ECOFORUM','F4SD','FREE DEMS'],
    'reg_number':[10003318,10003319,10003320,10003321,10003322,10003323,10003324,10003325,10003326,10003327,10003328,10003329,10003330,10003331,10003332,10003333,10003334,10003335,10003336,10003337],
    'member_count':[300000,2500,100,500000,250,500,12,8,10,670,900,2200,5679,90,3000,5000,6700,6890,2000,1457]
}

filtered_list = list(filter([list_of_parties['member_count'] for list_of_parties['member_count'] in list_of_parties if list_of_parties['member_count']< 1000]))
print(filtered_list)