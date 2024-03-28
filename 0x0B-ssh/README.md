Projects on Severs and how to connect to a server using SSH

    /*Author*/
Hannington Kiptoo <hanningtonkiptoo14@gmail.com>

    /*Objectives*/

    What is a server
    Where servers usually live
    What is SSH
    How to create an SSH RSA key pair
    How to connect to a remote host using an SSH RSA key pair
    The advantage of using #!/usr/bin/env bash instead of /bin/bash

scp {file path}  {remote server} : {file destination}

eg

scp /home/kali/0x0B-ssh/test.txt ubuntu@192.168.0.1 : ~/test
