-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 25, 2024 at 12:56 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbumc_pbo`
--

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa_pbo2`
--

CREATE TABLE `mahasiswa_pbo2` (
  `id` int(11) UNSIGNED NOT NULL,
  `nim` varchar(100) DEFAULT '',
  `nama` varchar(100) NOT NULL,
  `kelas` varchar(100) DEFAULT '',
  `program_studi` varchar(100) DEFAULT '',
  `fakultas` varchar(100) DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `mahasiswa_pbo2`
--

INSERT INTO `mahasiswa_pbo2` (`id`, `nim`, `nama`, `kelas`, `program_studi`, `fakultas`) VALUES
(1, '330510001', 'Nana', 'TF22A', 'Teknik Informatika', 'Teknik'),
(2, '330510002', 'Handre', 'TF22A', 'Teknik Informatika', 'Teknik'),
(6, '3002544', 'Saputra', 'TF22A', 'Teknik Informatika', 'Teknik'),
(13, '987987', 'Johan', 'TF33E', 'Teknik Informatika', 'Teknik');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mahasiswa_pbo2`
--
ALTER TABLE `mahasiswa_pbo2`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nidn` (`nim`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mahasiswa_pbo2`
--
ALTER TABLE `mahasiswa_pbo2`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
