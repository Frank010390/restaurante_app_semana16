# Aplicación de Gestión de Restaurante

*Estudiante:* Frank Marlon Carriel Santos  
*Asignatura:* Programación Orientada a Objetos  

---

Proyecto desarrollado en Python para la gestión básica de un restaurante, aplicando programación orientada a objetos (POO), arquitectura modular en capas y persistencia de datos mediante archivos JSON.

---

## 📁 Estructura del Proyecto

```text
Restaurante_app_semana13/
│
├── datos/
│   └── _init_.py
│
├── servicios/
│   ├── _init_.py
│   ├── archivo_servicio.py      # Servicio para lectura y escritura en JSON
│   └── restaurante_servicio.py  # Lógica de negocio y autenticación
│
├── ui/
│   ├── _init_.py
│   ├── login_view.py            # Vista de inicio de sesión (Tkinter)
│   └── main_view.py             # Vista prin…
🚀 Requisitos e Instalación
​Python 3.x instalado.
​No requiere bibliotecas externas (utiliza la librería estándar de Python tkinter y json).
​⚙️ Instrucciones de Ejecución
git clone https://github.com/Frank010390/Restaurante_app_semana13.git
Navega al directorio del proyecto:
cd Restaurante_app_semana13
Ejecuta el archivo principal:
python main.py
🔑 Credenciales de Prueba
​Al iniciar la aplicación por primera vez, el sistema genera automáticamente el archivo usuarios.json con los siguientes usuarios predeterminados:
UsuarioContraseñaRol
admin123Admin
mesero1123Mesero
✨ Características
​Autenticación: Formulario de inicio de sesión interactivo con validación de credenciales.
​Manejo de Sesiones: Cierre de sesión y control de vistas dinámico.
​Interfaz Gráfica: Diseñada con Tkinter usando pestañas (ttk.Notebook) y tablas de datos (ttk.Treeview).
​Persistencia: Almacenamiento y carga de información persistente a través de JSON.