import paramiko

# Создаем клиент SSH
client = paramiko.SSHClient()

# Устанавливаем политику подключения
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Подключаемся к удаленному серверу
client.connect('hostname', username='username')

local_port = 554
remote_port = 554


