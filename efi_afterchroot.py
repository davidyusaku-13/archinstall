import os
o = 0

while o != -1 :
	print("\nCommands: ")
	print("1. ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime")
	print("2. hwclock --systohc")
	print("3. sed '14s/^#//' /etc/locale.gen")
	print("4. locale-gen")
	print("5. echo 'LANG=en_US.UTF-8' > /etc/locale.conf")
	print("6. echo 'arch' > /etc/hostname")
	print("7. mkinitcpio -P")
	print("8. grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB")
	print("9. grub-mkconfig -o /boot/grub/grub.cfg")
	print("10. passwd")

	o = int(input("Choose: "))

	if o == 1:
		os.system("ln -sf /usr/share/zoneinfo/Asia/Jakarta /etc/localtime")
	elif o == 2:
		os.system("hwclock --systohc")
	elif o == 3:
		os.system("sed '14s/^#//' /etc/locale.gen")
	elif o == 4:
		os.system("locale-gen")
	elif o == 5:
		os.system("echo 'LANG=en_US.UTF-8' > /etc/locale.conf")
	elif o == 6:
		os.system("echo 'arch' > /etc/hostname")
	elif o == 7:
		os.system("mkinitcpio -P")
	elif o == 8:
		os.system("grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB")
	elif o == 9:
		os.system("grub-mkconfig -o /boot/grub/grub.cfg")
	elif o == 10:
		os.system("passwd")