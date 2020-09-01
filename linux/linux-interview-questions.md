# Linux Interview Questions

Remember that you can check the manual page for any command using `man ${COMMAND}`.  
And you can search for a specific phrase using grep: `man ${COMMAND} | grep ${PHRASE}`

## How to check the kernel version of a Linux System?

`uname -a` will show everything:

```
Linux LAPTOP-felicia 4.4.0-19041-Microsoft #1-Microsoft Fri Dec 06 14:06:00 PST 2019 x86_64 x86_64 x86_64 GNU/Linux
```

`uname -r` shows the release info only:
```
4.4.0-19041-Microsoft
```

## How to see the current IP address on Linux?

You can use `ifconfig`:
```
eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.56.1  netmask 255.255.255.0  broadcast 192.168.56.255
        inet6 fe80::e598:34f7:574b:130f  prefixlen 64  scopeid 0xfd<compat,link,site,host>
        ether 0a:00:27:00:00:0c  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 1500
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0xfe<compat,link,site,host>
        loop  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wifi0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.144  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::e598:e71d:f7fc:acb5  prefixlen 64  scopeid 0xfd<compat,link,site,host>
        ether 50:e0:85:01:63:c3  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

You can use `ip addr show` to show all:

````
11: eth0: <> mtu 1500 group default qlen 1
    link/ether 50:e0:85:01:63:c7
    inet 169.254.215.220/16 brd 169.254.255.255 scope global dynamic
       valid_lft forever preferred_lft forever
    inet6 fe80::e9:ed19:7ed0:d7dc/64 scope link dynamic
       valid_lft forever preferred_lft forever
14: eth1: <> mtu 1500 group default qlen 1
    link/ether 98:fa:9b:be:cf:04
    inet 169.254.219.222/16 brd 169.254.255.255 scope global dynamic
       valid_lft forever preferred_lft forever
    inet6 fe80::1c74:45b6:fc38:dbde/64 scope link dynamic
       valid_lft forever preferred_lft forever
12: eth2: <BROADCAST,MULTICAST,UP> mtu 1500 group default qlen 1
    link/ether 0a:00:27:00:00:0c
    inet 192.168.56.1/24 brd 192.168.56.255 scope global dynamic
       valid_lft forever preferred_lft forever
    inet6 fe80::e598:34f7:574b:130f/64 scope link dynamic
       valid_lft forever preferred_lft forever
2: eth3: <> mtu 1500 group default qlen 1
    link/ether a4:4c:c8:5b:7d:b4
    inet 169.254.90.254/16 brd 169.254.255.255 scope global dynamic
       valid_lft forever preferred_lft forever
    inet6 fe80::40e4:6d4e:86b2:5afe/64 scope link dynamic
       valid_lft forever preferred_lft forever
1: lo: <LOOPBACK,UP> mtu 1500 group default qlen 1
    link/loopback 00:00:00:00:00:00
    inet 127.0.0.1/8 brd 127.255.255.255 scope global dynamic
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host dynamic
       valid_lft forever preferred_lft forever
18: wifi0: <BROADCAST,MULTICAST,UP> mtu 1500 group default qlen 1
    link/ieee802.11 50:e0:85:01:63:c3
    inet 192.168.1.144/24 brd 192.168.1.255 scope global dynamic
       valid_lft 84796sec preferred_lft 84796sec
    inet6 fe80::e598:e71d:f7fc:acb5/64 scope link dynamic
       valid_lft forever preferred_lft forever
13: wifi1: <> mtu 1500 group default qlen 1
    link/ieee802.11 50:e0:85:01:63:c4
    inet 169.254.86.135/16 brd 169.254.255.255 scope global dynamic
       valid_lft forever preferred_lft forever
    inet6 fe80::157b:2086:c1b4:5687/64 scope link dynamic
       valid_lft forever preferred_lft forever
15: wifi2: <> mtu 1500 group default qlen 1
    link/ieee802.11 52:e0:85:01:63:c3
    inet 169.254.67.194/16 brd 169.254.255.255 scope global dynamic
       valid_lft forever preferred_lft forever
    inet6 fe80::bcc7:b153:ee2b:43c2/64 scope link dynamic
       valid_lft forever preferred_lft forever
````

Or `ip addr show wifi0` for a specific device:

```
18: wifi0: <BROADCAST,MULTICAST,UP> mtu 1500 group default qlen 1
    link/ieee802.11 50:e0:85:01:63:c3
    inet 192.168.1.144/24 brd 192.168.1.255 scope global dynamic
       valid_lft 84796sec preferred_lft 84796sec
    inet6 fe80::e598:e71d:f7fc:acb5/64 scope link dynamic
       valid_lft forever preferred_lft forever
