
#--------------------------------------------------------------
# Create a PolicyHolder object with the overload contructor, some
# Accessor and Mutator methods
#--------------------------------------------------------------
class policyHolder:
#--------------------------------------------------------------
# Constructor
#--------------------------------------------------------------
#    def __init__(self):
#       print ('the object if created')
#--------------------------------------------------------------
    def policyHolder(self, ppolnum, pcustomer, paccident):
        self.__policy = ppolnum
        self.__customer = pcustomer
        self.__accident = paccident
#--------------------------------------------------------------
# Mutator methods
#--------------------------------------------------------------     
    def set_Policy (self, ppolnum):
        self.__policy = ppolnum
        
    def set_Customer(self, pcustomer):
        if  pcustomer < 14 or pcustomer > 125:
            print ('age input error')
            self.__customer = 0
        else:
            self.__customer = pcustomer
        
    def set_Accident(self, paccident):
        self.__accident  = paccident
#--------------------------------------------------------------
# Accessor methods...
#--------------------------------------------------------------
    def get_Policy(self):
        return self.__policy

    def get_Customer(self):
        return self.__customer

    def get_Accident(self):
        return self.__accident

    def get_DispUser(self):
        print ('Policy Number: ', policyHolder.get_Policy(self))
        print ('Customer Age: ', policyHolder.get_Customer(self))
        print ('Number of Accidents: ', policyHolder.get_Accident(self))

def main():
#--------------------------------------------------------------
# Create a PolicyHolder object and initialize its
# fields with default values
#--------------------------------------------------------------
        newPolicyHolder = policyHolder()
#--------------------------------------------------------------
# Create a call to set the policy, customer
# & accident of the newPolicyHolder....
#--------------------------------------------------------------
        newPolicyHolder.set_Policy(int('0'))
        newPolicyHolder.set_Customer(int('44'))
        newPolicyHolder.set_Accident(int('1'))
#--------------------------------------------------------------
# call to check policy holder
#--------------------------------------------------------------
        checkAccident(newPolicyHolder)
#--------------------------------------------------------------
# Create a PolicyHolder object and using the overload
# constructor
#--------------------------------------------------------------
        defPolicyHolder = policyHolder()
#--------------------------------------------------------------
# Create a call to set the policy, customer
# & accident of the defPolicyHolder....
#--------------------------------------------------------------
        ppolnum = int(input('Enter in the Policy Number: '))
        defPolicyHolder.set_Policy(ppolnum)
        pcustomer = int(input('Enter in the Customer Age: '))
        defPolicyHolder.set_Customer(pcustomer)
        paccident = int(input('Enter in the number of Accidents: '))
        defPolicyHolder.set_Accident(paccident)
#--------------------------------------------------------------
# call to check policy holder
#--------------------------------------------------------------
        checkAccident(defPolicyHolder)
#--------------------------------------------------------------
# Create a second PolicyHolder object and using the overload
# constructor
#--------------------------------------------------------------
        replPolicyHolder = policyHolder()
#--------------------------------------------------------------
# Create a call to set the policy, customer
# & accident of the defPolicyHolder....
#--------------------------------------------------------------
        ppolnum = int(input('Enter in the Policy Number: '))
        replPolicyHolder.set_Policy(ppolnum)
        pcustomer = int(input('Enter in the Customer Age: '))
        replPolicyHolder.set_Customer(pcustomer)
        paccident = int(input('Enter in the number of Accidents: '))
        replPolicyHolder.set_Accident(paccident)
#--------------------------------------------------------------
# call to check policy holder
#--------------------------------------------------------------
        checkAccident(replPolicyHolder)
#--------------------------------------------------------------
# This module will accept a PolicyHolder argument and
# display the data for any policy holder that is over 35
# and has less than 2 accidents...
#--------------------------------------------------------------
def checkAccident(ph):
        age = ph.get_Customer()
        crash = ph.get_Accident()

        if (age > 35 and crash < 2):
            ph.get_DispUser()
          
main()
