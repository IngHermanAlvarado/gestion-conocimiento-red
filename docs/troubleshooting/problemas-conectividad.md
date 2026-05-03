# Problemas de Conectividad

## Problema: No hay conectividad a Internet

### Síntomas
- Los usuarios no pueden acceder a sitios web
- Los servidores no pueden resolver nombres DNS
- Pérdida de conexión intermitente

### Diagnóstico

#### Paso 1: Verificar conectividad física
```bash
# Verificar estado de interfaces
show interfaces status

# Verificar cables conectados
# Verificar luces LED en switches y routers
```

#### Paso 2: Verificar configuración IP
```bash
# En Windows
ipconfig /all

# En Linux
ip addr show
ifconfig
```

#### Paso 3: Pruebas de conectividad
```bash
# Ping a puerta de enlace
ping 192.168.1.1

# Ping a DNS
ping 8.8.8.8

# Traceroute
tracert www.google.com  # Windows
traceroute www.google.com  # Linux
```

### Soluciones

#### Solución 1: Reiniciar dispositivos
```bash
# Reiniciar router
show running-config
reload

# Reiniciar switch
reload

# Reiniciar interfaz de red
shutdown
no shutdown
```

#### Solución 2: Verificar configuración de routing
```bash
# Ver tabla de rutas
show ip route

# Verificar rutas por defecto
show ip route 0.0.0.0
```

#### Solución 3: Verificar DNS
```bash
# Cambiar servidor DNS
# En Windows: ipconfig /all
# En Linux: cat /etc/resolv.conf

# Usar DNS público
# Google: 8.8.8.8, 8.8.4.4
# Cloudflare: 1.1.1.1, 1.0.0.1
```

## Problema: Conectividad lenta

### Síntomas
- Navegación web lenta
- Transferencias de archivos lentas
- Latencia alta

### Diagnóstico
```bash
# Medir velocidad
iperf -c servidor

# Ver uso de ancho de banda
show interface GigabitEthernet0/0

# Verificar CPU y memoria
show processes cpu
show memory
```

### Soluciones
- Verificar congestión de red
- Revisar QoS (Quality of Service)
- Buscar dispositivos con mal funcionamiento
- Actualizar drivers de red

## Problema: Pérdida de paquetes

### Síntomas
- Conexiones que se cortan
- Transferencias incompletas
- Errores en aplicaciones

### Diagnóstico
```bash
# Ping con estadísticas
ping -c 100 192.168.1.1

# Ver errores de interfaz
show interface GigabitEthernet0/0
```

### Soluciones
- Verificar cables de red
- Revisar configuración de VLAN
- Buscar interferencias
- Actualizar firmware de dispositivos
