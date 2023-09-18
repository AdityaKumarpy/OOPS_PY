
import random 

class Password:
    """Class to generate random password 
    Parm:strength : Strength of Generated Password ex:-> 'low','mid','high'.
                    Default value is Mid 
    Parm:length : Length of the Genrated Password ex:-> 1,20,300
                  for low strength , length will be 8 
                      mid strength , length will be 12 
                      high strength , length will be 16 

    Return : New Random Password of given length & Strength    
    """

    sampler = {
        'letters':['a','b','c','d','e','f','g','h','i','j','k','l','m',
                   'n','o','p','q','r','s','t','u','v','w','x','y','z'],
        'numbers':[0,1,2,3,4,5,6,7,8,9],
        'punctuation':['!','@','#','$','%','^','&','*','(','{','}',')',';','/','|']
    }

  
    @staticmethod
    def random_lower_letter_genrator():
        return Password.sampler['letters'][random.randint(0,len(Password.sampler['letters'])-1)]
    @staticmethod
    def random_upper_letter_genrator():
        return Password.sampler['letters'][random.randint(0,len(Password.sampler['letters'])-1)].upper()

    @staticmethod
    def random_number_generator():
        return Password.sampler['numbers'][random.randint(0,len(Password.sampler['numbers'])-1)]
    
    @staticmethod
    def random_punctuation_generator():
        return Password.sampler['punctuation'][random.randint(0,len(Password.sampler['punctuation'])-1)]
    
    lowercase_uppercase =(random_lower_letter_genrator,
                          random_upper_letter_genrator
                          )
    lowercase_uppercase_number=(random_lower_letter_genrator,
                                random_upper_letter_genrator,
                                random_number_generator
                                )
    lowercase_uppercase_number_punctuation=(random_lower_letter_genrator,
                                            random_upper_letter_genrator,
                                            random_number_generator,
                                            random_punctuation_generator
                                            )
    
    password_strength = {'low' :{'length':8,'sample':lowercase_uppercase,'rand_size':1},
                       'mid' :{'length':12,'sample':lowercase_uppercase_number,'rand_size':2},
                       'high':{'length':16,'sample':lowercase_uppercase_number_punctuation,'rand_size':3},
                       }
    
    #insatance Methods
    def __init__(self,strength='mid',length=None):
        self.strength = strength
        self.length = Password.password_strength[strength]['length'] if length is None else length
        #print(self.strength,self.length)

    def generator(self):
        if self.strength not in ['low','mid','high']:
            return "Invalid Strengh Provided by the user"
        if self.length == 0 :
            return "0 length Password cannot be generated"
        pass_word = ''
        for i in range(0,self.length):
            sampler_from_smapler= Password.password_strength[self.strength]['sample'][random.randint(0,Password.password_strength[self.strength]['rand_size'])]()
            #print(sampler_from_smapler)
            pass_word = pass_word + str(sampler_from_smapler)
        return pass_word
    
    @classmethod
    def show_me_whole_universe(cls):
        return Password.sampler


    
#Driver Code 
give_me_password = Password('high',0)
print(give_me_password.generator())