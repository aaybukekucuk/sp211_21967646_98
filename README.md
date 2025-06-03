# sp211_21967646_98

Bu proje, **Dijkstra algoritması** kullanarak iki nokta arasındaki en kısa yolu bulmamıza yardımcı olan basit ama işlevsel bir Python modülüdür. Özellikle algoritma derslerinde ya da yol bulma uygulamaları geliştirmek isteyenler için ideal.

## Assignment Metadata

- Student Name: Aybüke Küçük  
- Student Number: 21967646  
- DD Code: 98  
- Course: SP211 – Data Structures and Algorithms  

---

## Görsel Anlatım

Aşağıdaki görsel oluşturduğum Sphinx dökümantasyonun web ekran görüntüsü:

![Sphinx Ekran Görüntüsü ](https://github.com/user-attachments/assets/d65c1e61-100f-4301-93c6-5f4b39a20083)

---

## Fonksiyon tablosu

| Fonksiyon Adı             | Açıklama                                                   | Parametreler                          | Dönüş Değeri                        |
|--------------------------|------------------------------------------------------------|----------------------------------------|-------------------------------------|
| `dijkstra_shortest_path` | İki nokta arasındaki en kısa yolu Dijkstra algoritması ile bulur. | `graph: dict, start: str, end: str` | `(mesafe: int, yol: list[str])`     |

---
## AI Usage – How I Benefited
In this project, I utilized artificial intelligence (AI) technology, specifically OpenAI's ChatGPT model, to assist me throughout the development process. I leveraged AI support to learn best practices and solve challenges related to coding and Python package development.

    - Specifically, AI helped me with:
    - Creating the Python package structure and setup.py file,
    - Resolving issues with Git and GitHub workflows,
    - Integrating logging functionality,

Using AI guidance saved me time and improved the overall quality of the project.

My level of AI usage 4/5

---
## Logging Kullanımı

Bu projede, programın çalışma sürecinde oluşan önemli olayları takip etmek için Python’un standart logging modülü kullanılmıştır. logging sayesinde hata mesajları, uyarılar veya bilgi mesajları kayıt altına alınabilir ve böylece kodun nasıl çalıştığını anlamak ve hataları kolayca tespit etmek mümkün olur.

import logging

# Logging seviyesini ayarla
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program başladı.")
logging.warning("Bu bir uyarı mesajıdır.")
logging.error("Bir hata oluştu.")

---

## Kurulum

Paketi PyPI üzerinden kurmak için:

```bash
pip install shortestpath-aybukekucuk

---

Module Structure
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

Not: GitHub Classroom üzerinden gönderim sırasında teknik sorunlar yaşadım. Classroom bağlantısıyla ilişkilendirilmiş repo üzerinde push/pull işlemleri sırasında kimlik doğrulama hataları aldım ve çözüme ulaşamadım. Bu nedenle, projemi kişisel GitHub hesabımda 
[bu repo](https://github.com/aaybukekucuk/sp211_21967646_98.git) üzerinden eksiksiz şekilde yayımladım.