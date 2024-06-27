-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 27, 2024 at 01:58 PM
-- Server version: 8.0.37-0ubuntu0.22.04.3
-- PHP Version: 8.1.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cmsbackend`
--

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_aboutpagesection`
--

CREATE TABLE `aboutus_aboutpagesection` (
  `id` bigint NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sub_title` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bg_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `slug` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aboutus_aboutpagesection`
--

INSERT INTO `aboutus_aboutpagesection` (`id`, `title`, `sub_title`, `bg_image`, `slug`) VALUES
(1, 'About us', NULL, 'about_page_images/MaskAbout.8aca19f5ec961d44b432_nif9kys.webp', 'about-page-section');

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_certificatetitle`
--

CREATE TABLE `aboutus_certificatetitle` (
  `id` bigint NOT NULL,
  `title` varchar(200) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_certifications`
--

CREATE TABLE `aboutus_certifications` (
  `id` bigint NOT NULL,
  `certificate_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_metatagsabout`
--

CREATE TABLE `aboutus_metatagsabout` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_milestone`
--

CREATE TABLE `aboutus_milestone` (
  `id` bigint NOT NULL,
  `year` int UNSIGNED NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `achievement1` longtext COLLATE utf8mb4_general_ci,
  `achievement2` longtext COLLATE utf8mb4_general_ci,
  `achievement3` longtext COLLATE utf8mb4_general_ci
) ;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_milestonetitle`
--

CREATE TABLE `aboutus_milestonetitle` (
  `id` bigint NOT NULL,
  `title` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `sub_title` longtext COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_ourstory`
--

CREATE TABLE `aboutus_ourstory` (
  `id` bigint NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `aboutus_ourstory`
--

INSERT INTO `aboutus_ourstory` (`id`, `title`, `description`, `image`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`) VALUES
(1, '<p>Our Story</p>', '<p>Founded in Oman in 2008 by Mr. Salim Ahmed Mohammed Al Badi, ALSI has evolved into a dynamic force in the logistics industry. Our commitment to excellence has been recognized with consecutive \'Best Customs Clearance Company\' awards from Oman Customs in 2021 and 2022, as well as the \'Smart Workplace Award\' from Dubai Customs in 2022.</p><p>With over 130+ professionals, we process an average of 9,000+ Customs Declarations monthly. Operating from 10 strategic locations in Oman, alongside offices in the UAE, Qatar, and Saudi Arabia, our round-the-clock operations ensure seamless service. We take pride in our ISO 9001:2015 certification, which highlights our commitment to quality. ALSI is also a registered member of WCA and the FIATA Freight Network, extending our global reach.</p><p>Our comprehensive services encompass Customs Clearance, Freight Forwarding, Project Cargo Solutions, and efficient GCC and Domestic Transportation. Our journey is a testament to unwavering dedication, forging enduring partnerships, and consistently delivering exceptional logistics solutions. At ALSI, our story embodies growth, innovation, and an unwavering pursuit of excellence across all aspects of logistics</p>', 'our_story_images/ourstory3_OM3xHEj.webp', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_ourstorytitle`
--

CREATE TABLE `aboutus_ourstorytitle` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_ourteam`
--

CREATE TABLE `aboutus_ourteam` (
  `id` bigint NOT NULL,
  `profile_pic` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `designation` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `order_by` int NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_ourteamtitle`
--

CREATE TABLE `aboutus_ourteamtitle` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_whatweare`
--

CREATE TABLE `aboutus_whatweare` (
  `id` bigint NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `aboutus_whatwearetitle`
--

CREATE TABLE `aboutus_whatwearetitle` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add home header', 7, 'add_homeheader'),
(26, 'Can change home header', 7, 'change_homeheader'),
(27, 'Can delete home header', 7, 'delete_homeheader'),
(28, 'Can view home header', 7, 'view_homeheader'),
(29, 'Can add achievement', 8, 'add_achievement'),
(30, 'Can change achievement', 8, 'change_achievement'),
(31, 'Can delete achievement', 8, 'delete_achievement'),
(32, 'Can view achievement', 8, 'view_achievement'),
(33, 'Can add achievement section', 9, 'add_achievementsection'),
(34, 'Can change achievement section', 9, 'change_achievementsection'),
(35, 'Can delete achievement section', 9, 'delete_achievementsection'),
(36, 'Can view achievement section', 9, 'view_achievementsection'),
(37, 'Can add highlights section', 10, 'add_highlightssection'),
(38, 'Can change highlights section', 10, 'change_highlightssection'),
(39, 'Can delete highlights section', 10, 'delete_highlightssection'),
(40, 'Can view highlights section', 10, 'view_highlightssection'),
(41, 'Can add home highlights', 11, 'add_homehighlights'),
(42, 'Can change home highlights', 11, 'change_homehighlights'),
(43, 'Can delete home highlights', 11, 'delete_homehighlights'),
(44, 'Can view home highlights', 11, 'view_homehighlights'),
(45, 'Can add industry', 12, 'add_industry'),
(46, 'Can change industry', 12, 'change_industry'),
(47, 'Can delete industry', 12, 'delete_industry'),
(48, 'Can view industry', 12, 'view_industry'),
(49, 'Can add location', 13, 'add_location'),
(50, 'Can change location', 13, 'change_location'),
(51, 'Can delete location', 13, 'delete_location'),
(52, 'Can view location', 13, 'view_location'),
(53, 'Can add market', 14, 'add_market'),
(54, 'Can change market', 14, 'change_market'),
(55, 'Can delete market', 14, 'delete_market'),
(56, 'Can view market', 14, 'view_market'),
(57, 'Can add market title', 15, 'add_markettitle'),
(58, 'Can change market title', 15, 'change_markettitle'),
(59, 'Can delete market title', 15, 'delete_markettitle'),
(60, 'Can view market title', 15, 'view_markettitle'),
(61, 'Can add meta tags home', 16, 'add_metatagshome'),
(62, 'Can change meta tags home', 16, 'change_metatagshome'),
(63, 'Can delete meta tags home', 16, 'delete_metatagshome'),
(64, 'Can view meta tags home', 16, 'view_metatagshome'),
(65, 'Can add our network title', 17, 'add_ournetworktitle'),
(66, 'Can change our network title', 17, 'change_ournetworktitle'),
(67, 'Can delete our network title', 17, 'delete_ournetworktitle'),
(68, 'Can view our network title', 17, 'view_ournetworktitle'),
(69, 'Can add service', 18, 'add_service'),
(70, 'Can change service', 18, 'change_service'),
(71, 'Can delete service', 18, 'delete_service'),
(72, 'Can view service', 18, 'view_service'),
(73, 'Can add social media', 19, 'add_socialmedia'),
(74, 'Can change social media', 19, 'change_socialmedia'),
(75, 'Can delete social media', 19, 'delete_socialmedia'),
(76, 'Can view social media', 19, 'view_socialmedia'),
(77, 'Can add location_page', 20, 'add_location_page'),
(78, 'Can change location_page', 20, 'change_location_page'),
(79, 'Can delete location_page', 20, 'delete_location_page'),
(80, 'Can view location_page', 20, 'view_location_page'),
(81, 'Can add meta tags location', 21, 'add_metatagslocation'),
(82, 'Can change meta tags location', 21, 'change_metatagslocation'),
(83, 'Can delete meta tags location', 21, 'delete_metatagslocation'),
(84, 'Can view meta tags location', 21, 'view_metatagslocation'),
(85, 'Can add office', 22, 'add_office'),
(86, 'Can change office', 22, 'change_office'),
(87, 'Can delete office', 22, 'delete_office'),
(88, 'Can view office', 22, 'view_office'),
(89, 'Can add meta tagsservices', 23, 'add_metatagsservices'),
(90, 'Can change meta tagsservices', 23, 'change_metatagsservices'),
(91, 'Can delete meta tagsservices', 23, 'delete_metatagsservices'),
(92, 'Can view meta tagsservices', 23, 'view_metatagsservices'),
(93, 'Can add specialized service', 24, 'add_specializedservice'),
(94, 'Can change specialized service', 24, 'change_specializedservice'),
(95, 'Can delete specialized service', 24, 'delete_specializedservice'),
(96, 'Can view specialized service', 24, 'view_specializedservice'),
(97, 'Can add specialized sub service', 25, 'add_specializedsubservice'),
(98, 'Can change specialized sub service', 25, 'change_specializedsubservice'),
(99, 'Can delete specialized sub service', 25, 'delete_specializedsubservice'),
(100, 'Can view specialized sub service', 25, 'view_specializedsubservice'),
(101, 'Can add subheading', 26, 'add_subheading'),
(102, 'Can change subheading', 26, 'change_subheading'),
(103, 'Can delete subheading', 26, 'delete_subheading'),
(104, 'Can view subheading', 26, 'view_subheading'),
(105, 'Can add sub service', 27, 'add_subservice'),
(106, 'Can change sub service', 27, 'change_subservice'),
(107, 'Can delete sub service', 27, 'delete_subservice'),
(108, 'Can view sub service', 27, 'view_subservice'),
(109, 'Can add contact form', 28, 'add_contactform'),
(110, 'Can change contact form', 28, 'change_contactform'),
(111, 'Can delete contact form', 28, 'delete_contactform'),
(112, 'Can view contact form', 28, 'view_contactform'),
(113, 'Can add contact header', 29, 'add_contactheader'),
(114, 'Can change contact header', 29, 'change_contactheader'),
(115, 'Can delete contact header', 29, 'delete_contactheader'),
(116, 'Can view contact header', 29, 'view_contactheader'),
(117, 'Can add faq', 30, 'add_faq'),
(118, 'Can change faq', 30, 'change_faq'),
(119, 'Can delete faq', 30, 'delete_faq'),
(120, 'Can view faq', 30, 'view_faq'),
(121, 'Can add meta tags contacts', 31, 'add_metatagscontacts'),
(122, 'Can change meta tags contacts', 31, 'change_metatagscontacts'),
(123, 'Can delete meta tags contacts', 31, 'delete_metatagscontacts'),
(124, 'Can view meta tags contacts', 31, 'view_metatagscontacts'),
(125, 'Can add section', 32, 'add_section'),
(126, 'Can change section', 32, 'change_section'),
(127, 'Can delete section', 32, 'delete_section'),
(128, 'Can view section', 32, 'view_section'),
(129, 'Can add blog post', 33, 'add_blogpost'),
(130, 'Can change blog post', 33, 'change_blogpost'),
(131, 'Can delete blog post', 33, 'delete_blogpost'),
(132, 'Can view blog post', 33, 'view_blogpost'),
(133, 'Can add meta tags blogs', 34, 'add_metatagsblogs'),
(134, 'Can change meta tags blogs', 34, 'change_metatagsblogs'),
(135, 'Can delete meta tags blogs', 34, 'delete_metatagsblogs'),
(136, 'Can view meta tags blogs', 34, 'view_metatagsblogs'),
(137, 'Can add about page section', 35, 'add_aboutpagesection'),
(138, 'Can change about page section', 35, 'change_aboutpagesection'),
(139, 'Can delete about page section', 35, 'delete_aboutpagesection'),
(140, 'Can view about page section', 35, 'view_aboutpagesection'),
(141, 'Can add certificate title', 36, 'add_certificatetitle'),
(142, 'Can change certificate title', 36, 'change_certificatetitle'),
(143, 'Can delete certificate title', 36, 'delete_certificatetitle'),
(144, 'Can view certificate title', 36, 'view_certificatetitle'),
(145, 'Can add certifications', 37, 'add_certifications'),
(146, 'Can change certifications', 37, 'change_certifications'),
(147, 'Can delete certifications', 37, 'delete_certifications'),
(148, 'Can view certifications', 37, 'view_certifications'),
(149, 'Can add meta tags about', 38, 'add_metatagsabout'),
(150, 'Can change meta tags about', 38, 'change_metatagsabout'),
(151, 'Can delete meta tags about', 38, 'delete_metatagsabout'),
(152, 'Can view meta tags about', 38, 'view_metatagsabout'),
(153, 'Can add milestone', 39, 'add_milestone'),
(154, 'Can change milestone', 39, 'change_milestone'),
(155, 'Can delete milestone', 39, 'delete_milestone'),
(156, 'Can view milestone', 39, 'view_milestone'),
(157, 'Can add milestone title', 40, 'add_milestonetitle'),
(158, 'Can change milestone title', 40, 'change_milestonetitle'),
(159, 'Can delete milestone title', 40, 'delete_milestonetitle'),
(160, 'Can view milestone title', 40, 'view_milestonetitle'),
(161, 'Can add our story', 41, 'add_ourstory'),
(162, 'Can change our story', 41, 'change_ourstory'),
(163, 'Can delete our story', 41, 'delete_ourstory'),
(164, 'Can view our story', 41, 'view_ourstory'),
(165, 'Can add ourstory title', 42, 'add_ourstorytitle'),
(166, 'Can change ourstory title', 42, 'change_ourstorytitle'),
(167, 'Can delete ourstory title', 42, 'delete_ourstorytitle'),
(168, 'Can view ourstory title', 42, 'view_ourstorytitle'),
(169, 'Can add our team', 43, 'add_ourteam'),
(170, 'Can change our team', 43, 'change_ourteam'),
(171, 'Can delete our team', 43, 'delete_ourteam'),
(172, 'Can view our team', 43, 'view_ourteam'),
(173, 'Can add our team title', 44, 'add_ourteamtitle'),
(174, 'Can change our team title', 44, 'change_ourteamtitle'),
(175, 'Can delete our team title', 44, 'delete_ourteamtitle'),
(176, 'Can view our team title', 44, 'view_ourteamtitle'),
(177, 'Can add what we are', 45, 'add_whatweare'),
(178, 'Can change what we are', 45, 'change_whatweare'),
(179, 'Can delete what we are', 45, 'delete_whatweare'),
(180, 'Can view what we are', 45, 'view_whatweare'),
(181, 'Can add what we are title', 46, 'add_whatwearetitle'),
(182, 'Can change what we are title', 46, 'change_whatwearetitle'),
(183, 'Can delete what we are title', 46, 'delete_whatwearetitle'),
(184, 'Can view what we are title', 46, 'view_whatwearetitle'),
(185, 'Can add industries page', 47, 'add_industriespage'),
(186, 'Can change industries page', 47, 'change_industriespage'),
(187, 'Can delete industries page', 47, 'delete_industriespage'),
(188, 'Can view industries page', 47, 'view_industriespage'),
(189, 'Can add meta tags industries', 48, 'add_metatagsindustries'),
(190, 'Can change meta tags industries', 48, 'change_metatagsindustries'),
(191, 'Can delete meta tags industries', 48, 'delete_metatagsindustries'),
(192, 'Can view meta tags industries', 48, 'view_metatagsindustries'),
(193, 'Can add career page', 49, 'add_careerpage'),
(194, 'Can change career page', 49, 'change_careerpage'),
(195, 'Can delete career page', 49, 'delete_careerpage'),
(196, 'Can view career page', 49, 'view_careerpage'),
(197, 'Can add career submission', 50, 'add_careersubmission'),
(198, 'Can change career submission', 50, 'change_careersubmission'),
(199, 'Can delete career submission', 50, 'delete_careersubmission'),
(200, 'Can view career submission', 50, 'view_careersubmission'),
(201, 'Can add meta tagscareers', 51, 'add_metatagscareers'),
(202, 'Can change meta tagscareers', 51, 'change_metatagscareers'),
(203, 'Can delete meta tagscareers', 51, 'delete_metatagscareers'),
(204, 'Can view meta tagscareers', 51, 'view_metatagscareers'),
(205, 'Can add key_diffrentiates', 52, 'add_key_diffrentiates'),
(206, 'Can change key_diffrentiates', 52, 'change_key_diffrentiates'),
(207, 'Can delete key_diffrentiates', 52, 'delete_key_diffrentiates'),
(208, 'Can view key_diffrentiates', 52, 'view_key_diffrentiates'),
(209, 'Can add key_diffrentiates section', 53, 'add_key_diffrentiatessection'),
(210, 'Can change key_diffrentiates section', 53, 'change_key_diffrentiatessection'),
(211, 'Can delete key_diffrentiates section', 53, 'delete_key_diffrentiatessection'),
(212, 'Can view key_diffrentiates section', 53, 'view_key_diffrentiatessection'),
(213, 'Can add chooses section', 54, 'add_choosessection'),
(214, 'Can change chooses section', 54, 'change_choosessection'),
(215, 'Can delete chooses section', 54, 'delete_choosessection'),
(216, 'Can view chooses section', 54, 'view_choosessection'),
(217, 'Can add footer', 55, 'add_footer'),
(218, 'Can change footer', 55, 'change_footer'),
(219, 'Can delete footer', 55, 'delete_footer'),
(220, 'Can view footer', 55, 'view_footer'),
(221, 'Can add industry card', 56, 'add_industrycard'),
(222, 'Can change industry card', 56, 'change_industrycard'),
(223, 'Can delete industry card', 56, 'delete_industrycard'),
(224, 'Can view industry card', 56, 'view_industrycard'),
(225, 'Can add industry titles', 57, 'add_industrytitles'),
(226, 'Can change industry titles', 57, 'change_industrytitles'),
(227, 'Can delete industry titles', 57, 'delete_industrytitles'),
(228, 'Can view industry titles', 57, 'view_industrytitles'),
(229, 'Can add services card', 58, 'add_servicescard'),
(230, 'Can change services card', 58, 'change_servicescard'),
(231, 'Can delete services card', 58, 'delete_servicescard'),
(232, 'Can view services card', 58, 'view_servicescard'),
(233, 'Can add service title', 59, 'add_servicetitle'),
(234, 'Can change service title', 59, 'change_servicetitle'),
(235, 'Can delete service title', 59, 'delete_servicetitle'),
(236, 'Can view service title', 59, 'view_servicetitle'),
(237, 'Can add home header custom', 60, 'add_homeheadercustom'),
(238, 'Can change home header custom', 60, 'change_homeheadercustom'),
(239, 'Can delete home header custom', 60, 'delete_homeheadercustom'),
(240, 'Can view home header custom', 60, 'view_homeheadercustom'),
(241, 'Can add servicecards custom', 61, 'add_servicecardscustom'),
(242, 'Can change servicecards custom', 61, 'change_servicecardscustom'),
(243, 'Can delete servicecards custom', 61, 'delete_servicecardscustom'),
(244, 'Can view servicecards custom', 61, 'view_servicecardscustom'),
(245, 'Can add chooseus custom', 62, 'add_chooseuscustom'),
(246, 'Can change chooseus custom', 62, 'change_chooseuscustom'),
(247, 'Can delete chooseus custom', 62, 'delete_chooseuscustom'),
(248, 'Can view chooseus custom', 62, 'view_chooseuscustom'),
(249, 'Can add ournetwork custom', 63, 'add_ournetworkcustom'),
(250, 'Can change ournetwork custom', 63, 'change_ournetworkcustom'),
(251, 'Can delete ournetwork custom', 63, 'delete_ournetworkcustom'),
(252, 'Can view ournetwork custom', 63, 'view_ournetworkcustom'),
(253, 'Can add keydiffrentiators custom', 64, 'add_keydiffrentiatorscustom'),
(254, 'Can change keydiffrentiators custom', 64, 'change_keydiffrentiatorscustom'),
(255, 'Can delete keydiffrentiators custom', 64, 'delete_keydiffrentiatorscustom'),
(256, 'Can view keydiffrentiators custom', 64, 'view_keydiffrentiatorscustom'),
(257, 'Can add acheievement custom', 65, 'add_acheievementcustom'),
(258, 'Can change acheievement custom', 65, 'change_acheievementcustom'),
(259, 'Can delete acheievement custom', 65, 'delete_acheievementcustom'),
(260, 'Can view acheievement custom', 65, 'view_acheievementcustom'),
(261, 'Can add highlights custom', 66, 'add_highlightscustom'),
(262, 'Can change highlights custom', 66, 'change_highlightscustom'),
(263, 'Can delete highlights custom', 66, 'delete_highlightscustom'),
(264, 'Can view highlights custom', 66, 'view_highlightscustom'),
(265, 'Can add industries cards custom', 67, 'add_industriescardscustom'),
(266, 'Can change industries cards custom', 67, 'change_industriescardscustom'),
(267, 'Can delete industries cards custom', 67, 'delete_industriescardscustom'),
(268, 'Can view industries cards custom', 67, 'view_industriescardscustom'),
(269, 'Can add market updates custom', 68, 'add_marketupdatescustom'),
(270, 'Can change market updates custom', 68, 'change_marketupdatescustom'),
(271, 'Can delete market updates custom', 68, 'delete_marketupdatescustom'),
(272, 'Can view market updates custom', 68, 'view_marketupdatescustom'),
(273, 'Can add about page section custom', 69, 'add_aboutpagesectioncustom'),
(274, 'Can change about page section custom', 69, 'change_aboutpagesectioncustom'),
(275, 'Can delete about page section custom', 69, 'delete_aboutpagesectioncustom'),
(276, 'Can view about page section custom', 69, 'view_aboutpagesectioncustom'),
(277, 'Can add ourstory custom', 70, 'add_ourstorycustom'),
(278, 'Can change ourstory custom', 70, 'change_ourstorycustom'),
(279, 'Can delete ourstory custom', 70, 'delete_ourstorycustom'),
(280, 'Can view ourstory custom', 70, 'view_ourstorycustom'),
(281, 'Can add milestone custom', 71, 'add_milestonecustom'),
(282, 'Can change milestone custom', 71, 'change_milestonecustom'),
(283, 'Can delete milestone custom', 71, 'delete_milestonecustom'),
(284, 'Can view milestone custom', 71, 'view_milestonecustom'),
(285, 'Can add ourteam custom', 72, 'add_ourteamcustom'),
(286, 'Can change ourteam custom', 72, 'change_ourteamcustom'),
(287, 'Can delete ourteam custom', 72, 'delete_ourteamcustom'),
(288, 'Can view ourteam custom', 72, 'view_ourteamcustom'),
(289, 'Can add whatweare custom', 73, 'add_whatwearecustom'),
(290, 'Can change whatweare custom', 73, 'change_whatwearecustom'),
(291, 'Can delete whatweare custom', 73, 'delete_whatwearecustom'),
(292, 'Can view whatweare custom', 73, 'view_whatwearecustom'),
(293, 'Can add certification custom', 74, 'add_certificationcustom'),
(294, 'Can change certification custom', 74, 'change_certificationcustom'),
(295, 'Can delete certification custom', 74, 'delete_certificationcustom'),
(296, 'Can view certification custom', 74, 'view_certificationcustom'),
(297, 'Can add contactform custom', 75, 'add_contactformcustom'),
(298, 'Can change contactform custom', 75, 'change_contactformcustom'),
(299, 'Can delete contactform custom', 75, 'delete_contactformcustom'),
(300, 'Can view contactform custom', 75, 'view_contactformcustom'),
(301, 'Can add footer custom', 76, 'add_footercustom'),
(302, 'Can change footer custom', 76, 'change_footercustom'),
(303, 'Can delete footer custom', 76, 'delete_footercustom'),
(304, 'Can view footer custom', 76, 'view_footercustom'),
(305, 'Can add headerournetwork custom', 77, 'add_headerournetworkcustom'),
(306, 'Can change headerournetwork custom', 77, 'change_headerournetworkcustom'),
(307, 'Can delete headerournetwork custom', 77, 'delete_headerournetworkcustom'),
(308, 'Can view headerournetwork custom', 77, 'view_headerournetworkcustom'),
(309, 'Can add ournetworkdescription custom', 78, 'add_ournetworkdescriptioncustom'),
(310, 'Can change ournetworkdescription custom', 78, 'change_ournetworkdescriptioncustom'),
(311, 'Can delete ournetworkdescription custom', 78, 'delete_ournetworkdescriptioncustom'),
(312, 'Can view ournetworkdescription custom', 78, 'view_ournetworkdescriptioncustom'),
(313, 'Can add service custom', 79, 'add_servicecustom'),
(314, 'Can change service custom', 79, 'change_servicecustom'),
(315, 'Can delete service custom', 79, 'delete_servicecustom'),
(316, 'Can view service custom', 79, 'view_servicecustom'),
(317, 'Can add ournetworklocation custom', 80, 'add_ournetworklocationcustom'),
(318, 'Can change ournetworklocation custom', 80, 'change_ournetworklocationcustom'),
(319, 'Can delete ournetworklocation custom', 80, 'delete_ournetworklocationcustom'),
(320, 'Can view ournetworklocation custom', 80, 'view_ournetworklocationcustom'),
(321, 'Can add ournetworkoffices custom', 81, 'add_ournetworkofficescustom'),
(322, 'Can change ournetworkoffices custom', 81, 'change_ournetworkofficescustom'),
(323, 'Can delete ournetworkoffices custom', 81, 'delete_ournetworkofficescustom'),
(324, 'Can view ournetworkoffices custom', 81, 'view_ournetworkofficescustom'),
(325, 'Can add careerspage custom', 82, 'add_careerspagecustom'),
(326, 'Can change careerspage custom', 82, 'change_careerspagecustom'),
(327, 'Can delete careerspage custom', 82, 'delete_careerspagecustom'),
(328, 'Can view careerspage custom', 82, 'view_careerspagecustom'),
(329, 'Can add headermarketupdatescustom', 83, 'add_headermarketupdatescustom'),
(330, 'Can change headermarketupdatescustom', 83, 'change_headermarketupdatescustom'),
(331, 'Can delete headermarketupdatescustom', 83, 'delete_headermarketupdatescustom'),
(332, 'Can view headermarketupdatescustom', 83, 'view_headermarketupdatescustom'),
(333, 'Can add market custom', 84, 'add_marketcustom'),
(334, 'Can change market custom', 84, 'change_marketcustom'),
(335, 'Can delete market custom', 84, 'delete_marketcustom'),
(336, 'Can view market custom', 84, 'view_marketcustom'),
(337, 'Can add industries header custom', 85, 'add_industriesheadercustom'),
(338, 'Can change industries header custom', 85, 'change_industriesheadercustom'),
(339, 'Can delete industries header custom', 85, 'delete_industriesheadercustom'),
(340, 'Can view industries header custom', 85, 'view_industriesheadercustom'),
(341, 'Can add industries blocks custom', 86, 'add_industriesblockscustom'),
(342, 'Can change industries blocks custom', 86, 'change_industriesblockscustom'),
(343, 'Can delete industries blocks custom', 86, 'delete_industriesblockscustom'),
(344, 'Can view industries blocks custom', 86, 'view_industriesblockscustom');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$mNXsHPQV8zlOSqTywASqcr$CmxJTXJ8S+K0TLppxAEowm1F0kiUucfz+FUVwaBBJf8=', NULL, 1, 'qwe', '', '', 'qwe@gmail.com', 1, 1, '2024-06-26 11:44:43.431563');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blogs_blogpost`
--

CREATE TABLE `blogs_blogpost` (
  `id` bigint NOT NULL,
  `header_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `header_title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `publish_date` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `quotes` longtext COLLATE utf8mb4_general_ci,
  `Highlight` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `author` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `slug` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blogs_blogpost`
--

INSERT INTO `blogs_blogpost` (`id`, `header_image`, `header_title`, `publish_date`, `quotes`, `Highlight`, `author`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`, `slug`) VALUES
(1, 'blog_headers/blog1.webp', 'On-Board Courier Clearance: Ensuring Secure and Timely Delivery Across Borders', '2024-06-27T09:13:31.204Z', 'An On-Board Courier is a dedicated individual who personally accompanies sensitive or time-critical shipments during transit.', '<p>In today\'s fast-paced global economy, the need for secure and timely international deliveries has become more critical than ever. As businesses expand their reach beyond borders, the demand for reliable shipping solutions has surged. One innovative approach that has gained immense popularity is the use of On-Board Couriers (OBC).</p><p><br></p><h6>Understanding On-Board Courier Services</h6><p>Before we delve into the clearance process, it\'s essential to grasp the fundamentals of On-Board Courier services. An On-Board Courier is a dedicated individual who personally accompanies sensitive or time-critical shipments during transit. Unlike traditional shipping methods, OBCs act as a guarantee for the safe and prompt delivery of valuable goods.</p><h6>Securing Shipments Beyond Borders</h6><p>One of the primary advantages of utilizing On-Board Couriers is the heightened level of security they provide. With increasing concerns about cargo safety, businesses are turning to OBCs to ensure that their shipments are in safe hands throughout the journey.</p><h6>On-Board Courier Clearance Process</h6><p>The clearance process for On-Board Couriers is a meticulous procedure designed to adhere to international regulations while expediting the movement of goods. Unlike standard shipping methods, the OBC clearance process involves personal oversight and swift decision-making.</p><h6>The Key Components of On-Board Courier Clearance</h6><p>● Document Verification and Preparation: Before embarking on a journey, On-Board Couriers meticulously verify and prepare all necessary shipping documents. This includes customs declarations, invoices, and any other paperwork required for international shipments. Ensuring the accuracy of these documents is crucial for seamless customs clearance.</p><p>● Customs Compliance: Navigating the complex landscape of international customs regulations is a core responsibility of On-Board Couriers. Their in-depth knowledge and expertise in customs procedures enable them to swiftly clear shipments, minimizing delays and avoiding potential issues.</p><p>● Real-time Tracking and Communication: To maintain transparency and ensure clients are well-informed, On-Board Couriers utilize advanced tracking systems. Real-time updates and communication channels enable clients to monitor the progress of their shipments, providing peace of mind and facilitating effective planning.</p><p>● Security Protocols: OBCs implement stringent security protocols throughout the entire journey. From the moment the shipment is handed over to the courier until its final delivery, security measures are in place to prevent theft, damage, or any unforeseen circumstances.</p><h6>The Impact on Global Supply Chains</h6><p>The utilization of On-Board Courier Clearance has a profound impact on global supply chains. Businesses relying on time-sensitive deliveries experience a significant boost in efficiency, allowing them to meet tight deadlines and maintain a competitive edge in the market.</p><p>In the dynamic landscape of international trade, On-Board Courier Clearance emerges as a game-changer for businesses seeking secure and timely deliveries. The meticulous process, combined with the expertise of dedicated couriers, ensures that shipments reach their destination without compromising on security or punctuality. As the global economy continues to evolve, leveraging On-Board Courier services can be the key to staying ahead in the competitive market.</p>', 'qwe', NULL, NULL, NULL, NULL, 'on-board-courier-clearance'),
(2, 'blog_headers/Blog2.webp', 'Temporary Moves, Lasting Impact: Understanding Temporary Import and Export Customs Clearance', '2024-06-27T09:15:51.568Z', 'Temporary import and export refer to the movement of goods across international borders for a pre-determined and limited period, with the explicit intention of re-exporting them in the same state they entered the country.', '<p>In today\'s interconnected world, temporary imports and exports play a vital role in facilitating international trade, cultural exchange, and various cross-border activities. Whether it\'s showcasing a prototype at a global trade show, touring with a band, or sending equipment abroad for repairs, understanding the customs clearance process for temporary goods is crucial. ALSI Global aims to demystify the ins and outs of temporary import and export customs clearance, providing a comprehensive guide to navigating this often-overlooked facet of international movement.</p><h6>Demystifying Temporary Movement: Defining the Landscape</h6><p>At its core, temporary import and export refer to the movement of goods across international borders for a pre-determined and limited period, with the explicit intention of re-exporting them in the same state they entered the country. This allows individuals and businesses to utilize goods abroad without incurring the full cost of import duties and taxes, fostering international engagement and economic activity.</p><h6>Common Scenarios for Temporary Movements:</h6><h6>Trade Shows and Exhibitions:</h6><ol><li>Businesses showcase products, equipment, and prototypes at international events, engaging with potential customers and partners.</li></ol><h6>Sporting Events and Competitions:</h6><ol><li>Athletes, teams, and support staff bring in essential equipment, uniforms, and personal belongings for competitions.</li></ol><h6>Film Productions and Theatrical Performances</h6><ol><li>Costumes, props, technical equipment, and other necessary items are transported abroad for filming or performing.</li></ol><h6>Repair and Maintenance:</h6><ol><li>Machinery, equipment, and vehicles are sent abroad for servicing, maintenance, or upgrades.</li></ol><h6>Educational and Research Activities:</h6><ol><li>Educational institutions and research bodies might require temporary importation of specialized equipment and materials for specific projects.</li></ol><h6>Navigating the Maze: Essential Considerations for Temporary Customs Clearance</h6><p>Understanding the specific requirements and procedures involved in temporary customs clearance is vital for a smooth and successful experience. Here are some key considerations:</p><h6>Time Limits:</h6><p>Each country meticulously defines the maximum time frame for which imported goods can remain under temporary admission. Missing these deadlines can lead to significant penalties, including storage fees, additional duties, and even confiscation of the goods. It\'s crucial to plan meticulously and factor in potential delays to ensure timely re-exportation within the stipulated time frame.</p><h6>Documentation Essentials:</h6><p>Proper documentation is the cornerstone of any successful customs clearance process. For temporary imports and exports, essential documents typically include:</p><p>○ Commercial invoices: Providing a detailed description of the goods, their value, and other relevant information.</p><p>○ Packing lists: Accurately listing the contents of each shipment, ensuring transparency and facilitating inspection.</p><p>○ Proof of ownership or intended use: Documents demonstrating ownership of the goods and their purpose for temporary entry, such as contracts, invitations, or exhibition registration documents.</p><h6>Security Deposits or Guarantees:</h6><p>To safeguard against potential non-compliance, customs authorities in certain countries might request a security deposit or guarantee. This deposit, typically in the form of cash or a bond, is refunded upon the successful re-exportation of the goods.</p><h6>Specific Procedures:</h6><p>Depending on the nature of the goods and the destination country, specific procedures might come into play. These may include:</p><p>○ Obtaining permits: Certain goods, such as artwork or endangered species materials, might require special permits for temporary import or export.</p><p>○ Utilizing ATA Carnets: An ATA Carnet is an internationally recognized customs document that streamlines temporary admission procedures in participating countries, eliminating the need for individual guarantees or security deposits.</p><h6>Unlocking the Benefits: Advantages of Utilizing Temporary Customs Procedures</h6><p>Embracing temporary customs procedures offers a multitude of benefits for individuals and businesses engaged in international activities:</p><h6>Cost Savings:</h6><p>By avoiding import duties and taxes, temporary procedures provide significant cost-effectiveness, especially for short-term endeavors. This financial advantage encourages participation in global events and fosters international collaboration.</p><h6>Simplified Process:</h6><p>Compared to regular import formalities, temporary clearance procedures can be streamlined and quicker, minimizing delays and facilitating smooth movement of goods. This allows individuals and businesses to focus on their core activities with minimal disruption.</p><h6>Facilitates International Engagement:</h6><p>Temporary imports and exports enable participation in various global events and collaborations. This fosters cultural exchange, promotes innovation, and drives economic growth by allowing businesses to showcase products and services to a wider audience.</p><h6>Seeking Guidance: The Importance of Consulting a Customs Broker</h6><p>Due to the complexities involved in international trade regulations and customs procedures, navigating temporary import and export formalities can be challenging. To ensure a smooth and compliant process, it\'s highly advisable to seek the guidance of a licensed customs broker. These professionals possess specialized knowledge and experience in navigating the intricacies of customs regulations and procedures. They can assist with:</p><p>● Classification of goods: Accurately classifying the goods under the appropriate customs tariff code, which directly impacts the applicable duties and taxes.</p><p>● Documentation preparation: Ensuring all necessary documents are complete and accurate, minimizing the risk</p><p><br></p>', 'qwe', NULL, NULL, NULL, NULL, 'temporary-moves-lasting-impact'),
(3, 'blog_headers/blogpost3.webp', 'Strategic Advisory: Securing Duty Exemption from Ministry of Commerce and Industry', '2024-06-27T09:17:50.876Z', 'Duty exemption entails a government-granted privilege allowing businesses to import or export goods without incurring specific tariffs or taxes.', '<p>In the dynamic arena of international trade, businesses face the imperative of staying ahead to ensure continual growth and endurance. One strategic avenue often explored by perceptive companies involves obtaining duty exemptions from Oman\'s Ministry of Commerce and Industry. This calculated move can wield substantial influence on the financial landscape and unlock novel pathways for business expansion. Let\'s explore the intricacies of acquiring duty exemptions and discern how it holds the potential to be a pivotal game-changer for your logistics enterprise.</p><h6>Decoding the Essence of Duty Exemption: A Gateway to Operational Excellence</h6><p><br></p><h6>Grasping the Fundamentals</h6><p>Before we embark on the strategic journey, let\'s establish a foundational understanding. Duty exemption entails a government-granted privilege allowing businesses to import or export goods without incurring specific tariffs or taxes. In Oman, the Ministry of Commerce and Industry is the gatekeeper of these exemptions, making it a pivotal entity for businesses seeking to optimize operational costs.</p><h6>Navigating Regulatory Waters</h6><p>Achieving duty exemption necessitates an intricate grasp of Oman\'s trade regulations. To navigate these waters successfully, staying informed about policy changes is imperative. Collaboration with legal experts well-versed in Omani trade laws is crucial to ensuring compliance and enhancing the chances of a successful exemption application.</p><h6>Crafting a Tactical Advisory Strategy</h6><p><br></p><h6>Conducting a Holistic Business Analysis</h6><p>Strategizing for duty exemption demands a comprehensive analysis of your business operations. Identify key areas where exemptions can yield maximum benefits, whether it be in the import of raw materials, acquisition of machinery, or export of finished products. Tailoring your strategy to align with your business dynamics is paramount.</p><h6>Forging Strong Government Ties</h6><p>In Oman, cultivating robust relationships with government officials can be a game-changer. Regular engagement with the Ministry of Commerce and Industry fosters a conducive environment for successful duty exemption applications. Personalized interactions contribute to building trust and credibility, critical factors in the decision-making process.</p><h6>Emphasizing Corporate Social Responsibility</h6><p>Highlighting your company\'s commitment to social responsibility enhances your case for duty exemption. Showcase initiatives that contribute to the local community, promote employment, or align with environmental sustainability. Such contributions resonate with Oman\'s vision and may sway the decision-making process in your favor.</p><h6>Navigating the Application Maze</h6><p><br></p><h6>Precision in Documentation</h6><p>A meticulously prepared duty exemption application is the linchpin of success. Ensure all necessary documents, including financial statements, import/export records, and compliance certificates, are in impeccable order. Any oversights or omissions may lead to delays or, worse, denials.</p><h6>Professional Assistance for Application Submission</h6><p>Enlisting professionals well-versed in duty exemption applications streamlines the process significantly. These experts navigate bureaucratic intricacies, ensuring your application meets all criteria and stands the best chance of approval.</p><h6>Conclusion: Propelling Your Logistics Venture Towards Unprecedented Heights</h6><p>In conclusion, securing duty exemption from Oman\'s Ministry of Commerce and Industry is not merely a cost-saving tactic; it\'s a strategic maneuver that can catapult your logistics business to unparalleled heights. By comprehending the intricacies of the process, building robust relationships, and presenting a compelling case, you can open doors to a realm of opportunities. Be proactive, stay well-informed, and witness your logistics business soar on the wings of strategic duty exemptions.</p><p>Remember, success lies not only in obtaining exemptions but also in leveraging them to elevate your business in the fiercely competitive logistics landscape. Embark on this strategic journey, and witness the metamorphosis of your logistics enterprise into a hub of efficiency and profitability.</p><p><br></p>', 'qwe', NULL, NULL, NULL, NULL, 'strategic-advisory-securing'),
(4, 'blog_headers/blogpost4.webp', 'ote Seamless Transit: Navigating the Customs Clearance Process for Transit Cargo', '2024-06-27T09:58:26.696Z', 'Transit clearance is a crucial component of the customs clearance process, particularly for cargo that passes through multiple countries or jurisdictions before reaching its final destination.', '<p>Navigating the intricate web of customs clearance is a crucial aspect of ensuring seamless transit for cargo. In today\'s globalized world, efficient customs clearance is not just a requirement but a strategic advantage. We will guide you through the essential steps and considerations involved in the customs clearance process for transit cargo, shedding light on how to streamline the journey for your shipments.</p><p><br></p><h6>Understanding Transit Clearance</h6><p>Transit clearance is a crucial component of the customs clearance process, particularly for cargo that passes through multiple countries or jurisdictions before reaching its final destination. Transit clearance allows goods to move smoothly through these transit points by obtaining necessary approvals and documentation while complying with relevant regulations. It\'s essential to understand and navigate transit clearance efficiently to ensure seamless transit for cargo and avoid delays or complications along the journey.</p><h6>Understanding Customs Clearance</h6><p>Before delving into the specifics, it\'s vital to comprehend the essence of customs clearance. Customs clearance is the official process that allows goods to enter or leave a country. It involves a series of checks, documentation, and approvals by customs authorities to ensure compliance with regulations.</p><h6>Importance of Smooth Transit</h6><p><br></p><h6>Timely Deliveries Matter</h6><p>In the realm of transit cargo, time is of the essence. Timely deliveries can make or break a business, impacting customer satisfaction and overall operational efficiency. A seamless customs clearance process is the linchpin to achieving this.</p><h6>Cost-Efficiency is Key</h6><p>Efficient customs clearance contributes significantly to cost-efficiency. Delays in the clearance process can lead to additional charges, including demurrage and storage fees. Minimizing these costs is essential for maintaining a competitive edge.</p><h6>Key Steps in Customs Clearance</h6><p><br></p><h6>Accurate Documentation</h6><p>The foundation of successful customs clearance lies in accurate documentation. Ensure all necessary paperwork, including invoices, bills of lading, and packing lists, is in order. Any discrepancies can lead to delays and complications.</p><h6>Tariff Classification Matters</h6><p>Assigning the correct tariff classification to your goods is paramount. Each product has a specific code, and accurate classification ensures adherence to customs regulations. Mistakes in classification can result in fines or even shipment rejection.</p><h6>Utilize Technology for Tracking</h6><p>In the digital age, technology can be your greatest ally. Utilize tracking systems and software that provide real-time updates on your cargo\'s location and clearance status. This not only enhances transparency but also allows for proactive problem-solving.</p><h6>Collaborate with Customs Brokers</h6><p>Engaging experienced customs brokers can be a game-changer. Their expertise in navigating the complexities of customs regulations can streamline the clearance process, saving both time and resources.</p><h6>Overcoming Challenges</h6><p><br></p><h6>Stay Informed on Regulatory Changes</h6><p>Customs regulations are subject to change, and staying informed is crucial. Regularly check for updates and ensure that your processes align with the latest requirements. Failure to do so can result in non-compliance issues.</p><h6>Addressing Customs Holds Promptly</h6><p>In some cases, customs may place a hold on your shipment. Promptly addressing the issues causing the hold, whether documentation errors or inspection requirements, is vital to avoid prolonged delays.</p><h6>The Human Touch in Customs Clearance</h6><p><br></p><h6>Communication is Key</h6><p>Behind every shipment, there\'s a team of people working to ensure its smooth passage. Effective communication, both within your organization and with customs authorities, fosters collaboration and expedites the clearance process.</p><h6>Communication is Key</h6><p>Behind every shipment, there\'s a team of people working to ensure its smooth passage. Effective communication, both within your organization and with customs authorities, fosters collaboration and expedites the clearance process.</p><h6>Continuous Improvement Strategies</h6><p>Finally, view customs clearance as an evolving process. Regularly assess your procedures, identify bottlenecks, and implement continuous improvement strategies. This proactive approach ensures long-term efficiency.</p><p>In the intricate dance of global transit, mastering the customs clearance process is non-negotiable. Timely deliveries, cost-efficiency, and compliance with regulations hinge on a well-orchestrated customs clearance strategy. By prioritizing accurate documentation, leveraging technology, collaborating with experts, and embracing a mindset of continuous improvement, your transit cargo can navigate the customs clearance process seamlessly, giving your business a competitive edge in the global marketplace.</p>', 'qwe', NULL, NULL, NULL, NULL, 'ote-seamless-transit'),
(5, 'blog_headers/blogpost5.webp', 'On the Move: Maximizing Efficiency with Special Equipment in Project Cargo', '2024-06-27T09:59:40.465Z', 'Multi Axle Trailers are the unsung heroes of project cargo logistics, offering a robust solution for transporting heavy and oversized loads.', '<p>In the fast-paced world of logistics and shipping, efficiency is not just a requirement but a necessity. For those in Oman seeking optimal project cargo transportation, understanding the nuances of multi-axle trailers, semi-modular solutions, SPMT (Self-Propelled Modular Transporters), and lowbed trailers is pivotal. Let\'s dive deep into how these heavy-duty movers are reshaping the landscape of project cargo logistics.</p><p><br></p><h6>The Power of Multi Axle Trailers</h6><p>Multi Axle Trailers are the unsung heroes of project cargo logistics, offering a robust solution for transporting heavy and oversized loads. These trailers, with their multiple axles, distribute weight effectively, providing stability and a smooth journey even on challenging terrains. From heavy machinery to large equipment, multi axle trailers are versatile and reliable.</p><h6>Semi-Modular Solutions: Bridging the Gap</h6><p>Sitting between traditional trailers and full modularity, semi-modular solutions provide a versatile middle ground. These systems offer flexibility in configuration adjustments based on cargo specifications. Whether it\'s adapting to odd-shaped cargo or resizing for various loads, semi-modular solutions bring adaptability to the forefront.</p><h6>SPMT: Autonomy Redefined</h6><p>Self-Propelled Modular Transporters (SPMT) take autonomy to the next level. With their self-propulsion capabilities, these trailers eliminate the need for external power sources, making them ideal for remote project cargo locations. SPMTs offer unparalleled maneuverability, adapting to the twists and turns of project cargo landscapes with ease.</p><h6>Lowbed Trailers: Beyond Height Limitations</h6><p>Navigating low heights and challenging terrains becomes seamless with Lowbed Trailers. These trailers are not just limited to their namesake; they excel in handling heavy loads, making them invaluable in various project cargo scenarios. The design of lowbed trailers allows for the transport of taller cargo, overcoming height restrictions effortlessly.</p><h6>Benefits Across the Board</h6><p>Investing in heavy-duty trailers comes with a myriad of benefits, each playing a crucial role in project cargo logistics:</p><h6>Stability and Weight Distribution:</h6><ol><li>Multi Axle Trailers provide enhanced stability and efficient weight distribution, ensuring a smooth ride even with the heaviest cargo.</li></ol><h6>Adaptability with Semi-Modular Systems:</h6><ol><li>Semi-modular solutions offer adaptability to cargo of various shapes and sizes, making them an ideal choice for diverse project requirements.</li></ol><h6>Versatility and Maneuverability of SPMT:</h6><ol><li>The autonomy of SPMT brings unparalleled versatility and maneuverability, especially in confined spaces or challenging project locations.</li></ol><h6>Beyond Low Heights with Lowbed Trailers:</h6><ol><li>Lowbed Trailers not only navigate low-clearance areas but also handle heavy loads, proving their versatility in diverse project scenarios.</li></ol><h6>Choosing the Right Trailer for Your Cargo</h6><p>Selecting the appropriate trailer is a pivotal decision in project cargo logistics. Understanding the unique requirements of your cargo and matching them with the capabilities of multi-axle trailers, semi-modular solutions, SPMT, or lowbed trailers ensures a seamless transportation process. Factors such as cargo dimensions, weight, and the terrain of transportation play a crucial role in this decision-making process.</p><h6>Safety Measures and Regulations</h6><p>In the world of heavy-duty transportation, safety is paramount. Implementing proper securing mechanisms, adhering to weight limits, and following transportation regulations are crucial steps in ensuring the safety of both cargo and personnel. Understanding and complying with safety measures contribute significantly to the success of project cargo logistics.</p><h6>Cost Considerations in Project Cargo Logistics</h6><p>While efficiency is a key factor, cost considerations are equally important. Delving into the financial aspects of utilizing different trailers is essential. Balancing efficiency with budgetary constraints ensures a cost-effective and successful project cargo transportation process. Understanding the long-term benefits and potential cost savings of investing in the right trailer is crucial for businesses in Oman.</p><h6>Real-world Case Studies</h6><p>Real-world case studies serve as valuable insights into successful project cargo transportation. These examples illustrate how the right choice of trailers can make or break a logistics project. Examining cases where multi-axle trailers, semi-modular solutions, SPMT, or lowbed trailers were instrumental provides practical knowledge for those embarking on similar ventures.</p><h6>Future Trends in Heavy Cargo Transportation</h6><p>As technology advances and industries evolve, the landscape of heavy cargo transportation is changing. Exploring future trends in the industry provides businesses with a strategic advantage. From the integration of smart technologies to eco-friendly solutions, staying informed about emerging trends ensures that logistics in Oman remain at the forefront of innovation.</p><h6>Conclusion: Paving the Way Forward</h6><p>In conclusion, the world of project cargo logistics in Oman is undergoing a transformative journey. The choice of trailers, be it the stability of multi-axle trailers, adaptability of semi-modular solutions, autonomy of SPMT, or versatility of lowbed trailers, plays a vital role in shaping this future. By embracing the power of these heavy-duty movers, businesses can pave the way forward, ensuring precision, reliability, and efficiency in every project cargo endeavor</p>', 'qwe', NULL, NULL, NULL, NULL, 'on-the-move-maximizing'),
(6, 'blog_headers/blogpost6.webp', 'Free Zone Advantage: Strategic Insights into Free Zone Clearance Dynamics in GCC Industries', '2024-06-27T10:00:57.823Z', 'At its core, a Free Zone is a sanctuary for businesses within a country, offering a range of benefits and privileges.', '<p>In the realm of business, staying ahead requires a keen eye for strategic advantages. For industries in the Gulf Cooperation Council (GCC), one such advantage that\'s been gaining traction is the Free Zone clearance dynamics. In this article, we\'ll dive into the nuances of how Free Zones provide a unique edge to businesses, unravelling complexities in a way that\'s easily digestible for the general public. So, let\'s embark on a journey into the world of business freedom in the GCC.</p><h6>Understanding the Free Zone Concept</h6><p><br></p><h6>What\'s a Free Zone, Anyway?</h6><p>At its core, a Free Zone is a sanctuary for businesses within a country, offering a range of benefits and privileges. It\'s a designated area where businesses operate under more relaxed regulations, fostering an environment conducive to growth. Picture it as a haven where businesses can spread their wings without the usual constraints.</p><h6>Decoding \'Clearance Dynamics\'</h6><p>The term \'clearance dynamics\' might sound complex, but at its essence, it\'s the strategic dance businesses engage in to navigate customs, paperwork, and efficiency. In this section, we\'ll break down the process, revealing how businesses seamlessly move through the bureaucratic maze.</p><h6>The Irresistible Allure of GCC Free Zones</h6><p><br></p><h6>Tax Incentives: Business Bliss</h6><p>Did you know? GCC Free Zones often come with attractive tax incentives, acting as magnets for businesses looking to maximise profits. Imagine a scenario where your hard-earned money stays with you, thanks to a tax-friendly haven – that\'s the allure these zones present.</p><h6>Global Connectivity: Beyond Borders</h6><p>In our interconnected world, global connectivity is the key to success. We\'ll explore how businesses in GCC Free Zones leverage their geographical advantage to establish international connections. This creates a ripple effect of opportunities, allowing businesses to transcend borders effortlessly.</p><h6>Infrastructure Magic: State-of-the-Art Facilities</h6><p>Infrastructure plays a pivotal role in business success. From cutting-edge technology to world-class facilities, GCC Free Zones provide an environment where businesses can thrive without getting bogged down by logistical hassles. It\'s a place where innovation meets efficiency.</p><h6>Navigating the Free Zone Landscape</h6><p><br></p><h6>Choosing the Right Free Zone</h6><p>Selecting the right Free Zone is paramount for businesses. We\'ll guide you through the factors to consider, ensuring that businesses make informed decisions aligning with their goals. It\'s about finding the perfect fit for sustainable growth.</p><h6>Simplifying Paper Trails</h6><p>Nobody enjoys drowning in paperwork. Discover how Free Zones streamline documentation processes, making it a breeze for businesses to operate efficiently without getting lost in a sea of forms. It\'s about simplifying the bureaucratic maze.</p><h6>Unlocking the Potential</h6><p><br></p><h6>Strategic Partnerships: Collaboration is Key</h6><p>Two heads are better than one - We\'ll explore how Free Zones in the GCC encourage collaboration, allowing businesses to form strategic partnerships that open doors to new possibilities. It\'s about recognizing that collective efforts often lead to greater success.</p><h6>Risk Mitigation: Navigating Challenges</h6><p>Every business faces challenges, but how they navigate them defines their success. We\'ll discuss how the Free Zone advantage extends to risk mitigation, providing businesses with a safety net in uncertain times. It\'s about turning challenges into opportunities.</p><h6>Conclusion: Embracing the Free Zone Advantage</h6><p>In wrapping up our exploration, it\'s clear that the Free Zone advantage in GCC industries goes beyond borders. From tax incentives to global connectivity, the benefits are substantial, creating a fertile ground for businesses to thrive. Embracing this advantage becomes a strategic move for those aiming for sustained growth in a competitive landscape.</p><p>Embark on your journey into the world of GCC Free Zones and witness firsthand how businesses turn challenges into opportunities. These zones offer more than just a location; they provide a pathway to unlocking strategic opportunities for sustainable growth.</p><p><br></p>', 'qwe', NULL, NULL, NULL, NULL, 'free-zone-advantage-strategic-'),
(7, 'blog_headers/blogpost7.webp', 'Cross-Border Customs Clearance: Navigating New Trade Realities', '2024-06-27T10:03:41.607Z', 'Logistics companies play a crucial role in facilitating cross-border customs clearance in Oman', '<p><span style=\"color: rgb(33, 37, 41);\">Cross-border customs clearance is an essential process in international trade, ensuring the smooth flow of goods across borders while adhering to legal regulations and requirements. As businesses continue to expand globally, understanding the intricacies of customs clearance becomes crucial for successful trade operations.</span></p><p><span style=\"color: rgb(33, 37, 41);\"><span class=\"ql-cursor\">﻿</span></span><img src=\"https://alsiglobal.com/images/BlogBanner/newtrade1.webp\" alt=\"Customs Clearance - 2\">Customs clearance involves the submission of necessary documents, payment of duties and taxes, and ensuring compliance with import and export regulations. It requires careful coordination between various stakeholders, including importers, exporters, customs authorities, and transportation companies. The process can vary from country to country, making it vital for businesses to have a comprehensive understanding of the specific requirements in each jurisdiction.</p><p>Logistics companies play a crucial role in facilitating cross-border customs clearance in Oman. These companies specialize in managing the transportation and storage of goods, ensuring efficient movement of shipments across borders. They possess the expertise and knowledge of local customs regulations, documentation requirements, and tariff classifications, enabling them to navigate the complexities of customs clearance seamlessly.</p><p>In Oman, logistics companies act as intermediaries between businesses and customs authorities. They assist in the preparation and submission of necessary documentation, such as commercial invoices, packing lists, and certificates of origin. They also provide valuable advice on customs valuation, duty rates, and any specific regulations that may apply to certain goods or industries.</p><p>Moreover, logistics companies in Oman collaborate with shipping companies to ensure a smooth flow of goods from the port of origin to the final destination. They coordinate transportation, handle documentation, and track shipments, offering end-to-end solutions for businesses engaged in cross-border trade.</p><p>Shipping companies play a vital role in cross-border customs clearance in Oman. These companies specialize in transporting goods by sea, providing essential services for businesses engaged in international trade. They ensure the safe and timely delivery of goods while complying with customs regulations and procedures.</p><p>In Oman, shipping companies work closely with logistics companies to facilitate customs clearance. They provide crucial information on vessel schedules, container availability, and port operations, enabling logistics companies to plan and execute shipments effectively. Shipping companies also assist in the preparation of shipping documents, such as bills of lading and cargo manifests, which are essential for customs clearance.</p><p>Furthermore, shipping companies in Oman have extensive knowledge of international shipping regulations, including the International Maritime Organization (IMO) conventions and the International Convention for the Safety of Life at Sea (SOLAS). This expertise ensures compliance with safety and security requirements, enhancing the efficiency and reliability of cross-border customs clearance.</p><h6>Navigating New Trade Realities</h6><p>The landscape of international trade is constantly evolving, influenced by various factors such as geopolitical changes, technological advancements, and shifts in global supply chains. Businesses must adapt to these new trade realities to remain competitive and ensure efficient cross-border customs clearance.</p><p>One of the significant trade realities businesses face today is the increasing emphasis on sustainability and environmental responsibility. Governments and consumers worldwide are demanding greater transparency and accountability in supply chain operations. Businesses must incorporate sustainable practices into their operations to meet these expectations, including reducing carbon emissions, managing waste, and promoting ethical sourcing.</p><p>Another trade reality is the growing importance of digitalization in customs clearance processes. Many countries are adopting electronic systems, such as Single Window platforms, to streamline and expedite customs procedures. Businesses should leverage digital solutions to enhance efficiency, reduce paperwork, and improve communication with customs authorities.</p><h6>Conclusion</h6><p>Furthermore, the emergence of new trade agreements and regional economic blocs presents both opportunities and challenges for businesses engaged in cross-border trade. These agreements, such as the Gulf Cooperation Council (GCC), offer preferential treatment to eligible goods. Businesses should carefully analyze the benefits and requirements of these agreements to maximize their advantages and remain competitive in the global marketplace.</p><p>If you\'re looking for reliable logistics and shipping services in Oman, contact us today to discuss how we can streamline your cross-border customs clearance and enhance your international trade operations.</p>', 'qwe', NULL, NULL, NULL, NULL, 'cross-border-customs-clearance'),
(8, 'blog_headers/blogpost8.webp', 'The Intricate Web of Automotive Logistics in GCC', '2024-06-27T10:06:51.764Z', 'The GCC automotive industry has experienced rapid expansion', '<p><br></p><p>Automotive logistics is an essential component of the thriving automotive industry in the Gulf Cooperation Council (GCC) region. Composed of Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, and the United Arab Emirates, the GCC has witnessed remarkable growth in its automotive sector over the past few decades. As a shipping company in Oman, we understand the intricate web of automotive logistics in the GCC and the challenges it presents.</p><p><br></p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/indricate1.webp\" alt=\"Customs Clearance - 2\">Overview of the GCC Automotive Industry</h6><p>The GCC automotive industry has experienced rapid expansion, fueled by factors such as a growing population, increasing disposable income, and favorable government policies. The GCC countries are major consumers of automobiles, with a significant demand for both passenger and commercial vehicles. Automotive manufacturers from around the world have recognized the potential of the GCC market and established their presence in the region. This has led to the development of a robust automotive supply chain, involving the import of vehicles, spare parts, and accessories, as well as the export of locally manufactured automobiles.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/indricate2.webp\" alt=\"Customs Clearance - 3\">Key Challenges in Automotive Logistics</h6><p>While the GCC automotive industry presents immense opportunities, it also poses unique challenges for logistics companies in Oman and other GCC countries. One of the primary challenges is the vast geographical spread of the region, which requires efficient transportation networks to ensure timely delivery of vehicles and parts. Additionally, customs regulations and documentation processes vary across the GCC countries, adding complexity to cross-border operations. Moreover, the extreme weather conditions in the region, particularly during the summer months, can impact the quality and performance of vehicles during transportation.</p><p>Another significant challenge is the fluctuating demand for different vehicle models in the GCC market. Automotive logistics companies need to adapt quickly to changing preferences and ensure the availability of the right vehicles at the right time. This requires effective inventory management and forecasting techniques. Furthermore, the GCC countries have diverse cultural and linguistic backgrounds, necessitating a nuanced understanding of local customs and business practices to ensure smooth operations.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/indricate3.webp\" alt=\"Customs Clearance - 4\">Supply Chain Management</h6><p>Efficient supply chain management is crucial for the success of automotive logistics in the GCC. It involves the coordination and integration of various stakeholders, including manufacturers, distributors, dealers, and logistics service providers. A well-managed supply chain ensures the timely delivery of vehicles, parts, and accessories, minimizes inventory costs, and enhances customer satisfaction.</p><p>Technology plays a vital role in optimizing supply chain management in the GCC automotive industry. Advanced tracking and tracing systems enable real-time monitoring of shipments, providing visibility and transparency throughout the logistics process. This helps identify bottlenecks and potential delays, allowing for proactive measures to mitigate risks. Additionally, cloud-based platforms and data analytics facilitate efficient inventory management and demand forecasting, enabling logistics companies to align their operations with market trends.</p><h6>Technologies Transforming GCC Automotive Logistics</h6><p>The GCC automotive logistics industry is undergoing a digital transformation, driven by technological advancements. One such technology is the Internet of Things (IoT), which involves the use of interconnected devices to collect and exchange data. In the context of automotive logistics, IoT devices can be utilized to track vehicles, monitor their condition, and optimize routing and delivery processes. This enables logistics companies to improve operational efficiency, reduce costs, and enhance customer satisfaction.</p><p>Another technology revolutionizing automotive logistics in the GCC is blockchain. By leveraging blockchain technology, logistics companies can create secure and transparent supply chain networks. Blockchain enables the verification and recording of every transaction in a decentralized and tamper-proof manner, reducing the risk of fraud and enhancing trust between stakeholders. This technology also simplifies the documentation process and facilitates seamless cross-border operations.</p><h6>Sustainable Practices in GCC Automotive Logistics</h6><p>As the world becomes increasingly conscious of environmental sustainability, the GCC automotive industry is also embracing greener practices in logistics. Electric vehicles (EVs) are gaining popularity in the region, and logistics companies are adapting their operations to accommodate the unique requirements of EV transportation. This includes the installation of charging infrastructure, training of personnel in EV handling, and the integration of EVs into the existing logistics fleet.</p><p>Furthermore, logistics companies in Oman and other GCC countries are exploring alternative fuels and energy-efficient vehicles to reduce carbon emissions. The use of hybrid vehicles and the adoption of eco-friendly packaging materials are becoming more prevalent in automotive logistics. Additionally, initiatives are being taken to optimize route planning and reduce empty miles, further minimizing the environmental impact of logistics operations.</p><h6>Future Trends and Innovations</h6><p>The future of automotive logistics in the GCC holds exciting possibilities. One emerging trend is the use of autonomous vehicles for transportation and last-mile delivery. Self-driving vehicles have the potential to revolutionize logistics by improving safety, reducing costs, and increasing efficiency. The GCC\'s modern infrastructure and supportive regulatory environment make it an ideal testing ground for autonomous vehicle technologies.</p><p>Another area of innovation is the integration of artificial intelligence (AI) in logistics operations. AI-powered systems can analyze vast amounts of data, predict demand patterns, optimize routing, and automate various aspects of the logistics process. This not only enhances operational efficiency but also enables logistics companies to offer personalized services and meet the evolving needs of customers.</p><h6>Wrapping Up</h6><p>Automotive logistics in the GCC is a complex and dynamic field that plays a vital role in supporting the growth of the regional automotive industry. As a shipping company in Oman, we understand the intricacies and challenges associated with automotive logistics in the GCC. From managing the supply chain to harnessing advanced technologies and adopting sustainable practices, logistics companies in the region are continuously evolving to meet the demands of the industry. With future trends such as autonomous vehicles and AI-driven operations on the horizon, the future of automotive logistics in the GCC holds immense potential for innovation and growth.</p>', 'qwe', NULL, NULL, NULL, NULL, 'the-intricate-web-of');
INSERT INTO `blogs_blogpost` (`id`, `header_image`, `header_title`, `publish_date`, `quotes`, `Highlight`, `author`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`, `slug`) VALUES
(9, 'blog_headers/blogpost9.webp', 'The future outlook for event and exhibition logistics in GCC, including the potential for growth and development', '2024-06-27T10:10:48.727Z', 'The GCC region is rapidly becoming an important hub for events and exhibitions.', '<p>Events and exhibitions are an increasingly important part of business and marketing in the GCC region. For event and exhibition logistics, ALSI is the perfect partner to help organisations unlock the full potential of their activities. With a wealth of experience in the industry and a commitment to delivering the best possible service, ALSI is the ideal choice for those looking to make the most of their events and exhibitions. Our innovative approach to logistics and our team of experts ensures that even the most demanding of requirements can be met. What’s more, ALSI is committed to creating a seamless experience for all of our customers, from start to finish. With ALSI, organisations can be confident that their events and exhibitions will be managed to the highest standards and will be a success.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/future1.webp\" alt=\"Customs Clearance - 2\">Know About Event and Exhibition Logistics</h6><p>Event and exhibition logistics is the process of planning, organising, and executing the necessary activities to ensure the success of an event or exhibition. This includes everything from selecting venues to arranging transportation, managing logistics, and ensuring the necessary supplies and materials are in place. This can be a complex process and one that requires detailed planning and organisation. Event and exhibition logistics can also include the services of a third-party logistics provider.</p><p>The GCC region is rapidly becoming an important hub for events and exhibitions. With the increasing number of international business conferences, exhibitions, and other events taking place, the potential for growth and development in the region is huge. The future of event and exhibition logistics in the GCC region is bright. With the growing demand for events and exhibitions, there is a need for companies that can provide reliable and efficient event and exhibition logistics services. This is where ALSI comes in. We specialise in providing event and exhibition logistics services, offering everything from event planning to supply chain management. By working with a third-party provider, organisations can benefit from the expertise and experience of a dedicated team of professionals who can ensure that all aspects of the event or exhibition are managed to the highest standards.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/future2.webp\" alt=\"Customs Clearance - 3\">The Benefits of Working with ALSI; Our Innovative Approach to Event and Exhibition Logistics</h6><p>At ALSI, we offer a multitude of benefits for those seeking event and exhibition logistics services. Our team brings decades of experience and expertise to the table, ensuring that every aspect of your event is planned and executed to the highest standards. We are committed to providing exceptional customer service, with a dedicated team that will work closely with you from beginning to end, ensuring that all of your needs are met. From venue selection to transportation and logistics management, ALSI will ensure that everything runs smoothly. We provide innovative solutions to enhance the success of your event, utilising cutting-edge technologies and streamlining supply chain processes.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/future3.webp\" alt=\"Customs Clearance - 4\">Unlock the Full Potential of Organizations’ Events and Exhibitions; Our Experienced Team in Event and Exhibition Logistics</h6><p>ALSI provides comprehensive event and exhibition management services to organisations, ensuring that all aspects of their event or exhibition are managed to the highest standards. Our team of experienced professionals is dedicated to delivering the best possible service to our customers. Each team member is highly trained and knowledgeable in their field, and we are committed to providing top-quality service. We understand that events and exhibitions can be complex and challenging, which is why we have a team of experienced event planners and logistics professionals who can ensure that all requirements are met. Moreover, we have extensive knowledge of the different venues and locations in the GCC region, allowing us to select the perfect venue for each event or exhibition.</p><p>At ALSI, we take an innovative approach to logistics. We understand that no two events or exhibitions are the same and that each one requires a tailored solution. This is why we work closely with our customers to develop a customised plan that meets their specific needs. We also use the latest technologies to ensure that all aspects of the event or exhibition are managed efficiently and effectively. From GPS tracking systems to sophisticated warehouse management systems, we have the tools and expertise to ensure the smooth running of the event or exhibition.</p><h6>Quality Assurance Process in Event and Exhibition Logistics</h6><p>At ALSI, we take quality assurance very seriously. We have a rigorous quality control process in place to ensure that all aspects of the event or exhibition are managed to the highest standards. The quality assurance process includes regular inspections and reviews of all aspects of the event or exhibition. This includes everything from the selection of venues to the logistics of the event or exhibition. This ensures that all aspects are managed to the highest standards and that the event or exhibition is a success.</p><h6>Commitment to Creating a Seamless Logistics Experience</h6><p>In conclusion, ALSI is the complete logistics solutions provider to help organisations unlock the full potential of their events and exhibitions in the GCC region. With a wealth of experience in the industry and a commitment to delivering the best possible service in events and exhibition logistics in GCC, ALSI is the perfect choice for those looking to make the most of their events and exhibitions. Our innovative approach to logistics and our team of experts ensures that even the most demanding of requirements can be met. What’s more, ALSI is committed to creating a seamless experience for all of its customers, from start to finish. With ALSI, organisations can be confident that their events and exhibitions will be managed to the highest standards and will be a success.</p><p><br></p>', 'qwe', NULL, NULL, NULL, NULL, 'the-future-outlook-for-event'),
(10, 'blog_headers/blogpost10.webp', 'The role of cross-border transportation in promoting trade facilitation and regional integration in GCC', '2024-06-27T10:18:21.715Z', 'Cross-border transportation is expected to continue to grow in importance in the GCC countries in the coming years.', '<p>Globalisation has brought immense opportunities for businesses to expand their reach beyond borders. The Gulf Cooperation Council (GCC) region is no exception. With the increase in cross-border trade, transportation has become a critical factor in facilitating trade and commerce within the region. The GCC countries have invested heavily in transportation infrastructure to support this growth, but there are still challenges that need to be addressed. In this article, we will explore the benefits of cross-border transportation for trade facilitation in the GCC and examine how it can help businesses to thrive in the global marketplace. From reducing transportation costs to improving supply chain efficiency, cross-border transportation has the potential to revolutionise trade in the region. So, let’s dive into the world of cross-border transportation and discover how it can help businesses to go beyond borders and capitalise on new opportunities.</p><p><br></p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/role1.webp\" alt=\"Customs Clearance - 2\">THE IMPORTANCE OF CROSS BORDER TRANSPORTATION FOR TRADE FACILITATION</h6><p>Transportation is a critical component of trade facilitation. It plays a vital role in connecting businesses and markets across borders. In the GCC countries, cross-border transportation is essential for businesses looking to expand their reach beyond their domestic markets. The GCC region is strategically located between Asia, Europe, and Africa, making it an ideal location for businesses to connect with markets in these regions. With the increase in cross-border trade, transportation has become a critical factor in facilitating trade and commerce within the region.</p><p>Cross-border transportation helps businesses to access new markets and connect with suppliers and customers around the world. It enables businesses to expand their reach beyond their domestic markets and capitalise on new opportunities. Efficient transportation systems can help businesses to reduce transportation costs, improve supply chain efficiency, and enhance their competitiveness in the global marketplace.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/role2.webp\" alt=\"Customs Clearance - 3\">CURRENT CHALLENGES IN CROSS BORDER TRANSPORTATION IN THE GCC</h6><p>Despite significant investments in transportation infrastructure, cross-border transportation in the GCC countries still faces several challenges. One of the primary challenges is the lack of coordination between customs authorities and transportation providers. This can lead to delays and increased transportation costs, making it difficult for businesses to compete in the global marketplace.</p><p>Another challenge is the lack of harmonisation in transportation regulations and policies. Each GCC country has its own transportation regulations and policies, making it difficult for businesses to navigate the complex regulatory environment. This can lead to delays and increased transportation costs, further hampering the competitiveness of businesses in the region.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/role3.webp\" alt=\"Customs Clearance - 4\">TECHNOLOGICAL ADVANCEMENTS IN CROSS BORDER TRANSPORTATION</h6><p>Technological advancements have the potential to revolutionise cross-border transportation in the GCC countries. Digital technologies such as blockchain, artificial intelligence, and the Internet of Things (IoT) can help to streamline transportation processes, reduce costs, and improve supply chain efficiency. For example, blockchain technology can help to secure and automate cross-border transactions, reducing the risk of fraud and increasing transparency. Artificial intelligence can help to optimise transportation routes and reduce transportation costs, while the IoT can help to track shipments in real-time, improving supply chain visibility.</p><p>The adoption of these technologies requires collaboration between transportation providers, customs authorities, and businesses. By working together, these stakeholders can create a more efficient and transparent transportation system that benefits everyone.</p><h6>BENEFITS OF CROSS BORDER TRANSPORTATION FOR BUSINESSES IN THE GCC</h6><p>Cross-border transportation offers several benefits for businesses in the GCC countries. One of the primary benefits is the ability to access new markets and connect with suppliers and customers around the world. Efficient transportation systems can help businesses to reduce transportation costs, improve supply chain efficiency, and enhance their competitiveness in the global marketplace.</p><p>Another benefit is the ability to leverage economies of scale. By expanding their reach beyond their domestic markets, businesses can take advantage of economies of scale and reduce their manufacturing and distribution costs. This can help to improve their profit margins and enhance their competitiveness in the global marketplace.</p><h6>CROSS BORDER TRANSPORTATION REGULATIONS AND POLICIES IN THE GCC</h6><p>Cross-border transportation regulations and policies in the GCC countries can be complex and difficult to navigate. Each GCC country has its own transportation regulations and policies, making it challenging for businesses to comply with them. This can lead to delays and increased transportation costs, further hampering the competitiveness of businesses in the region.</p><p>To address these challenges, the GCC countries have taken steps to harmonise their transportation regulations and policies. The GCC Customs Union, for example, has created a common customs tariff for all goods imported into the GCC countries, reducing customs clearance times and simplifying the clearance process. The GCC countries have also signed several agreements to facilitate cross-border transportation, such as the GCC Land Transport Agreement and the GCC Railways Network.</p><h6>STRATEGIES FOR SUCCESSFUL CROSS BORDER TRANSPORTATION IN THE GCC</h6><p>Cross-border transportation is expected to continue to grow in importance in the GCC countries in the coming years. As businesses look to expand their reach beyond their domestic markets, transportation will become increasingly critical in facilitating trade and commerce within the region. Technological advancements will play a significant role in shaping the future of cross-border transportation, with digital technologies such as blockchain, artificial intelligence, and the IoT expected to revolutionise transportation processes.</p><p>The GCC countries are also expected to continue to invest in transportation infrastructure to support this growth. This includes investments in roads, railways, ports, and airports to improve connectivity within the region and with other regions around the world.</p><h6>Conclusion</h6><p>Cross-border transportation is critical in facilitating trade and commerce within the GCC region. Despite significant investments in transportation infrastructure, cross-border transportation in the GCC countries still faces several challenges. However, with the adoption of digital technologies, the harmonisation of transportation regulations and policies, and collaboration between businesses, transportation providers, and customs authorities, cross-border transportation has the potential to revolutionise trade in the region. By leveraging the benefits of cross-border transportation, businesses in the GCC countries can expand their reach beyond their domestic markets and capitalise on new opportunities in the global marketplace.</p>', 'qwe', NULL, NULL, NULL, NULL, 'the-role-of-cross-border'),
(11, 'blog_headers/blogpost11.webp', 'The impact of UAE-Oman transportation on trade and commerce to driving economic growth', '2024-06-27T10:19:47.100Z', 'Efficient transportation links between the two countries have opened up new opportunities for businesses looking to expand their operations.', '<p>In today’s global economy, businesses are always looking for ways to expand their reach and increase profits. One of the key factors in achieving this is efficient transportation and logistics. The United Arab Emirates and Oman have experienced significant growth and development in their transportation sector, leading to increased connectivity between the two countries. This has opened up new opportunities for businesses looking to expand their operations and tap into new markets for logistics companies in Oman. However, navigating the complex world of transportation and logistics can be challenging, particularly for businesses with limited experience in this area. This is where the importance of a reliable logistics partner comes in. In this article, we will explore the impact of transportation on business growth in the UAE and Oman, and the crucial role that logistics partners play in helping businesses achieve their goals.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/impact1.webp\" alt=\"Customs Clearance - 2\">ECONOMIC BENEFITS OF TRANSPORTATION BETWEEN UAE AND OMAN</h6><p>The UAE and Oman have a long history of trade and economic cooperation. Both countries have made significant investments in their transportation infrastructure to facilitate the movement of goods and people between them. The economic benefits of transportation between the UAE and Oman are significant and wide-ranging. One of the most significant benefits is the boost it provides to economic growth in both countries. Improved transportation links facilitate trade and commerce, allowing businesses to expand their operations and tap into new markets. This, in turn, leads to increased investment, job creation, and higher incomes for people in both countries. In addition to the economic benefits, transportation between the UAE and Oman also provides social benefits. It facilitates the movement of people between the two countries, allowing for increased cultural exchange and tourism. This, in turn, leads to greater understanding and cooperation between the two countries.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/impact2.webp\" alt=\"Customs Clearance - 3\">IMPACT OF TRANSPORTATION ON BUSINESS GROWTH</h6><p>The impact of transportation on business growth cannot be overstated. The ability to move goods and people quickly and efficiently is essential for businesses looking to expand their reach and tap into new markets. This is particularly true in the UAE and Oman, where the transportation sector has undergone significant growth and development in recent years.</p><p>Efficient transportation links between the two countries have opened up new opportunities for businesses looking to expand their operations. Improved connectivity has led to increased trade and commerce, allowing businesses to reach new customers and tap into new markets. This, in turn, has led to increased investment, job creation, and higher incomes for people in both countries.</p><p>The impact of transportation on business growth goes beyond just economic benefits. It also provides social benefits, such as increased cultural exchange and tourism. This, in turn, leads to greater understanding and cooperation between the two countries.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/impact3.webp\" alt=\"Customs Clearance - 4\">THE ROLE OF LOGISTICS PARTNERS IN IMPROVING TRANSPORTATION</h6><p>The importance of a reliable logistics partner cannot be overstated when it comes to improving transportation. Logistics partners play a crucial role in helping businesses navigate the complex world of transportation and logistics. They provide a range of services, including freight forwarding, customs clearance, warehousing, and distribution.</p><p>Logistics partners can help businesses improve their transportation efficiency by providing end-to-end solutions that streamline the movement of goods and people. They can also help businesses navigate the complex regulations and procedures involved in cross-border transportation. This is particularly important in the UAE and Oman, where regulations and procedures can be complex and challenging to navigate.</p><p>In addition to improving transportation efficiency, logistics partners can also help businesses reduce their transportation costs. By leveraging their expertise and experience, logistics partners can help businesses optimise their transportation routes, reduce transit times, and minimise the risk of delays or disruptions.</p><h6>HOW MUCH IS CUSTOMS CLEARANCE IN OMAN?</h6><p>Customs clearance in Oman’s Free Trade Zones may involve minimal or no customs duties. The actual costs can vary depending on the nature of the goods and the specific FTZ. Consulting with a local customs broker or a company like Alsi can provide accurate information tailored to your situation.</p><h6>CHALLENGES FACED IN TRANSPORTATION BETWEEN UAE AND OMAN</h6><p>Despite the significant growth and development in the transportation sector in the UAE and Oman, there are still challenges that businesses face when it comes to transportation. One of the biggest challenges is the complex regulations and procedures involved in cross-border transportation.</p><p>Navigating the different regulations, customs procedures, and paperwork required can be a daunting task, particularly for businesses with limited experience in this area. This can lead to delays and added costs, which can impact businesses’ ability to compete effectively.</p><p>Another challenge that businesses face is the lack of infrastructure in some areas. While both countries have invested heavily in their transportation infrastructure, there are still areas where improvements are needed. This can lead to delays and added costs, particularly for businesses operating in remote or hard-to-reach areas.</p><h6>FUTURE DEVELOPMENTS IN UAE-OMAN TRANSPORTATION</h6><p>Despite the challenges that businesses face when it comes to transportation between the UAE and Oman, there are also significant opportunities for growth and development in the future for shipping companies in Oman. Both countries have ambitious plans to further improve their transportation infrastructure, which will lead to increased connectivity and improved transportation efficiency.</p><p>One of the most significant developments is the construction of the UAE-Oman rail network. This will provide a new and efficient mode of transportation between the two countries, facilitating the movement of goods and people. It is expected to be completed by 2023 and will provide significant benefits for businesses looking to expand their operations in the region.</p><p>In addition to the rail network, both countries are also investing in other modes of transportation, such as airports and seaports. These developments will provide businesses with even more options when it comes to transportation, allowing them to choose the most efficient and cost-effective mode of transportation for their needs.</p><h6>IMPORTANCE OF COLLABORATION BETWEEN UAE AND OMAN FOR ECONOMIC GROWTH</h6><p>Collaboration between the UAE and Oman is essential for achieving sustained economic growth in the region. Both countries have a long history of trade and economic cooperation, and this collaboration has led to significant benefits for both countries.</p><p>Efficient transportation links between the two countries are essential for maintaining this collaboration and achieving sustained economic growth. By working together, both countries can leverage their strengths and expertise to create a more efficient and connected transportation network. This, in turn, will lead to increased trade and commerce, job creation, and higher incomes for people in both countries.</p><h6>CONCLUSION AND CALL TO ACTION FOR BUSINESSES TO UTILISE UAE-OMAN TRANSPORTATION</h6><p>Efficient transportation is essential for businesses looking to expand their operations and tap into new markets. The UAE and Oman have made significant investments in their transportation infrastructure, leading to increased connectivity and improved transportation efficiency.</p><p>However, navigating the complex world of transportation and logistics can be challenging, particularly for businesses with limited experience in this area. This is where the importance of a reliable logistics partner comes in. Logistics partners play a crucial role in helping businesses navigate the complex regulations and procedures involved in cross-border transportation.</p><p>To take advantage of the opportunities presented by UAE-Oman transportation, businesses must work with reliable logistics partners to optimise their transportation routes and minimise costs. By doing so, they can tap into new markets and achieve sustained growth and success in the region.</p><p><br></p>', 'qwe', NULL, NULL, NULL, NULL, 'the-impact-of-uae-oman'),
(12, 'blog_headers/blogpost11_1ASBfUP.webp', 'The impact of UAE-Oman transportation on trade and commerce to driving economic growth', '2024-06-27T10:26:17.967Z', 'Efficient transportation links between the two countries have opened up new opportunities for businesses looking to expand their operations.', '<p>In today’s global economy, businesses are always looking for ways to expand their reach and increase profits. One of the key factors in achieving this is efficient transportation and logistics. The United Arab Emirates and Oman have experienced significant growth and development in their transportation sector, leading to increased connectivity between the two countries. This has opened up new opportunities for businesses looking to expand their operations and tap into new markets for logistics companies in Oman. However, navigating the complex world of transportation and logistics can be challenging, particularly for businesses with limited experience in this area. This is where the importance of a reliable logistics partner comes in. In this article, we will explore the impact of transportation on business growth in the UAE and Oman, and the crucial role that logistics partners play in helping businesses achieve their goals.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/impact1.webp\" alt=\"Customs Clearance - 2\">ECONOMIC BENEFITS OF TRANSPORTATION BETWEEN UAE AND OMAN</h6><p>The UAE and Oman have a long history of trade and economic cooperation. Both countries have made significant investments in their transportation infrastructure to facilitate the movement of goods and people between them. The economic benefits of transportation between the UAE and Oman are significant and wide-ranging. One of the most significant benefits is the boost it provides to economic growth in both countries. Improved transportation links facilitate trade and commerce, allowing businesses to expand their operations and tap into new markets. This, in turn, leads to increased investment, job creation, and higher incomes for people in both countries. In addition to the economic benefits, transportation between the UAE and Oman also provides social benefits. It facilitates the movement of people between the two countries, allowing for increased cultural exchange and tourism. This, in turn, leads to greater understanding and cooperation between the two countries.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/impact2.webp\" alt=\"Customs Clearance - 3\">IMPACT OF TRANSPORTATION ON BUSINESS GROWTH</h6><p>The impact of transportation on business growth cannot be overstated. The ability to move goods and people quickly and efficiently is essential for businesses looking to expand their reach and tap into new markets. This is particularly true in the UAE and Oman, where the transportation sector has undergone significant growth and development in recent years.</p><p>Efficient transportation links between the two countries have opened up new opportunities for businesses looking to expand their operations. Improved connectivity has led to increased trade and commerce, allowing businesses to reach new customers and tap into new markets. This, in turn, has led to increased investment, job creation, and higher incomes for people in both countries.</p><p>The impact of transportation on business growth goes beyond just economic benefits. It also provides social benefits, such as increased cultural exchange and tourism. This, in turn, leads to greater understanding and cooperation between the two countries.</p><h6><img src=\"https://alsiglobal.com/images/BlogBanner/impact3.webp\" alt=\"Customs Clearance - 4\">THE ROLE OF LOGISTICS PARTNERS IN IMPROVING TRANSPORTATION</h6><p>The importance of a reliable logistics partner cannot be overstated when it comes to improving transportation. Logistics partners play a crucial role in helping businesses navigate the complex world of transportation and logistics. They provide a range of services, including freight forwarding, customs clearance, warehousing, and distribution.</p><p>Logistics partners can help businesses improve their transportation efficiency by providing end-to-end solutions that streamline the movement of goods and people. They can also help businesses navigate the complex regulations and procedures involved in cross-border transportation. This is particularly important in the UAE and Oman, where regulations and procedures can be complex and challenging to navigate.</p><p>In addition to improving transportation efficiency, logistics partners can also help businesses reduce their transportation costs. By leveraging their expertise and experience, logistics partners can help businesses optimise their transportation routes, reduce transit times, and minimise the risk of delays or disruptions.</p><h6>HOW MUCH IS CUSTOMS CLEARANCE IN OMAN?</h6><p>Customs clearance in Oman’s Free Trade Zones may involve minimal or no customs duties. The actual costs can vary depending on the nature of the goods and the specific FTZ. Consulting with a local customs broker or a company like Alsi can provide accurate information tailored to your situation.</p><h6>CHALLENGES FACED IN TRANSPORTATION BETWEEN UAE AND OMAN</h6><p>Despite the significant growth and development in the transportation sector in the UAE and Oman, there are still challenges that businesses face when it comes to transportation. One of the biggest challenges is the complex regulations and procedures involved in cross-border transportation.</p><p>Navigating the different regulations, customs procedures, and paperwork required can be a daunting task, particularly for businesses with limited experience in this area. This can lead to delays and added costs, which can impact businesses’ ability to compete effectively.</p><p>Another challenge that businesses face is the lack of infrastructure in some areas. While both countries have invested heavily in their transportation infrastructure, there are still areas where improvements are needed. This can lead to delays and added costs, particularly for businesses operating in remote or hard-to-reach areas.</p><h6>FUTURE DEVELOPMENTS IN UAE-OMAN TRANSPORTATION</h6><p>Despite the challenges that businesses face when it comes to transportation between the UAE and Oman, there are also significant opportunities for growth and development in the future for shipping companies in Oman. Both countries have ambitious plans to further improve their transportation infrastructure, which will lead to increased connectivity and improved transportation efficiency.</p><p>One of the most significant developments is the construction of the UAE-Oman rail network. This will provide a new and efficient mode of transportation between the two countries, facilitating the movement of goods and people. It is expected to be completed by 2023 and will provide significant benefits for businesses looking to expand their operations in the region.</p><p>In addition to the rail network, both countries are also investing in other modes of transportation, such as airports and seaports. These developments will provide businesses with even more options when it comes to transportation, allowing them to choose the most efficient and cost-effective mode of transportation for their needs.</p><h6>IMPORTANCE OF COLLABORATION BETWEEN UAE AND OMAN FOR ECONOMIC GROWTH</h6><p>Collaboration between the UAE and Oman is essential for achieving sustained economic growth in the region. Both countries have a long history of trade and economic cooperation, and this collaboration has led to significant benefits for both countries.</p><p>Efficient transportation links between the two countries are essential for maintaining this collaboration and achieving sustained economic growth. By working together, both countries can leverage their strengths and expertise to create a more efficient and connected transportation network. This, in turn, will lead to increased trade and commerce, job creation, and higher incomes for people in both countries.</p><h6>CONCLUSION AND CALL TO ACTION FOR BUSINESSES TO UTILISE UAE-OMAN TRANSPORTATION</h6><p>Efficient transportation is essential for businesses looking to expand their operations and tap into new markets. The UAE and Oman have made significant investments in their transportation infrastructure, leading to increased connectivity and improved transportation efficiency.</p><p>However, navigating the complex world of transportation and logistics can be challenging, particularly for businesses with limited experience in this area. This is where the importance of a reliable logistics partner comes in. Logistics partners play a crucial role in helping businesses navigate the complex regulations and procedures involved in cross-border transportation.</p><p>To take advantage of the opportunities presented by UAE-Oman transportation, businesses must work with reliable logistics partners to optimise their transportation routes and minimise costs. By doing so, they can tap into new markets and achieve sustained growth and success in the region.</p><p><br></p>', 'qwe', NULL, NULL, NULL, NULL, 'the-impact-of-uae-oman-1'),
(13, 'blog_headers/2.jpg', 'TEST', '2024-06-27T10:29:59.452Z', 'TEST', '<p>TEST</p>', 'qwe', NULL, NULL, NULL, NULL, 'test-blog'),
(14, 'blog_headers/2_Wn1i6t1.jpg', 'TEST', '2024-06-27T10:30:42.542Z', 'TEST', '<p>TEST</p>', 'qwe', NULL, NULL, NULL, NULL, 'test');

-- --------------------------------------------------------

--
-- Table structure for table `blogs_metatagsblogs`
--

CREATE TABLE `blogs_metatagsblogs` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `blog_post_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `careers_careerpage`
--

CREATE TABLE `careers_careerpage` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `header_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `slug` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `careers_careerpage`
--

INSERT INTO `careers_careerpage` (`id`, `title`, `header_image`, `description`, `slug`) VALUES
(1, '<p>Careers</p>', 'career_page/CareerImgBanner.webp', 'Be a part of ALSI', 'Careers');

-- --------------------------------------------------------

--
-- Table structure for table `careers_careersubmission`
--

CREATE TABLE `careers_careersubmission` (
  `id` bigint NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `resume` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `submitted_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `careers_metatagscareers`
--

CREATE TABLE `careers_metatagscareers` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `chooses_choosessection`
--

CREATE TABLE `chooses_choosessection` (
  `id` bigint NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `subtitle` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `bg_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chooses_choosessection`
--

INSERT INTO `chooses_choosessection` (`id`, `title`, `subtitle`, `bg_image`) VALUES
(1, '<h1>why chooses us</h1>', '<p class=\"ql-align-center\">Partner with ALSI as your trusted logistics company for our unwavering commitment to reliability, seamlessness, and personalized service. With years of industry expertise, a global networkdedication to your success, we deliver tailored solutions that optimize your supply chain and drive your business with efficiency</p>', 'Chooses_Section/Ship-one-bg.a6bcc565972f3cf462da.webp');

-- --------------------------------------------------------

--
-- Table structure for table `contacts_contactform`
--

CREATE TABLE `contacts_contactform` (
  `id` bigint NOT NULL,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `contacts_contactheader`
--

CREATE TABLE `contacts_contactheader` (
  `id` bigint NOT NULL,
  `header_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `header_title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `header_description` longtext COLLATE utf8mb4_general_ci,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `slug` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts_contactheader`
--

INSERT INTO `contacts_contactheader` (`id`, `header_image`, `header_title`, `header_description`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`, `slug`) VALUES
(1, 'contact_header_images/contact-us-group.65ac2335701f3169e199.webp', '<h1><strong>Contact Us</strong></h1>', '<h1><strong>Let\'s Connect And Talk</strong></h1>', '', '', '', '', 'h1strongcontact-usstrongh1');

-- --------------------------------------------------------

--
-- Table structure for table `contacts_faq`
--

CREATE TABLE `contacts_faq` (
  `id` bigint NOT NULL,
  `question` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `answer` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `contacts_metatagscontacts`
--

CREATE TABLE `contacts_metatagscontacts` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `contacts_section`
--

CREATE TABLE `contacts_section` (
  `id` bigint NOT NULL,
  `section_title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `section_description` longtext COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(35, 'aboutus', 'aboutpagesection'),
(36, 'aboutus', 'certificatetitle'),
(37, 'aboutus', 'certifications'),
(38, 'aboutus', 'metatagsabout'),
(39, 'aboutus', 'milestone'),
(40, 'aboutus', 'milestonetitle'),
(41, 'aboutus', 'ourstory'),
(42, 'aboutus', 'ourstorytitle'),
(43, 'aboutus', 'ourteam'),
(44, 'aboutus', 'ourteamtitle'),
(45, 'aboutus', 'whatweare'),
(46, 'aboutus', 'whatwearetitle'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(33, 'blogs', 'blogpost'),
(34, 'blogs', 'metatagsblogs'),
(49, 'careers', 'careerpage'),
(50, 'careers', 'careersubmission'),
(51, 'careers', 'metatagscareers'),
(54, 'chooses', 'choosessection'),
(28, 'contacts', 'contactform'),
(29, 'contacts', 'contactheader'),
(30, 'contacts', 'faq'),
(31, 'contacts', 'metatagscontacts'),
(32, 'contacts', 'section'),
(5, 'contenttypes', 'contenttype'),
(69, 'customcss', 'aboutpagesectioncustom'),
(65, 'customcss', 'acheievementcustom'),
(82, 'customcss', 'careerspagecustom'),
(74, 'customcss', 'certificationcustom'),
(62, 'customcss', 'chooseuscustom'),
(75, 'customcss', 'contactformcustom'),
(76, 'customcss', 'footercustom'),
(83, 'customcss', 'headermarketupdatescustom'),
(77, 'customcss', 'headerournetworkcustom'),
(66, 'customcss', 'highlightscustom'),
(60, 'customcss', 'homeheadercustom'),
(86, 'customcss', 'industriesblockscustom'),
(67, 'customcss', 'industriescardscustom'),
(85, 'customcss', 'industriesheadercustom'),
(64, 'customcss', 'keydiffrentiatorscustom'),
(84, 'customcss', 'marketcustom'),
(68, 'customcss', 'marketupdatescustom'),
(71, 'customcss', 'milestonecustom'),
(63, 'customcss', 'ournetworkcustom'),
(78, 'customcss', 'ournetworkdescriptioncustom'),
(80, 'customcss', 'ournetworklocationcustom'),
(81, 'customcss', 'ournetworkofficescustom'),
(70, 'customcss', 'ourstorycustom'),
(72, 'customcss', 'ourteamcustom'),
(61, 'customcss', 'servicecardscustom'),
(79, 'customcss', 'servicecustom'),
(73, 'customcss', 'whatwearecustom'),
(55, 'footer', 'footer'),
(7, 'header', 'homeheader'),
(47, 'industry', 'industriespage'),
(48, 'industry', 'metatagsindustries'),
(56, 'industry_cards', 'industrycard'),
(57, 'industry_cards', 'industrytitles'),
(52, 'key', 'key_diffrentiates'),
(53, 'key', 'key_diffrentiatessection'),
(20, 'location_page', 'location_page'),
(21, 'location_page', 'metatagslocation'),
(22, 'location_page', 'office'),
(23, 'services', 'metatagsservices'),
(24, 'services', 'specializedservice'),
(25, 'services', 'specializedsubservice'),
(26, 'services', 'subheading'),
(27, 'services', 'subservice'),
(58, 'service_card', 'servicescard'),
(59, 'service_card', 'servicetitle'),
(6, 'sessions', 'session'),
(8, 'socialmedia', 'achievement'),
(9, 'socialmedia', 'achievementsection'),
(10, 'socialmedia', 'highlightssection'),
(11, 'socialmedia', 'homehighlights'),
(12, 'socialmedia', 'industry'),
(13, 'socialmedia', 'location'),
(14, 'socialmedia', 'market'),
(15, 'socialmedia', 'markettitle'),
(16, 'socialmedia', 'metatagshome'),
(17, 'socialmedia', 'ournetworktitle'),
(18, 'socialmedia', 'service'),
(19, 'socialmedia', 'socialmedia');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'aboutus', '0001_initial', '2024-06-26 11:43:56.768516'),
(2, 'aboutus', '0002_alter_ourteam_profile_pic', '2024-06-26 11:43:56.840292'),
(3, 'contenttypes', '0001_initial', '2024-06-26 11:43:56.886549'),
(4, 'auth', '0001_initial', '2024-06-26 11:43:57.392546'),
(5, 'admin', '0001_initial', '2024-06-26 11:43:57.501755'),
(6, 'admin', '0002_logentry_remove_auto_add', '2024-06-26 11:43:57.511080'),
(7, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-26 11:43:57.519087'),
(8, 'contenttypes', '0002_remove_content_type_name', '2024-06-26 11:43:57.607626'),
(9, 'auth', '0002_alter_permission_name_max_length', '2024-06-26 11:43:57.662007'),
(10, 'auth', '0003_alter_user_email_max_length', '2024-06-26 11:43:57.683934'),
(11, 'auth', '0004_alter_user_username_opts', '2024-06-26 11:43:57.692266'),
(12, 'auth', '0005_alter_user_last_login_null', '2024-06-26 11:43:57.743282'),
(13, 'auth', '0006_require_contenttypes_0002', '2024-06-26 11:43:57.745291'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2024-06-26 11:43:57.752443'),
(15, 'auth', '0008_alter_user_username_max_length', '2024-06-26 11:43:57.799618'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2024-06-26 11:43:57.842171'),
(17, 'auth', '0010_alter_group_name_max_length', '2024-06-26 11:43:57.860209'),
(18, 'auth', '0011_update_proxy_permissions', '2024-06-26 11:43:57.883904'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2024-06-26 11:43:57.932999'),
(20, 'blogs', '0001_initial', '2024-06-26 11:43:58.027257'),
(21, 'blogs', '0002_remove_blogpost_description_blogpost_slug', '2024-06-26 11:43:58.093527'),
(22, 'careers', '0001_initial', '2024-06-26 11:43:58.166851'),
(23, 'chooses', '0001_initial', '2024-06-26 11:43:58.187472'),
(24, 'contacts', '0001_initial', '2024-06-26 11:43:58.331088'),
(25, 'footer', '0001_initial', '2024-06-26 11:43:58.352003'),
(26, 'header', '0001_initial', '2024-06-26 11:43:58.375949'),
(27, 'industry', '0001_initial', '2024-06-26 11:43:58.416474'),
(28, 'industry', '0002_alter_industriespage_subtitle', '2024-06-26 11:43:58.453245'),
(29, 'industry_cards', '0001_initial', '2024-06-26 11:43:58.487494'),
(30, 'key', '0001_initial', '2024-06-26 11:43:58.522101'),
(31, 'socialmedia', '0001_initial', '2024-06-26 11:43:58.754273'),
(32, 'location_page', '0001_initial', '2024-06-26 11:43:58.857075'),
(33, 'location_page', '0002_location_page_slug', '2024-06-26 11:43:58.892395'),
(34, 'service_card', '0001_initial', '2024-06-26 11:43:58.928484'),
(35, 'services', '0001_initial', '2024-06-26 11:43:59.117238'),
(36, 'services', '0002_remove_specializedsubservice_alt_img_caption_and_more', '2024-06-26 11:43:59.301620'),
(37, 'sessions', '0001_initial', '2024-06-26 11:43:59.336622'),
(38, 'socialmedia', '0002_service_is_specialized', '2024-06-26 11:43:59.357270');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `footer_footer`
--

CREATE TABLE `footer_footer` (
  `id` bigint NOT NULL,
  `title` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `address` varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phone_number1` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phone_number2` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `footer_footer`
--

INSERT INTO `footer_footer` (`id`, `title`, `address`, `email`, `phone_number1`, `phone_number2`) VALUES
(1, 'Alsi Global LLC', '<p><span style=\"color: rgb(33, 37, 41);\">P.O.Box 608. P.C: 322.</span></p><p><span style=\"color: rgb(33, 37, 41);\">W. Sohar, Sultanate Of Oman.</span></p>', 'Info@alsioman.com', '+968 2675 5598', '+968 2675 5550'),
(2, 'United Arab Emirates', '<p><span style=\"color: rgb(33, 37, 41);\">Alsi Global LLC</span></p><p><span style=\"color: rgb(33, 37, 41);\">Business Bay, Churchill Towers</span></p><p><span style=\"color: rgb(33, 37, 41);\">Suite 3409, P.O. Box: 392585,</span></p><p><span style=\"color: rgb(33, 37, 41);\">Dubai, UAE.</span></p>', '', '+971 4 585 0934', '+971 52 376 7001'),
(3, 'State of Qatar', '<p><span style=\"color: rgb(33, 37, 41);\">C12 AL Emadi Business Center</span></p><p><span style=\"color: rgb(33, 37, 41);\"><span class=\"ql-cursor\">﻿</span>2nd Floor, Office 35,</span></p><p><span style=\"color: rgb(33, 37, 41);\">P.O. Box: 30611,</span></p><p><span style=\"color: rgb(33, 37, 41);\">Doha,&nbsp;Qatar.</span></p>', '', '+974 4047 8563', '+974 3362 5333'),
(4, 'Kingdom of Saudi Arabia', '<p><span style=\"color: rgb(33, 37, 41);\">Building No. 3475, Al Tail Street,</span></p><p><span style=\"color: rgb(33, 37, 41);\">9080, Dhahrat Laban Dist,</span></p><p><span style=\"color: rgb(33, 37, 41);\">PC 12564, Riyadh,</span></p><p><span style=\"color: rgb(33, 37, 41);\">Kingdom of Saudi Arabia</span></p>', '', '+966 050 362 5981', '');

-- --------------------------------------------------------

--
-- Table structure for table `header_homeheader`
--

CREATE TABLE `header_homeheader` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `subtitle` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `slug` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `header_homeheader`
--

INSERT INTO `header_homeheader` (`id`, `title`, `subtitle`, `description`, `image`, `url`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`, `slug`) VALUES
(1, '<h1><strong>Complete Logistics solution</strong></h1>', '<p>Reliable. Efficient. Seamless.</p>', '<p>ALSI: Your dedicated partner for comprehensive logistics services and solutions. With expertise in customs clearance, transportation, freight forwarding, project cargo services and warehousing, we optimize your supply chain. Partner with ALSI and experience hassle-free logistics that help achieve your business goals</p>', 'header_images/Landing_Page_image.f936b186837c223f2a9f_CUE8lO1.webp', 'http://localhost:5173/about_us', 'alt image text', 'alt img title', 'alt img caption', 'alt img description', 'Complete Logistics solution-1-1-1-1');

-- --------------------------------------------------------

--
-- Table structure for table `industry_cards_industrycard`
--

CREATE TABLE `industry_cards_industrycard` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `industry_cards_industrycard`
--

INSERT INTO `industry_cards_industrycard` (`id`, `title`, `description`, `image`, `alt_img_text`, `alt_img_title`, `alt_img_caption`, `alt_img_description`) VALUES
(1, '<p>Healthcare</p>', '<p>In the critical field of pharma and healthcare, we are dedicated to ensuring the safe and timely delivery of medical supplies, pharmaceuticals, and healthcare equipment. Our specialized logistics solutions adhere to the highest standards of compliance and precision</p>', 'industry_images/HealthcareLogistics.webp', 'alt image text', 'alt img title', 'alt img caption', 'alt img description'),
(2, '<p>Chemicals</p>', '<p>Safety and precision are paramount in the chemicals industry. We specialize in the secure transportation and storage of hazardous materials, ensuring compliance with strict regulations. Our expertise and state-of-the-art infrastructure guarantee the integrity of your chemical cargo, from point of origin to final destination.</p>', 'industry_images/ind3.webp', 'alt img text', 'alt img title', 'alt img caption', 'alt img description'),
(3, '<p>Energy</p>', '<p>We recognize the pivotal role of the energy industry. ALSI specializes in logistics solutions that prioritize safety, precision, and efficiency, tailored to the energy sector\'s unique demands. Whether you need equipment transport, project cargo management, or any energy-related logistics, count on ALSI for seamless operations.</p>', 'industry_images/Energy.webp', 'alt img text', 'alt img title', 'alt img caption', 'alt img description'),
(4, '<p>Oil &amp; Gas</p>', '<p>We understand the critical nature of the oil and gas industry. With a focus on safety, precision, and efficiency, we offer specialized logistics solutions tailored to this sector\'s unique demands. From transporting equipment to managing project cargo, ALSI is your trusted partner in ensuring seamless operations within the oil and gas sector.</p>', 'industry_images/oil.webp', '', '', '', ''),
(5, '<p>Food &amp; Beverages</p>', '<p>In the fast-paced world of Food and Beverage, we provide reliable logistics solutions to keep your products fresh and on time. Our temperature-controlled warehousing, efficient transportation, and expertise in handling delicate cargo make us the ideal partner for F&amp;B businesses.</p>', 'industry_images/bee.webp', 'alt image text', 'alt img title', 'alt img caption', 'alt img description'),
(6, '<p>Retail</p>', '<p>In the dynamic world of retail, we deliver tailored logistics solutions that meet your specific needs. Whether it\'s optimizing inventory management, ensuring just-in-time deliveries, or providing efficient warehousing and distribution, ALSI is your partner for success.</p>', 'industry_images/retail.webp', '', '', '', ''),
(7, '<p>Automative</p>', '<p>We drive excellence in the automotive sector with our comprehensive logistics solutions. From the manufacturing floor to dealerships, we specialize in efficiently transporting and managing vehicles and automotive components, ensuring on-time deliveries and cost-effective supply chain management.</p><p><br></p>', 'industry_images/AutomotiveLogistics.webp', '', '', '', ''),
(8, '<p>Aerospace</p>', '<p>In the aerospace industry, timing is everything. We specialize in time-critical shipments, including AOG (Aircraft on Ground) support, ensuring that vital components reach their destination swiftly to minimize downtime. As an experienced partner for Original Equipment Manufacturers (OEM), we understand the intricacies.</p>', 'industry_images/AerospaceLogistics.webp', '', '', '', ''),
(9, '<p>Manufacturing</p>', '<p>in the world of manufacturing, we offer tailored logistics solutions to optimize your production processes. From just-in-time delivery of raw materials to efficient distribution of finished products, we enhance your supply chain\'s efficiency and reduce costs.Making us your trusted logistics partner for seamless operations.</p><p><br></p>', 'industry_images/ManufacturingLogistics.webp', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `industry_cards_industrytitles`
--

CREATE TABLE `industry_cards_industrytitles` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `industry_cards_industrytitles`
--

INSERT INTO `industry_cards_industrytitles` (`id`, `title`) VALUES
(1, '<h1>Industries</h1>');

-- --------------------------------------------------------

--
-- Table structure for table `industry_industriespage`
--

CREATE TABLE `industry_industriespage` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `subtitle` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `industry_metatagsindustries`
--

CREATE TABLE `industry_metatagsindustries` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `key_key_diffrentiates`
--

CREATE TABLE `key_key_diffrentiates` (
  `id` bigint NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `tagline` longtext COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `key_key_diffrentiates`
--

INSERT INTO `key_key_diffrentiates` (`id`, `icon`, `tagline`) VALUES
(1, 'key_diffrentiates/iteration_1.webp', '<p>AGILE</p>'),
(2, 'key_diffrentiates/critical_1.webp', '<p>CRITICAL LOGISTICS EXPERTS</p>'),
(3, 'key_diffrentiates/customer_2.webp', '<p>CUSTOMER CENTRIC</p>'),
(4, 'key_diffrentiates/end.webp', '<h6>END-TO-END SERVICES AND SOLUTIONS</h6><h6><br></h6>'),
(5, 'key_diffrentiates/flexible.webp', '<p><span style=\"color: rgb(33, 37, 41);\">FLEXIBLE</span></p>'),
(6, 'key_diffrentiates/excellent.webp', '<p>EXCELLENT  CUSTOMER SERVICE</p>'),
(7, 'key_diffrentiates/operational.webp', '<h6>OPERATIONAL EXPERTISE</h6>'),
(8, 'key_diffrentiates/value.webp', '<h6>VALUE CREATION</h6>'),
(9, 'key_diffrentiates/round.webp', '<h6>ROUND THE CLOCK SERVICE</h6>'),
(10, 'key_diffrentiates/tailor.webp', '<h6>TAILOR-MADE SOLUTIONS</h6>');

-- --------------------------------------------------------

--
-- Table structure for table `key_key_diffrentiatessection`
--

CREATE TABLE `key_key_diffrentiatessection` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `subtitle` longtext COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `key_key_diffrentiatessection`
--

INSERT INTO `key_key_diffrentiatessection` (`id`, `title`, `subtitle`) VALUES
(1, '<p>Key Diffrentiators</p>', '<p>ALSI stands out through a combination of expertise, reliability, and flexibility. Our deep industry knowledge, commitment to meeting deadlines, and adaptability to changing market dynamics make us the preferred choice for all your logistics needs. We\'re not just a service provider; we\'re your trusted partner in streamlining your supply chain and achieving your business goals.</p>');

-- --------------------------------------------------------

--
-- Table structure for table `location_page_location_page`
--

CREATE TABLE `location_page_location_page` (
  `id` bigint NOT NULL,
  `Location_header_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `location_title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `location_subtitle` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `location_description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `slug` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `location_page_location_page`
--

INSERT INTO `location_page_location_page` (`id`, `Location_header_image`, `location_title`, `location_subtitle`, `location_description`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`, `slug`) VALUES
(1, 'Location_header_image/our-network-bg.webp', '<p>Our Network</p>', '<p><strong>ALSI is a proud and active member of multiple freight networks consisting of a large consortium of independent logistics companies worldwide. In addition to our network of partners for general cargo, we have access to key expertise in project cargo, perishables, pharma, time-critical and dangerous goods movement.</strong></p>', '<p>We are an active member of the following networks:</p><ul><li>WCA – Over 9,411 registered independent logistics companies in 194 countries</li><li>FIATA – Over 5,800 registered independent logistics companies in 150 countries</li></ul><p>With greater combined cargo volumes that eclipse even the largest multinational logistics companies, our membership provides us with strong global reach and local knowledge</p>', 'alt image text', 'alt image text', 'alt img caption', 'alt image description', 'location-page');

-- --------------------------------------------------------

--
-- Table structure for table `location_page_metatagslocation`
--

CREATE TABLE `location_page_metatagslocation` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `location_page_office`
--

CREATE TABLE `location_page_office` (
  `id` bigint NOT NULL,
  `place_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `office_address` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `fax` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `country_manager_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `designation` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `country_manager_phone1` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `country_manager_phone2` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `is_head_office` tinyint(1) NOT NULL,
  `office_url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `office_description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `location_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `services_metatagsservices`
--

CREATE TABLE `services_metatagsservices` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `services_specializedservice`
--

CREATE TABLE `services_specializedservice` (
  `id` bigint NOT NULL,
  `title` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `link` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `services_specializedsubservice`
--

CREATE TABLE `services_specializedsubservice` (
  `id` bigint NOT NULL,
  `header_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `header_title` longtext COLLATE utf8mb4_general_ci NOT NULL DEFAULT (_utf8mb3'1')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `services_subheading`
--

CREATE TABLE `services_subheading` (
  `id` bigint NOT NULL,
  `subheading` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `related_service_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `services_subservice`
--

CREATE TABLE `services_subservice` (
  `id` bigint NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `sub_title` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `related_heading_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `service_card_servicescard`
--

CREATE TABLE `service_card_servicescard` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(500) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service_card_servicescard`
--

INSERT INTO `service_card_servicescard` (`id`, `title`, `icon`, `description`) VALUES
(1, 'project cargo services', 'Services_Card/cargo.webp', '<p>specialized in project cargo handling complex and over sized shipments with precision,ensuring,succesfull execution</p>'),
(3, 'Custom Clearence', 'Services_Card/custom_1.webp', '<p>streamalined customos clearence for swift and complaint international trade,reducing dealy and ensuring smooth global trasaction</p>'),
(5, 'Specialized Services', 'Services_Card/special.webp', '<p>Offering specialized services tailord to meet your unique logistics needs,ensuring expectional solution for your business.</p>'),
(6, 'Road freight', 'Services_Card/road.webp', '<p>Road freight solutions offering reliable, on-time deliveries, leveraging our extensive network and expertise to optimize your ground transportation needs.</p>'),
(7, 'Ocean freight', 'Services_Card/sea.webp', '<p>Ocean freight solutions which ensure cost-effective, timely cargo transport, utilizing our global network and industry expertise for efficient ocean shipping.</p>'),
(8, 'Air freight', 'Services_Card/air_2.webp', '<p>Air freight services which provide rapid and dependable cargo transport, leveraging our extensive global network and industry know-how for efficient air shipping solutions.</p>'),
(9, 'Warehouse Distribution', 'Services_Card/warehouse_Rl6CHWQ.webp', '<p>Our streamlined solution ensure efficent storage and delivery, optimizing supply chain with timely and realible services</p>');

-- --------------------------------------------------------

--
-- Table structure for table `service_card_servicetitle`
--

CREATE TABLE `service_card_servicetitle` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service_card_servicetitle`
--

INSERT INTO `service_card_servicetitle` (`id`, `title`) VALUES
(1, '<p>Our Services</p>');

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_achievement`
--

CREATE TABLE `socialmedia_achievement` (
  `id` bigint NOT NULL,
  `achievements_icon` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `achievements_subtitle` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialmedia_achievement`
--

INSERT INTO `socialmedia_achievement` (`id`, `achievements_icon`, `achievements_subtitle`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`) VALUES
(1, 'achievements_icons/ACH.webp', '<h3><strong>Awarded Best Customs Clearance Company of 2021 &amp; 2022 by Oman Customs</strong></h3><p><br></p>', 'alt image text', 'alt img title', 'alt img caption', 'alt img description'),
(2, 'achievements_icons/AA.webp', '<h3><strong>15 Years of Excellence</strong></h3>', 'alt image text', 'alt img title', 'alt img caption', 'alt img description'),
(3, 'achievements_icons/PPP..webp', '<h3><strong>Honored with Smart Workplace 2022 Award by Dubai Customs</strong></h3>', 'alt image text', 'alt img title', 'alt img caption', 'alt image description');

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_achievementsection`
--

CREATE TABLE `socialmedia_achievementsection` (
  `id` bigint NOT NULL,
  `title` longtext COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialmedia_achievementsection`
--

INSERT INTO `socialmedia_achievementsection` (`id`, `title`) VALUES
(1, '<h1><strong>Achievements</strong></h1>');

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_highlightssection`
--

CREATE TABLE `socialmedia_highlightssection` (
  `id` bigint NOT NULL,
  `title` varchar(200) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialmedia_highlightssection`
--

INSERT INTO `socialmedia_highlightssection` (`id`, `title`) VALUES
(1, '<p>Highlights</p>');

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_homehighlights`
--

CREATE TABLE `socialmedia_homehighlights` (
  `id` bigint NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `sub_title` varchar(200) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialmedia_homehighlights`
--

INSERT INTO `socialmedia_homehighlights` (`id`, `icon`, `sub_title`) VALUES
(1, 'homehighlights/highlights-mark_1_7nzHzSp.webp', '<p>130+Employees</p>'),
(2, 'homehighlights/highlights-mark_2.webp', '<p>Average of 9000+ Custom Declarations Processed Per Month</p>'),
(3, 'homehighlights/highlights-mark_3.webp', '<p>10 Offices Accross Oman</p>'),
(4, 'homehighlights/highlights-mark_2_7r1oNPu.webp', '<p>Branch Offices in UAE,Qatar and  saudi Arabia</p>'),
(5, 'homehighlights/highlights-mark_2_15lOWQF.webp', '<p>24/7 Operations</p>'),
(6, 'homehighlights/highlights-mark_3_lXIGOXN.webp', '<p>ISO 9001:2015 Certified Company</p>'),
(7, 'homehighlights/highlights-mark_3_PToSCrR.webp', '<p>Registered Member of WCA and FIATA  Frieght  Network</p>');

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_industry`
--

CREATE TABLE `socialmedia_industry` (
  `id` bigint NOT NULL,
  `industry_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `industry_title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `industry_description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `slug` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_location`
--

CREATE TABLE `socialmedia_location` (
  `id` bigint NOT NULL,
  `place_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `short_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  `location_url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialmedia_location`
--

INSERT INTO `socialmedia_location` (`id`, `place_name`, `short_name`, `address`, `location_url`, `is_active`) VALUES
(1, 'Sulatanate of Oman', 'Oman', '<p>Alsi For Marine Services&nbsp;LLC</p><p>P.O. Box 608. P.C: 322.</p><p>W. Sohar, Sultanate Of OMAN.</p><p>Fax No: +968 2675 5550</p>', 'http://localhost:5173/our_network', 1),
(2, 'United Arab Emirates', 'Alsi For Marine Services LLC', '<p>Business Bay, Churchill Towers Suite 3409</p><p>P.O. Box: 392585, Dubai,&nbsp;UAE.</p>', 'http://localhost:5173/our_network', 1);

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_market`
--

CREATE TABLE `socialmedia_market` (
  `id` bigint NOT NULL,
  `market_image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `market_title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `slug` varchar(500) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialmedia_market`
--

INSERT INTO `socialmedia_market` (`id`, `market_image`, `alt_img_text`, `alt_img_title`, `alt_img_Caption`, `alt_img_description`, `market_title`, `slug`) VALUES
(1, 'market_images/market.webp', '', '', '', '', '<h1 class=\"ql-align-center\"><strong>Market Updates</strong></h1><p><br></p>', 'h1-classql-align-centerstrongmarket-updatesstrongh1pbrp');

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_markettitle`
--

CREATE TABLE `socialmedia_markettitle` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_metatagshome`
--

CREATE TABLE `socialmedia_metatagshome` (
  `id` bigint NOT NULL,
  `charset` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `viewport` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `keywords` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `author` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `robots` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `copyright` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `referrer` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_type` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_url` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_site_name` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `og_locale` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_card` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_site` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_title` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_description` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `twitter_image_alt` varchar(150) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_ournetworktitle`
--

CREATE TABLE `socialmedia_ournetworktitle` (
  `id` bigint NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `socialmedia_ournetworktitle`
--

INSERT INTO `socialmedia_ournetworktitle` (`id`, `title`) VALUES
(1, '<p><strong>Our Network</strong></p>');

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_service`
--

CREATE TABLE `socialmedia_service` (
  `id` bigint NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci,
  `is_active` tinyint(1) NOT NULL,
  `slug` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `is_specialized` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `socialmedia_socialmedia`
--

CREATE TABLE `socialmedia_socialmedia` (
  `id` bigint NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `link` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `icon` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `alt_img_text` longtext COLLATE utf8mb4_general_ci,
  `alt_img_title` longtext COLLATE utf8mb4_general_ci,
  `alt_img_Caption` longtext COLLATE utf8mb4_general_ci,
  `alt_img_description` longtext COLLATE utf8mb4_general_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aboutus_aboutpagesection`
--
ALTER TABLE `aboutus_aboutpagesection`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `aboutus_certificatetitle`
--
ALTER TABLE `aboutus_certificatetitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_certifications`
--
ALTER TABLE `aboutus_certifications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_metatagsabout`
--
ALTER TABLE `aboutus_metatagsabout`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_milestone`
--
ALTER TABLE `aboutus_milestone`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_milestonetitle`
--
ALTER TABLE `aboutus_milestonetitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_ourstory`
--
ALTER TABLE `aboutus_ourstory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_ourstorytitle`
--
ALTER TABLE `aboutus_ourstorytitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_ourteam`
--
ALTER TABLE `aboutus_ourteam`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `order_by` (`order_by`);

--
-- Indexes for table `aboutus_ourteamtitle`
--
ALTER TABLE `aboutus_ourteamtitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_whatweare`
--
ALTER TABLE `aboutus_whatweare`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aboutus_whatwearetitle`
--
ALTER TABLE `aboutus_whatwearetitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `blogs_blogpost`
--
ALTER TABLE `blogs_blogpost`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `blogs_metatagsblogs`
--
ALTER TABLE `blogs_metatagsblogs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `blogs_metatagsblogs_blog_post_id_a315a967_fk_blogs_blogpost_id` (`blog_post_id`);

--
-- Indexes for table `careers_careerpage`
--
ALTER TABLE `careers_careerpage`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `careers_careersubmission`
--
ALTER TABLE `careers_careersubmission`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `careers_metatagscareers`
--
ALTER TABLE `careers_metatagscareers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chooses_choosessection`
--
ALTER TABLE `chooses_choosessection`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contacts_contactform`
--
ALTER TABLE `contacts_contactform`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contacts_contactheader`
--
ALTER TABLE `contacts_contactheader`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `contacts_faq`
--
ALTER TABLE `contacts_faq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contacts_metatagscontacts`
--
ALTER TABLE `contacts_metatagscontacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contacts_section`
--
ALTER TABLE `contacts_section`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `footer_footer`
--
ALTER TABLE `footer_footer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `header_homeheader`
--
ALTER TABLE `header_homeheader`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `industry_cards_industrycard`
--
ALTER TABLE `industry_cards_industrycard`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `industry_cards_industrytitles`
--
ALTER TABLE `industry_cards_industrytitles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `industry_industriespage`
--
ALTER TABLE `industry_industriespage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `industry_metatagsindustries`
--
ALTER TABLE `industry_metatagsindustries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `key_key_diffrentiates`
--
ALTER TABLE `key_key_diffrentiates`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `key_key_diffrentiatessection`
--
ALTER TABLE `key_key_diffrentiatessection`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `location_page_location_page`
--
ALTER TABLE `location_page_location_page`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `location_page_metatagslocation`
--
ALTER TABLE `location_page_metatagslocation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `location_page_office`
--
ALTER TABLE `location_page_office`
  ADD PRIMARY KEY (`id`),
  ADD KEY `location_page_office_location_id_d9248f70_fk_socialmed` (`location_id`);

--
-- Indexes for table `services_metatagsservices`
--
ALTER TABLE `services_metatagsservices`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `services_specializedservice`
--
ALTER TABLE `services_specializedservice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `services_specializedsubservice`
--
ALTER TABLE `services_specializedsubservice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `services_subheading`
--
ALTER TABLE `services_subheading`
  ADD PRIMARY KEY (`id`),
  ADD KEY `services_subheading_related_service_id_a4969e15_fk_socialmed` (`related_service_id`);

--
-- Indexes for table `services_subservice`
--
ALTER TABLE `services_subservice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `services_subservice_related_heading_id_66ccf262_fk_services_` (`related_heading_id`);

--
-- Indexes for table `service_card_servicescard`
--
ALTER TABLE `service_card_servicescard`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `service_card_servicetitle`
--
ALTER TABLE `service_card_servicetitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_achievement`
--
ALTER TABLE `socialmedia_achievement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_achievementsection`
--
ALTER TABLE `socialmedia_achievementsection`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_highlightssection`
--
ALTER TABLE `socialmedia_highlightssection`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_homehighlights`
--
ALTER TABLE `socialmedia_homehighlights`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_industry`
--
ALTER TABLE `socialmedia_industry`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `socialmedia_location`
--
ALTER TABLE `socialmedia_location`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_market`
--
ALTER TABLE `socialmedia_market`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `socialmedia_markettitle`
--
ALTER TABLE `socialmedia_markettitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_metatagshome`
--
ALTER TABLE `socialmedia_metatagshome`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_ournetworktitle`
--
ALTER TABLE `socialmedia_ournetworktitle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socialmedia_service`
--
ALTER TABLE `socialmedia_service`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `socialmedia_socialmedia`
--
ALTER TABLE `socialmedia_socialmedia`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aboutus_aboutpagesection`
--
ALTER TABLE `aboutus_aboutpagesection`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `aboutus_certificatetitle`
--
ALTER TABLE `aboutus_certificatetitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_certifications`
--
ALTER TABLE `aboutus_certifications`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_metatagsabout`
--
ALTER TABLE `aboutus_metatagsabout`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_milestone`
--
ALTER TABLE `aboutus_milestone`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_milestonetitle`
--
ALTER TABLE `aboutus_milestonetitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_ourstory`
--
ALTER TABLE `aboutus_ourstory`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `aboutus_ourstorytitle`
--
ALTER TABLE `aboutus_ourstorytitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_ourteam`
--
ALTER TABLE `aboutus_ourteam`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_ourteamtitle`
--
ALTER TABLE `aboutus_ourteamtitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_whatweare`
--
ALTER TABLE `aboutus_whatweare`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `aboutus_whatwearetitle`
--
ALTER TABLE `aboutus_whatwearetitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=345;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `blogs_blogpost`
--
ALTER TABLE `blogs_blogpost`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `blogs_metatagsblogs`
--
ALTER TABLE `blogs_metatagsblogs`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `careers_careerpage`
--
ALTER TABLE `careers_careerpage`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `careers_careersubmission`
--
ALTER TABLE `careers_careersubmission`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `careers_metatagscareers`
--
ALTER TABLE `careers_metatagscareers`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chooses_choosessection`
--
ALTER TABLE `chooses_choosessection`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `contacts_contactform`
--
ALTER TABLE `contacts_contactform`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `contacts_contactheader`
--
ALTER TABLE `contacts_contactheader`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `contacts_faq`
--
ALTER TABLE `contacts_faq`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `contacts_metatagscontacts`
--
ALTER TABLE `contacts_metatagscontacts`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `contacts_section`
--
ALTER TABLE `contacts_section`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=87;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `footer_footer`
--
ALTER TABLE `footer_footer`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `header_homeheader`
--
ALTER TABLE `header_homeheader`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `industry_cards_industrycard`
--
ALTER TABLE `industry_cards_industrycard`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `industry_cards_industrytitles`
--
ALTER TABLE `industry_cards_industrytitles`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `industry_industriespage`
--
ALTER TABLE `industry_industriespage`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `industry_metatagsindustries`
--
ALTER TABLE `industry_metatagsindustries`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `key_key_diffrentiates`
--
ALTER TABLE `key_key_diffrentiates`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `key_key_diffrentiatessection`
--
ALTER TABLE `key_key_diffrentiatessection`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `location_page_location_page`
--
ALTER TABLE `location_page_location_page`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `location_page_metatagslocation`
--
ALTER TABLE `location_page_metatagslocation`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `location_page_office`
--
ALTER TABLE `location_page_office`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services_metatagsservices`
--
ALTER TABLE `services_metatagsservices`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services_specializedservice`
--
ALTER TABLE `services_specializedservice`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services_specializedsubservice`
--
ALTER TABLE `services_specializedsubservice`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services_subheading`
--
ALTER TABLE `services_subheading`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services_subservice`
--
ALTER TABLE `services_subservice`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `service_card_servicescard`
--
ALTER TABLE `service_card_servicescard`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `service_card_servicetitle`
--
ALTER TABLE `service_card_servicetitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialmedia_achievement`
--
ALTER TABLE `socialmedia_achievement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `socialmedia_achievementsection`
--
ALTER TABLE `socialmedia_achievementsection`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialmedia_highlightssection`
--
ALTER TABLE `socialmedia_highlightssection`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialmedia_homehighlights`
--
ALTER TABLE `socialmedia_homehighlights`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `socialmedia_industry`
--
ALTER TABLE `socialmedia_industry`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialmedia_location`
--
ALTER TABLE `socialmedia_location`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `socialmedia_market`
--
ALTER TABLE `socialmedia_market`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialmedia_markettitle`
--
ALTER TABLE `socialmedia_markettitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialmedia_metatagshome`
--
ALTER TABLE `socialmedia_metatagshome`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialmedia_ournetworktitle`
--
ALTER TABLE `socialmedia_ournetworktitle`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `socialmedia_service`
--
ALTER TABLE `socialmedia_service`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `socialmedia_socialmedia`
--
ALTER TABLE `socialmedia_socialmedia`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `blogs_metatagsblogs`
--
ALTER TABLE `blogs_metatagsblogs`
  ADD CONSTRAINT `blogs_metatagsblogs_blog_post_id_a315a967_fk_blogs_blogpost_id` FOREIGN KEY (`blog_post_id`) REFERENCES `blogs_blogpost` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `location_page_office`
--
ALTER TABLE `location_page_office`
  ADD CONSTRAINT `location_page_office_location_id_d9248f70_fk_socialmed` FOREIGN KEY (`location_id`) REFERENCES `socialmedia_location` (`id`);

--
-- Constraints for table `services_subheading`
--
ALTER TABLE `services_subheading`
  ADD CONSTRAINT `services_subheading_related_service_id_a4969e15_fk_socialmed` FOREIGN KEY (`related_service_id`) REFERENCES `socialmedia_service` (`id`);

--
-- Constraints for table `services_subservice`
--
ALTER TABLE `services_subservice`
  ADD CONSTRAINT `services_subservice_related_heading_id_66ccf262_fk_services_` FOREIGN KEY (`related_heading_id`) REFERENCES `services_subheading` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
