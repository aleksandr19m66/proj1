from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import xlsxwriter
import time
import subprocess

import requests
from bs4 import BeautifulSoup
from urllib import request

# Установка библиотеки pandas
try:
    subprocess.check_call(['pip', 'install', 'pandas'])
except subprocess.CalledProcessError as e:
   print(f"Ошибка при установке pandas: {e}")
   exit(1)

import pandas as pd

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('../../Expenses.xlsx')
worksheet = workbook.add_worksheet()
# Start from the first cell. Rows and columns are zero indexed.
expenses = (['Date',  'Teams1', 'Score', 'Teams2'])

row = 0
col = 0
for item in expenses:
    worksheet.write(row, col, item)
    col += 1

url = 'https://cyberscore.live/en/matches/?type=past'

# Путь к драйверу браузера
driver = webdriver.Edge()

driver.get(url)
sleep(6)
matches = driver.find_elements(By.CLASS_NAME, 'item')

def Convert(string):
    li = list(string.split('\n'))
    return li


for match in range(0, 20):
   row += 1
   col =0
   dd = Convert(matches[match].text)
   if dd[0] == 'Yesterday':
       dd[0] = time.strftime('%d/%m/%Y', time.gmtime())
   if dd[0] == 'Today':
       dd[0] = time.strftime('%d/%m/%Y')
   worksheet.write(row, col, dd[0])
   col += 1
   worksheet.write(row, col, dd[2])
   col += 1
   worksheet.write(row, col, dd[3])
   col += 1
   worksheet.write(row, col, dd[5])
   col += 1

workbook.close()

#Чтение из файла данных. Если парсить не удалось, то файл Expenses.xlsx можно заполнить с консоли
# Load the xlsx file
excel_data = pd.read_excel("file:///C:/Users/pyton/p1/pythonProject1/Expenses.xlsx")
# Read the values of the file in the dataframe
for item in range(8):
    data = pd.DataFrame(excel_data, columns=['Date',  'Teams1', 'Score', 'Teams2'])

##Print the content
print("The content of the file is:\n", data)


# Сортировка data по значению DATE
#data.sort(key=lambda it: it['DATE'], reverse=True)

# Генерация тегов строк таблицы
table = ''

for item in range(8):
    data = pd.DataFrame(excel_data, columns=['Date',  'Teams1', 'Score', 'Teams2'])

    for team in data:
        stat_html = f"""
        <div class="row z-index-common">
          <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_content">
                        <h3 class="team-card_title"><a href="#" class="text-inherit">{team["Teams1"]}</a></h3>
                    </div>
                </div>
          </div>
          <div class="col-md-6 col-xl-4">
                <div class="team-card">
                     <div class="team-card_content">
                        <span class="team-card_label">{team["Date"]}</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">{team["Score"]}</a></h3>
                    </div>
                </div>
          </div>
          <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_content">
                        <h3 class="team-card_title"><a href="#" class="text-inherit">{team["Teams2"]}</a></h3>
                    </div>
                </div>
          </div>
        </div> 
         """
    table += stat_html

print(table)


