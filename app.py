class Worker:
    def work(self):
        print("Working")

    def perform_task(self):
            print("Performing task: ", end='')
            self.work()

class DeliveryMan(Worker):
    def work(self):
        print("Delivering Goods")

class LumberJack(Worker):
    def work(self):
        print("Cutting Woods")

deliveryMan = DeliveryMan()
lumberJack = LumberJack()

deliveryMan.perform_task()
lumberJack.perform_task()