-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 16, 2023 at 01:15 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2heartnewdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `regtb`
--


-- --------------------------------------------------------

--
-- Table structure for table `reportb`
--

CREATE TABLE `reportb` (
  `id` bigint(250) NOT NULL auto_increment,
  `UserName` varchar(1000) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Height` varchar(250) NOT NULL,
  `Weight` varchar(250) NOT NULL,
  `ap_hi` varchar(250) NOT NULL,
  `ap_lo` varchar(250) NOT NULL,
  `cholesterol` varchar(250) NOT NULL,
  `glucose` varchar(250) NOT NULL,
  `Smoke` varchar(250) NOT NULL,
  `Alcohol` varchar(250) NOT NULL,
  `activity` varchar(250) NOT NULL,
  `Result` varchar(250) NOT NULL,
  `Prescription` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `reportb`
--

