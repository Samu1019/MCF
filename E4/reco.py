
class hit():
    def __init__(self,mod,sens,time):
        self.modulo = mod    
        self.sensore = sens
        self.hit_time = time
    def __eq__(self, other):
        return  self.hit_time == other.hit_time
    def __lt__(self, other):
        return self.hit_time < other.hit_time
    def __repr__(self):
        # Stampa i dati che ti interessano
        return f"Hit(Time={self.hit_time:.2f}, Mod={self.modulo}, Sens={self.sensore})"
    def __gt__(self, other):
        return self.hit_time > other.hit_time
    def __add__(self, other):
        return self.hit_time + other.hit_time
    def __sub__(self, other):
        return self.hit_time - other.hit_time

    