"""
Script para crear Brains preconfigurados de la UFRO.

Uso:
  UFRO_API_URL=http://localhost:5050 UFRO_API_KEY=<tu-api-key> python seed_ufro_brains.py

El UFRO_API_KEY es el JWT de Supabase de un usuario administrador de la plataforma.
Los brains se crearán como "public" para que toda la comunidad pueda usarlos.
"""

import os
import sys

import httpx

API_URL = os.getenv("UFRO_API_URL", "http://localhost:5050")
API_KEY = os.getenv("UFRO_API_KEY", "")

if not API_KEY:
    print("ERROR: Define la variable de entorno UFRO_API_KEY con el JWT del administrador.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

UFRO_BRAINS = [
    {
        "name": "📚 Reglamento Académico UFRO",
        "description": (
            "Asistente especializado en el Reglamento Académico de la Universidad de La Frontera. "
            "Responde preguntas sobre matrículas, evaluaciones, convalidaciones, becas y normativas "
            "académicas vigentes. Carga el documento PDF del reglamento para activarlo."
        ),
        "status": "public",
        "brain_type": "doc",
        "temperature": 0.1,
        "max_tokens": 2000,
    },
    {
        "name": "🗺️ Asistente de Mallas Curriculares",
        "description": (
            "Ayuda a estudiantes a navegar las mallas curriculares de todas las carreras de la UFRO. "
            "Consulta sobre ramos obligativos, electivos, prerrequisitos y créditos. "
            "Carga las mallas curriculares en PDF para activarlo."
        ),
        "status": "public",
        "brain_type": "doc",
        "temperature": 0.0,
        "max_tokens": 2000,
    },
    {
        "name": "🏛️ Servicios Estudiantiles UFRO",
        "description": (
            "Información sobre servicios disponibles para estudiantes: bienestar estudiantil, "
            "deportes, casino, biblioteca, salud estudiantil, becas internas y actividades "
            "extracurriculares de la Universidad de La Frontera."
        ),
        "status": "public",
        "brain_type": "doc",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
    {
        "name": "🔬 Investigación y Postgrado UFRO",
        "description": (
            "Asistente para la comunidad investigadora y postgraduada de la UFRO. "
            "Información sobre programas de magíster y doctorado, centros de investigación, "
            "fondos ANID, publicaciones y oportunidades de colaboración científica."
        ),
        "status": "public",
        "brain_type": "doc",
        "temperature": 0.2,
        "max_tokens": 2000,
    },
    {
        "name": "💼 Vinculación con el Medio y Empleabilidad",
        "description": (
            "Información sobre prácticas profesionales, bolsa de trabajo, titulación, "
            "relación de la UFRO con el sector público y privado de La Araucanía, "
            "y oportunidades de emprendimiento e innovación."
        ),
        "status": "public",
        "brain_type": "doc",
        "temperature": 0.3,
        "max_tokens": 1500,
    },
]


def create_brain(client: httpx.Client, brain_data: dict) -> dict | None:
    response = client.post(f"{API_URL}/brains/", json=brain_data, headers=HEADERS)
    if response.status_code == 200:
        created = response.json()
        print(f"  ✅ Brain creado: '{brain_data['name']}' (id: {created.get('id', '?')})")
        return created
    else:
        print(f"  ❌ Error creando '{brain_data['name']}': {response.status_code} - {response.text}")
        return None


def main() -> None:
    print("=== Seed de Brains UFRO ===\n")
    print(f"API: {API_URL}")
    print(f"Brains a crear: {len(UFRO_BRAINS)}\n")

    with httpx.Client(timeout=30.0) as client:
        created_count = 0
        for brain_data in UFRO_BRAINS:
            result = create_brain(client, brain_data)
            if result:
                created_count += 1

    print(f"\n=== Resultado: {created_count}/{len(UFRO_BRAINS)} brains creados exitosamente ===")
    if created_count < len(UFRO_BRAINS):
        print(
            "\nNota: Los brains creados son contenedores vacíos. "
            "Debes cargar los documentos PDF correspondientes en cada Brain "
            "desde la interfaz web para que puedan responder consultas."
        )


if __name__ == "__main__":
    main()
