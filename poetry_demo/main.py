import pendulum

def log():
    now = pendulum.now("Europe/Paris")
    print(now)

if __name__ == "__main__":
    log()