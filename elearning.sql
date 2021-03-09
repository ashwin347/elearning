-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 09, 2021 at 08:13 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elearning`
--

-- --------------------------------------------------------

--
-- Table structure for table `chatrequests`
--

CREATE TABLE `chatrequests` (
  `id` int(11) NOT NULL,
  `studentid` int(20) NOT NULL,
  `faculityid` int(20) NOT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `chatrequests`
--

INSERT INTO `chatrequests` (`id`, `studentid`, `faculityid`, `status`) VALUES
(2, 1, 1, 'accepted'),
(3, 1, 1, 'rejected'),
(5, 4, 0, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `faculities`
--

CREATE TABLE `faculities` (
  `id` int(11) NOT NULL,
  `faculityname` varchar(20) NOT NULL,
  `department` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculities`
--

INSERT INTO `faculities` (`id`, `faculityname`, `department`, `email`, `password`) VALUES
(1, 'sabu', 'social', 'sabu@gmail.com', 'sabu');

-- --------------------------------------------------------

--
-- Table structure for table `filerequests`
--

CREATE TABLE `filerequests` (
  `id` int(11) NOT NULL,
  `fileid` int(11) NOT NULL,
  `studentid` int(11) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `filerequests`
--

INSERT INTO `filerequests` (`id`, `fileid`, `studentid`, `status`) VALUES
(1, 1, 4, 'pending'),
(11, 1, 4, 'accepted'),
(12, 4, 1, 'pending'),
(13, 4, 1, 'pending'),
(14, 1, 3, 'pending'),
(15, 5, 1, 'pending'),
(16, 5, 4, 'pending'),
(17, 2, 4, 'pending'),
(18, 4, 4, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `filename` varchar(20) NOT NULL,
  `fileinfo` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `filename`, `fileinfo`) VALUES
(1, 'botony', 'botony new notes'),
(2, 'chemistry', 'chemistry new notes'),
(4, 'physics', 'physics new notes'),
(5, 'Math', 'Math new notes');

-- --------------------------------------------------------

--
-- Table structure for table `queries`
--

CREATE TABLE `queries` (
  `id` int(11) NOT NULL,
  `studentid` int(20) NOT NULL,
  `querytopic` varchar(100) NOT NULL,
  `querydescription` varchar(100) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `repliedfaculityid` int(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `queries`
--

INSERT INTO `queries` (`id`, `studentid`, `querytopic`, `querydescription`, `status`, `repliedfaculityid`, `reply`) VALUES
(1, 4, 'arts ', 'asdf', 'replied', 1, 'asd');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `studentname` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `studentname`, `email`, `password`, `phone`) VALUES
(1, 'rojin', '', '', 0),
(2, 'ashwin', '', '', 0),
(3, 'neha', '', '', 0),
(4, 'ashwin', 'ash@gmail.com', 'ash', 1233);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `chatrequests`
--
ALTER TABLE `chatrequests`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `faculities`
--
ALTER TABLE `faculities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `filerequests`
--
ALTER TABLE `filerequests`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `queries`
--
ALTER TABLE `queries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chatrequests`
--
ALTER TABLE `chatrequests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `faculities`
--
ALTER TABLE `faculities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `filerequests`
--
ALTER TABLE `filerequests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `queries`
--
ALTER TABLE `queries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
