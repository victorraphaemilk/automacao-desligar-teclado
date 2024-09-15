import subprocess

processo  = subprocess.run([' xinput list' ], shell=True, capture_output=True)
output = processo.stdout.decode('utf-8')

for line in output.splitlines():
    if "AT Translated Set 2 keyboard" in line:
        teclado_id = line.split('id=')[1].split()[0]
        print('teclado achado')
        subprocess.run([f'xinput float {teclado_id}'],shell=True)
        print('teclado desativado')
        break
        
    else:
        print('não consegiu desativar teclado')   

