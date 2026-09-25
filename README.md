# Restaurante App — Semana 15
**Estudiante:** Frank Marlon Carriel Santos
**Asignatura:** Programación Orientada a Objetos

## 📋 Descripción
Aplicación de escritorio para la gestión de un restaurante con inicio de sesión, catálogo de productos y registro de ventas.

## 🗂️ Estructura del Proyecto
Restaurante_app_semana13/
├── assets/ → Íconos y logotipo ✅
│ ├── icons/
│ └── logo/
├── datos/ → Archivos JSON
├── modelos/ → Clases Usuario, Producto, Venta
├── servicios/ → Lógica del sistema
├── ui/ → Interfaz gráfica
├── main.py → Programa principal
└── README.md → Este archivo

## 🔐 Credenciales de Acceso
- **Usuario:** `admin`
- **Contraseña:** `123`

## 🍽️ Productos del Menú
| ID | Nombre | Precio |
|---|---|---|
| P001 | Arroz con Pollo | $7.50 |
| P002 | Seco de Chivo | $9.00 |
| P003 | Encebollado | $5.00 |
| P004 | Ceviche de Camarón | $8.50 |

## ✅ Funcionalidades Implementadas
- Inicio y cierre de sesión
- Selección de usuario y producto para registrar venta
- Botón "Registrar Venta" con `command=` y callback
- Persistencia automática en `ventas.json`
- Carpeta `assets/` con recursos visuales ✅

## 🚀 Cómo Ejecutar
```bash
python main.py