```

## How do you check for free disk space?

`df -ah` for 'disk free' where the h flag is 'human-readable':

```
Filesystem      Size  Used Avail Use% Mounted on
rootfs          238G  224G   14G  95% /
none            238G  224G   14G  95% /dev
sysfs              0     0     0    - /sys
proc               0     0     0    - /proc
devpts             0     0     0    - /dev/pts
none            238G  224G   14G  95% /run
none            238G  224G   14G  95% /run/lock
none            238G  224G   14G  95% /run/shm
none            238G  224G   14G  95% /run/user
binfmt_misc        0     0     0    - /proc/sys/fs/binfmt_misc
tmpfs           238G  224G   14G  95% /sys/fs/cgroup
cgroup             0     0     0    - /sys/fs/cgroup/devices
C:\             238G  224G   14G  95% /mnt/c
```

## How do you manage services on a system / How to see if a Linux service is running?

For an example service called `udev`.


On older systems `service udev status` checks status of the service named `udev`:

```
udev start/running, process 286
```

`service udev start`, `service udev stop` starts or stops the service named udev.

On a newer systemd system use `systemctl status udev`:

```
*  systemd-udevd.service - udev Kernel Device Manager
     Loaded: loaded (/lib/systemd/system/systemd-udevd.service; static; vendor >
     Active: active (running) since Sun 2020-08-23 15:28:54 PDT; 4 days ago
TriggeredBy: *  systemd-udevd-control.socket
             *  systemd-udevd-kernel.socket
       Docs: man:systemd-udevd.service(8)
             man:udev(7)
   Main PID: 1198416 (systemd-udevd)
     Status: "Processing with 40 children at max"
      Tasks: 1
     Memory: 20.5M
     CGroup: /system.slice/systemd-udevd.service
             |-> 1198416 /lib/systemd/systemd-udevd
```

## How would you check the size of a directory's contents on disk?

Disk usage `du -sh speech-to-text-benchmark/` where -s only displays total space occupied by each directory:

```
183G    speech-to-text-benchmark/
```

## How to check for open ports on a Linux machine?

`netstat` will show everything. Filter it down using `netstat -tulpn`:

```
--tcp|-t
--udp|-u
--listening|-l
--program|-p
--numeric|-n
```

Shows you the address and port different things are listening on.  
Run as root to get the program names to show.

```
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:9050          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:17500           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:17600         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:17603         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:5902          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:2222            0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:5904            0.0.0.0:*               LISTEN      3299865/Xtigervnc   
tcp        0      0 127.0.0.1:5939          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 ::1:631                 :::*                    LISTEN      -                   
tcp6       0      0 :::17500                :::*                    LISTEN      -                   
tcp6       0      0 127.0.0.1:6942          :::*                    LISTEN      -                   
tcp6       0      0 127.0.0.1:63342         :::*                    LISTEN      -                   
tcp6       0      0 ::1:5902                :::*                    LISTEN      -                   
tcp6       0      0 :::2222                 :::*                    LISTEN      -                   
tcp6       0      0 :::5904                 :::*                    LISTEN      3299865/Xtigervnc   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 192.168.1.23:123        0.0.0.0:*                           -                   
udp        0      0 127.0.0.1:123           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:123             0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:631             0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:17500           0.0.0.0:*                           -                   
udp        0      0 224.0.0.251:5353        0.0.0.0:*                           -                   
udp        0      0 224.0.0.251:5353        0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:5353            0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:58113           0.0.0.0:*                           -                   
udp6       0      0 fe80::9d3c:8b5e:ba4:123 :::*                                -                   
udp6       0      0 ::1:123                 :::*                                -                   
udp6       0      0 :::123                  :::*                                -                   
udp6       0      0 :::53564                :::*                                -                   
udp6       0      0 :::5353                 :::*                                -              
```

`0.0.0.0` is all public addresses. The port number follows after the colon. `127...` is our local machine.

## How to check CPU usage for a process?

`ps aux | grep nginx` where the example process name is `nginx` (pronounced 'engine x'):

`ps` reports a snapshot of the current process running under the logged in use account from the current terminal.

In BSD UNIX style, options are supplied without an leading dashes (`aux` instead of `-aux` or `--sort`).

`a`: prints the running processes from all users.  
`u`: shows user or owner column in output.  
`x`: prints the processes that have not been executed from the terminal.  

So `aux` prints all running processes in the system regardless of where they have been executed.

We pipe it to `grep` so it searches for `nginx` in the output from `ps aux` and only shows output that contains `nginx`.

```
felicia  1736478  0.0  0.0  17532   732 pts/6    S+   11:23   0:00 grep --color=auto nginx
```

| Column      | Description |
| ----------- | ----------- |
| USER      | user account under which this process is running       |
| PID   | Process ID of this process        |
| %CPU   | CPU time used by this process (in percentage)        |
| %MEM   | Physical memory used by this process (in percentage)        |
| VSZ   | Virtual memory used by this process (in bytes)        |
| RSS   | Resident Set Size, the non-swappable physical memory used by this process (in KiB)        |
| TTY   | Terminal from which this process is started. Question mark (?) sign represents that this process is not started from a terminal        |
| STAT   | Process state        |
| START   | Starting time and date of this process        |
| TIME   | Total CPU time used by this process        |
| COMMAND   | The command with all its arguments which started this process        |

| Stat Code      | Description |
| ----------- | ----------- |
| S      | interruptible sleep (waiting for an event to complete)       |
| +      | is in the foreground process group       |

You can also use `top` which gives you a lot more information and is updated every few seconds.

```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
    1 root      20   0    8936    316    268 S   0.0  0.0   0:00.04 init
    6 root      20   0    8936    224    180 S   0.0  0.0   0:00.00 init
    7 felicia   20   0   20060   6692   6588 S   0.0  0.0   0:00.09 bash
  323 felicia   20   0   17624   2036   1504 R   0.0  0.0   0:00.03 top
```

## Dealing with Mounts

Example: how would you mount a new volume you just plugged in such as a USB stick?

Linux has a directory called 'mount' that is the canonical place to mount things:

`ls /mnt`

To mount a new volume: `mount ${absolute path to volume} ${mount point}` like `mount /dev/sda2 /mnt` where we just mount
the volume on `/mnt`.

To check for existing mounts, use `mount`:

```
rootfs on / type lxfs (rw,noatime)
none on /dev type tmpfs (rw,noatime,mode=755)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,noatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,noatime)
devpts on /dev/pts type devpts (rw,nosuid,noexec,noatime,gid=5,mode=620)
none on /run type tmpfs (rw,nosuid,noexec,noatime,mode=755)
none on /run/lock type tmpfs (rw,nosuid,nodev,noexec,noatime)
none on /run/shm type tmpfs (rw,nosuid,nodev,noatime)
none on /run/user type tmpfs (rw,nosuid,nodev,noexec,noatime,mode=755)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,relatime)
tmpfs on /sys/fs/cgroup type tmpfs (rw,nosuid,nodev,noexec,relatime,mode=755)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,devices)
C:\ on /mnt/c type drvfs (rw,noatime,uid=1000,gid=1000,case=off)
```

If you automatically need to mount a volume at boot, what file would you look in?

`less /etc/fstab`:

```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/nvme0n1p2 during installation
UUID=ec060539-3599-4287-b624-8b6f6cf69c00 /               ext4    errors=remount-ro 0       1
# /boot/efi was on /dev/nvme0n1p1 during installation
UUID=E808-DD66  /boot/efi       vfat    umask=0077      0       1
/swapfile
```

## How to access another user's files on Linux?

```
su
<rootpassword>
cd /home/username
ls
```

`su` switches you to the root user account and requires the root account's password.  
`sudo` runs a single command with root privileges; it does not switch to the root use or require a separate root user
password.

Linux goes `sudo` only by default.
