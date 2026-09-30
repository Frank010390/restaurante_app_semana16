# 🍽️ Restaurante App — Semana 16
**Estudiantes:** Frank Marlon Carriel Santos
**Asignatura:** Programación Orientada a Objetos

## 📋 Descripción
Proyecto de gestión de restaurante desarrollado en Python con Tkinter. En la Semana 16 se amplía el sistema con **gestión de usuarios mediante eventos**, incluyendo roles, atajos de teclado y persistencia en JSON.

## 📁 Estructura
restaurante_app/
├── datos/
│ ├── usuarios.json
│ ├── productos.json
│ └── ventas.json
├── modelos/
│ ├── usuario.py
│ ├── producto.py
│ └── venta.py
├── servicios/
│ ├── archivo_servicio.py
│ └── restaurante_servicio.py
├── ui/
│ ├── login_view.py
│ └── main_view.py
├── assets/
│ ├── icons/icono.png
│ └── logo/logo.png
├── main.py
└── README.md

## 👤 Gestión de Usuarios y Roles
- **Administrador** → acceso completo a todas las funciones incluida la gestión de usuarios
- **Empleado** → puede registrar productos y ventas, NO administra usuarios
- **Cliente** → visualización y compras

## ⚡ Eventos implementados
| Evento | Mecanismo | Acción |
|---|---|---|
| `<<TreeviewSelect>>` | `bind()` | Carga datos del usuario seleccionado en el formulario |
| `<Return>` (Enter) | `bind()` | Ejecuta el registro del usuario |
| `<Escape>` (Esc) | `bind()` | Limpia formulario y deselecciona fila |
| `<<ComboboxSelected>>` | `bind()` | Detecta cambio de rol seleccionado |
| Botones | `command=` | Registrar, Actualizar, Eliminar, Limpiar |

## 🚀 Cómo ejecutar
1. Abre la carpeta del proyecto
2. Ejecuta:
```bash
python main.py