import heapq
import logging

# Logging ayarları: seviyeyi INFO yaptım, zaman, seviye ve mesaj görünüyor
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def shortest_path(graph, start, end):
    """
    Bu fonksiyon, bana verilen bir graf yapısında
    başlangıç ve bitiş düğümleri arasındaki en kısa yolu bulur.

    graph: {'A': {'B': 3, 'C': 5}, ...}
    start: başlangıç düğümü
    end: bitiş düğümü

    NEGATİF ağırlık varsa KeyError fırlatır.
    Ulaşılamıyorsa (inf, []), başarıyla çalışır.
    """

    logging.info(f"Algoritma başladı. Başlangıç: {start}, Hedef: {end}")

    # 1) NEGATİF AĞIRLIK KONTROLÜ
    for node, komsular in graph.items():
        for agirlik in komsular.values():
            if agirlik < 0:
                logging.error("Negatif ağırlık tespit edildi. Dijkstra bunu sevmez!")
                raise KeyError("Graf negatif ağırlık içeremez")

    # 2) Kuyruk ve ziyaret kayıtlarını hazırlıyorum
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    visited = {start: 0}
    logging.info(f"{start} düğümü kuyruğa eklendi.")

    # 3) Kuyruk boşalana kadar en kısa yolu aramaya devam ediyorum
    while queue:
        cost, node, path = heapq.heappop(queue)
        logging.info(f"{node} düğümüne geldim. Maliyet: {cost}, Yol: {path}")

        # Hedefe ulaştıysam bitir
        if node == end:
            logging.info(f"Hedef {end} bulundu! Toplam maliyet: {cost}, İzlenen yol: {path}")
            return cost, path

        # Değilse komşuları gez
        for neighbor, weight in graph.get(node, {}).items():
            new_cost = cost + weight
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))
                logging.info(f"{neighbor} komşusu kuyruğa eklendi. Yeni maliyet: {new_cost}")

    # 4) Hedefe hiç ulaşılamadıysa
    logging.warning(f"{end} düğümüne ulaşılamadı. Geri dönüş: inf, []")
    return float('inf'), []

if __name__ == "__main__":
    # Test amaçlı basit bir graf
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'C': 1, 'D': 7},
        'C': {'D': 3},
        'D': {}
    }
    distance, path = shortest_path(graph, 'A', 'D')
    print("En kısa mesafe:", distance)
    print("İzlenen yol:", path)