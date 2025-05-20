from setuptools import setup, find_packages

# Ben projemi paket olarak yükleyebilmek için bu bilgileri hazırladım
setup(
    name='shortestpath',                             # Paket adı
    version='0.1.0',                                 # Sürüm numarası
    description='En kısa yol hesaplama modülü',      # Kısa açıklama
    author='Aybuke Kucuk',                           # Benim adım
    packages=find_packages(),                        # "shortestpath" klasörünü otomatik bulur
    install_requires=[],                             # Başka bağımlılık yok
    python_requires='>=3.7',                         # Desteklenen minimum Python sürümü
)