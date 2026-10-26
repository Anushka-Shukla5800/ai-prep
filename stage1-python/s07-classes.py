from dataclasses import dataclass

@dataclass
class Complaint:
    
    amount: int
    complaint: str
    
    def is_large(self) -> bool :
        if self.amount >= 50000 :
            return True
        return False
        
    

complaint1 = Complaint(100000,"What the hell?")
complaint2 = Complaint(678,"This is tricky")
complaint3 = Complaint(9234385638475,"huge mistake")

print(complaint1==complaint2)
print(complaint3)

print(complaint1.is_large())
print(complaint2.is_large())
print(complaint3.is_large())