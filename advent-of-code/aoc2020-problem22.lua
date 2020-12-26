-- Description fragment:
-- Before the game starts, split the cards so each player has their own deck (your puzzle input).
-- Then, the game consists of a series of rounds: both players draw their top card,
-- and the player with the higher-valued card wins the round. The winner keeps both cards,
-- placing them on the bottom of their own deck so that the winner's card is above the other card. 
-- If this causes a player to have all of the cards, they win, and the game ends.

-- Once the game ends, you can calculate the winning player's score. 
-- The bottom card in their deck is worth the value of the card multiplied by 1, 
-- the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. 
-- With 10 cards, the top card is worth the value on the card multiplied by 10. 

-- This problem was solved using the example data given in the description.

function main()
   player1 = {9, 2, 6, 3, 1}
   player2 = {5, 8, 4, 7, 10}
   print(play(player1, player2)) -- 306
end

function play(hand1, hand2)
   -- if list is empty
   if #hand1 < 1 then
      return calc(hand2)
   elseif #hand2 < 1 then
      return calc(hand1)
   else
      upHand1, upHand2 = updateHands(hand1, hand2)
      return play(upHand1, upHand2)
   end
end

function calc(hand)
   result = 0
   len = #hand
   for i,j in pairs(hand) do
      result = result + (len * j)
      len = len - 1
   end
   return result
end

-- The description does not specify what to do in case of a tie
-- I assume that the numbers will always be different.
function updateHands(hand1, hand2)
   if hand1[1] > hand2[1] then
      cycleCards(hand1, hand2)
   else
      cycleCards(hand2, hand1)
   end
   return hand1, hand2
end

-- Could use a more efficient queue implementation for larger inputs.
function cycleCards(hand1, hand2)
      table.insert(hand1, hand1[1])
      table.insert(hand1, hand2[1])
      table.remove(hand1, 1)
      table.remove(hand2, 1)
end   

-- thanks to lua for its tail recursion and its multiple return values.
main()

