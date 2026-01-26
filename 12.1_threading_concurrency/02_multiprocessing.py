from multiprocessing import Process
import time


def brew_chai(name):
    print(f"Start of {name} chai brewing {time.strftime("%Hh-%Mm-%Ss")}")
    time.sleep(2)
    print(f"End of {name} chai brewing {time.strftime("%Hh-%Mm-%Ss")}")


if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",))
       for i in range(3) 
    ]

    for p in chai_makers:
        p.start()

    #wait for all to complete
    for p in chai_makers:
        p.join()
