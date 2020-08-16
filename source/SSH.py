import sys
import time
import socket

import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException


def connection(**device: dict):
    # assign SSHClient class
    client = paramiko.SSHClient()
    print('Connecting to', device["hostname"])
    # automatic accept fingerprint
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        # ssh connect to SSH server
        client.connect(**device, look_for_keys=False, allow_agent=False)
    except AuthenticationException:
        sys.exit("Authentication Failed")
    except SSHException:
        sys.exit("Error connecting or establishing an SSH session")
    except socket.error as err:
        sys.exit("Caught exception socket.error : %s" % err.errno)
    return client


def get_shell(client):
    # interact with shell
    shell = client.invoke_shell()
    return shell


def send(shell, cmd: str, timeout: float):
    # sending commands
    shell.send(cmd + '\n')
    # wait shell respond
    time.sleep(timeout)


def receive(shell, byte: int):
    # receive in byte
    recv = shell.recv(byte)
    recv = recv.decode('utf-8')
    return recv


def close(client):
    if client.get_transport().is_active():
        print('Closing ssh connection')
        client.close()


if __name__ == "__main__":
    sys.exit("You could not run direct in this script")
