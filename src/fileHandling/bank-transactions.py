# Get the filepath from the command line
import sys
F1= sys.argv[1] 
F2= sys.argv[2]


# Your code goes here
def pipeTo2DArray(text):
    records = text.split("\n")
    for i in range(0, len(records)):
        records[i] = records[i].split("|")
    return records


def TwoDArrayToPipe(a):
    text= ""
    for i in range(0, len(a)):
        account = a[i]
        for j in range(0, len(account)):
            account[j] = str(account[j])
        text = text + "|".join(account) + "\n"
    return text


accounts = pipeTo2DArray(open(F1, 'r').read())
transactions = pipeTo2DArray(open(F2, 'r').read())

# for each transaction
for transactionIndex in range(0, len(transactions)):
  transaction = transactions[transactionIndex]
  if len(transaction) >= 4:
    # look through the accounts for the matching account
    for accountIndex in range(0,len(accounts)):
      account= accounts[accountIndex]
      if len(account) >= 3:                      # make sure we have
        balance= int(account[2])                  # enough fields
        transactionAmount = int(transaction[1])
        if account[0] == transaction[2]:         # account matches?
          if account[1] == transaction[3]:       # pin code matches?
            if transaction[0] == 'add':
              accounts[accountIndex][2] = balance + transactionAmount
            elif transaction[0] == 'sub' and transactionAmount <= balance:
              accounts[accountIndex][2]= balance - transactionAmount


# Write the answer back out to the original file
open(F1, 'w').write(TwoDArrayToPipe(accounts))