class Head():
    def __init__(self):
        pass


class Torso():
    def __init__(self, head, left_arm, right_arm):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm


class Arm():
    def __init__(self, hand):
        self.hand = hand


class Leg():
    def __init__(self, foot):
        self.foot = foot

class Hand():
    def __init__(self, fingers):
        self.fingers = fingers


class Foot():
    def __init__(self, fingers):
        self.fingers = fingers


class Fingers():
    def __init__(self):
        pass
        

class Human():
    def __init__(self, torso, left_leg, right_leg):
        self.torso = torso
        self.left_leg = left_leg
        self.right_leg = right_leg



fingers_feet_r = Fingers()
fingers_feet_l = Fingers()

fingers_hand_r = Fingers()
fingers_hand_l = Fingers()

left_hand = Hand(fingers_hand_l)
right_hand = Hand(fingers_hand_r)

arm_left = Arm(left_hand)
arm_right = Arm(right_hand)

right_foot = Foot(fingers_feet_r)
left_foot = Foot(fingers_feet_l)

one_leg = Leg(right_foot)
another_leg = Leg(left_foot)

head = Head()

torso = Torso(head, arm_left, arm_right)

human = Human(torso, one_leg, another_leg)