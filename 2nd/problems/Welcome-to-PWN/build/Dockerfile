FROM ubuntu:18.04

# update & upgrade
RUN apt-get update -y && apt-get -y upgrade
RUN apt-get -y install xinetd

# add pwn( user )
RUN groupadd -r pwn && useradd -r -g pwn pwn

# change directory to /home/pwn
WORKDIR /home/pwn

# copy file
COPY --chown=root:pwn  ./build/ctf.conf /etc/xinetd.d/ctf
COPY --chown=root:pwn  ./build/start.sh ./start.sh
COPY --chown=root:pwn  ./build/flag.txt ./flag.txt
COPY --chown=root:pwn  ./build/welcome_pwn.bin ./welcome_pwn.bin

# change permission
RUN chmod 444 ./flag.txt
RUN chmod 555 ./welcome_pwn.bin

USER pwn
EXPOSE 60000

CMD ["xinetd", "-dontfork", "-f", "/etc/xinetd.d/ctf"]
