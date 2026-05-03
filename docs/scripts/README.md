# Scripts

Este directorio contiene scripts útiles para la automatización y gestión de tareas de TI.

## Índice

- [Script de Backup de Configuraciones](#script-de-backup-de-configuraciones)
- [Script de Monitoreo de Servicios](#script-de-monitoreo-de-servicios)

## Script de Backup de Configuraciones

### Descripción
Script que automatiza el backup periódico de configuraciones de red desde routers y switches.

**Archivo:** `backup-configuraciones.sh`

### Características
- Backup automático de múltiples dispositivos
- Compresión de archivos antiguos
- Logging de operaciones
- Notificaciones por correo electrónico

### Uso
```bash
chmod +x backup-configuraciones.sh
./backup-configuraciones.sh
```

### Configuración
Editar el script para:
- Cambiar contraseñas
- Agregar más dispositivos
- Modificar directorios de backup
- Ajustar frecuencia de ejecución

## Script de Monitoreo de Servicios

### Descripción
Script que monitorea el estado de servicios críticos y genera alertas.

### Características
- Monitoreo en tiempo real
- Reinicio automático de servicios caídos
- Generación de reportes
- Alertas por correo

## Mejores Prácticas

1. **Seguridad**
   - No guardar contraseñas en texto plano
   - Usar variables de entorno o archivos de configuración seguros
   - Restringir permisos de archivos

2. **Mantenimiento**
   - Documentar cambios en scripts
   - Versionar scripts en Git
   - Realizar pruebas antes de ejecutar en producción

3. **Logging**
   - Registrar todas las operaciones
   - Mantener logs por al menos 30 días
   - Revisar logs regularmente

## Contribución

Para agregar nuevos scripts:
1. Crear archivo con nombre descriptivo
2. Agregar comentarios y documentación
3. Incluir manejo de errores
4. Actualizar este README
