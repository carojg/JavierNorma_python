-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-06-2019 a las 05:36:59
-- Versión del servidor: 10.1.40-MariaDB
-- Versión de PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `paises`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paises`
--

CREATE TABLE `paises` (
  `id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `numero_habitantes` int(11) NOT NULL,
  `url_bandera` varchar(200) NOT NULL,
  `capital` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `paises`
--

INSERT INTO `paises` (`id`, `nombre`, `numero_habitantes`, `url_bandera`, `capital`) VALUES
(1, 'Mexico', 122273473, 'https://restcountries.eu/data/mex.svg', 'Mexico City'),
(2, 'Afghanistan', 27657145, 'https://restcountries.eu/data/afg.svg', 'Kabul'),
(3, 'Italy', 60665551, 'https://restcountries.eu/data/ita.svg', 'Rome'),
(4, 'Ecuador', 16545799, 'https://restcountries.eu/data/ecu.svg', 'Quito'),
(5, 'Canada', 36155487, 'https://restcountries.eu/data/can.svg', 'Ottawa'),
(6, 'El Salvador', 6520675, 'https://restcountries.eu/data/slv.svg', 'San Salvador'),
(7, 'Nicaragua', 6262703, 'https://restcountries.eu/data/nic.svg', 'Managua'),
(8, 'Chile', 18191900, 'https://restcountries.eu/data/chl.svg', 'Santiago'),
(9, 'Belize', 370300, 'https://restcountries.eu/data/blz.svg', 'Belmopan'),
(10, 'Colombia', 48759958, 'https://restcountries.eu/data/col.svg', 'Bogotá'),
(11, 'Argentina', 43590400, 'https://restcountries.eu/data/arg.svg', 'Buenos Aires'),
(12, 'Albania', 2886026, 'https://restcountries.eu/data/alb.svg', 'Tirana'),
(13, 'Australia', 24117360, 'https://restcountries.eu/data/aus.svg', 'Canberra'),
(14, 'Bolivia (Plurinational State of)', 10985059, 'https://restcountries.eu/data/bol.svg', 'Sucre'),
(15, 'Brazil', 206135893, 'https://restcountries.eu/data/bra.svg', 'Brasília'),
(16, 'Cuba', 11239004, 'https://restcountries.eu/data/cub.svg', 'Havana'),
(17, 'Costa Rica', 4890379, 'https://restcountries.eu/data/cri.svg', 'San José'),
(18, 'Haiti', 11078033, 'https://restcountries.eu/data/hti.svg', 'Port-au-Prince'),
(19, 'Honduras', 8576532, 'https://restcountries.eu/data/hnd.svg', 'Tegucigalpa'),
(20, 'Peru', 31488700, 'https://restcountries.eu/data/per.svg', 'Lima');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `paises`
--
ALTER TABLE `paises`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `paises`
--
ALTER TABLE `paises`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
