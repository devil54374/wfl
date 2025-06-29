class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand  # 汽车品牌
        self.speed = speed  # 当前速度（默认0）

    def accelerate(self, m):
        """加速m次，每次速度增加10"""
        for _ in range(m):
            self.speed += 10
            print(f"{self.brand}加速 → 当前速度: {self.speed}km/h")

    def brake(self, n):
        """刹车n次，每次速度减少10（不低于0）"""
        for _ in range(n):
            self.speed = max(0, self.speed - 10)  # 确保速度不低于0
            status = "已停车" if self.speed == 0 else f"{self.speed}km/h"
            print(f"{self.brand}刹车 → {status}")

# 创建Car实例并测试方法
bmw = Car("BMW", 30)
print("\n=== 燃油车测试 ===")
bmw.accelerate(2)  # 加速2次
bmw.brake(4)       # 刹车4次（最后一次会停车）


class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        super().__init__(brand, speed)  # 继承父类属性
        self.battery = battery  # 新增电量属性

    def charge(self):
        """充电：电量增加20（不超过100）"""
        self.battery = min(self.battery + 20, 100)  # 确保电量不超过100
        print(f"{self.brand}充电 → 当前电量: {self.battery}%")

# 创建ElectricCar实例并测试方法
tesla = ElectricCar("Tesla", 20, 80)
print("\n=== 电动车测试 ===")
tesla.accelerate(3)  # 加速3次
tesla.brake(1)       # 刹车1次
tesla.charge()       # 充电
tesla.charge()       # 再次充电（测试上限）