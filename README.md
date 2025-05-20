# shortestpath-aybukekucuk

Bu proje, **Dijkstra algoritması** kullanarak iki nokta arasındaki en kısa yolu bulmamıza yardımcı olan basit ama işlevsel bir Python modülüdür. Özellikle algoritma derslerinde ya da yol bulma uygulamaları geliştirmek isteyenler için ideal.

---

## Görsel Anlatım

Aşağıdaki GIF, Dijkstra algoritmasının nasıl çalıştığını animasyonlu şekilde göstermektedir:

![Dijkstra Görseli](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

---

## Kurulum

Paketi test PyPI üzerinden kurmak için:

```bash
pip install -i https://test.pypi.org/simple/ shortestpath-aybukekucuk

## Kullanım

from shortestpath import dijkstra_shortest_path

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'C': 1, 'D': 4},
    'C': {'D': 1},
    'D': {}
}

distance, path = dijkstra_shortest_path(graph, 'A', 'D')
print("En kısa mesafe:", distance)
print("İzlenen yol:", path)

çıktı:
En kısa mesafe: 4
İzlenen yol: ['A', 'B', 'C', 'D']

## Klasör Yapısı

shortestpath_project/
│
├── shortestpath/
│   ├── __init__.py
│   └── shortestpath.py
│
├── tests/
│   └── test_shortestpath.py
│
├── README.md
├── pyproject.toml
├── requirements.txt
└── LICENSE

## Fonksiyon Özeti Tablosu

| Fonksiyon Adı             | Açıklama                                                   | Parametreler                          | Dönüş Değeri                        |
|--------------------------|------------------------------------------------------------|----------------------------------------|-------------------------------------|
| `dijkstra_shortest_path` | İki nokta arasındaki en kısa yolu Dijkstra algoritması ile bulur. | `graph: dict, start: str, end: str` | `(mesafe: int, yol: list[str])`     |
