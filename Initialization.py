import pygame
import time
import random

# Initialize the mixer
pygame.mixer.init()

# Song dictionaries with multiple valid answers
Punjabi={
    r"D:\Music_guesser\songs\Prabh - 9_45 (Official Music Video) feat. Jay Trak(MP3_160K).mp3":["9 45","shubh"],
r"D:\Music_guesser\songs\Shubh - Be Mine (Official Audio)(MP3_160K).mp3":["shubh","be mine"],
r"D:\Music_guesser\songs\AP Dhillon - Old Money (Official Audio)(MP3_160K).mp3":["ap dhillon","ap dhilon","old money"],
r"D:\Music_guesser\songs\Dekhha Tenu _ Mr. _ Mrs. Mahi _ Rajkummar Rao_ Janhvi Kapoor _ Mohd. Faiz _ Jaani _ Aadesh S_ Sameer(MP3_160K).mp3":["mr and mrs mahi","dekha tenu"],
r"D:\Music_guesser\songs\Shubh - Dior (Official Music Video)(MP3_160K).mp3":[],
r"D:\Music_guesser\songs\Aam Jahe Munde _ Parmish Verma feat Pardhaan _ Desi Crew _ Laddi Chahal(MP3_160K).mp3":["aam jahe munde","parmish verma"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ Lalkaara (Video) Feat. Sultaan _ GHOST _ Intense_ Raj Ranjodh(MP3_160K).mp3":["diljit","diljit dosanjh","lalkaara","lalkara"],
r"D:\Music_guesser\songs\Obsessed - Riar Saab_ _AbhijaySharma _ Official Music Video(MP3_160K).mp3":["obsessed","riar saab"],
r"D:\Music_guesser\songs\AMRIT MAAN - JOURNEY (Official Video) _ Mxrci _ Latest Punjabi Song 2023 _ New Punjabi Song 2024(MP3_160K).mp3":["journey","amrit maan"],
r"D:\Music_guesser\songs\Diljit Dosanjh _Lemonade_ (Visualiser) _ Drive Thru(MP3_160K).mp3":["diljit","diljit dosanjh","lemonade"],
r"D:\Music_guesser\songs\Rubicon Drill _ Laddi Chahal (Official Video) _ Parmish Verma _ Gurlez Akhtar _ EP - Forever(MP3_160K).mp3":["parmish verma","rubicon drill"],
r"D:\Music_guesser\songs\Parmish Verma Ft. Paradox - Check It Out (Official Music Video)(MP3_160K).mp3":["parmish verma","rubicon drill"],
r"D:\Music_guesser\songs\DAKU _ INDERPAL MOGA _ CHANI NATTAN _ NEW PUNJABI SONG _ LATEST PUNJABI SONG 2022 _Daku Ik number da(MP3_160K).mp3":["daku","indarpal moga"],
r"D:\Music_guesser\songs\Shubh - Cheques (Official Music Video)(MP3_160K).mp3":["shubh","cheques","cheque"],
r"D:\Music_guesser\songs\White Brown Black - Avvy Sra _ Karan Aujla _ Jaani _ Amanninder Singh _ Desi Melodies(MP3_160K).mp3":["white brown black","karan aujla"],
r"D:\Music_guesser\songs\SOFTLY (Official Music Video) KARAN AUJLA _ IKKY _ LATEST PUNJABI SONGS 2023(MP3_160K).mp3":["softly","karan aujla"],
r"D:\Music_guesser\songs\Ve Haaniyaan - Official Video _ Ravi Dubey _ Sargun Mehta _ Danny _ Avvy Sra _ Dreamiyata Music(MP3_160K).mp3":["ve haaniya"],
r"D:\Music_guesser\songs\Mi Amor(MP3_160K).mp3":["mi amor"],
r"D:\Music_guesser\songs\Shubh - King Shit (Official Audio)(MP3_160K).mp3":["shubh","king shit"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ Kinni Kinni (Official Audio) GHOST _ Thiarajxtt_ Raj Ranjodh(MP3_160K).mp3":["diljith","diljith dosanj","kinni kinni"],
r"D:\Music_guesser\songs\FOREVER - TEGI PANNU _ TANU GREWAL _ MANNI SANDHU _ PREM LATA (OFFICIAL MUSIC VIDEO)(MP3_160K).mp3":["forever","tegi panu"],
r"D:\Music_guesser\songs\SNAP (Official Music Video) Cheema Y _ Gurlez Akhtar _ Gur Sidhu _ New Punjabi Song(MP3_160K).mp3":["snap","gur sandhu"],
r"D:\Music_guesser\songs\MIRA - Love Again (Lyric Video)(MP3_160K).mp3":["mira","love again"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ Born To Shine (Official Music Video) G.O.A.T(MP3_160K).mp3":["diljith","diljith dosanjh","born to shine"],
r"D:\Music_guesser\songs\IDK HOW (MUSIC VIDEO) KARAN AUJLA  _ FOUR ME EP  _ LATEST PUNJABI SONGS 2024(MP3_160K).mp3":["i dont know","idk how","i dont know how","karan aujla"],
r"D:\Music_guesser\songs\Shubh - Bandana (Official Music Video)(MP3_160K).mp3":["bandana","shubh"],
r"D:\Music_guesser\songs\8 ASLE - SUKHA _ GURLEZ AKHTAR _ CHANI NATTAN _ PRODGK(MP3_160K).mp3":["8 asle","sukha"],
r"D:\Music_guesser\songs\Shubh - MVP (Official Music Video)(MP3_160K).mp3":["shubh","mvp"],
r"D:\Music_guesser\songs\Badshah X Karan Aujla - God Damn (Official Video) _ Hiten _ Ek THA RAJA(MP3_160K).mp3":["god damn","karan aujla","baadshah"],
r"D:\Music_guesser\songs\True Stories -  AP Dhillon _ Shinda Kahlon (Official Music Video)(MP3_160K).mp3":["true stories","ap","ap dhillon","ap dhilon"],
r"D:\Music_guesser\songs\Tauba Tauba _ Bad Newz _ Vicky Kaushal _ Triptii Dimri _ Karan Aujla(MP3_160K).mp3":["tauba tauba","bad newz","karan aujla"],
r"D:\Music_guesser\songs\SUNIYAN SUNIYAN (Official Video) Juss x MixSingh(MP3_160K).mp3":["suniyan suniyan","suniyan","juss"],
r"D:\Music_guesser\songs\Ambarsaria _ Navaan Sandhu _ HomeBoy _ Kaater _ Lavish Dhiman _ New Punjabi songs 2024(MP3_160K).mp3":["ambarsariyan","ambarsariya","ambarsaria","navaan sandhu"],
r"D:\Music_guesser\songs\That Girl (Official Video) _ Amrinder Gill _ Dr Zeus _ Raj Ranjodh _ Judaa 3 _ Chapter 2(MP3_160K).mp3":["that girl","judwaa 3","amrinder gill","amrindar gill"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ CASE (Official Video) GHOST(MP3_160K).mp3":["diljith","diljith dosanjh","case"],
r"D:\Music_guesser\songs\CALIFORNIA LOVE (Official Video) Cheema Y _ Gur Sidhu _ Punjabi Song 2023(MP3_160K).mp3":["california","california love","gur sindhu"],
r"D:\Music_guesser\songs\AP Dhillon - 315 (feat. Shinda Kahlon _ Jazzy B) (Official Audio)(MP3_160K).mp3":["315","ap dhillon","ap","ap dhilon"],
r"D:\Music_guesser\songs\Ek Daur x Mansoor _ Official Music Video(MP3_160K).mp3":["ek daur","mansoor"],
r"D:\Music_guesser\songs\Winning Speech (Music Video) Karan Aujla _ Mxrci _ Latest Punjabi Songs 2024(MP3_160K).mp3":["winning speech","karan aujla","karan"],
}
Hindi = {
    r"D:\Music_guesser\songs\[Songs.PK] Kick - 13 - Tu Hi Tu (House Mix).mp3":["kick","tu hi tu"],
    r"D:\Music_guesser\songs\01 Baarish - Half Girlfriend (Ash King) 190Kbps(1).mp3": ["baarish","hal girlfriend"],
    r"D:\Music_guesser\songs\01 Ban Ja Rani - Tumhari Sulu (Guru) 320Kbps.mp3":["ban ja tu meri rani","tumhari sulu"],
    r"D:\Music_guesser\songs\01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3":["chalti hai kya 9 se 12","judwaa 2"],
    r"D:\Music_guesser\songs\01 Ik Vaari Aa - Raabta (Arijit Singh) 190Kbps.mp3":["ik vaari aa","raabta","arijith","arijith singh","arijit","arijiit"],
    r"D:\Music_guesser\songs\01 Ok Jaanu - Title Song (AR Rehman) 190Kbps.mp3":["ok jaanu"],
    r"D:\Music_guesser\songs\02 Darkhaast - Shivaay (Arijit Singh) 190Kbps-1.mp3":["darkhaast","shivaay","arijith","arijith singh","arijit","arijiit"],
    r"D:\Music_guesser\songs\02 Raabta - Title Song (Arijit Singh) 190Kbps.mp3":["raabta","arijith","arijith singh","arijit","arijiit"],
    r"D:\Music_guesser\songs\01. Oh Girl You're Mine.mp3":["o girl you are mine","housefull"],
    r"D:\Music_guesser\songs\Anuv Jain - HUSN (Official Video)(MP3_160K).mp3":["anuv jain","husn"], 
r"D:\Music_guesser\songs\BAARISHEIN (Studio) Anuv Jain(MP3_160K).mp3":["baarishein","anuv jain","baarisheen"],
r"D:\Music_guesser\songs\Dil Haareya _ Arijit Singh _ Tanya Maniktala _ Danesh Razvi _ Vivian Richard _ JUNO _ Dharma 2.0(MP3_160K).mp3":["dil hareya","dil haareya","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Humdard Full Video Song _ Ek Villain _ Arijit Singh _ Mithoon(MP3_160K).mp3":["ek villain","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Dil Meri Na Sune Lyrical - Genius _ Utkarsh Sharma_ Ishita _ Atif Aslam _ Himesh Reshammiya(MP3_160K).mp3":["dil meri na sune","genius","atif aslam","atif","himesh reshamiya"],
r"D:\Music_guesser\songs\Full Song_ KHAIRIYAT (BONUS TRACK) _ CHHICHHORE _ Sushant_ Shraddha _ Pritam_ Amitabh B_Arijit Singh(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","khairiyat","chicchore"],
r"D:\Music_guesser\songs\Mann Jogiya _ Official Song _ Arijit Singh_Ishita Vishwakarma _ Anique _ Dheeraj _ Pyaar Hai Toh Hai(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","pyaar hai to hai","mann jogiya"],
r"D:\Music_guesser\songs\Tera Fitoor Lyrical - Genius _ Utkarsh Sharma_ Ishita Chauhan _ Arijit Singh _ Himesh Reshammiya(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","tera fitoor","genius"],
r"D:\Music_guesser\songs\Dunki_ O Maahi (Full Video) _ Shah Rukh Khan _ Taapsee Pannu _ Pritam _ Arijit Singh _ Irshad Kamil(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","dunki","oo mahi"],
r"D:\Music_guesser\songs\LO MAAN LIYA Full Video Song _ Raaz Reboot _ Arijit Singh_Emraan Hashmi_Kriti Kharbanda_Gaurav Arora(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","lo maan liya"],
r"D:\Music_guesser\songs\Lyrical_ Thodi Jagah Video _ Riteish D_ Sidharth M_ Tara S _ Arijit Singh _ Tanishk Bagchi(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","thodi jagah"],
r"D:\Music_guesser\songs\Saanson Ko - 4K Music Video _ ZiD _ Mannara_ Karanvir _ Arijit Singh _ Sharib Toshi _ Romantic Hits(MP3_160K).mp3":["saanson ko","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Ve Kamleya _ Rocky Aur Rani Kii Prem Kahaani _ Ranveer _ Alia _ Pritam _ Amitabh _ Arijit _ Shreya(MP3_160K).mp3":["ve kamleya","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Ae Dil Hai Mushkil - 4k Music Video _ Ranbir Kapoor _ Anushka Sharma _ Aishwarya Rai Bachchan(MP3_160K).mp3":["ae dil hai mushkil"],
r"D:\Music_guesser\songs\Raataan Lambiyan - Lyric Video _Shershaah_Sidharth_ Kiara_Tanishk B._Jubin_Asees(MP3_160K).mp3":["sheershah","raataan lambiyan","jubin nautiyal","jubin"],
r"D:\Music_guesser\songs\Zaalima _ Raees _ Shah Rukh Khan _ Mahira Khan _ Arijit Singh _ Harshdeep Kaur _ JAM8 _ Pritam(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","zaalima","raaes"],
r"D:\Music_guesser\songs\Apna Bana Le - Bhediya _ Varun Dhawan_ Kriti Sanon_ Sachin-Jigar_ Arijit Singh_ Amitabh Bhattacharya(MP3_160K).mp3":["apna bana le","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Kesariya - Film Version _ Brahmāstra _ Ranbir _ Alia _ Pritam _ Arijit _ Amitabh(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","brahmastra","kesariya"],
r"D:\Music_guesser\songs\Khamoshiyan (Title Song) Lyrics _ Arijit Singh _ Rashmi S _ Jeet G _ Ali Fazal _ Sapna P _ Gurmeet C(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","khamoshiyan"],
r"D:\Music_guesser\songs\Phir Bhi Tumko Chaahunga - Full Song _ Arijit Singh _ Arjun K _ Shraddha K _ Mithoon_ Manoj M(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","mai phir bhi tumko chahunga","half girlfriend"],
r"D:\Music_guesser\songs\Tere Hawaale (Full Video) Laal Singh Chaddha _ Aamir_Kareena _ Arijit_Shilpa _ Pritam_Amitabh_Advait(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","tere hawaale","laal singh chaddha"],
r"D:\Music_guesser\songs\Chahun Main Ya Naa Full Video Song Aashiqui 2 _ Aditya Roy Kapur_ Shraddha Kapoor(MP3_160K).mp3":["Chahun Main Ya Naa","aashique 2","aashiqui 2","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Humsafar (Full Video)  _ Varun _ Alia Bhatt _ Akhil Sachdeva _ _Badrinath Ki Dulhania_(MP3_160K).mp3":["Badrinath Ki Dulhania","akhil","humsafar"],
r"D:\Music_guesser\songs\Main Rang Sharbaton Ka _ Arijit Singh _ Phata Poster Nikhla Hero _ 2013(MP3_160K).mp3":["Phata Poster Nikhla Hero","Main Rang Sharbaton Ka","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\O Bedardeya (Film Version) Tu Jhoothi Main Makkaar _ Ranbir_ Shraddha _ Pritam_ Arijit S_ Amitabh B(MP3_160K).mp3":["o bedardeya","arijith","arijith singh","arijit","arijiit","tu jhuthi mai makkar"],
r"D:\Music_guesser\songs\Aaj Se Teri - Lyrical _ Padman _ Akshay Kumar _ Radhika Apte _ Arijit Singh _ Amit Trivedi(MP3_160K).mp3":["aaj se teri","padman","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Rabba Janda - Full Video _ Mission Majnu _ Sidharth Malhotra_ Rashmika _ Jubin N_ Tanishk B_ Shabbir(MP3_160K).mp3":["rabba janda","jubin nautiyal","jubin"],
r"D:\Music_guesser\songs\Sajni (Song)_ Arijit Singh_ Ram Sampath _ Laapataa Ladies _  Aamir Khan Productions(MP3_160K).mp3":["sajni","laapata ladies","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Tere Vaaste _ Zara Hatke Zara Bachke _ Vicky Kaushal_ Sara Ali Khan_ Varun J_ Sachin-Jigar_Amitabh B(MP3_160K).mp3":["Zara Hatke Zara Bachke","varun jain","tere vaaste"],
r"D:\Music_guesser\songs\Aaj Ki Raat _ Stree 2 _ Tamannaah Bhatia _ Sachin-Jigar _ Madhubanti _ Divya _ Amitabh(MP3_160K).mp3":["aaj ki raat","stree 2","madhubanti"],
r"D:\Music_guesser\songs\ANIMAL_ SATRANGA(Song) Ranbir Kapoor_Rashmika_Sandeep V_Arijit_Shreyas P_Siddharth-Garima _Bhushan K(MP3_160K).mp3":["satranga","animal","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Illuminati_Aavesham_Jithu Madhavan_Fahadh Faasil_Sushin Shyam_Dabzee_Vinayak_ Nazriya_Anwar Rasheed(MP3_160K).mp3":["illuminati"],
r"D:\Music_guesser\songs\JAWAN_ Chaleya (Hindi) _ Shah Rukh Khan _ Nayanthara _ Atlee _ Anirudh _ Arijit S_ Shilpa R _ Kumaar(MP3_160K).mp3":["jawan","jawaan","chaleya","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Naina _ Crew _ Diljit Dosanjh_ Ft. Badshah _ Tabu_ Kareena Kapoor Khan_ Kriti Sanon _ Raj Ranjodh(MP3_160K).mp3":["naina","baadshah","crew","diljith","diljith dosanj"],
r"D:\Music_guesser\songs\Darin - I Lost You (Lyric Video)(MP3_160K).mp3":["darin","i lost you"],
r"D:\Music_guesser\songs\Full Video_ Samayama Song _ Hi Nanna _ Nani_Mrunal Thakur _ Shouryuv _ Hesham Abdul Wahab(MP3_160K).mp3":["samayama"],
r"D:\Music_guesser\songs\Paon Ki Jutti - Jyoti Nooran _ Isha Malviya _ Shiv Panditt _ Jaani _ Arvvindr S Khaira _ Bunny(MP3_160K).mp3":["paon ki jutti"],
r"D:\Music_guesser\songs\Teri Baaton Mein Aisa Uljha Jiya (Title Track)_ Shahid Kapoor_ Kriti Sanon _ Raghav_Tanishk_ Asees(MP3_160K).mp3":["teri baaton mein aisa jo uljha jiya"],
r"D:\Music_guesser\songs\Tum Se (Song)_ Shahid Kapoor_ Kriti Sanon _ Sachin-Jigar_ Raghav Chaitanya_ Varun Jain_ Indraneel(MP3_160K).mp3":["tum se","teri baaton mein aisa jo uljha jiya"],
r"D:\Music_guesser\songs\Aayi Nai -Stree 2 _ Shraddha Kapoor _ Rajkummar Rao _ Sachin-Jigar _Pawan Singh_Simran_Divya_Amitabh(MP3_160K).mp3":["aayi nai","pawan singh","stree 2"],
r"D:\Music_guesser\songs\Akhiyaan Gulaab (Song)_ Shahid Kapoor_ Kriti Sanon _ Mitraz _ Teri Baaton Mein Aisa Uljha Jiya(MP3_160K).mp3":["Teri Baaton Mein Aisa Uljha Jiya","mitraaz","akhiyan gulaab"],
r"D:\Music_guesser\songs\ANIMAL_ HUA MAIN (Lyrical Video) _ Ranbir Kapoor_Rashmika M _ Sandeep V _ Raghav_Manoj M _ Bhushan K(MP3_160K).mp3":["hua main","sandeep vanga"],
r"D:\Music_guesser\songs\CHUMMA _ Vicky Vidya Ka Woh Wala Video _ Rajkummar R_ Triptii D_ Pawan Singh _ Sachin-Jigar_ Vayu(MP3_160K).mp3":[" Vicky Vidya Ka Woh Wala Video","pawann singh","chumma"],
r"D:\Music_guesser\songs\Nora Fatehi - Im Bossy [Official Music Video](MP3_160K).mp3":["i am bossy"],
r"D:\Music_guesser\songs\ANIMAL_ ARJAN VAILLY _ Ranbir Kapoor _ Sandeep Vanga _ Bhupinder B_ Manan B _ Bhushan K(MP3_160K).mp3":["arjan vailly","arjan velly","sandeep vanga","animal"],
r"D:\Music_guesser\songs\ANIMAL_SAARI DUNIYA JALAA DENGE(Audio)_Ranbir K_Rashmika_Anil_Bobby_Sandeep_B Praak_Jaani_Bhushan K(MP3_160K).mp3":["animal","saari duniya jala denge","b praak"],
r"D:\Music_guesser\songs\Emma - Daydream (Official Audio)(MP3_160K).mp3":["emma","daydream"],
r"D:\Music_guesser\songs\JAWAN_ Not Ramaiya Vastavaiya _ Shah Rukh Khan _ Atlee _ Anirudh _ Nayanthara _ Vishal D _ Shilpa R(MP3_160K).mp3":["not ramaiya vasta vaiya","vishal","jawan","jawaan","anirudh"],
r"D:\Music_guesser\songs\What Jhumka_ _ Rocky Aur Rani Kii Prem Kahaani _ Ranveer _ Alia _ Pritam _ Amitabh _ Arijit _ Jonita(MP3_160K).mp3":["rocky aur rani ki prem kahani","what jhumka","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Ammy Virk_ Main Suneya Video Song Feat. Simran Hundal_ Rohaan _SunnyV_ Raj _Navjit B _ Bhushan Kumar(MP3_160K).mp3":["ammy virk","main suneya"],
r"D:\Music_guesser\songs\FIGHTER_ Ishq Jaisa Kuch Song_ Hrithik_ Deepika_ Vishal-Sheykhar_ Shilpa_ Kumaar_ Bosco-Caesar(MP3_160K).mp3":["fighter","ishq jaisa kuch","vishal","vishal mishra"],
r"D:\Music_guesser\songs\Heeriye (Official Video) Jasleen Royal ft Arijit Singh_ Dulquer Salmaan_ Aditya Sharma _Taani Tanvir(MP3_160K).mp3":["heeriye","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Tere Naal Video Song _ Tulsi Kumar_ Darshan Raval _ Gurpreet Saini_ Gautam G Sharma _ Bhushan Kumar(MP3_160K).mp3":["tere naal","darshan raval"],
r"D:\Music_guesser\songs\Tiger Shroff _ I Am A Disco Dancer 2.0 _ Benny Dayal _Salim Sulaiman _ Bosco _ Official Music Video(MP3_160K).mp3":["i am a disco dancer"],
r"D:\Music_guesser\songs\FILHALL _ Akshay Kumar Ft Nupur Sanon _ BPraak _ Jaani _ Arvindr Khaira _ Ammy Virk _ DESI MELODIES(MP3_160K).mp3":["b praak","filhaal"],
r"D:\Music_guesser\songs\Mere Angne Mein _ Jacqueline F_ Asim Riaz _ Neha K_ Raja H_ Tanishk B _ Radhika - Vinay _ Bhushan K(MP3_160K).mp3":["mere angne mei"],
r"D:\Music_guesser\songs\Shayad - Love Aaj Kal _ Kartik _ Sara _ Arushi _ Pritam _ Arijit Singh(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","shayad","love aajkal"],
r"D:\Music_guesser\songs\Tum Hi Aana Full Video _ Marjaavaan _ Riteish D_ Sidharth M_ Tara S _ Jubin N _ Payal Dev Kunaal V(MP3_160K).mp3":["tum hi aana","marjaawan","marjaavan","jubin nautiyal"],
r"D:\Music_guesser\songs\Ishq Official Lyrical Video I Amir Ameer _ Faheem Abdullah _ Rauhan Malik I Love Song 2024(MP3_160K).mp3":["ishq"],
r"D:\Music_guesser\songs\Anuv Jain - JO TUM MERE HO (Official Video)(MP3_160K).mp3":["anuv jain","jo tum mere ho"],
 r"D:\Music_guesser\songs\Prabh - 9_45 (Official Music Video) feat. Jay Trak(MP3_160K).mp3":["9 45","shubh"],
r"D:\Music_guesser\songs\Shubh - Be Mine (Official Audio)(MP3_160K).mp3":["shubh","be mine"],
r"D:\Music_guesser\songs\AP Dhillon - Old Money (Official Audio)(MP3_160K).mp3":["ap dhillon","ap dhilon","old money"],
r"D:\Music_guesser\songs\Dekhha Tenu _ Mr. _ Mrs. Mahi _ Rajkummar Rao_ Janhvi Kapoor _ Mohd. Faiz _ Jaani _ Aadesh S_ Sameer(MP3_160K).mp3":["mr and mrs mahi","dekha tenu"],
r"D:\Music_guesser\songs\Shubh - Dior (Official Music Video)(MP3_160K).mp3":[],
r"D:\Music_guesser\songs\Aam Jahe Munde _ Parmish Verma feat Pardhaan _ Desi Crew _ Laddi Chahal(MP3_160K).mp3":["aam jahe munde","parmish verma"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ Lalkaara (Video) Feat. Sultaan _ GHOST _ Intense_ Raj Ranjodh(MP3_160K).mp3":["diljit","diljit dosanjh","lalkaara","lalkara"],
r"D:\Music_guesser\songs\Obsessed - Riar Saab_ _AbhijaySharma _ Official Music Video(MP3_160K).mp3":["obsessed","riar saab"],
r"D:\Music_guesser\songs\AMRIT MAAN - JOURNEY (Official Video) _ Mxrci _ Latest Punjabi Song 2023 _ New Punjabi Song 2024(MP3_160K).mp3":["journey","amrit maan"],
r"D:\Music_guesser\songs\Diljit Dosanjh _Lemonade_ (Visualiser) _ Drive Thru(MP3_160K).mp3":["diljit","diljit dosanjh","lemonade"],
r"D:\Music_guesser\songs\Rubicon Drill _ Laddi Chahal (Official Video) _ Parmish Verma _ Gurlez Akhtar _ EP - Forever(MP3_160K).mp3":["parmish verma","rubicon drill"],
r"D:\Music_guesser\songs\Parmish Verma Ft. Paradox - Check It Out (Official Music Video)(MP3_160K).mp3":["parmish verma","rubicon drill"],
r"D:\Music_guesser\songs\DAKU _ INDERPAL MOGA _ CHANI NATTAN _ NEW PUNJABI SONG _ LATEST PUNJABI SONG 2022 _Daku Ik number da(MP3_160K).mp3":["daku","indarpal moga"],
r"D:\Music_guesser\songs\Shubh - Cheques (Official Music Video)(MP3_160K).mp3":["shubh","cheques","cheque"],
r"D:\Music_guesser\songs\White Brown Black - Avvy Sra _ Karan Aujla _ Jaani _ Amanninder Singh _ Desi Melodies(MP3_160K).mp3":["white brown black","karan aujla"],
r"D:\Music_guesser\songs\SOFTLY (Official Music Video) KARAN AUJLA _ IKKY _ LATEST PUNJABI SONGS 2023(MP3_160K).mp3":["softly","karan aujla"],
r"D:\Music_guesser\songs\Ve Haaniyaan - Official Video _ Ravi Dubey _ Sargun Mehta _ Danny _ Avvy Sra _ Dreamiyata Music(MP3_160K).mp3":["ve haaniya"],
r"D:\Music_guesser\songs\Mi Amor(MP3_160K).mp3":["mi amor"],
r"D:\Music_guesser\songs\Shubh - King Shit (Official Audio)(MP3_160K).mp3":["shubh","king shit"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ Kinni Kinni (Official Audio) GHOST _ Thiarajxtt_ Raj Ranjodh(MP3_160K).mp3":["diljith","diljith dosanj","kinni kinni"],
r"D:\Music_guesser\songs\FOREVER - TEGI PANNU _ TANU GREWAL _ MANNI SANDHU _ PREM LATA (OFFICIAL MUSIC VIDEO)(MP3_160K).mp3":["forever","tegi panu"],
r"D:\Music_guesser\songs\SNAP (Official Music Video) Cheema Y _ Gurlez Akhtar _ Gur Sidhu _ New Punjabi Song(MP3_160K).mp3":["snap","gur sandhu"],
r"D:\Music_guesser\songs\MIRA - Love Again (Lyric Video)(MP3_160K).mp3":["mira","love again"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ Born To Shine (Official Music Video) G.O.A.T(MP3_160K).mp3":["diljith","diljith dosanjh","born to shine"],
r"D:\Music_guesser\songs\IDK HOW (MUSIC VIDEO) KARAN AUJLA  _ FOUR ME EP  _ LATEST PUNJABI SONGS 2024(MP3_160K).mp3":["i dont know","idk how","i dont know how","karan aujla"],
r"D:\Music_guesser\songs\Shubh - Bandana (Official Music Video)(MP3_160K).mp3":["bandana","shubh"],
r"D:\Music_guesser\songs\8 ASLE - SUKHA _ GURLEZ AKHTAR _ CHANI NATTAN _ PRODGK(MP3_160K).mp3":["8 asle","sukha"],
r"D:\Music_guesser\songs\Shubh - MVP (Official Music Video)(MP3_160K).mp3":["shubh","mvp"],
r"D:\Music_guesser\songs\Badshah X Karan Aujla - God Damn (Official Video) _ Hiten _ Ek THA RAJA(MP3_160K).mp3":["god damn","karan aujla","baadshah"],
r"D:\Music_guesser\songs\True Stories -  AP Dhillon _ Shinda Kahlon (Official Music Video)(MP3_160K).mp3":["true stories","ap","ap dhillon","ap dhilon"],
r"D:\Music_guesser\songs\Tauba Tauba _ Bad Newz _ Vicky Kaushal _ Triptii Dimri _ Karan Aujla(MP3_160K).mp3":["tauba tauba","bad newz","karan aujla"],
r"D:\Music_guesser\songs\SUNIYAN SUNIYAN (Official Video) Juss x MixSingh(MP3_160K).mp3":["suniyan suniyan","suniyan","juss"],
r"D:\Music_guesser\songs\Ambarsaria _ Navaan Sandhu _ HomeBoy _ Kaater _ Lavish Dhiman _ New Punjabi songs 2024(MP3_160K).mp3":["ambarsariyan","ambarsariya","ambarsaria","navaan sandhu"],
r"D:\Music_guesser\songs\That Girl (Official Video) _ Amrinder Gill _ Dr Zeus _ Raj Ranjodh _ Judaa 3 _ Chapter 2(MP3_160K).mp3":["that girl","judwaa 3","amrinder gill","amrindar gill"],
r"D:\Music_guesser\songs\Diljit Dosanjh_ CASE (Official Video) GHOST(MP3_160K).mp3":["diljith","diljith dosanjh","case"],
r"D:\Music_guesser\songs\CALIFORNIA LOVE (Official Video) Cheema Y _ Gur Sidhu _ Punjabi Song 2023(MP3_160K).mp3":["california","california love","gur sindhu"],
r"D:\Music_guesser\songs\AP Dhillon - 315 (feat. Shinda Kahlon _ Jazzy B) (Official Audio)(MP3_160K).mp3":["315","ap dhillon","ap","ap dhilon"],
r"D:\Music_guesser\songs\Ek Daur x Mansoor _ Official Music Video(MP3_160K).mp3":["ek daur","mansoor"],
r"D:\Music_guesser\songs\Winning Speech (Music Video) Karan Aujla _ Mxrci _ Latest Punjabi Songs 2024(MP3_160K).mp3":["winning speech","karan aujla","karan"],
}

mixed= {
    
     r"songs/WhatsApp Audio 2024-12-07 at 19.37.21_7cea9fce.mp3":["faded"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.22_66de4d6e.mp3":["bad boy"],
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":["worth it"],
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":["believer"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.26_dd986468.mp3":["no lies"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.27_19f266ce.mp3":["perfect"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_2b4b43c6.mp3":["without me"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_9509977e.mp3":["hey mamma"],
         r"D:\Music_guesser\songs\[Songs.PK] Kick - 13 - Tu Hi Tu (House Mix).mp3":["kick","tu hi tu"],
    r"D:\Music_guesser\songs\01 Baarish - Half Girlfriend (Ash King) 190Kbps(1).mp3": ["baarish","hal girlfriend"],
    r"D:\Music_guesser\songs\01 Ban Ja Rani - Tumhari Sulu (Guru) 320Kbps.mp3":["ban ja tu meri rani","tumhari sulu"],
    r"D:\Music_guesser\songs\01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3":["chalti hai kya 9 se 12","judwaa 2"],
    r"D:\Music_guesser\songs\01 Ik Vaari Aa - Raabta (Arijit Singh) 190Kbps.mp3":["ik vaari aa","raabta","arijith","arijith singh","arijit","arijiit"],
    r"D:\Music_guesser\songs\01 Ok Jaanu - Title Song (AR Rehman) 190Kbps.mp3":["ok jaanu"],
    r"D:\Music_guesser\songs\02 Darkhaast - Shivaay (Arijit Singh) 190Kbps-1.mp3":["darkhaast","shivaay","arijith","arijith singh","arijit","arijiit"],
    r"D:\Music_guesser\songs\02 Raabta - Title Song (Arijit Singh) 190Kbps.mp3":["raabta","arijith","arijith singh","arijit","arijiit"],
    r"D:\Music_guesser\songs\01. Oh Girl You're Mine.mp3":["o girl you are mine","housefull"],
    r"D:\Music_guesser\songs\Anuv Jain - HUSN (Official Video)(MP3_160K).mp3":["anuv jain","husn"], 
r"D:\Music_guesser\songs\BAARISHEIN (Studio) Anuv Jain(MP3_160K).mp3":["baarishein","anuv jain","baarisheen"],
r"D:\Music_guesser\songs\Dil Haareya _ Arijit Singh _ Tanya Maniktala _ Danesh Razvi _ Vivian Richard _ JUNO _ Dharma 2.0(MP3_160K).mp3":["dil hareya","dil haareya","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Humdard Full Video Song _ Ek Villain _ Arijit Singh _ Mithoon(MP3_160K).mp3":["ek villain","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Dil Meri Na Sune Lyrical - Genius _ Utkarsh Sharma_ Ishita _ Atif Aslam _ Himesh Reshammiya(MP3_160K).mp3":["dil meri na sune","genius","atif aslam","atif","himesh reshamiya"],
r"D:\Music_guesser\songs\Full Song_ KHAIRIYAT (BONUS TRACK) _ CHHICHHORE _ Sushant_ Shraddha _ Pritam_ Amitabh B_Arijit Singh(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","khairiyat","chicchore"],
r"D:\Music_guesser\songs\Mann Jogiya _ Official Song _ Arijit Singh_Ishita Vishwakarma _ Anique _ Dheeraj _ Pyaar Hai Toh Hai(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","pyaar hai to hai","mann jogiya"],
r"D:\Music_guesser\songs\Tera Fitoor Lyrical - Genius _ Utkarsh Sharma_ Ishita Chauhan _ Arijit Singh _ Himesh Reshammiya(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","tera fitoor","genius"],
r"D:\Music_guesser\songs\Dunki_ O Maahi (Full Video) _ Shah Rukh Khan _ Taapsee Pannu _ Pritam _ Arijit Singh _ Irshad Kamil(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","dunki","oo mahi"],
r"D:\Music_guesser\songs\LO MAAN LIYA Full Video Song _ Raaz Reboot _ Arijit Singh_Emraan Hashmi_Kriti Kharbanda_Gaurav Arora(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","lo maan liya"],
r"D:\Music_guesser\songs\Lyrical_ Thodi Jagah Video _ Riteish D_ Sidharth M_ Tara S _ Arijit Singh _ Tanishk Bagchi(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","thodi jagah"],
r"D:\Music_guesser\songs\Saanson Ko - 4K Music Video _ ZiD _ Mannara_ Karanvir _ Arijit Singh _ Sharib Toshi _ Romantic Hits(MP3_160K).mp3":["saanson ko","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Ve Kamleya _ Rocky Aur Rani Kii Prem Kahaani _ Ranveer _ Alia _ Pritam _ Amitabh _ Arijit _ Shreya(MP3_160K).mp3":["ve kamleya","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Ae Dil Hai Mushkil - 4k Music Video _ Ranbir Kapoor _ Anushka Sharma _ Aishwarya Rai Bachchan(MP3_160K).mp3":["ae dil hai mushkil"],
r"D:\Music_guesser\songs\Raataan Lambiyan - Lyric Video _Shershaah_Sidharth_ Kiara_Tanishk B._Jubin_Asees(MP3_160K).mp3":["sheershah","raataan lambiyan","jubin nautiyal","jubin"],
r"D:\Music_guesser\songs\Zaalima _ Raees _ Shah Rukh Khan _ Mahira Khan _ Arijit Singh _ Harshdeep Kaur _ JAM8 _ Pritam(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","zaalima","raaes"],
r"D:\Music_guesser\songs\Apna Bana Le - Bhediya _ Varun Dhawan_ Kriti Sanon_ Sachin-Jigar_ Arijit Singh_ Amitabh Bhattacharya(MP3_160K).mp3":["apna bana le","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Kesariya - Film Version _ Brahmāstra _ Ranbir _ Alia _ Pritam _ Arijit _ Amitabh(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","brahmastra","kesariya"],
r"D:\Music_guesser\songs\Khamoshiyan (Title Song) Lyrics _ Arijit Singh _ Rashmi S _ Jeet G _ Ali Fazal _ Sapna P _ Gurmeet C(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","khamoshiyan"],
r"D:\Music_guesser\songs\Phir Bhi Tumko Chaahunga - Full Song _ Arijit Singh _ Arjun K _ Shraddha K _ Mithoon_ Manoj M(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","mai phir bhi tumko chahunga","half girlfriend"],
r"D:\Music_guesser\songs\Tere Hawaale (Full Video) Laal Singh Chaddha _ Aamir_Kareena _ Arijit_Shilpa _ Pritam_Amitabh_Advait(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","tere hawaale","laal singh chaddha"],
r"D:\Music_guesser\songs\Chahun Main Ya Naa Full Video Song Aashiqui 2 _ Aditya Roy Kapur_ Shraddha Kapoor(MP3_160K).mp3":["Chahun Main Ya Naa","aashique 2","aashiqui 2","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Humsafar (Full Video)  _ Varun _ Alia Bhatt _ Akhil Sachdeva _ _Badrinath Ki Dulhania_(MP3_160K).mp3":["Badrinath Ki Dulhania","akhil","humsafar"],
r"D:\Music_guesser\songs\Main Rang Sharbaton Ka _ Arijit Singh _ Phata Poster Nikhla Hero _ 2013(MP3_160K).mp3":["Phata Poster Nikhla Hero","Main Rang Sharbaton Ka","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\O Bedardeya (Film Version) Tu Jhoothi Main Makkaar _ Ranbir_ Shraddha _ Pritam_ Arijit S_ Amitabh B(MP3_160K).mp3":["o bedardeya","arijith","arijith singh","arijit","arijiit","tu jhuthi mai makkar"],
r"D:\Music_guesser\songs\Aaj Se Teri - Lyrical _ Padman _ Akshay Kumar _ Radhika Apte _ Arijit Singh _ Amit Trivedi(MP3_160K).mp3":["aaj se teri","padman","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Rabba Janda - Full Video _ Mission Majnu _ Sidharth Malhotra_ Rashmika _ Jubin N_ Tanishk B_ Shabbir(MP3_160K).mp3":["rabba janda","jubin nautiyal","jubin"],
r"D:\Music_guesser\songs\Sajni (Song)_ Arijit Singh_ Ram Sampath _ Laapataa Ladies _  Aamir Khan Productions(MP3_160K).mp3":["sajni","laapata ladies","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Tere Vaaste _ Zara Hatke Zara Bachke _ Vicky Kaushal_ Sara Ali Khan_ Varun J_ Sachin-Jigar_Amitabh B(MP3_160K).mp3":["Zara Hatke Zara Bachke","varun jain","tere vaaste"],
r"D:\Music_guesser\songs\Aaj Ki Raat _ Stree 2 _ Tamannaah Bhatia _ Sachin-Jigar _ Madhubanti _ Divya _ Amitabh(MP3_160K).mp3":["aaj ki raat","stree 2","madhubanti"],
r"D:\Music_guesser\songs\ANIMAL_ SATRANGA(Song) Ranbir Kapoor_Rashmika_Sandeep V_Arijit_Shreyas P_Siddharth-Garima _Bhushan K(MP3_160K).mp3":["satranga","animal","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Illuminati_Aavesham_Jithu Madhavan_Fahadh Faasil_Sushin Shyam_Dabzee_Vinayak_ Nazriya_Anwar Rasheed(MP3_160K).mp3":["illuminati"],
r"D:\Music_guesser\songs\JAWAN_ Chaleya (Hindi) _ Shah Rukh Khan _ Nayanthara _ Atlee _ Anirudh _ Arijit S_ Shilpa R _ Kumaar(MP3_160K).mp3":["jawan","jawaan","chaleya","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Naina _ Crew _ Diljit Dosanjh_ Ft. Badshah _ Tabu_ Kareena Kapoor Khan_ Kriti Sanon _ Raj Ranjodh(MP3_160K).mp3":["naina","baadshah","crew","diljith","diljith dosanj"],
r"D:\Music_guesser\songs\Darin - I Lost You (Lyric Video)(MP3_160K).mp3":["darin","i lost you"],
r"D:\Music_guesser\songs\Full Video_ Samayama Song _ Hi Nanna _ Nani_Mrunal Thakur _ Shouryuv _ Hesham Abdul Wahab(MP3_160K).mp3":["samayama"],
r"D:\Music_guesser\songs\Paon Ki Jutti - Jyoti Nooran _ Isha Malviya _ Shiv Panditt _ Jaani _ Arvvindr S Khaira _ Bunny(MP3_160K).mp3":["paon ki jutti"],
r"D:\Music_guesser\songs\Teri Baaton Mein Aisa Uljha Jiya (Title Track)_ Shahid Kapoor_ Kriti Sanon _ Raghav_Tanishk_ Asees(MP3_160K).mp3":["teri baaton mein aisa jo uljha jiya"],
r"D:\Music_guesser\songs\Tum Se (Song)_ Shahid Kapoor_ Kriti Sanon _ Sachin-Jigar_ Raghav Chaitanya_ Varun Jain_ Indraneel(MP3_160K).mp3":["tum se","teri baaton mein aisa jo uljha jiya"],
r"D:\Music_guesser\songs\Aayi Nai -Stree 2 _ Shraddha Kapoor _ Rajkummar Rao _ Sachin-Jigar _Pawan Singh_Simran_Divya_Amitabh(MP3_160K).mp3":["aayi nai","pawan singh","stree 2"],
r"D:\Music_guesser\songs\Akhiyaan Gulaab (Song)_ Shahid Kapoor_ Kriti Sanon _ Mitraz _ Teri Baaton Mein Aisa Uljha Jiya(MP3_160K).mp3":["Teri Baaton Mein Aisa Uljha Jiya","mitraaz","akhiyan gulaab"],
r"D:\Music_guesser\songs\ANIMAL_ HUA MAIN (Lyrical Video) _ Ranbir Kapoor_Rashmika M _ Sandeep V _ Raghav_Manoj M _ Bhushan K(MP3_160K).mp3":["hua main","sandeep vanga"],
r"D:\Music_guesser\songs\CHUMMA _ Vicky Vidya Ka Woh Wala Video _ Rajkummar R_ Triptii D_ Pawan Singh _ Sachin-Jigar_ Vayu(MP3_160K).mp3":[" Vicky Vidya Ka Woh Wala Video","pawann singh","chumma"],
r"D:\Music_guesser\songs\Nora Fatehi - Im Bossy [Official Music Video](MP3_160K).mp3":["i am bossy"],
r"D:\Music_guesser\songs\ANIMAL_ ARJAN VAILLY _ Ranbir Kapoor _ Sandeep Vanga _ Bhupinder B_ Manan B _ Bhushan K(MP3_160K).mp3":["arjan vailly","arjan velly","sandeep vanga","animal"],
r"D:\Music_guesser\songs\ANIMAL_SAARI DUNIYA JALAA DENGE(Audio)_Ranbir K_Rashmika_Anil_Bobby_Sandeep_B Praak_Jaani_Bhushan K(MP3_160K).mp3":["animal","saari duniya jala denge","b praak"],
r"D:\Music_guesser\songs\Emma - Daydream (Official Audio)(MP3_160K).mp3":["emma","daydream"],
r"D:\Music_guesser\songs\JAWAN_ Not Ramaiya Vastavaiya _ Shah Rukh Khan _ Atlee _ Anirudh _ Nayanthara _ Vishal D _ Shilpa R(MP3_160K).mp3":["not ramaiya vasta vaiya","vishal","jawan","jawaan","anirudh"],
r"D:\Music_guesser\songs\What Jhumka_ _ Rocky Aur Rani Kii Prem Kahaani _ Ranveer _ Alia _ Pritam _ Amitabh _ Arijit _ Jonita(MP3_160K).mp3":["rocky aur rani ki prem kahani","what jhumka","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Ammy Virk_ Main Suneya Video Song Feat. Simran Hundal_ Rohaan _SunnyV_ Raj _Navjit B _ Bhushan Kumar(MP3_160K).mp3":["ammy virk","main suneya"],
r"D:\Music_guesser\songs\FIGHTER_ Ishq Jaisa Kuch Song_ Hrithik_ Deepika_ Vishal-Sheykhar_ Shilpa_ Kumaar_ Bosco-Caesar(MP3_160K).mp3":["fighter","ishq jaisa kuch","vishal","vishal mishra"],
r"D:\Music_guesser\songs\Heeriye (Official Video) Jasleen Royal ft Arijit Singh_ Dulquer Salmaan_ Aditya Sharma _Taani Tanvir(MP3_160K).mp3":["heeriye","arijith","arijith singh","arijit","arijiit"],
r"D:\Music_guesser\songs\Tere Naal Video Song _ Tulsi Kumar_ Darshan Raval _ Gurpreet Saini_ Gautam G Sharma _ Bhushan Kumar(MP3_160K).mp3":["tere naal","darshan raval"],
r"D:\Music_guesser\songs\Tiger Shroff _ I Am A Disco Dancer 2.0 _ Benny Dayal _Salim Sulaiman _ Bosco _ Official Music Video(MP3_160K).mp3":["i am a disco dancer"],
r"D:\Music_guesser\songs\FILHALL _ Akshay Kumar Ft Nupur Sanon _ BPraak _ Jaani _ Arvindr Khaira _ Ammy Virk _ DESI MELODIES(MP3_160K).mp3":["b praak","filhaal"],
r"D:\Music_guesser\songs\Mere Angne Mein _ Jacqueline F_ Asim Riaz _ Neha K_ Raja H_ Tanishk B _ Radhika - Vinay _ Bhushan K(MP3_160K).mp3":["mere angne mei"],
r"D:\Music_guesser\songs\Shayad - Love Aaj Kal _ Kartik _ Sara _ Arushi _ Pritam _ Arijit Singh(MP3_160K).mp3":["arijith","arijith singh","arijit","arijiit","shayad","love aajkal"],
r"D:\Music_guesser\songs\Tum Hi Aana Full Video _ Marjaavaan _ Riteish D_ Sidharth M_ Tara S _ Jubin N _ Payal Dev Kunaal V(MP3_160K).mp3":["tum hi aana","marjaawan","marjaavan","jubin nautiyal"],
r"D:\Music_guesser\songs\Ishq Official Lyrical Video I Amir Ameer _ Faheem Abdullah _ Rauhan Malik I Love Song 2024(MP3_160K).mp3":["ishq"],
r"D:\Music_guesser\songs\Anuv Jain - JO TUM MERE HO (Official Video)(MP3_160K).mp3":["anuv jain","jo tum mere ho"],

         }

English = {
    r"songs/WhatsApp Audio 2024-12-07 at 19.37.21_7cea9fce.mp3":["faded"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.22_66de4d6e.mp3":["bad boy"],
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":["worth it"],
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":["believer"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.26_dd986468.mp3":["no lies"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.27_19f266ce.mp3":["perfect"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_2b4b43c6.mp3":["without me"],
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_9509977e.mp3":["hey mamma"]
    
}

# Function to play the middle part of the song for a specific duration
def play_middle_part(file_path, duration=10):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(start=30)  # Starts playback at 30 seconds
    time.sleep(duration)
    pygame.mixer.music.stop()

# Main game function
def play_game():
    print("Hello Gamefreak, Welcome to the ultimate game of guessing songs!")
    print("Let's start the game by asking your preferences!")

    # User inputs
    try:
        rounds = int(input("How many rounds would you like to play?\n(1) 3\n(2) 5\n(3) 7\n"))
        language = input("Select the language you prefer:\n'e' for English\n'h' for Hindi\n'p' for Punjabi\n'm' for Mixed:\n").strip().lower()
    except ValueError:
        print("Invalid input. Please restart the game.")
        return

    print("""
Rules:
1. Guess either the song title or the movie name.
2. Artist name could also be guessed.
3. Spelling mistakes are not allowed.
4. Correct guesses give you points on time taken basis(30 for <4 seconds|20 for <7 seconds|15 for <10 seconds).
5. Answers after the 10 seconds time frame are not accepted
""")

    input("Press Enter to start the game!")

    # Select dictionary based on language choice
    if language == "h":
        selected_songs = list(Hindi.items())
    elif language == "e":
        selected_songs = list(English.items())
    elif language == "p":
        selected_songs = list(Punjabi.items())
    elif language == "m":
        selected_songs = list(mixed.items())
    else:
        print("Invalid language choice. Please restart the game.")
        return

    # Shuffle the songs
    random.shuffle(selected_songs)

    # Game logic
    score = 0
    for i in range(rounds):
        if i >= len(selected_songs):
            print("No more songs available. Ending game!")
            break

        song_path, valid_answers = selected_songs[i]
        print(f"Round {i + 1}: Playing music...")

        # Play the middle part of the song
        play_middle_part(song_path, duration=10)

        start_time = time.time()
        guess = input("Guess the song name: ").strip().lower()
        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("Time's up! No points for this round.")
        elif guess in [answer.lower() for answer in valid_answers]:
            if elapsed_time < 4:
                score += 30
                print(f"Wohoo! You got 30 points!\nTime taken: {round(elapsed_time, 2)} seconds")
            elif elapsed_time < 7:
                score += 20
                print(f"Great! You got 20 points!\nTime taken: {round(elapsed_time, 2)} seconds")
            elif elapsed_time <= 10:
                score += 15
                print(f"Nice! You got 15 points!\nTime taken: {round(elapsed_time, 2)} seconds")
        else:
            print(f"Better luck next time. The correct answers were: {', '.join(valid_answers)}.")
        
        print(f"Your current score is: {score}\n")

    print(f"Game Over! Your total score is: {score}")

# Replay loop
while True:
    play_game()
    replay = input("Do you want to play again? (y/n): ").strip().lower()
    if replay != 'y':
        print("Thanks for playing! Goodbye!")
        break
