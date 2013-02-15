-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 04, 2013 at 01:38 PM
-- Server version: 5.5.28
-- PHP Version: 5.4.6-1ubuntu1.1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `access`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=52 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add flat page', 7, 'add_flatpage'),
(20, 'Can change flat page', 7, 'change_flatpage'),
(21, 'Can delete flat page', 7, 'delete_flatpage'),
(22, 'Can add log entry', 8, 'add_logentry'),
(23, 'Can change log entry', 8, 'change_logentry'),
(24, 'Can delete log entry', 8, 'delete_logentry'),
(25, 'Can add user profile', 9, 'add_userprofile'),
(26, 'Can change user profile', 9, 'change_userprofile'),
(27, 'Can delete user profile', 9, 'delete_userprofile'),
(28, 'Can add Especialidad para citas', 10, 'add_especialidad'),
(29, 'Can change Especialidad para citas', 10, 'change_especialidad'),
(30, 'Can delete Especialidad para citas', 10, 'delete_especialidad'),
(31, 'Can add Cita', 11, 'add_cita'),
(32, 'Can change Cita', 11, 'change_cita'),
(33, 'Can delete Cita', 11, 'delete_cita'),
(34, 'Can add Tipo de Póliza', 12, 'add_tipo_poliza'),
(35, 'Can change Tipo de Póliza', 12, 'change_tipo_poliza'),
(36, 'Can delete Tipo de Póliza', 12, 'delete_tipo_poliza'),
(37, 'Can add Tipo de cobertura', 13, 'add_tipo_cobertura'),
(38, 'Can change Tipo de cobertura', 13, 'change_tipo_cobertura'),
(39, 'Can delete Tipo de cobertura', 13, 'delete_tipo_cobertura'),
(40, 'Can add membresia', 14, 'add_membresia'),
(41, 'Can change membresia', 14, 'change_membresia'),
(42, 'Can delete membresia', 14, 'delete_membresia'),
(43, 'Can add Info. adicional para activación', 15, 'add_info_adicional'),
(44, 'Can change Info. adicional para activación', 15, 'change_info_adicional'),
(45, 'Can delete Info. adicional para activación', 15, 'delete_info_adicional'),
(46, 'Can add Miembro adicional', 16, 'add_miembros_adicionales'),
(47, 'Can change Miembro adicional', 16, 'change_miembros_adicionales'),
(48, 'Can delete Miembro adicional', 16, 'delete_miembros_adicionales'),
(49, 'Can add kv store', 17, 'add_kvstore'),
(50, 'Can change kv store', 17, 'change_kvstore'),
(51, 'Can delete kv store', 17, 'delete_kvstore');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'dev', '', '', 'roberto@newemage.com', 'pbkdf2_sha256$10000$HIywNF4liWTq$AyhPQ4tBrsekXSGzAX40SXGBvxCe2QtUts/0FAkOwYI=', 1, 1, 1, '2013-01-04 12:33:09', '2013-01-04 12:29:17'),
(2, 'robertuj', 'Roberto', 'Urita Jimenez', 'roberto@newemage.com', 'pbkdf2_sha256$10000$2b19TwO4vkAN$bvEzTIsA44yIJordbWCejSU2S0fAF9pOxxZbotS2H4s=', 0, 1, 0, '2013-01-04 12:37:16', '2013-01-04 12:37:12');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `citas_cita`
--

