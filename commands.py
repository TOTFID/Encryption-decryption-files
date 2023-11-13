from pathlib import Path
from main import encryption, decryption


def choose_command():
   print('Hello!\n')
   commands = {1: 'encryption', 2: 'decryption'}
   
   for i, v in commands.items():
      print(f'{i}:{v}')
   
   command = int(input('\nChoose the command: '))
   
   if command not in commands.keys():
      raise KeyError(f'command {command} incorrect')
   
   if command == 1:     
      encryption_command()
   elif command == 2:
      decryption_command()



def encryption_command():
   enter_not_enc_file = str(input('\nFile: '))
   not_enc_file = f'encrypt/{enter_not_enc_file}'
   check_not_enc_file = Path(not_enc_file)
   
   if check_not_enc_file.exists():
      print('file exists')
   else: raise FileExistsError
   
   enter_enc_file = str(input('\nName for encryption file: '))
   enc_file = f'enc_results/{enter_enc_file}'
   
   if '.txt' not in enter_enc_file:
      raise NameError
   
   pwd = str(input('\nPassword: '))
   
   encryption(not_enc_file=not_enc_file, enc_file=enc_file, pwd=pwd)


def decryption_command():
   enter_ready_enc_file = str(input('\nChoose file for decryption: '))
   ready_enc_file = f'decrypt/{enter_ready_enc_file}'
   check_ready_enc_file = Path(ready_enc_file)
      
   if check_ready_enc_file.exists():
      print('file exists')
   else: raise FileExistsError
      
   enter_decrypt_file = str(input('\nName for file: '))
   decrypt_file = f'dec_results/{enter_decrypt_file}'
      
   if '.txt' not in enter_decrypt_file:
      raise NameError
      
   pwd = str(input('\nPassword: '))
      
   decryption(ready_enc_file=ready_enc_file, decrypt_file=decrypt_file, pwd=pwd)