
class envFeature:
    def __init__(self, featureName, featureType):
        self.name = featureName
        self.type = featureType
    

def getLanderFeaturesAndTarget():
    landerFeatureNames = ["lander_x", "lander_y", "x_velocity", "y_velocity", "angle", "angle_velocity", "left_leg_contact", "right_leg_contact"]
    landerFeatureTypes = ["number", "number", "number", "number", "number", "number", "bool", "bool"]
    landerTargetNames = ["nothing", "left_engine", "main_engine", "right_engine"]
    landerFeatures = []
    for i in range(0, 8):
        landerFeatures.append(envFeature(landerFeatureNames[i], landerFeatureTypes[i]))

    return landerFeatures, landerTargetNames

def getCartPoleFeaturesAndTarget():
    cartPoleFeatureNames = ["cart_position", "cart_velocity", "pole_angle", "pole_angular_velocity"]
    cartPoleFeatureTypes = ["number", "number", "number", "number"]
    cartPoleTargetNames = ["move_left", "move_right"]
    cartPoleFeatures = []
    for i in range(0, 4):
        cartPoleFeatures.append(envFeature(cartPoleFeatureNames[i], cartPoleFeatureTypes[i]))

    return cartPoleFeatures, cartPoleTargetNames

def getMountainCarFeaturesAndTarget():
    MountainCarFeatureNames = ["car_position", "car_velocity"]
    MountainCarFeatureTypes = ["number", "number"]
    MountainCarTargetNames = ["accelerate_left", "nothing", "accelerate_right"]
    MountainCarFeatures = []
    for i in range(0, 2):
        MountainCarFeatures.append(envFeature(MountainCarFeatureNames[i], MountainCarFeatureTypes[i]))

    return MountainCarFeatures, MountainCarTargetNames