import os
o = 0

while o != -1 :
	print("\nCommands: ")
	print("1. timedatectl set-ntp true")
	print("2. cgdisk /dev/sda")
	print("3. mkfs.fat -F32 /dev/sda1")
	print("4. mkswap /dev/sda2")
	print("5. mkfs.ext4 /dev/sda3")
	print("6. mount /dev/sda3 /mnt")
	print("7. mkdir -p /mnt/boot")
	print("8. mount /dev/sda1 /mnt/boot")
	print("9. swapon /dev/sda2")
	print("10. pacstrap /mnt base base-devel linux linux-firmware firefox vim nano git wget grub efibootmgr")
	print("11. genfstab -U /mnt >> /mnt/etc/fstab")
	print("12. arch-chroot /mnt\n")

	o = int(input("Choose: "))

	if o == 1:
		os.system("timedatectl set-ntp true")
	elif o == 2:
		os.system("cgdisk /dev/sda")
	elif o == 3:
		os.system("mkfs.fat -F32 /dev/sda1")
	elif o == 4:
		os.system("mkswap /dev/sda2")
	elif o == 5:
		os.system("mkfs.ext4 /dev/sda3")
	elif o == 6:
		os.system("mount /dev/sda3 /mnt")
	elif o == 7:
		os.system("mkdir -p /mnt/boot")
	elif o == 8:
		os.system("mount /dev/sda1 /mnt/boot")
	elif o == 9:
		os.system("swapon /dev/sda2")
	elif o == 10:
		os.system("pacstrap /mnt base base-devel linux linux-firmware firefox vim nano git wget grub efibootmgr")
	elif o == 11:
		os.system("genfstab -U /mnt >> /mnt/etc/fstab")
	elif o == 12:
		os.system("arch-chroot /mnt")