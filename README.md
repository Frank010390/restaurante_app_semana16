# 🍽️ Restaurante App — Semana 16
## Conceptos fundamentales de manejo de eventos

**Autores:** Frank Marlon Carriel Santos

---

## 📋 Descripción del Proyecto
Aplicación de gestión de restaurante desarrollada en Python con interfaz gráfica Tkinter, aplicando los conceptos de Programación Orientada a Objetos, arquitectura modular, persistencia en archivos JSON y manejo de eventos.

El objetivo es comprender cómo una acción del usuario (clic en botón, presionar una tecla, seleccionar un elemento) inicia una respuesta en la aplicación, relacionando usuarios con productos y registrando operaciones de venta.

---

## 📁 Estructura del Proyecto
Restaurante_app_semana16/
├── assets/
│ ├── icons/
│ │ └── icono.png
│ └── logo/
│ └── logo.png
├── datos/
│ ├── productos.json
│ ├── usuarios.json
│ └── ventas.json
├── modelos/
│ ├── init.py
│ ├── producto.py
│ ├── usuario.py
│ └── venta.py
├── servicios/
│ ├── init.py
│ ├── archivo_servicio.py
│ └── restaurante_servicio.py
├── ui/
│ ├── init.py
│ ├── login_view.py
│ └── main_view.py
├── main.py
└── README.md

---

## ✨ Funcionalidades Implementadas

### 🔐 Autenticación
- Inicio de sesión con usuario y contraseña
- Credenciales de prueba:
  - **Usuario:** `admin` | **Contraseña:** `123` → Administrador
  - **Usuario:** `empleado1` | **Contraseña:** `123` → Empleado

### 👤 Gestión de Usuarios (Semana 16 — Manejo de Eventos)
- **Registrar usuario nuevo:** Nombre, contraseña y rol (Administrador / Empleado / Cliente)
- **Seleccionar de la tabla:** Al hacer clic en una fila, los datos se cargan automáticamente en el formulario — Evento: `<<TreeviewSelect>>`
- **Actualizar datos:** Modificar información de un usuario existente
- **Eliminar usuario:** Protección activa → NO puedes eliminar tu propia cuenta
- **Limpiar formulario:** Botón dedicado o tecla ESC
- **Roles y permisos:** Solo los Administradores ven la pestaña de Gestión de Usuarios

### ⌨️ Manejo de Eventos
| Evento | Acción | Resultado |
|---|---|---|
| `<Return>` (Enter) | Presionar Enter en campos de texto | Registra el usuario sin tocar el botón |
| `<Escape>` (Esc) | Presionar tecla Esc en cualquier lugar | Limpia todo el formulario y deselecciona |
| `<<TreeviewSelect>>` | Clic sobre una fila de la tabla | Rellena el formulario con los datos |
| `<<ComboboxSelected>>` | Cambiar la opción de Rol | Detecta la selección del usuario |
| `command=` | Clic en botones (Registrar, Actualizar, Eliminar, Limpiar) | Ejecuta la operación correspondiente |

### 📦 Gestión de Productos
- Registrar, listar y visualizar productos disponibles
- Validación de ID duplicado

### 💰 Gestión de Ventas
- Seleccionar usuario y producto para registrar venta
- Historial completo con identificación automática
- Persistencia de datos entre sesiones

### 💾 Persistencia
- Todos los datos se guardan en archivos JSON
- La información se mantiene al cerrar y reabrir la aplicación

---

## 🚀 Cómo Ejecutar
```bash
python main.py
📝 Notas de la Actividad
Se mantuvo la arquitectura modular desarrollada en semanas anteriores
Se preservaron todos los datos de productos, ventas y usuarios existentes
Se implementó la delegación de operaciones a la capa de servicio
La interfaz responde a acciones del usuario mediante callbacks
Las contraseñas se muestran protegidas en el formulario de edición