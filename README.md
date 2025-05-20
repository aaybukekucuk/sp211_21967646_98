# 🔗 shortestpath-aybukekucuk

Bu Python paketi, yönlendirilmiş ve ağırlıklı bir graf üzerinde en kısa yolu hesaplamak için **Dijkstra Algoritması**'nı uygular. Proje, Hacettepe Üniversitesi Geomatik Mühendisliği kapsamında geliştirilmiştir.

---

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Fonksiyon Açıklamaları](#fonksiyon-açıklamaları)
- [Görsel Anlatım](#görsel-anlatım)
- [Testler](#testler)
- [Lisans](#lisans)

---

## Kurulum

PyPI üzerinden kolayca yüklenebilir:

```bash
pip install shortestpath-aybukekucuk

## Kullanım

from shortestpath import dijkstra

# Örnek graf
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

# A noktasından D noktasına en kısa yol
distance, path = dijkstra(graph, 'A', 'D')

print("En kısa mesafe:", distance)
print("İzlenen yol:", path)

##  Örnek Çıktı:
En kısa mesafe: 6
İzlenen yol: ['A', 'B', 'C', 'D']

![Dijkstra Örnek Grafiği](assets/graph.png)

## Test
pytest

