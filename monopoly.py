from tiles import *

# Create a board instance in the Monopoly class containing all the necessary information on
# each tile

class Monopoly:
   board = [
            Other(0,'Go'),									\
            Property(1,'Mediterranean Avenue',60,'brown',2,10,30,90,160,250,30),		\
            Other(2,'Community Chest'),								\
            Property(3,'Baltic Avenue',60,'brown',4,20,60,180,320,450,30),			\
            Tax(4,'Income Tax',200),								\
            Railroad(5,'Reading Railroad',200,25,100),						\
            Property(6,'Oriental Avenue',100,'lblue',6,30,90,270,400,550,50),			\
            Other(7,'Chance'),									\
            Property(8,'Vermont Avenue',100,'lblue',6,30,90,270,400,550,50),			\
            Property(9,'Connecticut Avenue',120,'lblue',8,40,100,300,450,600,60),		\
            Other(10,'Just Visiting / In Jail'),						\
            Property(11,'St. Charles Place',140,'pink',10,50,150,450,625,750,70),		\
            Utility(12,'Electric Company',150,75),						\
            Property(13,'States Avenue',140,'pink',10,50,150,450,625,750,70),			\
            Property(14,'Virginia Avenue',160,'pink',12,60,180,500,700,900,80),			\
            Railroad(15,'Pennsylvania Railroad',200,25,100),					\
            Property(16,'St. James Place',180,'orange',14,70,200,550,750,950,90),		\
            Other(17,'Community Chest'),							\
            Property(18,'Tenneessee Avenue',180,'orange',14,70,200,550,750,950,90),		\
            Property(19,'New York Avenue',200,'orange',16,80,220,600,800,1000,100),		\
            Other(20,'Free Parking'),								\
            Property(21,'Kentucky Avenue',220,'red',18,90,250,700,875,1050,110),		\
            Other(22,'Chance'),									\
            Property(23,'Indiana Avenue',220,'red',18,90,250,700,875,1050,110),			\
            Property(24,'Illinois Avenue',240,'red',20,100,300,750,925,1100,120),		\
            Railroad(25,'B. & O. Railroad',200,25,100),						\
            Property(26,'Atlantic Avenue',260,'yellow',22,110,330,800,975,1150,130),		\
            Property(27,'Ventnor Avenue',260,'yellow',22,110,330,800,975,1150,130),		\
            Utility(28,'Water Works',150,75),							\
            Property(29,'Marvin Gardens',280,'yellow',24,120,360,850,1025,1200,140),		\
            Other(30,'Go to Jail'),								\
            Property(31,'Pacific Avenue',300,'green',26,130,390,900,1100,1275,150),		\
            Property(32,'North Carolina Avenue',300,'green',26,130,390,900,1100,1275,150),	\
            Other(33,'Community Chest'),							\
            Property(34,'Pennsylvania Avenue',320,'green',28,150,450,1000,1200,1400,160),	\
            Railroad(35,'Short Line',200,25,100),						\
            Other(36,'Chance'),									\
            Property(37,'Park Place',350,'blue',35,175,500,1100,1300,1500,175),			\
            Tax(38,'Luxury Tax',100),								\
            Property(39,'Boardwalk',400,'blue',50,200,600,1400,1700,2000,200)			\
           ]