old = f"""
 <!doctype html>
<html class="no-js" lang="zxx">

<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Ancients League - Teams</title>
    <meta name="author" content="Angfuzsoft">
    <meta name="description" content="Ancients League - Teams">
    <meta name="keywords" content="Ancients League - Teams">
    <meta name="robots" content="INDEX,FOLLOW">

    <!-- Mobile Specific Metas -->
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Favicons - Place favicon.ico in the root directory -->
    <link sizes="57x57" rel="icon" href="assets/img/favicons/favicon.svg">

    <!--==============================
	  Google Fonts
	============================== -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="css2?family=Poppins:wght@300;400;600&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">


    <!--==============================
	    All CSS File
	============================== -->
    <!-- Bootstrap -->
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <!-- Fontawesome Icon -->
    <link rel="stylesheet" href="assets/css/fontawesome.min.css">
    <!-- Magnific Popup -->
    <link rel="stylesheet" href="assets/css/magnific-popup.min.css">
    <!-- Slick Slider -->
    <link rel="stylesheet" href="assets/css/slick.min.css">
    <!-- Theme Custom CSS -->
    <link rel="stylesheet" href="assets/css/style.css">

</head>

<body>


<!--[if lte IE 9]>
<p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade
    your browser</a> to improve your experience and security.</p>
<![endif]-->


<!--********************************
       Code Start From Here
******************************** -->

<!-- Custom Cursor  -->
<div class="vs-cursor"></div>


<!--==============================
 Preloader
==============================-->
<div class="preloader  ">
    <button class="vs-btn preloaderCls">Cancel Preloader</button>
    <div class="preloader-inner">
        <div class="vs-loadholder">
            <div class="vs-loader">
                <span class="loader-text">Loading</span>
            </div>
        </div>
    </div>
</div>
<!--==============================
Mobile Menu
============================== -->
<div class="vs-menu-wrapper">
    <div class="vs-menu-area text-center">
        <button class="vs-menu-toggle"><i class="fal fa-times"></i></button>
        <div class="mobile-logo">
            <a href="index.html"><img src="assets/img/logo.svg" class="logo-main" alt="Spiel"></a>
        </div>
        <div class="vs-mobile-menu">
            <ul>
                <li class="menu-item-has-children">
                    <a href="index.html">ГЛАВНАЯ</a>
                </li>
                <li class="menu-item-has-children">
                    <a href="team.html">КОМАНДЫ</a>
                </li>
                
                <!--<li class="menu-item-has-children">
                    <a href="tournament.html">РЕЗУЛЬТАТЫ</a>
                </li>-->
                <li class="menu-item-has-children">
                    <a href="statistic.html">СТАТИСТИКА</a>
                </li>
                <li class="menu-item-has-children">
                                            <a href="results.html">Результаты</a>
                                        </li>
            
            </ul>
        </div>
    </div>
</div>
<!--==============================
Popup Search Box
============================== -->
<div class="popup-search-box d-none d-lg-block  ">
    <button class="searchClose border-theme text-theme"><i class="fal fa-times"></i></button>
    <form action="#">
        <input type="text" class="border-theme" placeholder="What are you looking for">
        <button type="submit"><i class="fal fa-search"></i></button>
    </form>
</div>
<!--==============================
Sidemenu
============================== -->
<div class="sidemenu-wrapper d-none d-lg-block  ">
    <div class="sidemenu-content">
        <button class="closeButton sideMenuCls"><i class="far fa-times"></i></button>
        <div class="widget  ">
            <div class="vs-widget-about">
                <div class="footer-logo">
                    <a href="index.html"><img src="assets/img/logo.svg" alt="Spiel"></a></div>
                <p class="footer-about-text">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
                    dolore The League of Legends offseason is in full effect and teams are looking to sign new players
                    to strengthen their roster or to re current players.</p>
                <div class="multi-social">
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-pinterest-p"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i> </a>
                </div>
            </div>
        </div>
        <div class="widget  ">
            <h3 class="widget_title">Recent Articles</h3>
            <div class="recent-post-wrap">
                <div class="nav recent-post-tab" data-asnavfor="#recent-post-slide2">
                    <button class="nav-link active">Recent</button>
                    <button class="nav-link">Most Commented</button>
                    <button class="nav-link">Popular</button>
                </div>
                <div class="recent-post-slide vs-carousel" id="recent-post-slide2" data-fade="true" data-slide-show="1" data-md-slide-show="1" data-speed="800" data-adaptive-height="true" data-infinite="fasle">
                    <div class="slide">
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-1.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">Counter in
                                    global offensive</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>Dec 12, 2021</a>
                                </div>
                            </div>
                        </div>
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-2.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">Call of duty
                                    Balck Ops</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>Jun 08, 2021</a>
                                </div>
                            </div>
                        </div>
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-3.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">Until recently
                                    prevail</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>May 07, 2021</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="slide">
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-4.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">The placeholder
                                    beginn with</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>Apr 13, 2021</a>
                                </div>
                            </div>
                        </div>
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-5.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">Richard
                                    McClintock Latin!</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>Jan 05, 2021</a>
                                </div>
                            </div>
                        </div>
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-6.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">Counter strike
                                    global offensive</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>July 08, 2021</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="slide">
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-7.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">Lorem minim
                                    veniam nostrud</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>Mar 18, 2021</a>
                                </div>
                            </div>
                        </div>
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-8.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">From its
                                    medieval origins to the</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>Feb 22, 2021</a>
                                </div>
                            </div>
                        </div>
                        <div class="recent-post">
                            <div class="media-img">
                                <a href="blog-details.html"><img src="assets/img/blog/recent-post-1-9.jpg" alt="Blog Image"></a>
                            </div>
                            <div class="media-body">
                                <h4 class="post-title"><a class="text-inherit" href="blog-details.html">Latin derived
                                    from Cicero's 1st</a></h4>
                                <div class="recent-post-meta">
                                    <a href="blog.html"><i class="fal fa-user"></i>By Admin</a>
                                    <a href="blog.html"><i class="fal fa-calendar-alt"></i>Dec 15, 2021</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!--==============================
    Header Area
==============================-->
<header class="vs-header header-layout2">
    <div class="sticky-wrapper">
        <div class="sticky-active">
            <div class="header-menu-area">
                <div class="container">
                    <div class="row align-items-center justify-content-between">
                        <div class="col-auto">
                            <a href="index.html" class="header-logo">
                                <img src="assets/img/logo.svg" class="logo-main" alt="Logo">
                            </a>
                        </div>
                        <div class="col-auto">
                            <nav class="main-menu menu-style2 d-none d-lg-block">
                                <ul>
                                    <li class="menu-item-has-children">
                                        <a href="index.html">ГЛАВНАЯ</a>
                                    </li>
                                    <li class="menu-item-has-children">
                                        <a href="team.html">КОМАНДЫ</a>
                                    </li>
                                    
                                   <!-- <li>
                                        <a href="tournament.html">РЕЗУЛЬТАТЫ</a>
                                    </li>-->
                                    <li class="menu-item-has-children">
                                        <a href="statistic.html">СТАТИСТИКА</a>
                                    </li>
                                    <li class="menu-item-has-children">
                                            <a href="results.html">Результаты</a>
                                        </li>
                                
                                </ul>
                            </nav>
                            <button type="button" class="vs-menu-toggle d-inline-block d-lg-none"><i class="fas fa-bars"></i></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>
<!--==============================
Match Area
==============================-->
<section class="vs-match-wapper space-top-2 bg-title">
    <div class="container">
        <div class="row justify-content-between">
            <div class="col-auto">
                <div class="title-area">
                    <h2 class="sec-title text-white">ANCIENT LEAGUE - РЕЗУЛЬТАТЫ МАТЧЕЙ</h2>
                    <div class="sec-shape">
                        <div class="sec-shape_bar"></div>
                        <div class="sec-shape_bar"></div>
                        <div class="sec-shape_bar"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!--==============================
Team Area
==============================-->
<section class="vs-team-wrapper bg-title">
    <div class="container">
        <div class="row z-index-common">
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/crew-x.png" alt="Stream Logo" width="160px">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Беларусь</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Crew-X</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/Big%20Bang%20Gaming.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Беларусь</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Big Bang Gaming</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/Parallel-eSports.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Украина</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Parallel eSports</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/LBR.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Казахстан</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Lucky Bulldogs Rescue</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/Marvelous.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Украина</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Marvelous Warriors</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/fenix.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Fenix</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/dominatrix.jpg" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Украина</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">dominatrix</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/Ninja Bros.jpg" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Ninja Bros</a></h3>
                    </div>
                </div>
            </div>
              <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/BulletProofs.jpg" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Казахстан</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">BulletProofs</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/ThunderLab.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">ThunderLab</a></h3>
                    </div>
                </div>
            </div>
             <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/vs.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">04.04.2024</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">3-2</a></h3>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-xl-4">
                <div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/Lighting Legend.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">Lighting Legend</a></h3>
                    </div>
                </div>
                 
                
            <div class="col-md-6 col-xl-4">
                <!--<div class="team-card">
                    <div class="team-card_icon"><img src="assets/img/icon/team-stream-icon.png" alt="Icon shape"></div>
                    <div class="team-card_shape"></div>
                    <div class="team-card_logo">
                        <img src="assets/img/brand/SuperRare.png" alt="Stream Logo">
                    </div>
                    <div class="team-card_content">
                        <span class="team-card_label">Россия</span>
                        <h3 class="team-card_title"><a href="#" class="text-inherit">SuperRare</a></h3>
                    </div>
                </div>-->
            </div>
        </div>
    </div>
        </div>
</section>
<!--==============================
        Footer Area
==============================-->
<footer class="footer-wrapper footer-layout2 ">
    <div class="copyright-wrap text-center">
        <div class="container">
            <p>© Copyright 2023 | <a class="text-theme2" href="index.html">AMUSE MOBILE LEAGUE</a> | All rights reserved
            </p>
        </div>
    </div>
</footer>


<!--********************************
        Code End  Here
******************************** -->


<!-- Scroll To Top -->
<a href="#" class="scrollToTop scroll-btn"><i class="far fa-arrow-up"></i></a>


<!--==============================
    All Js File
============================== -->
<!-- Jquery -->
<script src="assets/js/vendor/jquery-3.6.0.min.js"></script>
<!-- Slick Slider -->
<script src="assets/js/slick.min.js"></script>
<!-- Bootstrap -->
<script src="assets/js/bootstrap.min.js"></script>
<!-- Smooth Scroll -->
<script src="assets/js/SmoothScroll.min.js"></script>
<!-- Parallax -->
<script src="assets/js/universal-parallax.min.js"></script>
<!-- Magnific Popup -->
<script src="assets/js/jquery.magnific-popup.min.js"></script>
<!-- Isotope Filter -->
<script src="assets/js/imagesloaded.pkgd.min.js"></script>
<script src="assets/js/isotope.pkgd.min.js"></script>
<!-- Custom Carousel -->
<script src="assets/js/vscustom-carousel.min.js"></script>
<!-- Form Js -->
<script src="assets/js/ajax-mail.js"></script>
<!-- Main Js File -->
<script src="assets/js/main.js"></script>

</body>

</html>
   
    """
#print(old)

# Перезапись statistic.html
with open('Result.html', 'w', encoding="utf-8") as file:
    file.write(old)

input("Для завершения нажмите Enter")



