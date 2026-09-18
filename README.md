# Restaurante App — Programación Orientada a Objetos

**Estudiante:** Frank Marlon Carriel Santos
**Materia:** Programación Orientada a Objetos
**Etapa:** Semana 14 — Componentes y Contenedores

---

## 📋 Descripción del Proyecto

Aplicación de escritorio para la gestión de un restaurante, desarrollada en Python con Tkinter. El proyecto evoluciona por etapas, manteniendo arquitectura modular, persistencia de datos en archivos JSON y separación de responsabilidades entre interfaz, lógica de negocio y acceso a datos.

### 🎯 Objetivo de la Semana 14
Aplicar el uso de **componentes, contenedores y gestores de geometría** de Tkinter para mejorar la interfaz gráfica, incorporando formularios estructurados, áreas de visualización y botones de acción, sin alterar la funcionalidad ya implementada.

---

## 🗂️ Estructura del Proyecto
Restaurante_app_semana13/
├── datos/
│ ├── productos.json # Almacén de productos
│ └── usuarios.json # Almacén de usuarios
├── modelos/
│ ├── producto.py # Clase modelo Producto
│ └── usuario.py # Clase modelo Usuario
├── servicios/
│ ├── archivo_servicio.py # Lectura y escritura en JSON
│ └── restaurante_servicio.py # Lógica de negocio
├── ui/
│ ├── login_view.py # Interfaz de inicio de sesión
│ └── main_view.py # Interfaz principal con pestañas
├── main.py # Punto de entrada de la aplicación
└── README.md # Documentación
plaintext

---

## ✅ Funcionalidades Implementadas

### 🔐 Autenticación
- Inicio de sesión con usuario y contraseña
- Control de sesión y cierre seguro
- Credenciales de prueba: `admin` / `123`

### 👥 Gestión de Usuarios (Semana 13)
- Visualización de usuarios registrados en tabla
- Persistencia en `usuarios.json`

### 📦 Gestión de Productos (Semana 14)
| Operación | Descripción |
|---|---|
| ✅ **Registrar** | Agregar nuevo producto con ID, nombre y precio |
| 🔍 **Consultar** | Buscar producto por su identificador |
| 🔄 **Actualizar** | Modificar nombre y precio de producto existente |
| 🗑️ **Eliminar** | Remover producto del listado |
| 📊 **Listar** | Visualización en tabla de todos los productos |

---

## 🧩 Mejoras de Interfaz — Semana 14

| Componente / Contenedor | Uso |
|---|---|
| `ttk.Notebook` | Organización por pestañas: Usuarios y Productos |
| `ttk.LabelFrame` | Agrupación lógica: Datos del Producto, Acciones, Listado |
| `tk.Frame` | Separación de áreas en la ventana |
| `ttk.Treeview` | Visualización tabular de productos |
| `ttk.Entry` + `ttk.Button` | Formularios interactivos |
| Gestores `pack()` y `grid()` | Distribución ordenada y adaptable |

---

## 🚀 Ejecución del Proyecto

### Requisitos
- Python 3.x instalado
- Tkinter incluido en la instalación estándar de Python

### Pasos
```bash
# 1. Ingresar a la carpeta del proyecto
cd Restaurante_app_semana13

# 2. Ejecutar la aplicación
python main.py
Credenciales de acceso
Usuario: admin
Contraseña: 123
💾 Persistencia de Datos
Los datos se guardan automáticamente en archivos JSON dentro de la carpeta datos/
productos.json — Base de productos gestionados
usuarios.json — Usuarios con acceso al sistema
Se maneja mediante la clase ArchivoServicio con métodos cargar_json() y guardar_json()