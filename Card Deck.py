#!/usr/bin/env python
# coding: utf-8

# In[93]:


#create deck, shuffle deck, divide cards between players

suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#create deck and distribute to both players
class Deck():
    
    deck=[]
    
    def __init__(self):
        self.suit = suit
        self.rank = rank
        
        for s in self.suit:
            for r in self.rank:
                self.deck.append(r + ' of ' + s)
        
    def __str__(self):
        print(*self.deck, sep='\n')
        
        
    def shuffle_deck(self):
        import random
        
        return random.shuffle(self.deck)

    def deal_cards(self,player_stack,computer_stack):
        player_stack = self.deck[0:26]
        computer_stack = self.deck[26:]


#create hand, draw card





# In[94]:


deck=Deck()


# In[95]:


deck.shuffle_deck()


# In[96]:


deck.deal_cards(player_stack,computer_stack)


# In[97]:


player_stack


# In[98]:


computer_stack

