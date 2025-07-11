from pyalex import Works

# Palavras a buscar
palavra_x = "climate"
palavra_y = "biodiversity"

# Consulta com filtros separados (AND implícito)
resultados = Works().filter(
    **{
        "title.search": palavra_x,
        "abstract.search": palavra_y
    }
).get()

for artigo in resultados:
    print(f"Título: {artigo['title']}")
    print(f"Autores: {[a['author']['display_name'] for a in artigo['authorships']]}")
    print(f"Publicado em: {artigo['publication_date']}")
    print(f"Resumo: {artigo.get('abstract', 'Sem resumo disponível')[:300]}...")
    print(f"Link: {artigo['id']}")
    print("-" * 80)