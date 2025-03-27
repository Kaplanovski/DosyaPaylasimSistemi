-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 29 Ara 2024, 17:40:06
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `ngrok_proje`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `izinli_ogrenciler`
--

CREATE TABLE `izinli_ogrenciler` (
  `id` int(11) NOT NULL,
  `ogrenci_no` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `izinli_ogrenciler`
--

INSERT INTO `izinli_ogrenciler` (`id`, `ogrenci_no`) VALUES
(1, '33233304053'),
(5, '33233304087'),
(3, '33233304088'),
(2, '789012'),
(6, 'mehmetozcan');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `izinli_ogrenciler`
--
ALTER TABLE `izinli_ogrenciler`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ogrenci_no` (`ogrenci_no`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `izinli_ogrenciler`
--
ALTER TABLE `izinli_ogrenciler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
