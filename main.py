while True:
    print("choose your option:\n\t1)Encrypt\n\t2)Decrypt\n]\t 3)Exit")
     if choice == "1":
        plain_text = input("text:")
        encrypted_text=""
          for c in plain_text:
            x = ord(c) * 2 +5
            encrypted_text += chr(x)
        print("encryted_text:", encrypted_text)
        print("*"*40 + "\n")
     elif choice == "2":
         encrypted_text = input("encrypted_text:")
         plain_text = ""
         for c in encrypted_text:
             x = ( ord (c) - 5) // 2
             plain_text += chr(x)
         print("plaintext:", plain_text)
         print("*"*40 + "\n")
     elif choice == "3":
         print("Goodbye!")
         print("*"*40 + "\n")
         break