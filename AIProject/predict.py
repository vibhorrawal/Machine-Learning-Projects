from functools import reduce
import pandas as pd

class Classifier():
    data = None
    class_attr = None
    priori = {}
    cp = {}
    hypothesis = None

    def __init__(self,filename=None, class_attr=None ):
        self.data = pd.read_csv(filename, sep=',', header =(0))
        self.class_attr = class_attr

    def calculate_priori(self):
        class_values = list(set(self.data[self.class_attr]))
        class_data =  list(self.data[self.class_attr])
        
        for i in class_values:
            self.priori[i]  = class_data.count(i)/float(len(class_data))
        print ("Priori Values: ", self.priori)


    def get_cp(self, attr, attr_type, class_value):
        data_attr = list(self.data[attr])
        class_data = list(self.data[self.class_attr])
        total =1
        for i in range(0, len(data_attr)):
            if class_data[i] == class_value and data_attr[i] == attr_type:
                #print(class_data[i]," ",data_attr[i])
                total+=1
        return total/float(class_data.count(class_value))

    def calculate_conditional_probabilities(self, hypothesis):
        for i in self.priori:
            self.cp[i] = {}
            for j in hypothesis:
                self.cp[i].update({ hypothesis[j]: self.get_cp(j, hypothesis[j], i)})
        print ("\nCalculated Conditional Probabilities: \n")
        print("Yes : ",self.cp['yes'])
        print("\nNo : ",self.cp['no'],"\n")
    
    def get_cp_val(self, condition):
        return reduce(lambda x, y: x*y, self.cp[condition].values())*self.priori[condition]
    def classify(self):
        print ("Result: ")
        if get_cp_val('no') > get_cp_val('no'):
                print("Do not go Class")
                print("Conditional Probabilities are")
                print("No:", get_cp_val('no'))
                print("Yes:", get_cp_val('yes'))
        else:
                print("You Should go Class")
                print("Conditional Probabilities are :")
                print("Yes:", get_cp_val('yes'))
                print("No:", get_cp_val('no'))

def exitSystem():
        print("Exiting...\nThank you")
        exit()

if __name__ == "__main__":
    c = Classifier(filename="dataset.csv", class_attr="Go")
    print("Enter 'x' or 'exit' to exit from the system")
    outlook = input("Whats the weather outside? (Sunny, Rainy, Overcast):")
    if outlook.lower() == 'x' or outlook.lower() == 'exit':
        exitSystem()
    temp = input("Whats the temperature today? (Hot, Mild, Cool):")
    if temp.lower() == 'x' or temp.lower()== 'exit':
        exitSystem()
    humidity = input("Whats the humidity? (High, Normal):")
    if humidity.lower() == 'x' or humidity.lower()== 'exit':
        exitSystem()
    windy = input("Is it windy tody? (t or f):")
    if windy.lower() == 'x' or windy.lower()== 'exit':
        exitSystem()
    attandance = input("How about your attandance?(Low,High):")
    if attandance.lower() == 'x' or attandance.lower()== 'exit':
        exitSystem()

    c.hypothesis = {"Outlook":outlook, "Temp":temp, "Humidity":humidity , "Windy":windy,"Attandance":attandance}
    c.calculate_priori()
    c.calculate_conditional_probabilities(c.hypothesis)
    c.classify()
