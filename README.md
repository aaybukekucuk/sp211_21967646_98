# sp211_21967646_98

Bu proje, **Dijkstra algoritması** kullanarak iki nokta arasındaki en kısa yolu bulmamıza yardımcı olan basit ama işlevsel bir Python modülüdür. Özellikle algoritma derslerinde ya da yol bulma uygulamaları geliştirmek isteyenler için ideal.

## Assignment Metadata

- Student Name: Aybüke Küçük  
- Student Number: 21967646  
- DD Code: 98  
- Course: SP211 – Data Structures and Algorithms  

---

## Görsel Anlatım

Aşağıdaki GIF, Dijkstra algoritmasının nasıl çalıştığını animasyonlu şekilde göstermektedir:

![Dijkstra Görseli](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

---

## Fonksiyon tablosu

| Fonksiyon Adı             | Açıklama                                                   | Parametreler                          | Dönüş Değeri                        |
|--------------------------|------------------------------------------------------------|----------------------------------------|-------------------------------------|
| `dijkstra_shortest_path` | İki nokta arasındaki en kısa yolu Dijkstra algoritması ile bulur. | `graph: dict, start: str, end: str` | `(mesafe: int, yol: list[str])`     |

---

## Kurulum

Paketi PyPI üzerinden kurmak için:

```bash
pip install shortestpath-aybukekucuk

Klasör yapısı
shortestpath_project/
│
├── shortestpath/
│ ├── init.py
│ └── shortestpath.py
│
├── tests/
│ └── test_shortestpath.py
│
├── README.md
├── pyproject.toml
├── requirements.txt
└── LICENSE

---