CREATE TABLE IF NOT EXISTS `citas_cita` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_membresia_id` int(11) NOT NULL,
  `es_titular` tinyint(1) NOT NULL,
  `relacion_titular` varchar(255) DEFAULT NULL,
  `nombre_completo` varchar(255) DEFAULT NULL,
  `datos_contacto` longtext,
  `fecha_cita` date NOT NULL,
  `especialidad_cita_id` int(11) NOT NULL,
  `especialidad_cita_otra` varchar(255) DEFAULT NULL,
  `motivos_cita` longtext,
  `estudios_fechas` longtext,
  `uso_poliza` tinyint(1) NOT NULL,
  `recomendaciones` tinyint(1) NOT NULL,
  `atendido_huston` tinyint(1) NOT NULL,
  `donde` varchar(255) DEFAULT NULL,
  `cuando` date DEFAULT NULL,
  `comentarios` longtext,
  `confirmada` tinyint(1) NOT NULL,
  `fecha` datetime NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `info_vuelo` longtext,
  `socio_id` int(11) DEFAULT NULL,
  `miembro_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `citas_cita_34f44c1b` (`no_membresia_id`),
  KEY `citas_cita_6422758d` (`especialidad_cita_id`),
  KEY `citas_cita_2fc74d8c` (`socio_id`),
  KEY `citas_cita_4478c0b0` (`miembro_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `citas_cita`
--

INSERT INTO `citas_cita` (`id`, `no_membresia_id`, `es_titular`, `relacion_titular`, `nombre_completo`, `datos_contacto`, `fecha_cita`, `especialidad_cita_id`, `especialidad_cita_otra`, `motivos_cita`, `estudios_fechas`, `uso_poliza`, `recomendaciones`, `atendido_huston`, `donde`, `cuando`, `comentarios`, `confirmada`, `fecha`, `estado`, `info_vuelo`, `socio_id`, `miembro_id`) VALUES
(3, 1, 1, '', '', '', '2013-05-15', 2, '', 'asdf', '', 1, 1, 0, '', NULL, 'asdfasdf', 0, '2013-01-04 14:20:30', 1, '', 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `citas_especialidad`
--

CREATE TABLE IF NOT EXISTS `citas_especialidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `especialidad` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `citas_especialidad`
--

INSERT INTO `citas_especialidad` (`id`, `especialidad`) VALUES
(1, 'test 1'),
(2, 'tes 2'),
(3, 'test 3');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2013-01-04 12:35:17', 1, 13, '1', 'test 1', 1, ''),
(2, '2013-01-04 12:35:20', 1, 13, '2', 'test 2', 1, ''),
(3, '2013-01-04 12:35:23', 1, 13, '3', 'test 3', 1, ''),
(4, '2013-01-04 12:35:31', 1, 12, '1', 'test 1', 1, ''),
(5, '2013-01-04 12:35:34', 1, 12, '2', 'test 2', 1, ''),
(6, '2013-01-04 12:35:37', 1, 12, '3', 'test 3', 1, ''),
(7, '2013-01-04 13:04:01', 1, 10, '1', 'test 1', 1, ''),
(8, '2013-01-04 13:04:04', 1, 10, '2', 'tes 2', 1, ''),
(9, '2013-01-04 13:04:07', 1, 10, '3', 'test 3', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'flat page', 'flatpages', 'flatpage'),
(8, 'log entry', 'admin', 'logentry'),
(9, 'user profile', 'usuarios', 'userprofile'),
(10, 'Especialidad para citas', 'citas', 'especialidad'),
(11, 'Cita', 'citas', 'cita'),
(12, 'Tipo de Póliza', 'membresias', 'tipo_poliza'),
(13, 'Tipo de cobertura', 'membresias', 'tipo_cobertura'),
(14, 'membresia', 'membresias', 'membresia'),
(15, 'Info. adicional para activación', 'membresias', 'info_adicional'),
(16, 'Miembro adicional', 'membresias', 'miembros_adicionales'),
(17, 'kv store', 'thumbnail', 'kvstore');

-- --------------------------------------------------------

--
-- Table structure for table `django_flatpage`
--

CREATE TABLE IF NOT EXISTS `django_flatpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `template_name` varchar(70) NOT NULL,
  `registration_required` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_flatpage_a4b49ab` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_flatpage_sites`
--

CREATE TABLE IF NOT EXISTS `django_flatpage_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flatpage_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flatpage_id` (`flatpage_id`,`site_id`),
  KEY `django_flatpage_sites_21210108` (`flatpage_id`),
  KEY `django_flatpage_sites_6223029` (`site_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('e5ccd7682f122fbcc4d5fc60be1bfa9d', 'MzU3N2I5YTliZTUzMmQzMDZhMmE0Mjg0NGZjNzc2OWFkZDAyOWYzYTqAAn1xAShVDG1lbWJyZXNp\nYV9pZIoBAVUJaWRzX2NpdGFzXXECWAEAAAAzYVUFcGtNZW2KAQFVEl9hdXRoX3VzZXJfYmFja2Vu\nZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVDV9hdXRoX3VzZXJf\naWSKAQJ1Lg==\n', '2013-01-18 20:28:19'),
('fe63af1a94e3a8155dbbf4fefc4f2fe7', 'ZjVjODNkMTk1NDViMjQ4ZDc0MmVmYmFmNmMxMjgxNDkxN2JkMTVhNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-01-18 12:33:09');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `membresias_info_adicional`
--

CREATE TABLE IF NOT EXISTS `membresias_info_adicional` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `membresia_id` int(11) NOT NULL,
  `compania_seguros` varchar(255) NOT NULL,
  `nombre_representante` varchar(255) DEFAULT NULL,
  `telefono_representante` varchar(255) DEFAULT NULL,
  `poliza` varchar(255) NOT NULL,
  `tipo_poliza_id` int(11) NOT NULL,
  `tipo_cobertura_id` int(11) NOT NULL,
  `tipo_poliza_otro` varchar(255) DEFAULT NULL,
  `tipo_cobertura_otro` varchar(255) DEFAULT NULL,
  `fecha_vencimiento` date NOT NULL,
  `contacto_emergencia_usa` varchar(255) DEFAULT NULL,
  `telefono_contacto_usa` varchar(50) DEFAULT NULL,
  `nombre_dr_mexico` varchar(255) DEFAULT NULL,
  `telefono_dr_mexico` varchar(255) DEFAULT NULL,
  `info_adicional_tx_center` longtext,
  `no_pasaporte` varchar(255) DEFAULT NULL,
  `no_visa` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `membresias_info_adicional_1f04a814` (`membresia_id`),
  KEY `membresias_info_adicional_115c44b` (`tipo_poliza_id`),
  KEY `membresias_info_adicional_67a644a2` (`tipo_cobertura_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `membresias_info_adicional`
--

INSERT INTO `membresias_info_adicional` (`id`, `membresia_id`, `compania_seguros`, `nombre_representante`, `telefono_representante`, `poliza`, `tipo_poliza_id`, `tipo_cobertura_id`, `tipo_poliza_otro`, `tipo_cobertura_otro`, `fecha_vencimiento`, `contacto_emergencia_usa`, `telefono_contacto_usa`, `nombre_dr_mexico`, `telefono_dr_mexico`, `info_adicional_tx_center`, `no_pasaporte`, `no_visa`) VALUES
(1, 1, 'Test Nombre Seguros', 'Juan Perez', '656 8421541', '65487', 2, 1, '21547', 'a5487', '2060-05-15', 'Rafael Caro', '016191457875', 'Alfredo Olivarez', '6568754835', '', '21548745487', '13215787897');

-- --------------------------------------------------------

--
-- Table structure for table `membresias_membresia`
--

CREATE TABLE IF NOT EXISTS `membresias_membresia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido_paterno` varchar(100) NOT NULL,
  `apellido_materno` varchar(255) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `nacionalidad` varchar(100) NOT NULL,
  `genero` varchar(10) NOT NULL,
  `estado_civil` varchar(50) NOT NULL,
  `calle` varchar(100) NOT NULL,
  `no_exterior` varchar(10) NOT NULL,
  `no_interior` varchar(10) DEFAULT NULL,
  `colonia` varchar(100) NOT NULL,
  `municipio` varchar(150) NOT NULL,
  `ciudad` varchar(100) NOT NULL,
  `cp` int(11) NOT NULL,
  `pais` varchar(150) NOT NULL,
  `email` varchar(200) NOT NULL,
  `email_alternativo` varchar(200) DEFAULT NULL,
  `lada_movil` varchar(20) NOT NULL,
  `tel_movil` varchar(20) NOT NULL,
  `lada_fijo` varchar(20) NOT NULL,
  `tel_fijo` varchar(20) NOT NULL,
  `codigo_promocion` varchar(20) DEFAULT NULL,
  `call_center_id` int(11) DEFAULT NULL,
  `miembro_id` int(11) DEFAULT NULL,
  `password` varchar(250) NOT NULL,
  `renovo_pass` tinyint(1) NOT NULL,
  `online` tinyint(1) NOT NULL,
  `fecha_registro` date NOT NULL,
  `fecha_envio` date DEFAULT NULL,
  `fecha_recibo` date DEFAULT NULL,
  `activa` tinyint(1) NOT NULL,
  `activa_paquete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `membresias_membresia_72602a1f` (`call_center_id`),
  KEY `membresias_membresia_4478c0b0` (`miembro_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `membresias_membresia`
--

INSERT INTO `membresias_membresia` (`id`, `tipo`, `nombre`, `apellido_paterno`, `apellido_materno`, `fecha_nacimiento`, `nacionalidad`, `genero`, `estado_civil`, `calle`, `no_exterior`, `no_interior`, `colonia`, `municipio`, `ciudad`, `cp`, `pais`, `email`, `email_alternativo`, `lada_movil`, `tel_movil`, `lada_fijo`, `tel_fijo`, `codigo_promocion`, `call_center_id`, `miembro_id`, `password`, `renovo_pass`, `online`, `fecha_registro`, `fecha_envio`, `fecha_recibo`, `activa`, `activa_paquete`) VALUES
(1, '1', 'Roberto', 'Urita', 'Jimenez', '1986-06-18', 'Mexicano', 'Masculino', 'Casado', 'Antonio Canova', '9589', '9589', 'Fracc. Parajes del Sol', 'Juarez', 'Juarez', 32696, 'Mexico', 'roberto@newemage.com', 'robertuj@gmail.com', '656', '8435474', '656', '8435474', '', NULL, 2, 'v2ZdnKYE80qs', 1, 0, '2013-01-04', NULL, NULL, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `membresias_miembros_adicionales`
--

CREATE TABLE IF NOT EXISTS `membresias_miembros_adicionales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `membresia_id` int(11) DEFAULT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido_paterno` varchar(255) NOT NULL,
  `apellido_materno` varchar(255) NOT NULL,
  `genero` varchar(10) NOT NULL,
  `nacionalidad` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `parentesco` varchar(255) NOT NULL,
  `comparte_poliza` tinyint(1) NOT NULL,
  `nombre_representante` varchar(255) DEFAULT NULL,
  `telefono_representante` varchar(255) DEFAULT NULL,
  `poliza` varchar(255) DEFAULT NULL,
  `tipo_poliza_id` int(11) DEFAULT NULL,
  `tipo_cobertura_id` int(11) DEFAULT NULL,
  `tipo_poliza_otro` varchar(255) DEFAULT NULL,
  `tipo_cobertura_otro` varchar(255) DEFAULT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `no_pasaporte` varchar(255) DEFAULT NULL,
  `no_visa` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `membresias_miembros_adicionales_1f04a814` (`membresia_id`),
  KEY `membresias_miembros_adicionales_115c44b` (`tipo_poliza_id`),
  KEY `membresias_miembros_adicionales_67a644a2` (`tipo_cobertura_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `membresias_tipo_cobertura`
--

CREATE TABLE IF NOT EXISTS `membresias_tipo_cobertura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cobertura` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `membresias_tipo_cobertura`
--

INSERT INTO `membresias_tipo_cobertura` (`id`, `cobertura`) VALUES
(1, 'test 1'),
(2, 'test 2'),
(3, 'test 3');

-- --------------------------------------------------------

--
-- Table structure for table `membresias_tipo_poliza`
--

CREATE TABLE IF NOT EXISTS `membresias_tipo_poliza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_poliza` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `membresias_tipo_poliza`
--

INSERT INTO `membresias_tipo_poliza` (`id`, `tipo_poliza`) VALUES
(1, 'test 1'),
(2, 'test 2'),
(3, 'test 3');

-- --------------------------------------------------------

--
-- Table structure for table `thumbnail_kvstore`
--

CREATE TABLE IF NOT EXISTS `thumbnail_kvstore` (
  `key` varchar(200) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `usuarios_userprofile`
--

CREATE TABLE IF NOT EXISTS `usuarios_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `tipo_usuario` varchar(2) DEFAULT NULL,
  `genero` varchar(1) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `estado_civil` varchar(20) DEFAULT NULL,
  `hijos_menores_edad` varchar(5) DEFAULT NULL,
  `calle` varchar(255) DEFAULT NULL,
  `no_exterior` varchar(10) DEFAULT NULL,
  `no_interior` varchar(10) DEFAULT NULL,
  `colonia` varchar(100) DEFAULT NULL,
  `municipio` varchar(150) DEFAULT NULL,
  `ciudad` varchar(150) DEFAULT NULL,
  `estado` varchar(150) DEFAULT NULL,
  `cp` int(11) DEFAULT NULL,
  `telefono` varchar(150) DEFAULT NULL,
  `membresia_activa` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `usuarios_userprofile`
--

INSERT INTO `usuarios_userprofile` (`id`, `user_id`, `tipo_usuario`, `genero`, `fecha_nacimiento`, `estado_civil`, `hijos_menores_edad`, `calle`, `no_exterior`, `no_interior`, `colonia`, `municipio`, `ciudad`, `estado`, `cp`, `telefono`, `membresia_activa`) VALUES
(1, 1, '1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0),
(2, 2, '1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `citas_cita`
--
ALTER TABLE `citas_cita`
  ADD CONSTRAINT `no_membresia_id_refs_id_23fde645` FOREIGN KEY (`no_membresia_id`) REFERENCES `membresias_membresia` (`id`),
  ADD CONSTRAINT `especialidad_cita_id_refs_id_26d83c16` FOREIGN KEY (`especialidad_cita_id`) REFERENCES `citas_especialidad` (`id`),
  ADD CONSTRAINT `miembro_id_refs_id_29b53580` FOREIGN KEY (`miembro_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `socio_id_refs_id_29b53580` FOREIGN KEY (`socio_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_flatpage_sites`
--
ALTER TABLE `django_flatpage_sites`
  ADD CONSTRAINT `flatpage_id_refs_id_3f17b0a6` FOREIGN KEY (`flatpage_id`) REFERENCES `django_flatpage` (`id`),
  ADD CONSTRAINT `site_id_refs_id_4e3eeb57` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);

--
-- Constraints for table `membresias_info_adicional`
--
ALTER TABLE `membresias_info_adicional`
  ADD CONSTRAINT `tipo_cobertura_id_refs_id_186e0fae` FOREIGN KEY (`tipo_cobertura_id`) REFERENCES `membresias_tipo_cobertura` (`id`),
  ADD CONSTRAINT `membresia_id_refs_id_1cda2624` FOREIGN KEY (`membresia_id`) REFERENCES `membresias_membresia` (`id`),
  ADD CONSTRAINT `tipo_poliza_id_refs_id_a6007db` FOREIGN KEY (`tipo_poliza_id`) REFERENCES `membresias_tipo_poliza` (`id`);

--
-- Constraints for table `membresias_membresia`
--
ALTER TABLE `membresias_membresia`
  ADD CONSTRAINT `miembro_id_refs_id_1d41f638` FOREIGN KEY (`miembro_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `call_center_id_refs_id_1d41f638` FOREIGN KEY (`call_center_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `membresias_miembros_adicionales`
--
ALTER TABLE `membresias_miembros_adicionales`
  ADD CONSTRAINT `tipo_cobertura_id_refs_id_77a9255a` FOREIGN KEY (`tipo_cobertura_id`) REFERENCES `membresias_tipo_cobertura` (`id`),
  ADD CONSTRAINT `membresia_id_refs_id_35aedbe4` FOREIGN KEY (`membresia_id`) REFERENCES `membresias_membresia` (`id`),
  ADD CONSTRAINT `tipo_poliza_id_refs_id_5f8d9013` FOREIGN KEY (`tipo_poliza_id`) REFERENCES `membresias_tipo_poliza` (`id`);

--
-- Constraints for table `usuarios_userprofile`
--
ALTER TABLE `usuarios_userprofile`
  ADD CONSTRAINT `user_id_refs_id_1a285776` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
