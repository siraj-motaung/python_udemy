chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
        print("Kitchen chai", chai_type)
    kitchen()
    print("Outside function", chai_type)

front_desk()