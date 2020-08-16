import contants
import re
from source import SSH


if __name__ == "__main__":
    # Connect to switch
    client = SSH.connection(**contants.switch)
    # Get interact with shell
    shell = SSH.get_shell(client)
    # Send command to get temperature
    SSH.send(shell, "swctrl env show", 0.5)
    # Receive message
    msg = SSH.receive(shell, 1024)
    # receive word parsing for temperature
    list_gen_temp = re.findall("General.*: [0-9]+", msg)
    list_temp = re.findall("[0-9]+", list_gen_temp[0])
    temp = int(list_temp[0])

    print(temp)
    # Close tunnel
    SSH.close(client)
