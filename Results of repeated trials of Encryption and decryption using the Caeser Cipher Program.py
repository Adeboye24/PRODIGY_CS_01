Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======== RESTART: C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py ========
Caesar Cipher Program
Would you like to (E)ncrypt or (D)ecrypt? E
Enter the text: I am on my way to school.
Enter the shift value: 5
Encrypted text: N fr ts rd bfd yt xhmttq.
D
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> Caeser Cipher Program
SyntaxError: invalid syntax
>>> 
======== RESTART: C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py ========
Caesar Cipher Program
Would you like to (E)ncrypt or (D)ecrypt? D
Enter the text: N fr ts rd bfd yt xhmttq.
... D
Enter the shift value: Traceback (most recent call last):
  File "C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py", line 35, in <module>
    main()
  File "C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py", line 25, in main
    shift = int(input("Enter the shift value: ").strip())
ValueError: invalid literal for int() with base 10: 'D'
>>> caeser_cipher.py
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    caeser_cipher.py
NameError: name 'caeser_cipher' is not defined
>>> 
======== RESTART: C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py ========
Caesar Cipher Program
Would you like to (E)ncrypt or (D)ecrypt? D
Enter the text: N fr ts rd bfd yt xhmttq.
... 
Enter the shift value: Traceback (most recent call last):
  File "C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py", line 35, in <module>
    main()
  File "C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py", line 25, in main
    shift = int(input("Enter the shift value: ").strip())
ValueError: invalid literal for int() with base 10: ''
>>> 
================================================== RESTART: C:\Users\joseph\Desktop\JOSEPH\LAGOS\caeser_cipher.py =================================================
Caesar Cipher Program
Would you like to (E)ncrypt or (D)ecrypt? D
Enter the text: N fr ts rd bfd yt xhmttq.
Enter the shift value: 5
Decrypted text: I am on my way to school.
