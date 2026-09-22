# ==============================================================================
# SISTEMA DE ORIENTACIÓN Y REGISTRO DE ATENCIONES - SOPORTE ACADÉMICO
# ==============================================================================

# Lista global de tipos permitidos para validación (Req. 3)
TIPOS_PERMITIDOS = ["matrícula", "pagos", "constancia", "plataforma", "otro"]




def validar_codigo(codigo: str, min_longitud: int = 4) -> bool:
    """Función con retorno (Req. 2): Valida código no vacío y con longitud mínima."""
    codigo_limpio = codigo.strip()
    return len(codigo_limpio) >= min_longitud and codigo_limpio.isalnum()


def validar_tipo_consulta(tipo: str) -> bool:
    """Función con retorno (Req. 3): Verifica si el tipo pertenece a la lista."""
    return tipo.strip().lower() in TIPOS_PERMITIDOS


def asignar_prioridad(tipo: str) -> str:
    """Función con retorno (Req. 5): Asigna prioridad Alta o Baja según tipo de consulta."""
    tipo_normalizado = tipo.strip().lower()
    if tipo_normalizado in ["matrícula", "pagos"]:
        return "Alta"
    return "Baja"


def mostrar_resumen(solicitud: dict):
    """Función sin retorno (Req. 7): Formatea y muestra los datos de la solicitud."""
    print("\n----------------------------------------")
    print("       DATOS DE LA ATENCIÓN REGISTRADA   ")
    print("----------------------------------------")
    print(f"Código Estudiante : {solicitud['codigo']}")
    print(f"Nombre Estudiante : {solicitud['nombre']}")
    print(f"Tipo de Consulta  : {solicitud['tipo'].capitalize()}")
    print(f"Descripción       : {solicitud['descripcion']}")
    print(f"Prioridad Asignada: {solicitud['prioridad']}")
    print("----------------------------------------")


def registrar_solicitud() -> dict:
    """Registra datos básicos, valida la entrada y retorna la solicitud formateada (Req. 1, 8, 9)."""
    print("\n--- NUEVA SOLICITUD DE SOPORTE ---")

    # Validación de Código
    while True:
        codigo = input("Ingrese código de estudiante (mín. 4 caracteres): ")
        if validar_codigo(codigo):
            break
        print("❌ Error: El código debe ser alfanumérico y tener al menos 4 caracteres.")

    # Validación de Nombre
    while True:
        nombre = input("Ingrese nombre completo del estudiante: ")
        if validar_texto_obligatorio(nombre):
            break
        print("❌ Error: El nombre no puede estar vacío.")

    # Validación de Tipo de Consulta
    print(f"Opciones válidas: {', '.join(TIPOS_PERMITIDOS)}")
    while True:
        tipo = input("Ingrese tipo de consulta: ")
        if validar_tipo_consulta(tipo):
            break
        print("❌ Error: Tipo de consulta no válido.")

    # Validación de Descripción
    while True:
        descripcion = input("Ingrese breve descripción del problema: ")
        if validar_texto_obligatorio(descripcion):
            break
        print("❌ Error: La descripción no puede estar vacía.")

    # Asignación de Prioridad
    prioridad = asignar_prioridad(tipo)

    # Construcción de estructura local
    nueva_solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo": tipo.strip().lower(),
        "descripcion": descripcion.strip(),
        "prioridad": prioridad
    }

    mostrar_resumen(nueva_solicitud)
    return nueva_solicitud


def main():
    """Programa principal para controlar la ejecución y registrar múltiples solicitudes (Req. 10)."""
    solicitudes = []  # Lista local para guardar atenciones

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            solicitud = registrar_solicitud()
            solicitudes.append(solicitud)
            print(f"✅ Registrado exitosamente. Total acumulado: {len(solicitudes)}")

        elif opcion == "2":
            if not solicitudes:
                print("\n⚠️ No hay solicitudes registradas aún.")
            else:
                print(f"\n================ ATENCIONES REGISTRADAS ({len(solicitudes)}) ================")
                for idx, sol in enumerate(solicitudes, 1):
                    print(f"[{idx}] Código: {sol['codigo']} | Alumno: {sol['nombre']} | Tipo: {sol['tipo']} | Prioridad: {sol['prioridad']}")

        elif opcion == "3":
            if len(solicitudes) < 3:
                print(f"\n⚠️ Nota: Llevas {len(solicitudes)} registro(s). La guía requiere probar con al menos 3 solicitudes.")
                confirmar = input("¿Deseas salir de todas formas? (s/n): ").lower()
                if confirmar != 's':
                    continue
            print("\n¡Gracias por utilizar el sistema de Soporte Académico!")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()