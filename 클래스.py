# # 공격 함수
# def attack(name, location, damage):
#   print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# # 마린
# marine_name = "마린"
# marine_hp = 40
# marine_damage = 5

# print("{} 유닛이 생성되었습니다.".format(marine_name))
# print("체력 {0}, 공격력 {1}\n".format(marine_hp, marine_damage))

# # 탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
  
# attack(marine_name, "1시", marine_damage)
# attack(tank_name, "1시", tank_damage)

# 클래스

# class Unit:
#   def __init__(self, name, hp, damage):
#     self.name = name
#     self.hp = hp
#     self.damage = damage
#     print("{0} 유닛이 생성되었습니다.".format(self.name))
#     print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))
    
# marine1 = Unit("마린", 40, 5)
# marine22 = Unit("마린", 40, 5)
# tank1 = Unit("탱크", 150, 35)

# __init__ => 생성자

# 멤버 변수
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#   print("{0}는 현재 클로킹 상태 입니다.".format(wraith2.name))
  
# 메소드

# class Unit:
#   def __init__(self, name, hp, damage):
#     self.name = name
#     self.hp = hp
#     self.damage = damage
    
# class AttackUnit:
#   def __init__(self, name, hp, damage):
#     self.name = name
#     self.hp = hp
#     self.damage = damage
  
#   def attack(self, location):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    
#   def damaged(self, damage):
#     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#     self.hp = self.hp - damage
#     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#     if self.hp <= 0:
#       print("{0} : 파괴 되었습니다.".format(self.name))
      
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속 = 물려받다.
# class Unit:
#   def __init__(self, name, hp):
#     self.name = name
#     self.hp = hp
    
# class AttackUnit(Unit):
#   def __init__(self, name, hp, damage):
#     Unit.__init__(self, name, hp)
#     self.damage = damage
  
#   def attack(self, location):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    
#   def damaged(self, damage):
#     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#     self.hp = self.hp - damage
#     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#     if self.hp <= 0:
#       print("{0} : 파괴 되었습니다.".format(self.name))
      
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중 상속

# class Unit:
#   def __init__(self, name, hp):
#     self.name = name
#     self.hp = hp
    
# class AttackUnit(Unit):
#   def __init__(self, name, hp, damage):
#     Unit.__init__(self, name, hp)
#     self.damage = damage
  
#   def attack(self, location):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    
#   def damaged(self, damage):
#     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#     self.hp = self.hp - damage
#     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#     if self.hp <= 0:
#       print("{0} : 파괴 되었습니다.".format(self.name))
  
      
# class Flyable:
#   def __init__(self, flying_speed):
#     self.flying_speed = flying_speed
    
#   def fly(self, name, location):
#     print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#   def __init__(self, name, hp, damage, flying_speed):
#     AttackUnit.__init__(self, name, hp, damage)
#     Flyable.__init__(self, flying_speed)
    

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 메소드 오버라이딩
# class Unit:
#   def __init__(self, name, hp, speed):
#     self.name = name
#     self.hp = hp
#     self.speed = speed
    
#   def move(self, location):
#     print("[지상 유닛 이동]")
#     print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
# class AttackUnit(Unit):
#   def __init__(self, name, hp, damage, speed):
#     Unit.__init__(self, name, hp, speed)
#     self.damage = damage
  
#   def attack(self, location):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    
#   def damaged(self, damage):
#     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#     self.hp = self.hp - damage
#     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#     if self.hp <= 0:
#       print("{0} : 파괴 되었습니다.".format(self.name))
  
      
# class Flyable:
#   def __init__(self, flying_speed):
#     self.flying_speed = flying_speed
    
#   def fly(self, name, location):
#     print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#   def __init__(self, name, hp, damage, flying_speed):
#     AttackUnit.__init__(self, name, hp, damage, 0)
#     Flyable.__init__(self, flying_speed)
    
#   def move(self, location):
#     print("[공중 유닛 이동]")
#     self.fly(self.name, location)

# # valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# # valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 20, 10)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")


# pass = 그냥 넘어감
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    
  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
    
class AttackUnit(Unit):
  def __init__(self, name, hp, damage, speed):
    Unit.__init__(self, name, hp, speed)
    self.damage = damage
  
  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    
  def damaged(self, damage):
    print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
    self.hp = self.hp - damage
    print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴 되었습니다.".format(self.name))
  
      
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed
    
  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, damage, 0)
    Flyable.__init__(self, flying_speed)
    
  def move(self, location):
    print("[공중 유닛 이동]")
    self.fly(self.name, location)

class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    #Unit.__init__(self, name, hp, 0)
    super().__init__(name, hp, 0)
    self.location = location
