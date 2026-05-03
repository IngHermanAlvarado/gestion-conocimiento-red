#!/bin/bash

# Script de Backup de Configuraciones
# Descripción: Realiza backup automático de configuraciones de red
# Autor: Equipo de TI
# Fecha: 2024

# Variables
BACKUP_DIR="/backups/network-configs"
DATE=$(date +%Y%m%d_%H%M%S)
LOG_FILE="/var/log/backup_network.log"

# Crear directorio de backup si no existe
mkdir -p $BACKUP_DIR

# Función de logging
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

# Iniciar backup
log_message "Iniciando backup de configuraciones de red"

# Backup de router
echo "Realizando backup del router..."
sshpass -p 'PASSWORD' ssh admin@192.168.1.1 "show running-config" > $BACKUP_DIR/router_config_$DATE.txt
if [ $? -eq 0 ]; then
    log_message "Backup de router completado exitosamente"
else
    log_message "ERROR: Fallo en backup de router"
fi

# Backup de switch
echo "Realizando backup del switch..."
sshpass -p 'PASSWORD' ssh admin@192.168.1.2 "show running-config" > $BACKUP_DIR/switch_config_$DATE.txt
if [ $? -eq 0 ]; then
    log_message "Backup de switch completado exitosamente"
else
    log_message "ERROR: Fallo en backup de switch"
fi

# Comprimir backups antiguos
find $BACKUP_DIR -name "*.txt" -mtime +30 -exec gzip {} \;
log_message "Archivos antiguos comprimidos"

# Enviar notificación
log_message "Backup completado. Archivos guardados en $BACKUP_DIR"
echo "Backup completado" | mail -s "Backup de Configuraciones" admin@banco.com

log_message "Proceso de backup finalizado"
