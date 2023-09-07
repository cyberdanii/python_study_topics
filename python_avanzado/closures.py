def make_repeater_of(n):

    # aqui empieza el closure
    def repeater(string):

        assert type(string)==str, "Solo se peuden repetir strings"

        return string * n
    return repeater

def run():
    repeater1 = make_repeater_of(2)

    # aqui se ejecuta el closure
    print(repeater1('Dani'))

# entry point
if __name__ == "__main__":
    run()
