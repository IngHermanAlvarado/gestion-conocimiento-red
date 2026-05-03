# Configuración de Router Cisco

## Objetivo
Este procedimiento describe los pasos para configurar un router Cisco en la red del banco tecnológico.

## Requisitos Previos
- Acceso físico al router
- Cable de consola
- Software de terminal (PuTTY, Tera Term)
- Credenciales de administrador

## Procedimiento

### 1. Conexión Inicial
```
1. Conectar el cable de consola al puerto de consola del router
2. Abrir el software de terminal
3. Configurar: 9600 baud, 8 data bits, 1 stop bit, no parity
4. Presionar Enter para acceder al prompt
```

### 2. Acceso al Modo de Configuración
```
Router> enable
Router# configure terminal
Router(config)#
```

### 3. Configuración de Interfaz
```
Router(config)# interface GigabitEthernet0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

### 4. Configuración de Rutas Estáticas
```
Router(config)# ip route 0.0.0.0 0.0.0.0 192.168.1.254
```

### 5. Guardar Configuración
```
Router(config)# exit
Router# copy running-config startup-config
```

## Verificación
```
Router# show ip interface brief
Router# show ip route
```

## Notas Importantes
- Siempre guardar la configuración después de cambios
- Documentar todos los cambios realizados
- Realizar backups periódicos de la configuración
