from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import SportCategory, Base, SportItem
engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# List for Soccer
category1 = SportCategory(name="Soccer")
session.add(category1)
session.commit()

sportItem1 = SportItem(name="Soccer Ball",
                       description="Aim for the corners and practice "
                       "through-passes with this adidas Starlancer V Adult "
                       "Soccer Ball. The butyl bladder retains air while you "
                       "train and hone your on-field skills, while the machine"
                       "-stitched imitation leather cover provides a great"
                       "feel as you pass and shoot.",
                       price="$12.99", sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Shin Guards",
                       description="You'll get the most protection with the "
                       "least amount of coverage with the Nike Adults"
                       " Neymar Mercurial Lite Soccer Shin Guards. The "
                       "durable resin shells are matched with EVA foam to "
                       "help diffuse any kicks to the shin, and they are "
                       "anatomically shaped for targeted comfort.",
                       price="$21.99", sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Soccer Gloves",
                       description="Allround grip design provides a soft, "
                       "cushioned surface without sacrificing grip",
                       price='$29.99', sportcategory=category1)
session.add(sportItem1)
session.commit()

# List for Baseball
category1 = SportCategory(name="Baseball")
session.add(category1)
session.commit()

sportItem1 = SportItem(name="Helmet",
                       description="Your little slugger can knock out a home "
                       "run in the Rawlings Youth MLB Authentic Style T-Ball "
                       "Batting Helmet with Faceguard. Featuring an "
                       "MLB-inspired design and venting to offer protection "
                       "out on the diamond, this batting helmet offers a "
                       "clear-coat finish for a classic look", price='$29.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Bat",
                       description="Crafted with a 2-5/8-inchbarrel, the "
                       "Rawlings Kids' USA Fuel Aluminum Big Barrel Baseball "
                       "Bat -8 offers an enhanced sweet spot to boost your "
                       "performance at home plate. Aerospace-grade aluminum "
                       "alloy construction offers lasting endurance, while "
                       "the cushioned grip keeps you comfortable at home "
                       "plate. 3-1/32-inch handle.", price='$34.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Batting Gloves",
                       description="Get on base and knock in runs when you "
                       "wear these Nike Boys' Huarache Edge Batting Gloves to "
                       "the plate. Made of polyurethane, polyester, neoprene, "
                       "nylon and silicone, the gloves help enhance your grip "
                       "on the bat, so you can focus on hitting the baseball "
                       "in the sweet spot.", price='$19.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

# List for Football
category1 = SportCategory(name="Football")
session.add(category1)
session.commit()

sportItem1 = SportItem(name="Football Helmet",
                       description="Help protect your star player's head as "
                       "he faces tough opponents with the Riddell Youth "
                       "Victor Football Helmet. The Speed Shell Profile "
                       "delivers side impact protection, while the fitted "
                       "liner system and inflatable jaw pads offer a "
                       "comfortable, custom fit. Ventilated for "
                       "breathability. Made in USA.", price='$109.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Official Game Ball",
                       description="The Wilson NFL The Duke Official Game "
                       "Ball is the official game ball of the NFL. The "
                       "leather cover has deep pebbles and a firm texture to "
                       "offer outstanding grip. This official-size football "
                       "features a pro pattern.", price='$99.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Gloves",
                       description="Description: Featuring Magnigrip on the "
                       "palms, the Nike Adult 2018 Super Bowl Vapor Jet 4.0 "
                       "Gloves are great for all-weather play and the "
                       "flexible knuckles with mesh allow for natural "
                       "movement.", price='$45.99', sportcategory=category1)
session.add(sportItem1)
session.commit()

# List for Snowboarding
category1 = SportCategory(name="Snowboarding")
session.add(category1)
session.commit()

sportItem1 = SportItem(name="Ski Pant",
                       description="Description: Hit the slopes with the "
                       "Magellan Outdoors Women's Softshell Ski Pant, which "
                       "is made of multilayered softshell fabric and spandex "
                       "for warm, comfortable wear. Featuring a waistband "
                       "with belt loops and adjustable tabs, this pant has "
                       "wind gators at the ankles with reinforced kick panels "
                       "to help keep wind and snow out. Downhill design.",
                       price='$34.99', sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Snowboard Jacket",
                       description="It doesn't matter if it's your first time "
                       "on the slopes, because with the Free Country Girls' "
                       "Snowboard Jacket, you're sure to look like a pro. As "
                       "you coast through the powder, the jacket's snow skirt "
                       "and wind- and water-resistant fabric will help keep "
                       "you warm and dry. Put up the hood with faux-fur trim "
                       "for extra protection, and use the 2 zipper pockets to "
                       "secure your gear.", price='$44.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Traveller Soft Racks",
                       description="Carry your canoe, kayak, snowboard or "
                       "other sporting equipment on the roof of your vehicle "
                       "with the Sea to Summit Traveller Soft Racks. "
                       "Compatible with most tie-downs, the racks feature "
                       "strong, removable daisy chains that provide multiple "
                       "tie-down points and a heavy-duty, die-cast cam buckle "
                       "to help ensure a secure hold. 3-step quick-fit system "
                       "for easy mounting", price='$99.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

# List for Hockey
category1 = SportCategory(name="Hockey")
session.add(category1)
session.commit()

sportItem1 = SportItem(name="Cup",
                       description="Make sure you're always protected while "
                       "skating on the ice with the Battle Men's NuttyBuddy "
                       " Mongo Cup and Hockey Compression Short. The "
                       "anatomically correct cup is designed with Lexan124-R, "
                       "which is used in bulletproof glass, to ensure "
                       "reliable, yet comfortable protection all practice and "
                       "game long. The compression short supports your muscles"
                       " through every face off and goal.", price='$39.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Hockey Ball Set",
                       description="Make each game one to remember with the "
                       "Franklin NHL 3-Piece Hockey Ball Set. An extreme "
                       "color high-density ball allows you to keep track of "
                       "the competition with ease, while the included "
                       "glow-in-the-dark ball makes low-light action a "
                       "breeze. Each ball is officially sized to accommodate "
                       "versatile use.", price='$10.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Goal",
                       description="Make your way to the top while "
                       "practicing with the Franklin NHL Mini Hockey Goal "
                       "Set. With 2 sticks, 2 balls and a goal, you can "
                       "simulate real gameplay by challenging your friend to "
                       "a duel. And no matter how hard you hit the balls into "
                       "the polyester net, the high-impact, rugged frame "
                       "won't falter.", price='$24.99',
                       sportcategory=category1)
session.add(sportItem1)
session.commit()

# List for Weight Training
category1 = SportCategory(name="Weight Training")
session.add(category1)
session.commit()

sportItem1 = SportItem(name="Weight Lifting Belt",
                       description="The Harbinger 6 inch Padded Leather "
                       "Weight Lifting Belt is constructed from leather with "
                       "double stitching for durability. Polyester foam "
                       "padding and a contoured design provides comfort and "
                       "protection, while the double-pronged steel buckle "
                       "offers easy and secure tensioning. The belt also "
                       "features full board backing and suede lining.",
                       price='$24.99', sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Power Gloves",
                       description="Keep your hands protected and "
                       "comfortable while you lift weights with the Harbinger "
                       "Women's Power Gloves. StretchBack mesh material "
                       "extends along the back of the hand and between the "
                       "fingers for flexibility and breathability, and "
                       "double-leather construction offers cushioning for "
                       "your palms. The gloves feature reinforced thumbs and "
                       "a short finger length for ample surface contact, and "
                       "the fingers are backed with foam to help protect "
                       "hands from abrasion. Slip-on design. Black.",
                       price='$12.99', sportcategory=category1)
session.add(sportItem1)
session.commit()

sportItem1 = SportItem(name="Stability Ball",
                       description="Enjoy a comprehensive stretching and "
                       "toning workout with the BCG Weighted Stability Ball. "
                       "Designed with 2 lb. of weighted fill material and "
                       "constructed from long-lasting PVC, this ball will "
                       "stay conveniently in place throughout your routine "
                       "and can be used to add slight resistance to each "
                       "exercise.", price='$18.99', sportcategory=category1)
session.add(sportItem1)
session.commit()

print "Items added successfully"
