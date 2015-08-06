#!/usr/bin/python

from tbay import session, Item, User, Bid

chris = User() 
chris.username = "rosuav" 
chris.password = "thinkful"
session.add(chris)
session.commit()

ashley = User(username = "ashybon", password = "Ashl3y")
session.add(ashley)
session.commit()

lianna = User(username = "nuki", password = "liannaliannal1ann4")
session.add(lianna)
session.commit()

baseball = Item()
baseball.name = "Giants World Series 2014"
baseball.description = "Foul ball in game 2"
chris.items.append(baseball)
session.add(baseball)
session.commit()

guitar = Item(name = "Fender", description = "rock out with this electric guitar")
ashley.items.append(guitar)
session.add(guitar)
session.commit()

bid_ashley = Bid(price = 5000, item = baseball, bidder = ashley)
session.add(bid_ashley)
session.commit()

bid_lianna = Bid(price = 2500, item = baseball, bidder = lianna)
session.add(bid_lianna)
session.commit()

highest_bid = session.query(Bid).filter(Bid.item==baseball).order_by(Bid.price.desc()).first()
#bid = session.query(Bid).(baseball)
#session.query(Bid).filter(price>3000)

print highest_bid.bidder.username