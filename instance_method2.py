#Instance Method with parameter
class Mobile:
    def __init__(self):
        self.model = 'Realme x'

    def show_model(self, p):
        self.price = p
        print("Model:", self.model, "Price:",self.price)

realme = Mobile()
realme.show_model(1000)
redmi =Mobile()
redmi.show_model(2000)
